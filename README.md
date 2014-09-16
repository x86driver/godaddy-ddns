godaddy-ddns
============

It can update godaddy dns record with current ip address.

Setup
============

Modify username and password in godaddy.py

Usage
============
```shell
$ ./godaddy.py hostname [ip]
```

IP address is optional. If you don't specify ip address, it will get ip address using http://ip.42.pl/raw automatically.
