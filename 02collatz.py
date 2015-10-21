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


# Have the user pick a number, and verify the number.
def pickNumber():
	while True:
		try:
			# Pick a number, remove commas, and convert to int.
			number = int(input().replace(",", ""))
			# Make sure it's less than 12 digits.
			if len(str(number)) < 12:
				return number
			else:
				print("Sorry, try a number under 1,000,000,000,000.")
				continue
		# If it's not a number, give friendly error and repeat.
		except ValueError:
			print("This requires a whole number (no decimals).  Please try again.")
			print(" ")


# Would you like to rerun the program?
def rerun(answer, function):
	if answer in ("Yes", "yes", "y"):
		function()
	else:
		print("See you next time!")


# Run Collatz: Take number.  If 1, end.  If even, divide by 2.  If odd, multiply by 3 and add 1.
# Print victory message, and ask if they'd like to try again.
def collatz():
	# Print intro
	collatzIntro()
	# Get number from user
	num = pickNumber()
	# Run Collatz formula and start counter
	counter = 0
	while num != 1:
		if num // 2 == num /2:
			num = int(num / 2)
		else:
			num = int(num * 3 + 1)
		print(num)
		counter += 1
	# Print victory message and ask player if they want to try again.
	print("Huzzah!  It only took " + str(counter) + " operations.  Would you like to " +\
		"try again? (Yes / No)")
	response = input()
	print(" ")
	print(" ")
	# Rerun or exit based on user response.
	rerun(response, collatz)

collatz()