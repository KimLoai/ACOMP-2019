#!/bin/bash

ab -p ~/nwdisk/script/a.txt -c 16 -n 65000 http://10.28.8.70:19090/httplistener

./wrk -t32 -c32 -d100s -s ./post.lua http://10.28.8.70:19090/httplistener
