#!/usr/bin/env bash
#Prepare your web servers 
if ! which nginx > /dev/null 2>&1; then
sudo apt-get -y update
sudo apt-get -y install nginx
sudo servce nginx start
fi
mkdir -p /data/web_static/releases/test
mkdir -p /data/web_static/shared
echo -e "
<html>
    <head></head>
    <body>
        Holberton School
    </body>
</html>" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test /data/web_static/current
chown -R ubuntu:ubuntu /data/
sudo sed -i '40 i\ \tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\tindex index.html;\n\t}\n' /etc/nginx/sites-enabled/default
sudo service nginx restart

