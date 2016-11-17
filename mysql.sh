sudo /etc/init.d/mysqld start
sudo mysql -u root -e "CREATE DATABASE box_django CHARACTER SET utf8"
sudo mysql -u root -e "CREATE USER 'box'@'localhost' IDENTIFIED BY '1234'"
sudo mysql -u root -e "GRANT ALL PRIVELEGES ON box_django.* TO 'box'@'localost'"
