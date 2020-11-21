# ReadInventory.py
amountFile = open("InventoryFile.txt", "r")
allLines = amountFile.read().split("\n")
inventory = {}
for i in allLines:
	eachLine = i.split(";")
	if (len(eachLine) == 2):
		inventory[eachLine[0]] = eachLine[1]
print(inventory)
