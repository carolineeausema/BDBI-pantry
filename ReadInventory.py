from tkinter import ttk
import tkinter as tk

from tkinter import *

# ReadInventory.py

# https://docs.google.com/drawings/d/1IhOvTogBLOuWQyc_lfCRX-MFBejrGhJ5V1xRU8-HJwQ/edit?usp=sharing

points = 0
class Application:
	def __init__(self, master):

		self.master = master
		self.retrieve_inventory()
		master.title("Ace Campus Food Pantry")
		master.geometry("500x500")


		# WIDGETS
		#	random
		self.food_dictionary = self.retrieve_inventory()
		self.order_dictionary = {}
		for i in self.food_dictionary:
			self.order_dictionary[i] = StringVar()
			self.order_dictionary[i].set(0)
		self.internal_frame = LabelFrame(root, text = "Order:", padx = 100, pady = 80)

		#	labels
		self.num_guest_label = Label(root, text = "Guest(s):")
		self.num_points_label = Label(root, text = "Points: " + str(points))

		#	Combobox + setting defaults
		self.view_guest_num = StringVar()
		self.view_guest_num.set(1)
		self.guest_num_values = ttk.Combobox(root, textvariable = self.view_guest_num, values = (1, 2, 3, 4, 5, 6, 7), width = 1)

		#	buttons




	def push_changes(self):

		points = int(self.view_guest_num.get()) * 15
		self.guest_num_values.bind("<FocusIn>", sense_record)
		self.num_points_label = Label(root, text = "Points: " + str(points))


		self.num_guest_label.pack(padx = 5, pady = 10, anchor = "nw", side = "left")
		self.guest_num_values.pack(padx = 5, pady = 10, anchor = "nw", side = "left")
		self.num_points_label.pack(padx = 5, pady = 10, anchor = "ne", side = "right")


		self.internal_frame.pack(padx = 5, pady = 10, expand = 1)


		for i in self.order_dictionary:
			food_item_values = ttk.Combobox(self.internal_frame, textvariable = self.order_dictionary[i], values = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15), width = 2) # change 15 to points
			food_item_values.grid(row = list(self.order_dictionary.keys()).index(i) + 1, column = 1)
			val = Label(self.internal_frame, text = i)
			val.grid(row = list(self.order_dictionary.keys()).index(i) + 1, column = 2)


	def forget_widgets(self):

		self.num_guest_label.forget()
		self.guest_num_values.forget()
		self.num_points_label.forget()
		self.internal_frame.forget()


	def retrieve_inventory(self):

		amountFile = open("InventoryFile.txt", "r")
		allLines = amountFile.read().split("\n")
		inventory = {}
		for i in allLines:
		    eachLine = i.split(";")
		    if (len(eachLine) == 2):
		        inventory[eachLine[0]] = eachLine[1]
		return inventory


# MAIN FRAME
root = Tk()
frame = Application(root)

def sense_record(event): # add on produce points?
	frame.forget_widgets()
	frame.push_changes()

# PUSH ELEMENTS TO MAIN FRAME
frame.push_changes()
root.mainloop()
