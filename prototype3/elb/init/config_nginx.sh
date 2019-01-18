#!/bin/bash
sudo apt-get update -y
sudo apt-get install nginx -y
# git clone https://github.com/Joy57/4996wsu-Senior-Project.git
# cd 4996wsu-Senior-Project
# cd configFiles
sudo rm /etc/nginx/nginx.conf
sudo rm /etc/nginx/sites-enabled/default
sudo cp nginx.conf /etc/nginx/nginx.conf
sudo cp default /etc/nginx/sites-enabled/default
sudo service nginx restart
chmod u+x init.sh
echo "completed all steps..."
echo "now you can run init.sh"