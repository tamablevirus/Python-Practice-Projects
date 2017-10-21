import random
randomnum = random.randint(1,101)
randomguess = -1
print "You can either guess a number from 1-100 or say stop to stop the program!"
while randomguess != randomnum and randomguess != "stop":
	randomguess = raw_input("Guess a number between 1-100: ")
	randomguess = randomguess.lower()
	try:
		if randomguess == "stop":
			break

		elif int(randomguess) < 1 or int(randomguess)> 100:
			print("Please enter a number between 1-100!")
		else:
			print("You guessed wrong! Try again!")	
	except Exception as e:
	
		print"Please enter a valid number."
		
		
if randomguess == randomnum:
	print("You guessed the number!")
else:
	print("Stopped....")