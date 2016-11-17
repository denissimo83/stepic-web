sudo /etc/init.d/mysqld start
sudo /etc/init.d/mysql start
sudo mysql -u root -e "CREATE DATABASE box_django CHARACTER SET utf8"
sudo mysql -u root -e "CREATE USER 'box'@'localhost' IDENTIFIED BY '1234'"
sudo mysql -u root -e "GRANT ALL PRIVILEGES ON box_django.* TO box@'localhost'"
sudo mysql -u root -e "FLUSH PRIVILEGES"
