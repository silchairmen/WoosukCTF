#!/bin/sh
/etc/init.d/xinetd restart

/bin/bash 
socat TCP-LISTEN:2012,reuseaddr,fork EXEC:'su pwn -c /home/pwn/noob_oob'
sleep infinity