import os
import subprocess


class ServerHelper:

    def __init__(self):
        pass

    def exec_command(self,command: str) -> str:
        """
        @command:       要执行的命令
        """
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True
        )
        return result.stdout.strip()

    def detect_bt(self) -> bool:
        cmd1 = 'test -d /www/server/panel && echo "目录存在" || echo "目录不存在"'
        cmd2 = 'test -f /usr/bin/bt && echo "文件存在" || echo "文件不存在"'
        out1 = self.exec_command(cmd1)
        out2 = self.exec_command(cmd2)
        if out1 == '目录存在' and out2 == '文件存在':
            return True
        return False


    def detect_one(self) -> bool:
        cmd1 = 'test -f /usr/bin/1panel && echo "文件存在" || echo "文件不存在"'
        cmd2 = 'test -f /usr/bin/1pctl && echo "文件存在" || echo "文件不存在"'
        out1 = self.exec_command(cmd1)
        out2 = self.exec_command(cmd2)
        if out1 == '文件存在' and out2 == '文件存在':
            return True
        return False


    def detect_xp(self) -> bool:
        cmd1 = 'test -f /usr/bin/xp && echo "文件存在" || echo "文件不存在"'
        cmd2 = 'test -f /usr/local/phpstudy/system/phpstudy && echo "文件存在" || echo "文件不存在"'
        out1 = self.exec_command(cmd1)
        out2 = self.exec_command(cmd2)
        if out1 == '文件存在' and out2 == '文件存在':
            return True
        return False

    def detect_mouse(self) -> bool:
        cmd1 = 'test -f /usr/local/sbin/panel-cli && echo "文件存在" || echo "文件不存在"'
        cmd2 = 'test -f /usr/local/etc/panel/config.yml && echo "文件存在" || echo "文件不存在"'
        out1 = self.exec_command(cmd1)
        out2 = self.exec_command(cmd2)
        if out1 == '文件存在' and out2 == '文件存在':
            return True
        return False

    def detect_panel(self) -> str:
        if self.detect_bt():
            return 'bt'
        if self.detect_one():
            return 'one'
        if self.detect_xp():
            return 'xp'
        if self.detect_mouse():
            return 'mouse'
        return '未找到任何面板'


    def detect_bt_version(self) -> int:
        cmd1 = 'test -f /www/server/panel/data/div.pl && echo "文件存在" || echo "文件不存在"'
        cmd2 = 'test -d /www/server/panel/data/db && echo "目录存在" || echo "目录不存在"'
        out1 = self.exec_command(cmd1)
        out2 = self.exec_command(cmd2)
        if out1 == '文件存在' and out2 == '目录存在':
            return 1
        if out1 == '文件存在' and out2 == '目录不存在':
            return 2
        return 0

