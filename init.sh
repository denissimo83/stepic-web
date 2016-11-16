sudo rm -f /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -s /home/box/web/etc/hello.py /etc/gunicorn.d/test
sudo /etc/init.d/gunicorn stop
cd /home/box/web
gunicorn -D -c ./etc/hello.py hello:application
sudo /etc/init.d/mysql start
