from xueqing.settings import BASE_DIR
import os
from threading import Thread

SECRET = "YzfCGkrIIWZUtnkU4RiFkBdO4Eyjrrm9"
RELOAD_CMD = "bash reload.sh"

def reload():
    Thread(target=do_reload).start()

def do_reload():
    os.chdir(BASE_DIR)
    os.system(RELOAD_CMD)