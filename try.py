# ---------------------------- IMPORT/Variable------------------------------- #
from tkinter import *
import random
import pandas

index = None
BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- FILE MANAGEMENT ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

# def button_click():
#     global userInput
#     userInput = 1
#     window.destroy()
#
#
# def button_click2():
#     global userInput
#     userInput = 2
#     window.destroy()


window = Tk()
window.title("Purdue University | West Lafayette")
window.geometry("1200x700")
# window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

img = PhotoImage(file="map 2.png")
canvas = Canvas(width=800, height=800, highlightthickness=0)
canvas.create_image(400, 350, image=img)
canvas.place(x=0, y=0)

# Labels
my_label = Label(text="FLYBYS FOR THE DAY", relief=FLAT, font=("Impact", 45))
my_label.place(x=820, y=20)
# my_label = Label(text="HIT AND RUN", relief=FLAT, font=("Impact", 13))
# my_label.place(x=1105, y=52)


def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana","Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.place(x=800,y=200)
# # Buttons
# my_image = PhotoImage(file="FF 2.png")
# food_button = Button(image=my_image, highlightthickness=0, borderwidth=0, command=button_click)
# food_button.place(x=315, y=386)
#
# my_image2 = PhotoImage(file="FS 2.png")
#
# stuff_button = Button(image=my_image2, highlightthickness=0, borderwidth=0, command=button_click2)
# stuff_button.place(x=330, y=422)

mainloop()
