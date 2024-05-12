#!/bin/sh
/etc/init.d/xinetd restart

/bin/bash 
socat TCP-LISTEN:2013,reuseaddr,fork EXEC:'su pwn -c /home/pwn/run_shell'
sleep infinity