#! /usr/bin/env	 python
the_world_is_flat = 1
if the_world_is_flat:
	print "Be careful not to fall off!"
else:
	print "Yes it's not flat!"

the_world_is_flat = "ALP SAYIN"

i = 1
while i<10:
	print the_world_is_flat
	i+=1
	print i

print i

def fib(n):
	"""Print a Fibonacci series up to n."""
	x = [1]
	a,b  = 0,1
	while a < n:
		x[len(x)-1] = a
		print a,
		a, b = b, a+b
	return x
fib(5)
print ""
fib(10);

def cheeseshop(kind, *arguments, **keywords):
	"""This is the the cheeseshop documentation string
	"""
	print "-- Do you have any", kind, "?"
	print "-- I'm sorry, we're all out of", kind
	for arg in arguments:
		print arg
	print "-" * 40
	keys = sorted(keywords.keys())
	for kw in keys:
		print kw, ":", keywords[kw]

cheeseshop("Limburger",
 	"It's very runny, sir.",
	"It's really very, VERY runny, sir.",
	shopkeeper='Michael Palin',
	client="John Cleese",
	sketch="Cheese Shop Sketch",
	time="20.07.2012")

print cheeseshop.__doc__

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
	print 'What is your {0}?  It is {1}.'.format(q, a)

def alp():
	print "Alp Sayin",

if __name__ == "__main__":
	alp()
	fib(150)
	import sys
	print ""
	mapped = {}
	for i in range(len(sys.argv)):
		print i, sys.argv[i]
		mapped[sys.argv[i]]=i
	for k in sys.argv:
		print k

	print mapped

	if len(sys.argv) >= 3:
		print 'First arg is {} and second arg is {}'.format(sys.argv[1], sys.argv[2]);
		print 'Second arg is {1} and first arg is {0}'.format(sys.argv[1], sys.argv[2]);

	import math
	print "pi = %5.8f" % math.pi

	try:
		f = open('pickleDump.txt', 'w+')
		import pickle
		pickle.dump(fib(10), f)
		f.seek(0)
		x = pickle.load(f)
	except IOError as e:
		print "I/O error({0}): {1}".format(e.errno, e.strerror)
	except ValueError:
		print "Could not convert data to an integer."
	except:
		print "Unexpected error:", sys.exc_info()[0]
		raise
	finally:
		f.close()
		print "\nfile closed"
		print type(x)

	class Car:
		"""Alp's Class"""
		def __init__(self, model, color, name):
			self.model = model
			self.color = color
			self.name = name
		def __str__(self):
			return self.getInformation()
		def getInformation(self):
			return str(self.model)+' '+self.color+' '+self.name;

	polo = Car(1998, 'blue', 'polo');
	polo2011 = Car(2011, 'gray', 'polo');
	print "my car is: "+polo.getInformation()
	print "my other car is: "+str(polo2011)

	polo.fault = 'left window is not opening'

	print polo.fault
	del polo.fault
	
#	a = input("input python cmd\n")
	print str(polo)

	class Volkswagen(Car):
		"""Volkswagen SubClass"""
		def getInformation(self):
			return 'Volkswagen '+Car.getInformation(self);

	golf = Volkswagen(2000, 'blue', 'golf')
	print str(golf)

	def reverse(data):
		for index in range(len(data)-1, -1, -1):
			yield data[index];

	for char in reverse(str(golf)):
		print char+' ',
	print ""

	original_stdout = sys.stdout
	sys.stdout = open('stdout.txt','a+')

	sys.stderr.write('this is the stderr\n')
	sys.stdout.write('this is the stdout\n')

	sys.stdout = original_stdout

	sys.stdout.write('this is the stdout again\n')

	def getHostname(link):
		if(link.startswith('http://')):
			hostname = link[0:link.find('/', 8)+1]
		else:
			hostname = link[0:link.find('/')+1]
		return hostname

	def downloadFile(link, makedir):
		import urllib2
		remoteFile = urllib2.urlopen(link)
		remoteFile_info = remoteFile.info()
		#print remoteFile_info
		for key in remoteFile_info:
			if key=='content-length':
				print remoteFile_info[key]

		import os
		# filename = link[link.rfind('/')+1:]
		filename = link[len(getHostname(link)):]
		print filename

		if(makedir):
			if(not os.path.exists(filename[:filename.rfind('/')])):
				os.makedirs(filename[:filename.rfind('/')])

		if(os.path.exists(filename)):
			os.remove(filename)

		localFile = open(filename, 'w+')
		
		localFile.write(remoteFile.read())
		#for i in range( int(remoteFile_info['content-length'])):
		#	localFile.write(remoteFile.read(1))
		
		# for line in remoteFile:
		# 	localFile.write(line)

		localFile.close()
		return filename

	def scanFileForImageLinks(filename):
		localFile = open(filename, 'r')
		start = 0
		end = 0
		source = localFile.read()
		linklist = []
		while(start != -1):
			start = source.find('<img', end)
			if(start == -1):
				break
			end = source.find('>', start)
			imgtag = source[start:end+1]
			print imgtag
			innerStart = imgtag.find('src=')
			innerEnd = imgtag.find( '"', innerStart+5)
			imglink = imgtag[innerStart+5:innerEnd]
			print imglink + '->' + str(innerStart) +':'+ str(innerEnd)+'/'+str(len(imgtag))
			linklist.append(imglink)
		return linklist

	def downloadFileWithImages(link):
		filename = downloadFile(link, False)
		linklist = scanFileForImageLinks(filename)
		for imglink in linklist:
			downloadFile(getHostname(link)+imglink, True)

	print getHostname('http://alpsayin.com/kth-format-thesis_proposal_v2_rev4.htm')
	downloadFileWithImages('http://alpsayin.com/kth-format-thesis_proposal_v2_rev4.htm')

	class DynamicEmptyStruct:
		pass

	myDynStruct = DynamicEmptyStruct()
	myDynStruct.floatMember = 0.5423534
	myDynStruct.stringMember = 'alp sayin'
	myDynStruct.dynstructmember = DynamicEmptyStruct()