#This is a program to determine the angle to set a crossbow for penguines to target the enimy polar bear.
# By Jay Monpara
print
def ang():
		import math		# this gives us the degrees and arcsine functions
		invalid = True
		while invalid:
		
			v= input("Velovity of the projectile in meters per second= ")		
			
			while v!=0:
				
				for d in range(1000,1500,100):
					try:
						ang = math.degrees(0.5*(math.asin(9.81*d/v**2)))
						print
						d=d+100
						print "The angle of the projectile to be launched at distance = ", d, "meters is =" ,round(ang), "degrees"
					except:
						print '\nPenguine velocity is too low. try again.'
				break	
						
						
			ask = raw_input("Hit enter to continue or [done] to exit the program: ")
			if ask == 'done':
				print "\nGoodbye"
				invalid = False
			else:
				continue
				
ang()






		