# Lets talk about 'Name'.
#He is 'cm' tall.
#He's 

def main():
	print
	my_name		= raw_input("ENter a name :")
	my_age 		= input("Enter age: ")
	my_height 	= input("Enter hight (in cm):")
	my_weight 	= input("ENter weight (in kilos):")
	my_eyes 	= raw_input("Enter eye color:")
	my_teeth	= raw_input("Enter teeth color:")
	my_hair		= raw_input("Enter hair color:")
	awh			= (my_age + my_weight + my_height)
	print
	print "Lets talk about %s." % my_name
	print "He's %d cm tall." % my_height
	print "He is %d kilos heavy." % my_weight
	print "Actually that's not heavy."
	print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
	print "His teeth are usually White depending on the coffee."
	print "If I add age %d, weight %d, and height %d, i get %d." %(my_age,my_weight,my_height, awh)
	
main()