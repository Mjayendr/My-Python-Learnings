# This program converts distance from feet to either inches, yards or meters.
# By: Jay Monpara

def main():
	print
	invalid = True
	while invalid:
		while True:
			try:												# using try --- except statements for numeric validation
				distance = raw_input("Enter the distance in feet: ") # prompt user to enter the number to convert from feet to other units.
				distance = float(distance)				# converts string into a float number.
				print
				print "Distance= ", distance, "feet."
				break
							
			except:
				print
				print "Please enter a numeric number"
				print	
		print	
		convert_to = raw_input("Enter [i] for inches, [y] for yards or [m] for meters: ") # asking user for the specific requirement.
		print
		if convert_to == 'i':
			inches = distance * 12.0
			print " The distance in inches is %0.3f inches = " % inches  # string formatting to get the precise answer with 3 decimals.
			
		if convert_to =='y':
			yards = distance/1.50
			print "The distance in yards is %0.3f yards. " % yards
			
		if convert_to =='m':
			meters = distance/3.2
			print "The distance in meters is %0.3f meters." % meters
		print	
		more = raw_input("Enter [Y] to convert another distance or [done] to finish: ") # asking user wheather he wants to continue
		print
		if more == 'done':
			invalid = False # breaking the while loop
		else: continue
		
main()

	

	