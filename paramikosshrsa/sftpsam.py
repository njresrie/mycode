#!/usr/bin/env python3

import paramiko
import os

def commandissue(command_to_issue):
    ssh_stdin, ssh_stdout, ssh_stderr = sshsession.exec_command(command_to_issue)
    return ssh_stdout.read()

sshsession = paramiko.SSHClient()

sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())

sshsession.connect("10.10.2.3", username="bender", password="alta3")

our_commands = ["netstat -nr", "uptime", "pwd", "df -h"]

for x in our_commands:
    print(commandissue(x))

sshsession.close()

