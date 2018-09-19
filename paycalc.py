# This program calculates the pay based on rate and working hours.

def main():
	print
	invalid = True
	while invalid:
		print
		hours = raw_input("Enter number of hours worked : ")
		h = float(hours)
		if h <= 0:
			print "Working hours can not be less than 0"
			continue
		invalid = False
	print
	invalid = True
	while invalid:
		rate = raw_input ("Enter the rate per hour : ")
		r = float(rate)
		if r <= 0:
			print "The rante can not be less than 0"
			continue
		invalid = False
	if h <= 40:
		pay = h * r
			
	elif h > 40 and h <= 44:
		pay = ((40 * r) + ((1.5 * r) * (h-40)))
		
	else: pay = ((40 * r) + ((1.5 * r) * 4) + ( 2* r ) * ( h -44 ))
	print
	print "Rate per hour is = $%0.2f" % r
	print
	print "The calculated pay is $%0.2f. Thank you " % pay
		
		
main()