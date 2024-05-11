#!/bin/sh
/etc/init.d/xinetd restart

/bin/bash 
socat TCP-LISTEN:3010,reuseaddr,fork EXEC:'su pwn -c /home/pwn/under_the_sea'
sleep infinity