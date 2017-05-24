#!/usr/bin/env python

import sys

if len(sys.argv) != 2:
    #Exit Script
    sys.exit ("Usage: ./week3_ex1.py <ip_address>")

ip_address = sys.argv.pop()
octets = ip_address.split(".")
ip_addr_bin = []

if len(octets) == 4:

    for octet in octets:

        octet_bin = bin(int(octet))

        # Strip 0b from string
        octet_bin = octet_bin[2:]

        # prepend 0 until 8 characters long
        while True:
            if len(octet_bin) >= 8:
                break
            octet_bin = '0' + octet_bin
        #add octet to list
        ip_addr_bin.append(octet_bin)

    ip_addr_bin = ".".join(ip_addr_bin)
    print ip_addr_bin
    print "\n%-15s %-45s" % ("IP Address", "Binary")
    print "\n%-15s %-45s" % (ip_address, ip_addr_bin)

else:
    sys.exit("Invalid IP address entered")
