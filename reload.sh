git pull
source /root/anaconda3/bin/activate django
python manage.py makemigrations
python manage.py migrate
uwsgi --reload uwsgi.pid
echo "Done!"
