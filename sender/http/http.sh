#!/bin/bash

# How to send data by ab
echo a > a.txt
ab -p a.txt -c 8 -n 10000 http://10.28.8.86 :19090/httplistener
# How to install ab
sudo apt install apache2-utils


# How to send data by wrk
./wrk -t8 -c8 -d100s -s ./post.lua http://10.28.8.86:19090/httplistener
# How to install wrk
sudo apt-get install build-essential libssl-dev git -y
git clone https://github.com/wg/wrk.git wrk
cd wrk; make; sudo cp wrk /usr/local/bin

# How to send data by curl
curl -X POST --data 'a' 'http://10.28.8.86:19090/httplistener'

# How to install
sudo apt install curl
