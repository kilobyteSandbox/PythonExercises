# Creates a list of items, then prints [a, b, c] as "a, b, and c"


# Create list
itemList = []

print("Enter item names.  Press enter when done.")

while True:
	itemName = input()
	if itemName == '':
		break
	itemList += [itemName]


# Create a string from the list [a, b, c] in format "a, b, and c"
def commaAnd(list):
        stringX = ''
        for i in range(len(list)):
                if i < len(list) - 1:
                        stringX += (list[i] + ', ')
                else:
                        stringX += ("and " + list[i])
        return stringX


# Print list
print(commaAnd(itemList))

