#!/usr/bin/env python3

from sys import argv
from time import time
from ipaddress import ip_network as net
from socket import socket, AF_INET, SOCK_DGRAM, setdefaulttimeout, timeout

"""
    --- Python DNS Open Resolver Scanner ---
    Originally written in 2013 in Python2. Refactored in 2021/22 for Python3.
    It still uses Pure Python and the Low-level Python networking interface.

    PEP8 compliant
    “Readability counts."
    “Beautiful is better than ugly.”
    — The Zen of Python
"""

''' build a packet using BSD Socket UDP datagram for "l.root-servers.net" '''

PAYLOADHEX = 'ff0001000001000000000000016c0c726f6f\
              742d73657276657273036e65740000010001'

PREFIX = argv[1] if len(argv) == 2 else exit("Provide one HOST IP Address or \
one NETWORK IP/CIDR as argument.")

if ('/31' in PREFIX or '/32' in PREFIX):
    exit("Use a unique host address. Ex: 1.1.1.1 instead of 1.1.1.1/31 or /32")


def iplist():

    try:

        for IPADDRESS in net(PREFIX).hosts():
            yield IPADDRESS

    except ValueError as error:
        print(f'iplist() function Error >>> {error}')


for HOST in iplist():

    setdefaulttimeout(0.05)

    try:

        with socket(AF_INET, SOCK_DGRAM) as packet:

            ''' send PAYLOADHEX to HOSTs in the list using port 53 '''
            
            packet.connect((str(HOST), 53))
            packet.send(bytes.fromhex(PAYLOADHEX))
            RESPONSE = packet.recv(64)

            ''' check if RESPONSE contains a valid DNS RESPONSE with
                l.root-servers.net's IP address 199.7.83.42
                It also checks if recursion is disabled with x81x85 flag '''

            if (b'\x01\x6c\x0c\x72\x6f\x6f\x74\x2d\x73' 
                and b'\xc0\x0c\x00\x01\x00\x01' 
                and b'\x00\x04\xc7\x07') in RESPONSE:  # 199.7.83.42
                
                print(f'{HOST},open,{int(time())}')

            elif (b'\x81\x05') in RESPONSE:  # recursion disabled on server
                
                print(f'{HOST},not_an_open_resolver,{int(time())}')

    except timeout:
        print(f'{HOST},timeout_or_port53_not_open,{int(time())}')
        continue

    except ValueError as error:
        print(f'Error >>> {error}')

    except KeyboardInterrupt:
        exit('Program execution interrupted.')
