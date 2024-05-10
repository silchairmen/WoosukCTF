#!/bin/sh
/etc/init.d/xinetd restart

/bin/bash 
socat TCP-LISTEN:2010,reuseaddr,fork EXEC:'su pwn -c /home/pwn/i_hate_auth_key'
sleep infinity