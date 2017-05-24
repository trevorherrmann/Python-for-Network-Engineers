#!/usr/bin/env python

import sys

if len(sys.argv) != 2:
    #check to make sure input is correct
    sys.exit("Usage: ./week3_ex4.py <ip_address>")

ip_addr = sys.argv.pop()

octets = ip_addr.split(".")

#check to validate that there are 4 octets in the IP address
if len(octets) != 4:
    sys.exit("Incorrect number of octets in the IP, must equal 4")

#assign variables
octet_1, octet_2, octet_3, octet_4 = octets

#check first octet validity
if int(octet_1) < 1:
    sys.exit("Invalid first octet, must be greater than 1")
elif int(octet_1) > 223:
    sys.exit("Invalid first octet, must be less than 223")
elif int(octet_1) == 127:
    sys.exit("Invalid first octet, must not be 127")

#check self-assigned
if int(octet_1) == 169 and int(octet_2) == 254:
    sys.exit("Invalid IP address, self-assigned")

#check the last three octets are between 0 and 255
for octet in (octet_2, octet_3, octet_4):
    if (int(octet) < 0) or (int(octet) > 255):
        sys.exit("Invalid IP addres, last three octets must be between 0 and 255")

print "\nIP address valid!\n"
