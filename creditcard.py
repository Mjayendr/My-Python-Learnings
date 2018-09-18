# program to extract data from mock data file.

def main():
	import string

	#input
	#give a name to inputfile and outputfile
	print
	infilename = raw_input("Enter the inputfile name: ")
	print
	outfilename = raw_input("Enter the outputfile name: ")

	#open inputfile and outputfile
	infile = open(infilename, 'r')
	outfile = open(outfilename,'w')

	#id, firstname, lastname, city, gender, CCN, CCtype, amount

	# create outfile heading
	outstring = "%-5s %-13s %-14s %-30s %-18s %20s " %("ID","LastName","FirstName","City","CCN","Amount")
	outfile.write(outstring+"\n")
	
	firsttime = True

	#process
	for line in infile:					# python for loop to go through ech lines in the file
		if firsttime:
			firsttime = False
			continue
		record = string.split(line,",") 		#split the lines in infile by ","
		#assign names to each substring by indexing
		ID = record[0]	
		FirstName = record[1]
		LastName = record[2]
		City = record[3]
		CCN = record[5]
		Amount =record[7]
		
		# Write the extrated data into outfile	
		outstring = ("%-5s %-13s %-14s %-30s %-18s %20s ") %(ID,LastName,FirstName,City,CCN,Amount)
		outfile.write(outstring+"\n")

	#close both files	
	infile.close()
	outfile.close()
	
	print	
	print "The required data written to ", outfilename
	
main()
	
	






