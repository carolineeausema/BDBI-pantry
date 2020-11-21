import tkinter as tk

# ReadInventory.py

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="Exit", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

    def retrieve_inventory(self):
        amountFile = open("InventoryFile.txt", "r")
        allLines = amountFile.read().split("\n")
        inventory = {}
        for i in allLines:
            eachLine = i.split(";")
            if (len(eachLine) == 2):
                inventory[eachLine[0]] = eachLine[1]
        print(inventory)



root = tk.Tk()
app = Application(master=root)
app.mainloop()
