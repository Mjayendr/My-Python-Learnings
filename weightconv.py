# This program converts weight from stones to kg, lb or tons.
# by: Jay Monpara


def main():
	print
	invalid = True
	while invalid:

#input
		while True:
			try:													 # try---except block used for validation.
				stone = raw_input("Please enter weight in stones: ") # invoke user to input the weight in stones.
				stone = float(stone)								 # conver the string into a floating number
				print
				print " Entered weight is = ", stone, "stones"
				break
			except:
				print
				print "Please enter a numeric number"
				print
		print
		convert = raw_input("Please enter [kg] for kilograms, [lb] for pounds or [t] for tons: ") # ask user for the requirement.
		print

# Process and output:
		if convert == 'kg':											
			kg = stone * 13.5
			print "Converted weight in kilograms = %0.3f kgs." %kg	 # string formated to get precise answer up to 3 decimals points.
		
		if convert == 'lb':
			lb = stone * 13.5 * 0.53
			print "Converted weight in pounds = %0.3f lbs." %lb
			
		if convert == 't':
			t = stone *13.5 / 1000
			print "Converted weight in tons = %0.3f tons." % t
		print

# program continuation
		
		ask = raw_input("Hit enter to convert another number or type [done] to exit the program: ") # asking user if he need to convert another number.
		print
		if ask == 'done':
			invalid = False # Breaking the loop if user type [done] in previous statement.
		else:
			continue

main()
			
	
			
	