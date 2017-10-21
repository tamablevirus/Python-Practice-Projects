word = raw_input("Enter the word you want to check for a plaindrome: ")
word_check = word.lower()
if word_check[::-1] == word_check:
	print word,"is a plaindrome."
else:
	print word,"is not a plaindrome."