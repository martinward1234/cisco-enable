#!/usr/bin/python

# A script to ssh into a cisco device, set the terminal length
# such that paging is turned off, then run commands.
# the results go into 'resp', then are displayed.
# Tweak to your hearts content!

import paramiko
import cmd
import time
import sys


buff = ''
resp = ''

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('172.16.1.69', username='python', password='python')
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
(print) ("SSH connection established, please wait for output...")
chan = ssh.invoke_shell()

# first we enable!
chan.send('enable\r\n')
time.sleep(0.5)
resp = chan.recv(1024)
(print) (resp)

# enablepassword!
chan.send('python\r\n')
time.sleep(0.5)
resp = chan.recv(1024)
(print) (resp)

# turn off paging
chan.send('terminal length 0\r\n')
time.sleep(0.5)
resp = chan.recv(1024)
(print) (resp)

# Issue the Show Run command to prove script function
chan.send('sh run\r\n')
time.sleep(7.5)
resp = chan.recv(10240)
(print) (resp.splitlines())
