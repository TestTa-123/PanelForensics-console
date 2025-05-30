import ast
import json
import os
from datetime import datetime

from helper.DBHelper import DBHelper
from helper.DecHelper import DecHelper


class BTPanel3:
    def __init__(self):
        # self.db_path = '/www/server/panel/data/db/default.db'
        self.db_path = '/home/a/Downloads/sql.db'
        self.backup_db = '/www/server/panel/data/db/backup.db'
        self.client_db = '/www/server/panel/data/db/client_info.db'
        self.crontab_db = '/www/server/panel/data/db/crontab.db'
        self.database_db = '/www/server/panel/data/db/database.db'
        self.default_db = '/www/server/panel/data/db/default.db'
        self.docker_db = '/www/server/panel/data/db/docker.db'
        self.firewall_db = '/www/server/panel/data/db/firewall.db'
        self.ftp_db = '/www/server/panel/data/db/ftp.db'
        self.log_db = '/www/server/panel/data/db/log.db'
        self.panel_db = '/www/server/panel/data/db/panel.db'
        self.site_db = '/www/server/panel/data/db/site.db'
        self.task_db = '/www/server/panel/data/db/task.db'
        self.default_path = '/www/server/panel/default.pl'
        self.admin_path = '/www/server/panel/data/admin_path.pl'
        self.port_path = '/www/server/panel/data/port_path.pl'
        self.user_path = '/www/server/panel/data/userInfo.json'
        self.limitip_path = ''
        self.basic_auth_path = ''
        self.title_path = '/www/server/panel/data/title.pl'
        self.memo_path = ''

        if os.path.exists('/www/server/panel/data/memo.txt'):
            self.memo_path = '/www/server/panel/data/memo.txt'
        if os.path.exists('/www/server/panel/data/limitip.conf'):
            self.limitip_path = '/www/server/panel/data/limitip.conf'
        if os.path.exists('/www/server/panel/config/basic_auth.json'):
            self.basic_auth_path = '/www/server/panel/config/basic_auth.json'

        self.history_path = []
        self.cipher = DecHelper()
        self.users_sql = 'select username,password,login_ip,login_time,email,salt from users'
        self.users_sql2 = 'select username,password,login_ip,login_time,email from users'
        self.users_name = ['用户名', '密码', '登录IP', '登录时间', '邮箱', '盐值']
        self.tasks_sql = 'select name,type,addtime,datetime(start,"unixepoch"),datetime(end,"unixepoch"),execstr from tasks'
        self.tasks_name = ['任务名', '类型', '添加时间', '开始时间(UTC0)', '结束时间(UTC0)', '内容']
        self.sites_sql = 'select s.name,path,ps,s.addtime,d.name,d.port from sites s left join domain d on d.pid = s.id'
        self.sites_name = ['网站名称', '路径', '备注', '添加时间', '域名', '端口']
        self.logs_sql = 'select type,log,addtime,username from logs'
        self.logs_name = ['类型', '详情', '操作时间', '操作人']
        self.ftps_sql = 'select name,password,path,ps,addtime from ftps'
        self.ftps_name = ['用户名', '密码', '路径', '备注', '添加时间']
        self.firewall_sql = 'select port,ps,addtime from firewall'
        self.firewall_name = ['端口', '备注', '添加时间']
        self.firewall_trans_sql = 'select start_port,ended_ip,ended_port,protocol,addtime from firewall_trans'
        self.firewall_trans_name = ['起始端口', '目标IP', '目标端口', '协议', '添加时间']
        self.firewall_ip_sql = 'select types,address,brief,addtime from firewall_ip'
        self.firewall_ip_name = ['类型', '地址', '备注', '添加时间']
        self.databases_sql = 'select name,username,password,accept,ps,addtime,type from databases'
        self.databases_name = ['数据库名', '用户名', '密码', '访问权限', '备注', '添加时间', '类型']
        self.databases_sql2 = 'select db_host,db_port,db_user,db_password,ps,datetime(addtime,"unixepoch"),type from database_servers'
        self.databases_name2 = ['数据库地址', '端口', '用户名', '密码', '备注', '添加时间(UTC0)', '类型']
        self.crontab_sql = 'select name,type,where1,where_hour,where_minute,echo,addtime,backupTo,sBody,sType,urladdress from crontab'
        self.crontab_name = ['任务名', '周期', '条件1', '时', '分', '执行文件', '添加时间', '备份至', '执行内容',
                             '任务类型', '请求URL']
        self.config_sql = 'select webserver,backup_path,sites_path,mysql_root from config'
        self.config_name = ['WEB容器', '备份路径', '网站路径', 'MySQL管理员密码']
        self.backup_sql = 'select type,name,filename,size,addtime,ps,cron_id from backup'
        self.backup_name = ['类型', '名称', '文件路径', '文件大小', '备份时间', '备注', '定时任务ID']

    def connect(self) -> None:
        self.conn = DBHelper(self.db_path)

    def close(self) -> None:
        self.conn.close()

    def decrypt(self, data: tuple) -> tuple:
        lst = data[1]
        print(data)
        print(lst)
        for i in range(len(lst)):
            for j in range(len(lst[i])):
                if str(lst[i][j]).startswith('BT-0x:'):
                    enc_data = lst[i][j].split('BT-0x:')[1]
                    dec_data = self.cipher.decrypt_bt(enc_data)
                    lst[i][j] = dec_data
        return (data[0], lst)

    def get_history(self) -> tuple:
        import datetime
        history = []
        for history_path in self.history_path:
            with open(history_path, 'r', encoding='utf-8') as f:
                data = f.readlines()
                for line in data:
                    t = ast.literal_eval(line.strip())
                    t.extend([history_path.split('\\')[-1].split('_')[0]])
                    t[0] = datetime.datetime.fromtimestamp(int(t[0])).strftime("%Y-%m-%d %H:%M:%S")
                    history.append(t)
        return (['时间', '本地IP', '用户', '命令', '连接IP'], history)

    def get_users(self) -> tuple:
        users = self.conn.select(self.users_sql)
        users = [list(t) for t in users]
        return (self.users_name, users)

    def get_tasks(self) -> tuple:
        tasks = self.conn.select(self.tasks_sql)
        tasks = [list(t) for t in tasks]

        return (self.tasks_name, tasks)

    def get_sites(self) -> tuple:
        sites = self.conn.select(self.sites_sql)
        sites = [list(t) for t in sites]

        return (self.sites_name, sites)

    def get_logs(self) -> tuple:
        logs = self.conn.select(self.logs_sql)
        logs = [list(t) for t in logs]

        return (self.logs_name, logs)

    def get_ftps(self) -> tuple:
        ftps = self.conn.select(self.ftps_sql)
        ftps = [list(t) for t in ftps]

        return (self.ftps_name, ftps)

    def get_firewall(self) -> tuple:
        firewall = self.conn.select(self.firewall_sql)
        firewall = [list(t) for t in firewall]

        return (self.firewall_name, firewall)

    def get_firewall_trans(self) -> tuple:
        firewall = self.conn.select(self.firewall_trans_sql)
        firewall = [list(t) for t in firewall]

        return (self.firewall_trans_name, firewall)

    def get_firewall_ip(self) -> tuple:
        firewall = self.conn.select(self.firewall_ip_sql)
        firewall = [list(t) for t in firewall]

        return (self.firewall_ip_name, firewall)

    def get_databases(self) -> tuple:
        databases = self.conn.select(self.databases_sql)
        databases = [list(t) for t in databases]

        return (self.databases_name, databases)

    def get_databases_server(self) -> tuple:
        databases = self.conn.select(self.databases_sql2)
        databases = [list(t) for t in databases]

        return (self.databases_name2, databases)

    def get_crontab(self) -> tuple:
        crontab = self.conn.select(self.crontab_sql)
        crontab = [list(t) for t in crontab]

        return (self.crontab_name, crontab)

    def get_config(self) -> tuple:
        config = self.conn.select(self.config_sql)
        config = [list(t) for t in config]

        return (self.config_name, config)

    def get_backup(self) -> tuple:
        backup = self.conn.select(self.backup_sql)
        backup = [list(t) for t in backup]

        return (self.backup_name, backup)

    def get_div(self) -> str:
        sql = 'select div from div_list'
        div = self.conn.select(sql)[0][0]
        # 解密div
        self.cipher.decrypt_bt_div(div)
        return div

    def get_settings(self) -> tuple:
        settings = []
        name = []
        with open(self.admin_path, 'r') as fr:
            try:
                settings.append(fr.read().strip())
                name.append('安全入口')
            except:
                settings.append('admin_path.pl提取异常')
                name.append('Warning')
        with open(self.default_path, 'r') as fr:
            try:
                settings.append(fr.read().strip())
                name.append('默认密码')
            except:
                settings.append('default.pl提取异常')
                name.append('Warning')
        if self.limitip_path != '':
            with open(self.limitip_path, 'r') as fr:
                try:
                    settings.append(fr.read().strip())
                    name.append('限制IP')
                except:
                    settings.append('limitip.conf提取异常')
                    name.append('Warning')
        try:
            with open(self.port_path, 'r') as fr:
                try:
                    settings.append(fr.read().strip())
                    name.append('访问端口')
                except:
                    settings.append('port.pl提取异常')
                    name.append('Warning')
        except:
            pass

        try:
            with open(self.title_path, 'r', encoding='utf8') as fr:
                try:
                    settings.append(fr.read().strip())
                    name.append('网站标题')
                except:
                    settings.append('title.pl提取异常')
                    name.append('Warning')
        except Exception as e:
            pass

        if self.memo_path != '':
            with open(self.memo_path, 'r', encoding='utf8') as fr:
                try:
                    settings.append(fr.read().strip())
                    name.append('备忘录')
                except:
                    settings.append('memo.txt提取异常')
                    name.append('Warning')

        if self.basic_auth_path != '':
            with open(self.basic_auth_path, 'r') as fr:
                try:
                    data = json.load(fr)
                    settings.append(data['basic_user'])
                    name.append('basic_auth用户名')
                    settings.append(data['basic_pwd'])
                    name.append('basic_auth密码')
                    settings.append(data['open'])
                    name.append('basic_auth开关')
                except:
                    settings.append('basic_auth文件不存在')
                    name.append('Warning')

        try:
            with open(self.user_path, 'r') as fr:
                try:
                    data = json.load(fr)
                    settings.append(data['uid'])
                    name.append('用户ID')
                    settings.append(data['address'])
                    name.append('IP地址')
                    settings.append(data['access_key'])
                    name.append('access_key')
                    settings.append(data['secret_key'])
                    name.append('secret_key')
                    settings.append(str(datetime.datetime.fromtimestamp(data['addtime'])))
                    name.append('添加时间')
                    settings.append(data['username'])
                    name.append('用户名')
                    settings.append(data['idc_code'])
                    name.append('idc_code')
                    settings.append(data['ukey'])
                    name.append('ukey')
                    settings.append(data['serverid'])
                    name.append('serverid')
                except:
                    settings.append('userInfo提取异常')
                    name.append('Warning')
            return (name, [settings])
        except:
            pass

if __name__ == "__main__":
    btPanel = BTPanel3()
    btPanel.connect()
    btPanel.get_div()
    print({'备份记录': btPanel.get_backup()})
    print({'配置': btPanel.decrypt(btPanel.get_config())})
    print({'计划任务': btPanel.get_crontab()})
    print({'数据库': btPanel.decrypt(btPanel.get_databases())})
    print({'远程数据库': btPanel.decrypt(btPanel.get_databases_server())})
    print({'防火墙': btPanel.get_firewall()})
    print({'防火墙-ip': btPanel.get_firewall_ip()})
    print({'防火墙-端口转发': btPanel.get_firewall_trans()})
    print({'FTP服务': btPanel.decrypt(btPanel.get_ftps())})
    print({'操作日志': btPanel.get_logs()})
    print({'历史命令': btPanel.get_history()})
    print({'网站': btPanel.get_sites()})
    print({'任务': btPanel.get_tasks()})
    print({'面板用户': btPanel.decrypt(btPanel.get_users())})
    print({'面板配置': btPanel.get_settings()})
    btPanel.close()