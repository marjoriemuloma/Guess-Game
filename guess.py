"""
Write a programme where the computer randomly generates a
number between 0 and 20. The user needs to guess what the 
number is. If the user guesses wrong, tell them their guess 
is either too high, or too low. This will get you started with 
the random library if you haven't already used it.
"""

## Project Dependencies or Libraries that we are importing
import time
import random

# Registering and Welcoming users..
user_name = str(input('Please Enter Your Name... '))
print('Welcome to the Guess Game ' + user_name + ' . To play...')
time.sleep(3)
print(
	"""
		Guess a number between 0 and 20.
	"""	
)
time.sleep(0.5)
print(
	"""
		Good ... Luck :D
	"""	
)
print('.........33%')
time.sleep(0.5)
print('....................66%')
time.sleep(0.5)
print('....................................100%')

## Use guesses a number
guessed_number = input('Enter a number between 0 and 20: ')

## Check that the guessed number is an integer!!!
try:
	guess = int(guessed_number)
	if int(guessed_number) > 0 and int(guessed_number) < 20:
		## User must return integer or try again...
		try:
			val = int(guessed_number)
			## Computer Generates a Number
			generated_number = random.randint(0, 21)
			if int(guessed_number) == generated_number:
				print(generated_number)
				time.sleep(2)
				print('Congratulations... You won!')
			elif int(guessed_number) < generated_number:
				print('Correct Number -->  ' + str(generated_number))
				time.sleep(3)
				print('Sorry.. Your Guess is too Low')
			else:
				print('Correct Number -->  ' + str(generated_number))
				time.sleep(3)
				print('Sorry... Your Guess is too High')
		except ValueError:
			print('Try Again... Integer!')

	else:
		print('Guess Must Be a Number between 0 and 20...')
except ValueError:
	print('Guess Must be an Integer!')
