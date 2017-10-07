import random
randomnum = random.randint(1,101)
randomguess = -1
print "You can either guess a number from 1-100 or say stop to stop the program!"
def check_int(integervar): #checks to see if var is truly int
	if integervar is int:
		return false
	elif integervar is str:
		if str[0].isdigit():
			return true
		else: 
			return false	
	else:
	  return false
				

while randomguess != randomnum and randomguess != "stop":
	randomguess = raw_input("Guess a number between 1-100: ")
	try:
		if check_int(randomguess) == false:
			randomguess = randomguess.lower()

		elif int(randomguess) < 1 or int(randomguess)> 100:
			print("Please enter a number between 1-100!")
		else:
			print("You guessed wrong! Try again!")	
	except Exception as e:
		print"Please enter a valid number."
		
		
if randomguess == "stop":
	print("Stopped....")
else:
	print("You guessed the number!")	