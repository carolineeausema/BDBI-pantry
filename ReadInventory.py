from tkinter import *

# ReadInventory.py

# https://docs.google.com/drawings/d/1IhOvTogBLOuWQyc_lfCRX-MFBejrGhJ5V1xRU8-HJwQ/edit?usp=sharing

class Text(Frame):
	def __init__(self, master = None):
		super().__init__(master)
		self.master = master
		self.retrieve_inventory()

	def retrieve_inventory(self):
		amountFile = open("InventoryFile.txt", "r")
		allLines = amountFile.read().split("\n")
		inventory = {}
		for i in allLines:
		    eachLine = i.split(";")
		    if (len(eachLine) == 2):
		        inventory[eachLine[0]] = eachLine[1]


def place_menu(location):
#	 initialize drop down menu
	OPTIONS = []
	for i in range(16):
		OPTIONS.append(i)
	view_value = StringVar()
	view_value.set(OPTIONS[0])
	drop_values = OptionMenu(location, view_value, *OPTIONS)
	return drop_values

def place_label(parent, location):
    text = Label(location, text = parent)
    return text






# MAIN FRAME
root = Tk()
root.title("Ace Campus Food Pantry")
root.geometry("500x500")



# WIDGETS
#	labels
num_guest_label = Label(root, text = "Guest(s)")

#	buttons

#	frame w text file in it
temp_list = [
	"beans",
	"ratatouille",
	"rice"
]
internal_frame = LabelFrame(root, text = "Welcome!", padx = 100, pady = 30)



# PUSH ELEMENTS TO MAIN FRAME
place_menu(root).grid(row = 0, column = 0)
num_guest_label.grid(row = 0, column = 1)
internal_frame.grid(row = 3, column = 1)
for i in range(len(temp_list)):
	place_menu(internal_frame).grid(row = i + 1, column = 0)
	place_label(temp_list[i], internal_frame).grid(row = i + 1, column = 1)

text_frame = Text(master = root)

root.mainloop()
