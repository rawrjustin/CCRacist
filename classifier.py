import sys

if (len(sys.argv) > 1):
	PATH = sys.argv[1]
else:
	print "Needs argument: path of last name file"

class Racist:
	def __init__(self):
		#asians (top 1000) (top 1000)
		asians = open('./asians.txt',"r")
		self.asiannames = asians.read().lower()
		asians.close()
		#asians (manually classified)
		asians2 = open('./asian2.txt',"r")
		self.asiannames2 = asians2.read().lower()
		asians2.close()

		#blacks (top 1000)
		blacks = open('./blacks.txt',"r")
		self.blacknames = blacks.read().lower()
		blacks.close()

		#hispanics (top 1000)
		hispanics = open('./hispanics.txt',"r")
		self.hispanicnames = hispanics.read().lower()
		hispanics.close()
		#hispanics (manually classified)
		hispanics2 = open('./hispanic2.txt',"r")
		self.hispanicnames2 = hispanics2.read().lower()
		hispanics2.close()

		#whites (top 1000)
		whites = open('./whites.txt',"r")
		self.whitenames = whites.read().lower()
		whites.close()
		#whites (manually classified)
		whites2 = open('./white2.txt',"r")
		self.whitenames2 = whites2.read().lower()
		whites2.close()

		self.numasians = 0
		self.numblacks = 0
		self.numhispanics = 0
		self.numwhites = 0
		self.unknown = 0
		self.total = 0
	
	def tellRaceDistribution(self):
		print "Total Amount of People Clasified: " + str(self.total)
		print "asians: " + str(self.numasians) + " (" + str(float(self.numasians)/float(self.total)*100)[:5] + "%)"
		print "blacks: " + str(self.numblacks) + " (" + str(float(self.numblacks)/float(self.total)*100)[:5] + "%)"
		print "whites: " + str(self.numwhites) + " (" + str(float(self.numwhites)/float(self.total)*100)[:5] + "%)"
		print "hispanics: " + str(self.numhispanics) + " (" + str(float(self.numhispanics)/float(self.total)*100)[:5] +"%)"
		print "unclassified: " + str(self.unknown) + " (" + str(float(self.unknown)/float(self.total)*100)[:5] + "%)"


	def judgePeopleByLastName(self, fileinputPATH):
		datafile = open(fileinputPATH,"r")
		
		for aline in datafile:
			line = aline.lower().strip()

			self.total+=1
			#bias for counting asians, followed by whites, by hispanics, by blacks
			if line in self.asiannames or line in self.asiannames2:
				self.numasians += 1
			elif line in self.whitenames or line in self.whitenames2:
				self.numwhites += 1
			elif line in self.hispanicnames or line in self.hispanicnames2:
				self.numhispanics += 1
			elif line in self.blacknames:
				self.numblacks += 1
			
			else:
				#print the aliens (unclassified lastnames) if you'd like
				#u = open('unknown_names.txt', 'w')
				#u.write(line)
				#u.close()
				self.unknown += 1
				#print line
		datafile.close()

sagar = Racist()
sagar.judgePeopleByLastName(PATH)
sagar.tellRaceDistribution()

