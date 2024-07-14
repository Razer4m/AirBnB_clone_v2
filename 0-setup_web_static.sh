#!/usr/bin/env bash
# Update package lists
sudo apt-get update -y
sudo apt-get -y upgrade
# Install Nginx if not already installed
if ! command -v nginx &> /dev/null
then
	sudo apt-get install -y nginx
fi
# Create the required directories
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
# Create a fake HTML file
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
# Give ownership of /data/ folder to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/i
# Update the Nginx configuration
CONFIG="server {
    listen 80 default_server;
    listen [::]:80 default_server;
    root /var/www/html;

    index index.html index.htm;

    server_name _;

    location /hbnb_static/ {
        alias /data/web_static/current/;
    }

    location / {
        try_files \$uri \$uri/ =404;
    }
}"

echo "$CONFIG" > /etc/nginx/sites-available/default

# Restart Nginx to apply the changes
sudo service nginx restart

exit 0
