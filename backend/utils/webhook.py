from xueqing.settings import BASE_DIR
import os
from threading import Thread

SECRET = "YzfCGkrIIWZUtnkU4RiFkBdO4Eyjrrm9"
RELOAD_CMD = "bash reload.sh"

def reload():
    Thread(target=__reload).start()

def __reload():
    os.chdir(BASE_DIR)
    os.system(RELOAD_CMD)