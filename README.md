# Python DNS Open Resolver Scanner

## Python3 DNS Open Resolver Scanner

**It was written in pure python3 and using the low-level networking interface in Python's core.**

**Intended to be used with _1 argument_ (e.g. 8.8.8.8 or 10.10.0.0/16 as examples.)**

**If parallelism is extremely necessary, GNU parallel is _highly_ recommended.**

**It's way faster than Nmap. Below is a very simple test using a high-speed network**
**with very low latency to some known DNS servers around the globe.**


└─$ time sudo nmap -T5 -n -P0 -sU -p53 --open --script=dns-recursion 1.1.1.3 && time ./scan-dns-openresolvers.py 1.1.1.3
Starting Nmap 7.94 ( https://nmap.org ) at 2023-06-20 17:54 UTC
Nmap scan report for 1.1.1.3
Host is up (0.0033s latency).

PORT   STATE SERVICE
53/udp open  domain
|_dns-recursion: Recursion appears to be enabled

Nmap done: 1 IP address (1 host up) scanned in 0.23 seconds

real    0m0.266s
user    0m0.000s
sys     0m0.010s
1.1.1.3,open,1687283676

real    0m0.035s
user    0m0.030s
sys     0m0.000s




## One can use this repo to fetch all IP Blocks allocated for a particular country (it's really useful):

[https://github.com/bashrootshell/ip-country-codes]
