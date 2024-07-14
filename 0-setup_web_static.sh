#!/usr/bin/env bash
# Update package lists
apt-get update -y
apt-get -y upgrade
# Install Nginx if not already installed
if ! command -v nginx &> /dev/null
then
	apt-get install -y nginx
fi
# Create the required directories
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
# Create a fake HTML file
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
# Give ownership of /data/ folder to ubuntu user and group
chown -R ubuntu:ubuntu /data/
chgrp -R ubuntu /data/
# Update the Nginx configuration
CONFIG="server {
    listen 80 default_server;
    listen [::]:80 default_server;
    root /var/www/html;

    index index.html index.htm;

    server_name _;

    location /hbnb_static/ {
        alias /data/web_static/current/;
        index index.html index.htm;
    }

    location /redirect_me {
        return 301 http://cuberule.com/;
    }

    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}"

echo "$CONFIG" > /etc/nginx/sites-available/default

# Restart Nginx to apply the changes
service nginx restart

exit 0
