import sys, os
import re
# f = open("cardinals-1940.txt")
if len(sys.argv) < 2:
	sys.exit("Usage: %s filename" % sys.argv[0])
 
filename = sys.argv[1]
 
if not os.path.exists(filename):
	sys.exit("Error: File '%s' not found" % sys.argv[1])
	
f = open(filename, "r")

class Player(object):
	def __init__(self, name):
		self.name = name
	def getAvg(self):
		batTotal = 0
		hitTotal = 0
		f = open(filename, "r")
		for line in f:
			if self.name in line:
				batpat="\\bbatted\s\d\\b"
				r1 = re.search(batpat, line)
				batted = r1.group()
				r2 = re.search("\d", batted)
				numBat = float(r2.group())
				batTotal = batTotal+numBat
				hitpat="\\b\d\shits\\b"
				r3 = re.search(hitpat, line)
				hit = r3.group()
				r4 = re.search("\d", hit)
				numHit = float(r4.group())
				hitTotal = hitTotal + numHit
		# print batTotal
		# print hitTotal
		avg = hitTotal/batTotal
		return "%s:%.3f" %(self.name, avg)
	def who(self):
		print self.name
name = []
with open(filename) as f_in:
    lines = (line.rstrip() for line in f_in) 
    lines = list(line for line in lines if line and not line.startswith('#') and not line.startswith('=')) # Non-blank lines in a list
for line in lines:
	# namepat = "^\\b\w+\s\w+\\b"
	# r5 = re.search(namepat, line)
	# name = r5.group()
	#Player(name).getAvg
	nameSplit = line.split(" ", 2)
	name.append("%s %s" % (nameSplit[0], nameSplit[1]))
keep = set(name)
avg = []
test = []
for thing in keep:
	player = Player(thing)
	gotAvg = player.getAvg()
	avg.append(gotAvg)
for item in avg:
	test.append(tuple(item.split(":", 2)))
sorted = sorted(test, key=lambda tup: tup[1], reverse=True)
for thing in sorted:
	print thing