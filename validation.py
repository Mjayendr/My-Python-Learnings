#def main():
#	infilename = raw_input("Enter the input file name: ")
#	infile = open(infilename,"r")
#	for i in range(10):
#		line = infile.readline()
#		print line[:-1]
#	infile.close()
	
#main()

#input
def main():
	print
	print "This program is a practice for validation of input data"
	invalid = True			# set the condition
	print
	while invalid:			# if the condition is true, go through the while loop
		answer = raw_input("Please enter a number (6 digits, min 10, max 101000)? : ") # input the number
		
		if len(answer)!=6:		# checking for length of the string, if it's not 6 print the message and go back to start of while loop
			print " the number is not 6 digits"
			continue			# asks to go back to start of the while loop
		
		if int(answer)< 10 or int(answer)>101000:	#  checking for value of the input data
			print "the number is not in between 10 and 101000"
			continue			# asks to go back to start of the while loop
		pin = answer			# assign the answer to pin
		
		invalid = False			# completes the while loop
	print
	print "The PIN is now", pin  # print the decision
	
main()
	

