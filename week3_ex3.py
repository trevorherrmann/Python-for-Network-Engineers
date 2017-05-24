#!/usr/bin/env python

import pprint

show_ip_int_brief = '''
Interface            IP-Address      OK?     Method      Status     Protocol
FastEthernet0   unassigned      YES     unset          up          up
FastEthernet1   unassigned      YES     unset          up          up
FastEthernet2   unassigned      YES     unset          down      down
FastEthernet3   unassigned      YES     unset          up          up
FastEthernet4    6.9.4.10          YES     NVRAM       up          up
NVI0                  6.9.4.10          YES     unset           up          up
Tunnel1            16.25.253.2     YES     NVRAM       up          down
Tunnel2            16.25.253.6     YES     NVRAM       up          down
Vlan1                unassigned      YES    NVRAM       down      down
Vlan10              10.220.88.1     YES     NVRAM       up          up
Vlan20              192.168.0.1     YES     NVRAM       down      down
Vlan100            10.220.84.1     YES     NVRAM       up          up
'''

#Break into multiple lines
ip_lines = show_ip_int_brief.split('\n')

#Create blank list to append to
final_list = []

for line in ip_lines:

    #skip header
    if "Interface" in line:
        continue

    #break lines into words
    line_split = line.split()

    #filter out lines that don't have the correct number of fields
    if len(line_split) == 6:

        #map to variables
        if_name, ip_addr, discard1, discard2, if_status, if_proto = line_split

        if (if_status == 'up') and (if_proto == 'up'):
            final_list.append((if_name, ip_addr, if_status, if_proto))
print "\n"

pprint.pprint(final_list)

print "\n"
