from xueqing.settings import BASE_DIR
import os

SECRET = "YzfCGkrIIWZUtnkU4RiFkBdO4Eyjrrm9"
RELOAD_CMD = "bash reload.sh"

def do_reload():
    os.chdir(BASE_DIR)
    os.system(RELOAD_CMD)