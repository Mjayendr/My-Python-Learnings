
import string

nums = raw_input("Enter number: ")
	
numlist = string.split(nums,',')
total = 0
count = 0
for num in numlist:
	num = float(num)
	total = total + num
	count = count + 1

print total
print count

average = total/count
print average