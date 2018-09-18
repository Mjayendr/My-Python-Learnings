# This program encode the message into sequence of numbers utilizing underlying ascii codes.
# By Jay Monpara
print
def main():
	# Input a message to be encoded
	print
	print 'This program converts a textual message into a sequence'
	print 'of numbers by utilizing underlying ascii codes'
	message = raw_input('Enter your message to encode:')
	print
	print 'Here are the ASCII codes'
	print
	for code in message:
		print ord(code), # used comma to get the result in one line
		
main()

print
# This program converts a sequence of ASCII codes into a string of text it represants

import string
def main():
	print
	print "This program converts ASCII codes"
	print
	print "into string of texts it represants"
	print
	# Get the encoded message that needs to be decoded.
	code = raw_input('Enter the code for the message:')
	# Loop through each substring and build an ASCII message.
	print
	message = '' # define the empty message
	print
	for letter in string.split(code):	#sring.split is to split the string code into sub strings
		ascii = eval(letter)			# eval will convert each substring in to integers for ascii codes
		message = message + chr(ascii)	# chr() will convert each ascii value in to a character
	print 'The encoded message is:',message

main()
	
		
