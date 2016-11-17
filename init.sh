sudo rm -f /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -s /home/box/web/etc/hello.py /etc/gunicorn.d/test
sudo /etc/init.d/gunicorn stop
sudo killall gunicorn
cd /home/box/web
gunicorn -D -c /home/box/web/etc/hello.py hello:application
cd /home/box/web/ask
gunicorn -D -c /home/box/web/etc/ask.py ask.wsgi:application
#sudo /etc/init.d/mysql start
