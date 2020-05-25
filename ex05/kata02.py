import datetime

#t = (3, 30, 2019, 9, 25)

#hour = t[0]
#min = t[1]
#year = t[2]
#month = t[3]
#day = t[4]
#print("{:0>2d}/{:0>2d}/{} {:0>2d}:{:0>2d}".format(month, day, year, hour, min))

print("{3:0>2d}/{4:0>2d}/{2} {0:0>2d}:{1:0>2d}".format(*(3, 30, 2019, 9, 25)))
# 09/25/2019 03:30