import re

MOBILE_TYPE_HOME = 0
MOBILE_TYPE_FOREIGN = 1
MOBILE_REGEX = r"^1[356789]\d{9}$"

def check_mobile_valid(mobile, type):
    if type == MOBILE_TYPE_HOME:
        return re.match(MOBILE_REGEX, mobile)
    return False

def check_password_valid(password):
    if len(password) < 6:
        return False, "密码长度不能少于6位"
    return True, None