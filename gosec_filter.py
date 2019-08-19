import re
from filter_definition import the_gosec_filter
from filter_definition import GosecWarning

pattern = "\[([^\]]+)\] - (.+)"
p = re.compile(pattern)
warnings = []

with open("gosec_report.txt") as file: # Use file to refer to the file object

   data = file.readlines()

   count = 0
   obj = GosecWarning()
   for line in data:
      count = count + 1
      if count > 4:
          #print line,
          if line[0] == "[":
              m = p.match(line)
              #print line,
              if m != None:
                  #print m.group(0)
   		  obj = GosecWarning(location=m.group(1),error=m.group(2),store=True)
                  #print "Location: " + m.group(1)
                  #print "Error:    " + m.group(2)
              else:
                  #print "No match"
                  pass
          elif line[:4] == "  > ":
              #print "Code: %s" % (line[4:])
              if obj.store:
                  obj.code = line[4:].strip()
                  warnings.append(obj)

for x in warnings:
    if x not in the_gosec_filter:
	    print x
