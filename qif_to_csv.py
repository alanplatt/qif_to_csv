#
# Python script to convert qif files to csv
#
import re

outfile = open("output.csv",'w')
# open file object and assign to variable
with open("input.qif") as infile:
  for line in infile:
    if re.match('^[DT].*', line) is not None:
      outfile.write(line.rstrip('\r\n')[1:].strip(',') + ",")
#      print "%s," % line.rstrip('\r\n')[1:],
#    elif re.match('^T.*', line) is not None:
#      print "%s," % line.rstrip('\r\n')[1:],
    elif re.match('^P.*', line) is not None:
      outfile.write(line.rstrip('\r')[1:].strip(','))

outfile.close()


# read file line by line into dictionary
# print file corretly as csv to new file
