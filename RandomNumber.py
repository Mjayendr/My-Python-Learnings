#this program is about guessing random number.
# By Jay Monpara
import random
print
def main():
	print 'This program is about guessing a random number.'
	print
	print 'guess a random number between 0 and 100.'
	randomNumber = random.randint(1,100)
	found = False
	while not found:
		print
		guess = input('Your Guess:')
		if guess ==randomNumber:
			print
			print 'Well Done you got it, thanks for playing the game. you are genius.'
			found = True
		elif guess > randomNumber:
			print 'Guess Lower'
		else:
			print 'Guess Higher'
			
main()
		
	
	
