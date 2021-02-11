# Python DNS Open Resolver Scanner

## Python3 DNS Open Resolver Scanner

It was written in pure python3 and using the low-level networking interface in
Python's core.


**It's way faster than Nmap. Below is a very simple test using a high-speed network
with very low latency to some known DNS servers around the globe.**

ubuntu@ubuntu:~$ ping 1.1.1.3 -c 5

PING 1.1.1.3 (1.1.1.3) 56(84) bytes of data.

64 bytes from 1.1.1.3: icmp_seq=1 ttl=51 time=3.37 ms

64 bytes from 1.1.1.3: icmp_seq=2 ttl=51 time=3.45 ms

64 bytes from 1.1.1.3: icmp_seq=3 ttl=51 time=3.34 ms

64 bytes from 1.1.1.3: icmp_seq=4 ttl=51 time=3.43 ms

64 bytes from 1.1.1.3: icmp_seq=5 ttl=51 time=3.43 ms


--- 1.1.1.3 ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 4007ms

rtt min/avg/max/mdev = 3.342/3.401/3.445/0.039 ms

ubuntu@ubuntu:~$ time sudo nmap -T5 -n -P0 -sU -p53 --open --script=dns-recursion 1.1.1.3 && time ./scan-dns-openresolvers.py 1.1.1.3

Starting Nmap 7.80 ( https://nmap.org ) at 2021-02-11 17:48 UTC

Nmap scan report for 1.1.1.3

Host is up.


PORT   STATE SERVICE

53/udp open  domain

|_dns-recursion: Recursion appears to be enabled


Nmap done: 1 IP address (1 host up) scanned in 0.74 seconds


real	0m0.763s

user	0m0.241s

sys	0m0.008s



1.1.1.3,open,1613065689

real	0m0.036s

user	0m0.022s

sys	0m0.009s



## One can use this repo to fetch all IP Blocks allocated for a particular country (it's really useful):

[https://github.com/bashrootshell/ip-country-codes]
