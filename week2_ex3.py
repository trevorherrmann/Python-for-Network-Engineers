entry1 = "*  1.0.192.0/18   157.130.10.233        0 701 38040 9737 i"
entry2 = "*  1.1.1.0/24      157.130.10.233         0 701 1299 15169 i"
entry3 = "*  1.1.42.0/24     157.130.10.233        0 701 9505 17408 2.1465 i"
entry4 = "*  1.0.192.0/19   157.130.10.233        0 701 6762 6762 6762 6762 38040 9737 i"

print "\n\n"
print "%-20s %-50s\n" % ("Prefix", "AS_Path")

#entry1 Breakup
entry1_split = entry1.split()
entry1_prefix = entry1_split[1]
entry1_as_path = entry1_split [4:-1]
print "%-20s %-50s\n" % (entry1_prefix, entry1_as_path)

#entry2 Breakup
entry2_split = entry2.split()
entry2_prefix = entry2_split[1]
entry2_as_path = entry2_split [4:-1]
print "%-20s %-50s\n" % (entry2_prefix, entry2_as_path)

#entry3 Breakup
entry3_split = entry3.split()
entry3_prefix = entry3_split[1]
entry3_as_path = entry3_split [4:-1]
print "%-20s %-50s\n" % (entry3_prefix, entry3_as_path)

#entry4 Breakup
entry4_split = entry4.split()
entry4_prefix = entry4_split[1]
entry4_as_path = entry4_split [4:-1]
print "%-20s %-50s\n" % (entry4_prefix, entry4_as_path)
