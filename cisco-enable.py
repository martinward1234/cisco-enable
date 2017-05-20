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
ssh.connect('172.16.1.69', username='cisco', password='cisco')
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
chan = ssh.invoke_shell()

# first we enable!
chan.send('en\n')
time.sleep(1)
resp = chan.recv(9999)
#print resp

# enablepassword!
chan.send('cisco\n')
time.sleep(1)
resp = chan.recv(9999)
#print resp

# get into config mode
# chan.send('conf t\n')
# time.sleep(1)
# resp = chan.recv(9999)
#print resp

# turn off paging
chan.send('terminal pager 0\n')
time.sleep(1)
resp = chan.recv(9999)
#print resp

# Display how many users are connected to the IPSEC vpn
chan.send('sh run\n')
time.sleep(10)
resp = chan.recv(655355)
(print) (resp)
