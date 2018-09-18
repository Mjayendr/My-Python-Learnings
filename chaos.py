# program for chaos function.

def main():
	print
	print ("This program illustrate a chaotic function.")
	print
	x = input("Enter a nuber between 0 and 1: ")
	print
	y = input("Enter 2nd number between 0 and 1: ")
	print
	z = input ("Enter 3rd number beteen 0 and 1: ")
	
	print
	n = input ("Enter how many times you want to run the loop:")
	print
	print ('the input values of x are: %12.2f %10.2f %12.2f'%(x,y,z))
	for x in range(n):
		x = 3.9 * x * (1-x)
		y = 3.9 * y * (1-y)
		z = 3.9 * y * (1-z)
		
		print ('the calculated value of x is %10.3f %10.3f %12.3f ' %(x,y,z))
		
main()


