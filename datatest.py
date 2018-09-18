# userfile.py
#    Program to create a file of usernames in batch mode.

import string

def main():
    print "This program creates a file of usernames from a"
    print "file of names."

    # get the file names
    infileName = raw_input("What is the input file ? ")
    outfileName = raw_input("What file should the report go in? ")

    # open the files
    infile = open(infileName, 'r')
    outfile = open(outfileName, 'w')
    
    outstring = "%-18s %-18s %-10s %-18s %8s" % ("Lastname","Firstname","City","CCN","Amount")
    outfile.write(outstring+"\n")
	
    firsttime = True

    # process each line of the input file
    for line in infile:
        if firsttime:
            firsttime = False
            continue
        # get the first and last names from line
        # first, last = string.split(line,",")
        record = string.split(line,",")
        
        first =  record[1]
        last =   record[2]
        city =   record[3]
        ccn =    record[5]
        amount = record[7]
        # create a username
        #uname = string.lower(first[0]+last[:7])
        #uname = string.replace(uname, " ", "X")

        outstring = "%-18s %-18s %-10s %-18s %8s" % (last,first,city,ccn,amount)
		
        # write it to the output file
        outfile.write(outstring)

    # close both files
    infile.close()
    outfile.close()

    print "Report has been written to", outfileName

main()
