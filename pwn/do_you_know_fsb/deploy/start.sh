#!/bin/sh
/etc/init.d/xinetd restart

/bin/bash 
socat TCP-LISTEN:2011,reuseaddr,fork EXEC:'su pwn -c /home/pwn/fsb'
sleep infinity