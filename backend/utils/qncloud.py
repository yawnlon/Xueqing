import qiniu

ACCESS_KEY = 'U9zpiGXmGCSvvTF_M-G7eb4lhu7mamNBwXFYPBlN'
SECRET_KEY = 'ZutkqcJKiqMS4K_JDTky2s4k6td8UWBQLTrGiolW'
BUCKET_NAME = 'xueqing'
TOKEN_EXPIRED_TIME = 3600  # 单位 sec
UPLOAD_DOMAIN = 'up-z1.qiniup.com'
DOWNLOAD_DOMAIN = 'xueqing-qn.yawnlon.cn'

q = qiniu.Auth(ACCESS_KEY, SECRET_KEY)

def gen_token():
    policy = {}
    return q.upload_token(BUCKET_NAME, None, TOKEN_EXPIRED_TIME, policy)