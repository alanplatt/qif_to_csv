#
# Python script to convert qif files to csv
#
import re

outfile = open("output.csv",'w')

with open("input.qif") as infile:
  for line in infile:
    if re.match('^[DT].*', line) is not None:
      outfile.write(line.rstrip('\r\n')[1:].strip() + "\t")
    elif re.match('^P.*', line) is not None:
      outfile.write(line.rstrip('\r')[1:])

outfile.close()

