ip_address = raw_input("\n\nPlease enter an IP Address in dotted decimal format: ")
octets = ip_address.split(".")
first_octet_bin = bin(int(octets[0]))
second_octect_bin = bin(int(octets[1]))
third_octect_bin = bin(int(octets[2]))
fourth_octet_bin = bin(int(octets[3]))

print "\n\n"
print "%15s %15s %15s %15s" % ("first_octet", "second_octet", "third_octet", "fourth_octet")
print "%15s %15s %15s %15s" % (first_octet_bin, second_octect_bin, third_octect_bin, fourth_octet_bin)
print "\n\n"
