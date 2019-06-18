PROJECT_DIR = '/root/python/Xueqing'

echo 'start'
cd $PROJECT_DIR
echo 'pull code'
# git reset --hard origin/master && git clean -f
# git pull && git checkout master
git pull
source /root/anaconda3/bin/activate django
pip install -r pip.pkg
python manage.py makemigrations
python manage.py migrate
uwsgi --reload uwsgi.pid
echo "Done!"
