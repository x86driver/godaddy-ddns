#!/usr/bin/python

import urllib2
import sys
from pygodaddy import GoDaddyClient

username = "username"
password = "password"

if len(sys.argv) <= 1:
    print("Usage: " + sys.argv[0] + "hostname [ip]")
    sys.exit(1);

hostname = sys.argv[1]

print(hostname)
if len(sys.argv) == 2:
    sys.stdout.write("Get IP...")
    sys.stdout.flush()
    ip = urllib2.urlopen('http://ip.42.pl/raw').read()
if len(sys.argv) == 3:
    ip = sys.argv[2]

print(ip)

client = GoDaddyClient()

print("Logging into GoDaddy...")
if client.login(username, password):
    print("Updating IP...")
    if client.update_dns_record(hostname, ip):
        print("Update OK!")
    else:
        print("Update fail!")
