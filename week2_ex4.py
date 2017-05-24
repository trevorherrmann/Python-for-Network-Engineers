cisco_ios = "Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.0(1)M4, RELEASE SOFTWARE (fc1)"
cisco_ios_split = cisco_ios.split(",")
version = cisco_ios_split[2]
version_split = version.split()
ios_version = version_split[1]

print "\n\nThe IOS version is: %s\n\n" % ios_version
