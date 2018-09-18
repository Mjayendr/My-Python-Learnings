#userfile.py
# program to create a file of usernames in batch mode.

import string

def main():
	print "This program creates a file of usernames and a"
	print "file of names."
	
	#get the file names.
	
	infilename = raw_input("What files are the names in?")
	outfilename = raw_input("What file should the usernames go in?")
	
	# open the files
	
	infile = open(infilename, 'r')
	outfile = open(outfilename, 'w')
	
	# process each line of the input file
	
	for line in infile:
		#get the first and last names from line
		first, last = string.split(line)
		
		# create usernames
		uname = string.lower(first[0]+last[:7])
		
		# write to the output file
		
		outfile.write(uname+'\n')
		
	#cose both files
	infile.close()
	outfile.close()
	
	print "Usernames have been written to", outfilename
	
main()