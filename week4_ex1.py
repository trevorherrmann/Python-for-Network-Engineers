#!/usr/bin/env python

import sys

#if len(sys.argv) != 2:
    #check to make sure input is correct
    #sys.exit("Usage: ./week3_ex4.py <ip_address>")

not_done = True

#check to validate that there are 4 octets in the IP address
while not_done:
    ip_addr = raw_input("\nPlease enter an IP address: ")
    valid_ip = True
    octets = ip_addr.split(".")
    if len(octets) != 4:
        print "Incorrect number of octets in the IP, must equal 4, plese try again\n"
        valid_ip = False
        continue

    #assign variables
    octet_1, octet_2, octet_3, octet_4 = octets

    #check first octet validity
    if int(octet_1) < 1:
        print "Invalid first octet, must be greater than 1, please try again\n"
        valid_ip = False
    elif int(octet_1) > 223:
        print "Invalid first octet, must be less than 223, please try again\n"
        valid_ip = False
    elif int(octet_1) == 127:
        "Invalid first octet, must not be 127, please try again\n"
        valid_ip = False

    #check self-assigned
    if int(octet_1) == 169 and int(octet_2) == 254:
        print "Invalid IP address, self-assigned, please try again\n"
        valid_ip = False

    #check the last three octets are between 0 and 255
    for octet in (octet_2, octet_3, octet_4):
        if (int(octet) < 0) or (int(octet) > 255):
            valid_ip = False
    #break out of while
    if valid_ip == True:
        not_done = False

print "\nIP address %s valid!\n" % ip_addr
