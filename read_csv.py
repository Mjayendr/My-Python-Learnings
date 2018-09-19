# program to pull data from .csv file

import string

def main():
	# get the input and output file names
	
	infilename = raw_input("Enter the input file name ")
	outputfilename = raw_input("Enter the output file name")
	
	# open the files
	
	infile = open(infilename, 'r')
	outfile = open(outputfilename, 'w')
	
	outstring = "%-18s,%-18s,%-10s,%-18s,%8s" % ('Lastname','Firstname','City','CCN','Amount')
	outfile.write(outstring+"\n")
	
	firsttime = True
	
	#get the data required from the files.
	
	for line in infile:
		if firsttime:
			firsttime=False
			continue
		record = string.split(line, ",")
		last = record[2]
		first = record[1]
		city = record[3]
		ccn = record[5]
		amount = record[7]
		
		outstring = "%-18s,%-18s,%-10s,%-18s,%8s" % (last,first,city,ccn,amount)
		
		outfile.write(outstring+"\n")
				
				
	#close the files
	
	infile.close()
	outfile.close()
	
	print "The required data written to", outputfilename
		
main()