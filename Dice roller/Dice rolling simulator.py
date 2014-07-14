""" Dice rolling simulator, will ask user to press Enter to roll.
	Will print a random number between 1 to 6. Will ask user if they want to roll again. """
 
import random
 
print "Welcome to the Dice Rolling Simulator!\n"
print "Press Enter to roll the dice."
begin = raw_input("")
 
""" function where random numbers are generated """
def dice_roll():
	# A while that does one iteration is equivalent to no while at all
	print "You have rolled..."
	print random.randint(1,6)
	print "and"
	print random.randint(1,6)
	print "\n"
 
""" ask whether player wants to roll the dice again. will only accept yes or no. 
	otherwise loops back. """
def roll_dice_again():
	while True:
		again = str(raw_input("Would you like to roll the dice again? 'Yes' or 'No'?\n").lower())
	
		if again == "yes": 
			print "\n"
			dice_roll()
			
		elif again == "no":
			print "\n"
			print "Thank you for playing."
			break  # exit while. `return` can also be used here to exit both `while` and `roll_dice_again`
		
		else:
			print "\n"
			print "That is incorrect."
			
		# no `break` happened, continue looping
 
dice_roll()
roll_dice_again()



