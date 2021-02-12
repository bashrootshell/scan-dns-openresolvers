#!/usr/bin/env python3

from sys import argv
from time import time
from ipaddress import ip_network
from random import shuffle
import socket as com

"""
    Python DNS Open Resolver Scanner
    Originally written in 2013 in Python2. Refactored in 2021 with Python3.
    It still uses Pure Python and the Low-level networking interface.
    It's faster than nmap dns-recursion script, even for a large CIDR network.

    PEP8 compliant
    “Readability counts."
    “Beautiful is better than ugly.”
    — The Zen of Python
"""

''' set BSD socket to use a UDP datagram '''

packet = com.socket(com.AF_INET, com.SOCK_DGRAM)
packet.settimeout(0.150)  # adjust timout according to your network latency

''' DNS type "A" set to l.root-servers.net as hexadecimal value '''

payloadhex = 'ff0001000001000000000000016c0c726f6f742d73657276657273036e6574\
0000010001'

iplist = []

''' check if there's an argument, and check if IP address is larger than a /32.
if not, there's 1 IP only in the list '''

if len(argv) == 1:
    exit("Provide a single IP Address or an IP/CIDR format as the argument.")
elif ip_network(argv[1]).num_addresses > 1:
    iplist = [ipaddr for ipaddr in ip_network(argv[1]).hosts()]
else:
    iplist.append(argv[1])  # only one IP address in the list

shuffle(iplist)

for prefix in iplist:
    try:
        ''' send the payloadhex to hosts in the list (port 53 (DNS)) '''

        packet.sendto(bytes.fromhex(payloadhex), (str(prefix), int(53)))
        response = packet.recv(128)
        ''' if response contains valid DNS response with the correct
        l.root-servers.net's IP address and type A query, it's open '''

        if (b'\xc0\x0c\x00\x01\x00\x01' and b'\x00\x04\xc7\x07') in response:
            nixtime = int(time())
            print(f'{prefix},open,{nixtime}')

    except com.timeout:
        continue
