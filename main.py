from tkinter import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from email.message import EmailMessage
import smtplib


# ---------------------------- MAP FUNCTION  ------------------------------- #
def findmap(location):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.google.com/maps")

    search_box = driver.find_element(By.ID, "searchboxinput")
    search_box.send_keys(location, Keys.ENTER)


# ---------------------------- REMINDER FUNCTION  ------------------------------- #
my_mail = "purduefreeloaders@gmail.com"
my_pass = "lkqlwoywgrlefkcy"


def reminder(email):
    iteration = eventList.index(desired_output)
    location = eventLocation_List[iteration]
    time = eventDetails[iteration]
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()  # Ensures a secure connection.
        connection.login(user=my_mail, password=my_pass)
        connection.sendmail(from_addr=my_mail, to_addrs="shivam20050125@gmail.com",
                            msg=f"Subject:Purdue Free Loaders\n\nThere is an event in{location}at{time}.Have a nice day!\nWith regards,\nFree Loaders")
        connection.close()


# ---------------------------- TKINTER UI -01  ------------------------------- #
def button_click():
    global userInput
    userInput = "FreeFood"
    window.destroy()


def button_click2():
    global userInput
    userInput = "Merchandise"
    window.destroy()


window = Tk()
window.title("Purdue University | West Lafayette")
window.geometry("800x600")

img = PhotoImage(file="./Images/int_bg_2.png")
canvas = Canvas(width=800, height=600, highlightthickness=0)
canvas.create_image(400, 300, image=img)
canvas.place(x=0, y=0)

# Buttons
my_image = PhotoImage(file="./Images/FF 2.png")
food_button = Button(image=my_image, highlightthickness=0, borderwidth=0, command=button_click)
food_button.place(x=315, y=386)

my_image2 = PhotoImage(file="./Images/FS 2.png")
stuff_button = Button(image=my_image2, highlightthickness=0, borderwidth=0, command=button_click2)
stuff_button.place(x=330, y=422)

mainloop()
# ------------------------------ WEB SCRAPING -------------------------------- #
bolierlinkURL = "https://boilerlink.purdue.edu/events?perks="

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('headless')
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(bolierlinkURL + userInput + "&shortcutdate=tomorrow")

eventList = driver.find_elements(By.CSS_SELECTOR,
                                 "h3[style='font-size: 1.06rem; font-weight: 600; overflow: visible; margin: 0.125rem 0px 0.313rem; line-height: 1.313rem; display: -webkit-box; max-width: 400px; -webkit-line-clamp: 2; -webkit-box-orient: vertical; text-overflow: initial;'")
eventList = [item.text for item in eventList]
eventDetails = driver.find_elements(By.CSS_SELECTOR, "div[style='margin: 0px 0px 0.125rem;']")
eventDetails = [item.text for item in eventDetails]
eventLocation_List = []
for i in range(len(eventDetails)):
    eventLocation = driver.find_element(By.XPATH, "//*[@id='event-discovery-list']/div/div[" + str(
        i + 1) + "]/a/div/div[3]/div[1]/div[2]")
    eventLocation_List.append(eventLocation.text)

driver.quit()

# ---------------------------- TKINTER UI -02  ------------------------------- #
window = Tk()
window.title("Purdue University | West Lafayette")
window.geometry("1200x700")

# Canvas
img = PhotoImage(file="./Images/map.png")
img2 = PhotoImage(file="./Images/PU3.png")
img3 = PhotoImage(file="./Images/PU4.png")
canvas = Canvas(width=1200, height=700, highlightthickness=0)
canvas.create_image(600, 350, image=img)
canvas.create_image(1100, 350, image=img2)
canvas.create_image(170, 350, image=img3)
canvas.place(x=0, y=0)

# Labels
my_label = Label(text="FREE LOADERS", relief=FLAT, font=("Impact", 65), bg='#CEB888', borderwidth=6)
my_label.place(x=425, y=20)
my_label = Label(text="PURDUE", relief=FLAT, font=("Impact", 18), highlightthickness=0, borderwidth=0, bg='#CEB888')
my_label.place(x=447, y=20)
my_label = Label(text="WEST LAFAYETTE", relief=FLAT, font=("Impact", 15), highlightthickness=0, borderwidth=0,
                 bg='#CEB888')
my_label.place(x=690, y=97)
my_label = Label(text="Freebies for the Day", relief=FLAT, font=("Arial", 15, 'bold'), highlightthickness=0,
                 borderwidth=0, bg='#CEB888')
my_label.place(x=430, y=160)
my_label_change = Label(
    text="Introduction\n\nWelcome to the Purdue University Free Loaders \nprogram! This program is designed to help Purdue University students and \ncommunity members discover and access free food and other items on or \naround the campus. Many valuable resources often go unnoticed, and this \ntool aims to bridge that gap by providing daily updates on available freebies.\n\nThe program has been compiled by:\n1)Shivam Rastogi\n2)Ian Condes\n3)Priyanka Bansal",
    relief=FLAT, font=("Big Caslon", 15,), highlightthickness=0,
    borderwidth=0, bg='#CEB888', width=63)
my_label_change.place(x=370, y=450)

# Input Box
input = Entry()
input.config(width=34)
input.insert(END, string="Enter your mail id:")
input.place(x=458, y=345)


# Butttons
def button_click3():
    try:
        iteration = eventList.index(desired_output)
        my_label_change["text"] = eventDetails[iteration] + eventLocation_List[iteration]
    except:
        pass


def button_click4():
    if (desired_output):
        iteration = eventList.index(desired_output)
        location = eventLocation_List[iteration] + " Purdue University"
        findmap(location)


def button_click5():
    user_mail = input.get()
    reminder(user_mail)
    # window.destroy()


info_button = Button(text="More Information", command=button_click3)
info_button.place(x=485, y=300, width=220)

location_image = PhotoImage(file="./Images/mapicon.png")
location_button = Button(image=location_image, highlightthickness=0, borderwidth=0, command=button_click4)
location_button.place(x=715, y=300)

remind_image = PhotoImage(file="./Images/log 2.png")
remind_button = Button(image=remind_image, highlightthickness=0, borderwidth=0, command=button_click5)
remind_button.place(x=540, y=380)


def listbox_output(event):
    global desired_output
    selected_indices = mylist2.curselection()
    if selected_indices:
        desired_output = mylist2.get(selected_indices)
    else:
        desired_output = ""


scrollbar = Scrollbar(window)
scrollbar.place(x=760, y=190, height=102)
mylist2 = Listbox(window, height=6, yscrollcommand=scrollbar.set)
if (eventList == []):
    eventList = ["!! --There are no such Events for today.-- !!"]
for item in eventList:
    mylist2.insert(eventList.index(item), item)
mylist2.bind("<<ListboxSelect>>", listbox_output)
mylist2.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=mylist2.yview)
mylist2.place(x=460, y=190, width=300)

mainloop()
