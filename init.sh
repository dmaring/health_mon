#!/bin/bash
apt-get update -y &&
apt-get install wget fontconfig libfreetype6 libjpeg62-turbo \
    libpng16-16 libx11-6 libxcb1 libxext6 libxrender1 xfonts-75dpi \
    xfonts-base -y
apt --fix-broken install -y
# Download wkhtmltopdf deb package
wget https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-1/wkhtmltox_0.12.6-1.buster_amd64.deb
dpkg -i wkhtmltox_0.12.6-1.buster_amd64.deb
cp /usr/local/bin/wkhtmlto* /usr/bin/


