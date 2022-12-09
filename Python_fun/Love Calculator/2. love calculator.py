from tkinter import *
import random

root = Tk()
root.geometry('400x240')  # Defining the container size, width=400, height=240
root.title('Love Calculator????')  # Title of the container


def calculate_love():
    st = '0123456789'  # value will contain digits between 0-9
    digit = 2  # result will be in double digits
    temp = "".join(random.sample(st, digit))
    result.config(text=temp)


# Top heading
heading = Label(root, text='Love Calculator - How much is he/she into you')
heading.pack()

# Slot/input for the first name
slot1 = Label(root, text="Enter Your Name:")
slot1.pack()
name1 = Entry(root, border=5)
name1.pack()

# Slot/input for the partner name
slot2 = Label(root, text="Enter Your Partner Name:")
slot2.pack()
name2 = Entry(root, border=5)
name2.pack()

bt = Button(root, text="Calculate", height=1,
            width=7, command=calculate_love)
bt.pack()

# Text on result slot
result = Label(root, text='Love Percentage between both of You:')
result.pack()

# Starting the GUI
root.mainloop()