# 好学知单词速记网站

# 从零开始的环境配置(Ubuntu 16.04)
会Docker的话就不用这么麻烦了！！！！
<!-- 0. 安装node, npm, vue-cli等全局环境 -->
* [安装Anaconda Linux](http://docs.continuum.io/anaconda/install/linux/)
* 安装mysql(sudo apt-get install mysql-server libmysqlclient-dev)
* 登录mysql并 create schema xueqing default character set utf8 collate utf8_general_ci;
* 从conda.yaml配置文件中创建或更新Django环境(conda env create/update -f conda.yaml)
* 激活环境(conda activate django)
* 从pip.pkg文件中创建或更新Django环境(pip install -r pip.pkg)
* 修改xueqing/settings.py DATABASES的相关配置（root, 123QWEasd!@#）
* python manage.py makemigrations
* python manage.py migrate
* python manage.py createsuperuser # 可选，创建超级用户，例如用户名(admin)  
  用户名: admin  
  密码: super-admin  
  登录mysql  
  use xueqing;  
  update users_baseinfo set mobile="13051975811", type=1, name="admin" where username="admin"; #修改超级用户的手机号  
* 安装Nginx（sudo apt-get install nginx）
* 修改Nginx的配置文件

# 产品原型
https://b9zvtw.axshare.com/

# TODO
* mysql 划分用户权限
* 短信验证码一次一密
* 关闭API Root
