# =======
# Collatz
# =======


# Print intro
def collatzIntro():
	print("========")
	print("Collatz!")
	print("========")
	print(" ")
	print("This program will end when it reaches 1.  When the number is even, it will " +\
		"divide by 2.  When the number is odd, it will multiply by 3 and add 1.")
	print("Enter a number:")
	print(" ")


# Pick number and check to make sure input is a number
def pickNumber():
	while True:
		try:
			number = int(input())
			return number
		except ValueError:
			print("This requires a whole number (no commas or decimals).  Please try again.")
			print(" ")


# Would you like to rerun the program?
# Currently bugged.  All answers rerun.
def rerun(answer, function):
	if answer in ("Yes", "yes", "y"):
		function
	else:
		print("See you next time!")


# Take number.  If 1, end.  If even, divide by 2.  If odd, multiply by 3 and add 1.
def collatz():
	collatzIntro()
	num = pickNumber()
	counter = 0
	while num != 1:
		if num // 2 == num /2:
			num = int(num / 2)
		else:
			num = int(num * 3 + 1)
		print(num)
		counter += 1
	print("Huzzah!  It only took " + str(counter) + " operations.  Would you like to " +\
		"try again? (Yes / No)")
	response = input()
	print(" ")
	print(" ")
	rerun(response, collatz())

collatz()