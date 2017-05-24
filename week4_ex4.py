#!/usr/bin/env python

import pprint

DEBUG = False

MINUTE_SECONDS = 60
HOUR_SECONDS = 60 * MINUTE_SECONDS
DAY_SECONDS = 24 * HOUR_SECONDS
WEEK_SECONDS = 7 * DAY_SECONDS
YEAR_SECONDS = 365 * DAY_SECONDS

uptime1 = 'twb-sf-881 uptime is 6 weeks, 4 days, 2 hours, 25 minutes'
uptime2 = '3750RJ uptime is 1 hour, 29 minutes'
uptime3 = 'CATS3560 uptime is 8 weeks, 4 days, 18 hours, 16 minutes'
uptime4 = 'rtr1 uptime is 5 years, 18 weeks, 8 hours, 23 minutes'

uptime_dict = {}

for uptime in (uptime1, uptime2, uptime3, uptime4):
    uptime_fields = uptime.split(",")

    #extract hostname from the uptime fields
    (hostname, time_field1) = uptime_fields[0].split(' uptime is ')
    uptime_fields[0] = time_field1

    if DEBUG:
        print hostname
        print uptime_fields

    #initialize uptime seconds
    uptime_seconds = 0

    #iterate through the uptime fields
    for time_field in uptime_fields:

        #convert years to seconds
        if 'years' in time_field:
            (years, junk) = time_field.split()
            try:
                uptime_seconds += int(years) * YEAR_SECONDS
            except ValueError:
                print "Error, during string conversion to integer"

        #convert weeks to seconds
        if 'weeks' in time_field:
            (weeks, junk) = time_field.split()
            try:
                uptime_seconds += int(weeks) * WEEK_SECONDS
            except ValueError:
                print "Error, during string conversion to integer"

        #convert days to seconds
        if 'days' in time_field:
            (days, junk) = time_field.split()
            try:
                uptime_seconds += int(days) * DAY_SECONDS
            except ValueError:
                print "Error, during string conversion to integer"

        #convert hours to seconds
        if 'hours' in time_field:
            (hours, junk) = time_field.split()
            try:
                uptime_seconds += int(hours) * HOUR_SECONDS
            except ValueError:
                print "Error, during string conversion to integer"

        #convert minutes to seconds
        if 'minutes' in time_field:
            (minutes, junk) = time_field.split()
            try:
                uptime_seconds += int(minutes) * MINUTE_SECONDS
            except ValueError:
                print "Error, during string conversion to integer"

        #add the seconds
        if 'seconds' in time_field:
            (seconds, junk) = time_field.split()
            try:
                uptime_seconds += int(seconds)
            except ValueError:
                print "Error, during string conversion to integer"

    uptime_dict[hostname] = uptime_seconds

print
pprint.pprint(uptime_dict)
print
