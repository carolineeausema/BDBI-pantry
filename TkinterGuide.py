from tkinter import *
from PIL import ImageTk, Image # used for images
from tkinter import messagebox # used for messagebox
import sqlite3

root = Tk() # defines frame/window



# EX: LABEL WIDGET
"""
myLabel = Label(root, text = "ratatouille").pack()
"""

# NOTE: PUSH CONTENT TO Frame
#       you can only use .pack() or .grid() seperately

# .pack() :		places element in the center frame, rescales dimension upon
#				frame resizing
"""
myLabel = Label(root, text = "Hello world") # Label widget
myLabel.pack() # adds to Frame
"""

# .grid() :		 places an element in specific location RELATIVE to others,
#				 cannot be manipulated
"""
myLabel1 = Label(root, text = "Hello World") # Label widget
myLabel2 = Label(root, text = "ratatouille") # Label widget
myLabel1.grid(row = 0, column = 0) # adds to Frame
myLabel2.grid(row = 1, column = 5) # adds to Frame
"""



# EX: BUTTON WIDGET,
#	  customize with state (active vs. disabled) / padx (width) /
#	  pady (length) / fg (font color) / bg (background color)
"""
myButton = Button(root, text = "Click me!", state = ACTIVE, padx = 50,
 pady = 50, fg="blue", bg="beige")
myButton.pack()
"""



# EX: build button functionality with command=[function]
"""
def myClick():
	myLabel = Label(root, text = "ratatouille")
	myLabel.pack()
myButton = Button(root, text = "Click me!", pady = 50, command = myClick)
myButton.pack()
"""



# EX: INPUT BOX,
#	  customize with width / bg (background color) / fg (font) /
#	  borderwidth (square around input box),
#	  default text with .insert(),
#	  add action using .myClick() / myButton
"""
e = Entry(root, width = 50, bg = "black", fg = "green", borderwidth = 5)
e.pack()
e.insert(0, "ratatouille")
def myClick():
	myLabel = Label(root, text = "u just said: " + e.get())
	myLabel.pack()
myButton = Button(root, text = "Enter", command = myClick)
myButton.pack()
"""



# EX: simple calculator
"""
root.title("Simple Calculator")
e = Entry(root, width = 35, borderwidth = 5)
e.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)
e.insert(0, "")
def button_click(number):
	current = e.get()
	e.delete(0, END)
	e.insert(0, str(current) + str(number))
def button_clear():
	e.delete(0, END)
def button_add():
	first_number = e.get()
	global first_num
	global math
	first_num = int(first_number)
	math = "addition"
	e.delete(0, END)
def button_subtract():
	first_number = e.get()
	global first_num
	global math
	first_num = int(first_number)
	math = "subtraction"
	e.delete(0, END)
def button_multiply():
	first_number = e.get()
	global first_num
	global math
	first_num = int(first_number)
	math = "multiplication"
	e.delete(0, END)
def button_divide():
	first_number = e.get()
	global first_num
	global math
	first_num = int(first_number)
	math = "division"
	e.delete(0, END)
def button_equal():
	second_number = e.get()
	e.delete(0, END)
	if math == "addition":
		e.insert(0, first_num + int(second_number))
	if math == "subtraction":
			e.insert(0, first_num - int(second_number))
	if math == "multiplication":
			e.insert(0, first_num * int(second_number))
	if math == "division":
		e.insert(0, first_num / int(second_number))
button_1 = Button(root, text = "1", padx = 40, pady = 20,
 command = lambda: button_click(1))
button_2 = Button(root, text = "2", padx = 40, pady = 20,
 command = lambda: button_click(2))
button_3 = Button(root, text = "3", padx = 40, pady = 20,
 command = lambda: button_click(3))
button_4 = Button(root, text = "4", padx = 40, pady = 20,
 command = lambda: button_click(4))
button_5 = Button(root, text = "5", padx = 40, pady = 20,
 command = lambda: button_click(5))
button_6 = Button(root, text = "6", padx = 40, pady = 20,
 command = lambda: button_click(6))
button_7 = Button(root, text = "7", padx = 40, pady = 20,
 command = lambda: button_click(7))
button_8 = Button(root, text = "8", padx = 40, pady = 20,
 command = lambda: button_click(8))
button_9 = Button(root, text = "9", padx = 40, pady = 20,
 command = lambda: button_click(9))
button_0 = Button(root, text = "0", padx = 40, pady = 20,
 command = lambda: button_click(0))
button_add = Button(root, text = "+", padx = 40, pady = 20,
 command = button_add)
button_subtract = Button(root, text = "-", padx = 40, pady = 20,
 command = button_subtract)
button_multiply = Button(root, text = "*", padx = 40, pady = 20,
 command = button_multiply)
button_divide = Button(root, text = "/", padx = 40, pady = 20,
 command = button_divide)
button_equal = Button(root, text = "=", padx = 120, pady = 20,
 command = button_equal)
button_clear = Button(root, text = "Clearo", padx = 20, pady = 20,
 command = button_clear)
button_1.grid(row = 3, column = 0)
button_2.grid(row = 3, column = 1)
button_3.grid(row = 3, column = 2)
button_4.grid(row = 2, column = 0)
button_5.grid(row = 2, column = 1)
button_6.grid(row = 2, column = 2)
button_7.grid(row = 1, column = 0)
button_8.grid(row = 1, column = 1)
button_9.grid(row = 1, column = 2)
button_add.grid(row = 4, column = 0)
button_subtract.grid(row = 4, column = 1)
button_0.grid(row = 4, column = 2)
button_multiply.grid(row = 5, column = 0)
button_divide.grid(row = 5, column = 1)
button_clear.grid(row = 5, column = 2)
button_equal.grid(row = 6, column = 0, columnspan = 3)
"""



# EX: set icon
"""
root.title("ratatouille")
root.iconbitmap('arrow.ico')
"""



# EX: quit button
"""
button_quit = Button(root, text = "Exit Program", command = root.quit)
button_quit.pack()
"""



# EX: display image
# NOTE: images must be added to a widget, then added to frame
"""
my_img = ImageTk.PhotoImage(Image.open("Pic3.jpg"))
my_label = Label(image = my_img)
my_label.pack()
"""



# EX: frame within root
"""
frame = LabelFrame(root, text = "ratatouille", padx = 50, pady = 50)
frame.pack(padx = 100, pady = 100)
b = Button(frame, text = "click")
b.pack()
"""



# EX: radio buttons
"""
MODES = [
	("ratat", "ouille"),
	("rat", "atouille"),
	("ratatou", "ille"),
]
remy = StringVar()
remy.set("ratat")
for text, mode in MODES:
	Radiobutton(root, text = text, variable = remy, value = mode).pack()
def clicked(value):
	myLabel = Label(root, text = value)
	myLabel.pack()

myButton = Button(root, text = "click here", command = lambda: clicked(remy.get())).pack()
"""



# EX: message box
"""
# NOTE: some method options include:
#		showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
def popup():
	messagebox.showinfo("popup", "ratatouille")
Button(root, text = "popup", command = popup).pack()
"""



# EX: create new window
"""
def open():
	top = Toplevel()
	myLabel = Label(top, text = "hello hello").pack()
	button2 = Button(top, text = "close window", command = top.destroy).pack()
myButton = Button(root, text = "open second window", command = open).pack()
"""



# EX: checkboxes
"""
root.geometry("400x400")
def show():
	myLabel = Label(root, text = var.get()).pack()
var = StringVar()
c = Checkbutton(root, text = "check dis", variable = var, onvalue = "on",
 offvalue = "off")
c.pack()
c.deselect() # box is unchecked on default
myLabel = Label(root, text = var.get())
myButton = Button(root, text = "show selection", command = show).pack()
"""



# EX: dropdown menu
"""
root.geometry("400x400")
def show():
	myLabel = Label(root, text = clicked.get()).pack()
options = [
	"Monday",
	"Tuesdsay",
	"Wednesday",
	"Thursday",
	"Friday",
	"Saturday",
	"Sunday",
]
clicked = StringVar()
clicked.set(options[0]) # set default menu value
drop = OptionMenu(root, clicked, *options) # *options is the same as "M", "T"...
myButton = Button(root, text = "show selection", command = show).pack()
drop.pack()
"""



# EX: databases
#conn = sqlite3.connect("address_book.db") # if this database doesn't already
#											exist, this will create it
# cursor:		we send off the cursor to get stuff from database
#c = conn.cursor()
"""
def submit():
	conn = sqlite3.connect("address_book.db")
	c = conn.cursor()

	c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
	 	{
			"f_name": f_name.get(),
			"l_name": l_name.get(),
			"address": address.get(),
			"city": city.get(),
			"state": state.get(),
			"zipcode": zipcode.get()
		})


	conn.commit() # commit changes
	conn.close() # close connection
	# clear text boxes
	f_name.delete(0, END)
	l_name.delete(0, END)
	address.delete(0, END)
	city.delete(0, END)
	state.delete(0, END)
	zipcode.delete(0, END)

def query():
		conn = sqlite3.connect("address_book.db")
		c = conn.cursor()
		c.execute("SELECT *, oid FROM addresses")
		records = c.fetchall() # can specify exact number if needed
		#print(records) # can print out lines to terminal
		print_records = ''
		for record in records:
			print_records += str(record[0]) + "\t" + str(record[6]) + "\n"
		query_label = Label(root, text = print_records)
		query_label.grid(row = 11, column = 0, columnspan = 2)
		conn.commit()
		conn.close()

def delete():
	conn = sqlite3.connect("address_book.db")
	c = conn.cursor()
	c.execute("DELETE from addresses WHERE oid =" + delete_box.get())
	conn.commit()
	conn.close()

f_name = Entry(root, width = 30) # create text boxes
f_name.grid(row = 0, column = 1, padx = 20, pady = (10, 0))
l_name = Entry(root, width = 30)
l_name.grid(row = 1, column = 1)
address = Entry(root, width = 30)
address.grid(row = 2, column = 1)
city = Entry(root, width = 30)
city.grid(row = 3, column = 1)
state = Entry(root, width = 30)
state.grid(row = 4, column = 1)
zipcode = Entry(root, width = 30)
zipcode.grid(row = 5, column = 1)
delete_box = Entry(root, width = 30)
delete_box.grid(row = 9, column = 1, pady = 5)

f_name_label = Label(root, text = "First Name") # create text box labels
f_name_label.grid(row = 0, column = 0, pady = (10, 0))
l_name_label = Label(root, text = "Last Name")
l_name_label.grid(row = 1, column = 0)
address_label = Label(root, text = "Address")
address_label.grid(row = 2, column = 0)
city_label = Label(root, text = "City")
city_label.grid(row = 3, column = 0)
state_label = Label(root, text = "State")
state_label.grid(row = 4, column = 0)
zipcode_label = Label(root, text = "Zipcode")
zipcode_label.grid(row = 5, column = 0)
delete_box_label = Label(root, text = "Delete ID")
delete_box_label.grid(row = 9, column = 0, pady = 5)

submit_btn = Button(root, text = "add record to db", command = submit)
submit_btn.grid(row = 6, column = 0, columnspan = 2, pady = 10, padx = 100,
 ipadx = 100)
query_btn = Button(root, text = "Show Records", command = query)
query_btn.grid(row = 7, column = 0, columnspan = 2, pady = 10, padx = 10,
 ipadx = 137)
delete_btn = Button(root, text = "delete records", command = delete)
delete_btn.grid(row = 10, column = 0, columnspan = 2, pady = 10, padx = 10,
 ipadx = 136)
"""





root.mainloop() # repeats ^ instructions until Frame is closed
