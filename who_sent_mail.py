# this program counts total numbe of mails sent by.
# jay monpara

import string
def main():
	print "\nThis program will count the number of mail senders"
	infile = raw_input("Enter the input file name: ")
		
	infile = open(infile, 'r')
	print
	count = 0
	for line in infile:
		if line[:4]=='From':
			words = string.split(line)
			print words[1]
			count = count + 1
		
	
	print "\n total number of senders", count
	
main()

	
	