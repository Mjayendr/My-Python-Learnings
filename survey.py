#Q3 Write a program to determine student satifaction in a survey.
#Ask the user to enter 1 to 7 in a scale of student satisfaction with
#a course. Keep entering values until the types a 0.
#Then count the number of entries for each scale value.
#Display the counts along with the text values of the scale in the
#ascending order of the scale
#1=Rubbish, 2=Bad, 3=Okay, 4=Fair, 5=Average, 6=Good, 7=Outstanding

def main():
	
	print
	print "This program will run the survey and display the numbers on scale 1 to 7"
	print " based on student satisfaction level in a course."
	print
	print "Satisfaction level is scaled from 1 to 7 for Rubbish, Bad, Okay"
	print " Fair, Average, Good and Outstanding, respectively."
		
	Rubbish, Bad, Okay, Fair, Average, Good, Outstanding = 0,0,0,0,0,0,0
	invalid = True
	while invalid:
		while True:
			print
			try:
				scale= raw_input("Please enter number from 1 to 7 based on your satisfaction level : ")
				scale = int(scale)
				print
				if (scale < 1) or (scale > 7):
					print " Scale value only allowed from 1 to 7"
					print
					continue
				else: break
				
			except:
				print
				print "Please enter a numeric number between 1 and 7"
			
		if scale == 1:
			print "Rubbish"
			Rubbish = Rubbish + 1
		if scale == 2:
			print "Bad"
			Bad = Bad + 1
		if scale == 3:
			print "Okay"
			Okay =  Okay + 1
		if scale == 4:
			print "Fair"
			Fair = Fair + 1
		if scale == 5:
			print "Average"
			Average = Average + 1
		if scale == 6:
			print "Good"
			Good = Good + 1
		if scale == 7:
			print "Outstanding"
			Outstanding = Outstanding + 1
			
		more = raw_input("Hit Enter for another input or [0] to finish the survey: ")
		print
		if more == '0':
			invalid = False
		else:
			continue
					
	print "Score is as below:"
	print "Rubbish=%10d" %Rubbish
	print "Bad = 	%10d" % Bad
	print "Okay = 	%10d" % Okay
	print  "Fair = 	%10d" % Fair
	print "Average=%10d" % Average
	print "Good = 	%10d" % Good
	print "Outstanding =%5d" % Outstanding
	#print "Score in descending order is ", sorted(score, reverse = True)
			
	print "Done"
		
		
main()
			
