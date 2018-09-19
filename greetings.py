import string
def person(name):
	for greeting in string.split(name):
		print "Happy Birthday", greeting
		print 
		
def main():
	print
	name = raw_input("Enter the name of the person: ")
	
	print
	print 'Greetings'
	print
	message = person(name)
	
main()
