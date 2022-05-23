# This is going to be a dice rolling program
# Ideally this is primarily a way to somewhat better understand making GUI's with python with a simple program

# Needed imports
import random
import tkinter as tk

# Creating a die class
class Die:
    def __init__(self, name, faces):    # Setting attributes
        self.name = name
        self.faces = faces
    def roll(self, faces):    # Setting methods
        rolled = random.randint(1, faces)
        return rolled

# Defining the die objects
d4 = Die("d4", 4)
d6 = Die("d6", 6)
d8 = Die("d8", 8)
d10 = Die("d10", 10)
d12 = Die("d12", 12)
d20 = Die("d20", 20)

# Setting up the window and the empty result label
main_window = tk.Tk()
result = tk.Label(text="")

# This function updates the result label with the rolled values
def update_result(die_val):
    if isinstance(die_val, Die):
        updated = die_val.roll(die_val.faces)
        result.config(text=updated)
    
# Setting up the buttons - Needed to remember the lambda function
d4_button = tk.Button(main_window, text="D4", command=lambda: update_result(d4))
d6_button = tk.Button(main_window, text="D6", command=lambda: update_result(d6))
d8_button = tk.Button(main_window, text="D8", command=lambda: update_result(d8))
d10_button = tk.Button(main_window, text="D10", command=lambda: update_result(d10))
d12_button = tk.Button(main_window, text="D12", command=lambda: update_result(d12))
d20_button = tk.Button(main_window, text="D20", command=lambda: update_result(d20))

# Attempt to make the gui scale when you enlarge the main_window
main_window.rowconfigure(0,weight=1)
main_window.rowconfigure(1,weight=1)
main_window.rowconfigure(2,weight=1)
main_window.columnconfigure(1,weight=1)
main_window.columnconfigure(2,weight=1)
main_window.columnconfigure(3,weight=1)

# Putting the buttons and result label on the window using the grid
d4_button.grid(row=0, column=1,sticky="NSEW")
d6_button.grid(row=0, column=2,sticky="NSEW")
d8_button.grid(row=0, column=3,sticky="NSEW")
d10_button.grid(row=1, column=1,sticky="NSEW")
d12_button.grid(row=1, column=2,sticky="NSEW")
d20_button.grid(row=1, column=3,sticky="NSEW")
result.grid(row=2, column =2,sticky="NSEW")

# Displaying the window
main_window.mainloop()
