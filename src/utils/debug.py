from datetime import datetime
from colorama import init, Back
init(autoreset=True)

class Logger:
    def __init__(self, name, displayName=False, enabled=True):
        self.name = name
        self.display = displayName
        self.enabled = enabled 

    def _timestamp(self):
        now = datetime.now()
        return now.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]  

    def warn(self, text):
        if self.enabled:
            if self.display:
                print(f"{Back.YELLOW}[{self._timestamp()}] [{self.name}] [*] {text}")
            else:
                print(f"{Back.YELLOW}[{self._timestamp()}] [*] {text}")

    def info(self, text):
        if self.enabled:
            if self.display:
                print(f"{Back.BLUE}[{self._timestamp()}] [{self.name}] [i] {text}")
            else:
                print(f"{Back.BLUE}[{self._timestamp()}] [i] {text}")

    def error(self, text):
        if self.enabled:
            if self.display:
                print(f"{Back.RED}[{self._timestamp()}] [{self.name}] [!] {text}")
            else:
                print(f"{Back.RED}[{self._timestamp()}] [!] {text}")