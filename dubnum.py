

def inputnum():
	inputnum = raw_input("Enter a numeric number - ")
	x = int(inputnum)
	return x


def dublenum(w):
	
	b = 2 * w
	return b
	
def printnum(a):
	print "The double number is ", a

def main():
	num = inputnum() # assign a variable('num') to a 'x' from inputnum()
	dnum = dublenum(num) # assign a variable('dnum') to a 'dubnum' from dublenum(num)
	printnum(dnum) # don't need to assign a variable as no retrun from printnum(dnum)

main()