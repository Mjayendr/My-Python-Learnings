# currcon.py
# This program converts currency from Euro to USD, GBP or AUD.
# By - Jay Monpara

def main():
	print "\nThis currnecy converter program, converts Euro amount into"
	print "\nan equivalent amount of US dollers (USD), Australian dollers (AUD) or British Pound (GBP)."
	print "\nPlease choose the currency you want to transfer from Euro"
	invalid = True
	while invalid:
		while True:
			print
			convert = raw_input("Please enter [USD] for US dollers, or [GBP] for British pound or [AUD] for Australian doller : " )
			if (convert!= 'USD') and (convert!= 'GBP') and (convert!= 'AUD'):
				print "\nInvalid currency. Please select from USD or GBP or AUD only."
				continue
			else: break
		while True:
			try:
				print
				amount = raw_input("Enter the amount in Euro: ")
				amount = float(amount)
				break
			except:	
				print "\nEntered amount is not a numeric value. please enter a numeric value."
		
		if convert == "USD":
			USD = amount * 1.09709
			print "\nThe converted amount in USD is = $%0.5f." % USD
			
		if convert == "GBP":
			GBP = amount * 0.89994
			print "\nThe converted amount in GBP is = %0.5f Pounds." % GBP
			
		if convert == "AUD":
			AUD = amount * 1.43938
			print "\nThe converted amount in AUD is = $%0.5f." % AUD
		
		print "\nDo you want to convert another amount?"
		print
		ask = raw_input("Please hit 'Enter' convert another amount or type [done] to exit the program: ")
		
		if ask == 'done':
			invalid = False
		else: 
			continue
	
	print "\nGood Bye"
		

main()	
	
