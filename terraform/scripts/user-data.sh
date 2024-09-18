#!/bin/bash
yum update -y
yum install -y httpd
systemctl start httpd
systemctl enable httpd
echo "<h1>Hola Mundo desde $(hostname -f)</h1>" >/var/www/html/index.html
