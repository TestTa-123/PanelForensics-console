from BTPanel.BTPanel import BTPanel
from BTPanel.BTPanel2 import BTPanel2
from BTPanel.BTPanel3 import BTPanel3
from MousePanel.MousePanel import MousePanel
from OnePanel.OnePanel import OnePanel
from XPanel.XpPanel import XpPanel
from helper.ServerHelper import ServerHelper


class Main:
    def __init__(self):
        super().__init__()
        self.path = {}
        self.flag = ''
        self.bt_flag = 0
        self.onePanelData = {}
        self.btPanelData = {}
        self.xpPanelData = {}
        self.mousePanelData = {}

    def get_btPanel_data2(self):
        btPanel = BTPanel2()
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
        print({'网站': btPanel.get_sites()})
        print({'任务': btPanel.get_tasks()})
        print({'面板用户': btPanel.decrypt(btPanel.get_users())})
        print({'面板配置': btPanel.get_settings()})

    def get_btPanel_data3(self):
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

    def get_btPanel_data(self):
        btPanel = BTPanel()
        btPanel.connect()
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

    def get_xpPanel_data(self):
        xpPanel = XpPanel()
        xpPanel.set_path()
        xpPanel.connect()
        print({'防火墙': xpPanel.get_accept_port()})
        print({'用户': xpPanel.get_admins()})
        print({'黑名单': xpPanel.get_deny_ip()})
        print({'FTP用户': xpPanel.get_ftp_account()})
        print({'安装信息': xpPanel.get_install_info()})
        print({'MySQL用户': xpPanel.get_mysql_account()})
        print({'MySQL备份': xpPanel.get_mysql_backup_info()})
        print({'MySQL': xpPanel.get_mysql_db_info()})
        print({'MySQL文件上传': xpPanel.get_mysql_upload_file()})
        print({'操作日志': xpPanel.get_operlog()})
        print({'回收站': xpPanel.get_recycle()})
        print({'Server': xpPanel.get_server_info()})
        print({'系统配置': xpPanel.get_syscfg()})
        print({'计划任务记录': xpPanel.get_task_runlog()})
        print({'计划任务': xpPanel.get_taskmng()})
        print({'URL': xpPanel.get_urlmng()})
        print({'网站': xpPanel.get_website()})
        xpPanel.close()

    def get_onePanel_data(self):
        onePanel = OnePanel()
        onePanel.set_path()
        onePanel.connect()
        print({'登录日志': onePanel.get_login_logs()})
        print({'操作日志': onePanel.get_operation_logs()})
        print({'备份记录': onePanel.get_backup_records()})
        print({'命令': onePanel.get_commands()})
        print({'计划任务': onePanel.get_cronjobs()})
        print({'数据库': onePanel.get_database()})
        print({'安装应用': onePanel.get_installed_app()})
        print({'计划任务执行记录': onePanel.get_job_records()})
        print({'Mysql配置': onePanel.get_mysql()})
        print({'Postgresql配置': onePanel.get_postgresql()})
        print({'面板配置': onePanel.get_settings()})
        print({'网站': onePanel.get_websites()})
        print({'远程连接': onePanel.get_hosts()})
        onePanel.close()

    def get_mousePanel_data(self):
        mousePanel = MousePanel()
        mousePanel.set_path()
        mousePanel.connect()
        print({'用户': mousePanel.get_users()})
        print({'SSH连接': mousePanel.get_ssh()})
        print({'证书': mousePanel.get_certs()})
        print({'证书DNS': mousePanel.get_cert_dns()})
        print({'证书用户': mousePanel.get_cert_accounts()})
        print({'数据库用户': mousePanel.get_dbusers()})
        print({'数据库': mousePanel.get_databases()})
        print({'计划任务': mousePanel.get_crontab()})
        print({'面板任务': mousePanel.get_tasks()})
        print({'配置': mousePanel.get_config()})
        print({'站点': mousePanel.get_sites()})
        pass


    # 获取面板数据
    def get_panel_data(self):
        if self.flag == 'bt':
            if self.bt_flag == 1:
                self.get_btPanel_data2()
            elif self.bt_flag == 2:
                self.get_btPanel_data3()
            else:
                self.get_btPanel_data()
            return self.btPanelData
        elif self.flag == 'xp':
            self.get_xpPanel_data()
            return self.xpPanelData
        elif self.flag == 'one':
            self.get_onePanel_data()
            return self.onePanelData
        elif self.flag == 'mouse':
            self.get_mousePanel_data()
            return self.mousePanelData
        else:
            print("未检测出支持的面板！")
        return {}


    # 判断面板版本
    def main(self):
        # 获取面板
        serverHelper = ServerHelper()
        panel = serverHelper.detect_panel()
        self.path = {}
        if panel == 'bt':
            self.flag = 'bt'
            if serverHelper.detect_bt_version() == 1:
                self.bt_flag = 1
            elif serverHelper.detect_bt_version() == 2:
                self.bt_flag = 2
            else:
                self.bt_flag = 0
        elif panel == 'one':
            self.flag = 'one'
        elif panel == 'xp':
            self.flag = 'xp'
        elif panel == 'mouse':
            self.flag = 'mouse'
        else:
            print(panel)
            return None

        self.get_panel_data()


if __name__ == '__main__':
    Main.main(self=Main())
