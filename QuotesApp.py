import requests
from tkinter import *
from tkinter import messagebox
import random

def fetchQuote():
    response = requests.get("https://type.fit/api/quotes")

    data = response.json()

    i = random.randint(0,len(data))

    text = data[i]["text"]
    author = data[i]["author"]

    quoteField.insert(0, text)
    authorField.insert(0, author)

def clearQuote():
    quoteField.delete(0, "end")
    authorField.delete(0, "end")

root = Tk()

# setting the title
root.title("My Quotes App")
root.geometry("600x450")
root.configure(bg="#ff4d4d")

label1 = Label(root,text="Today's Quote",font=("verdana",18,"bold"),justify=CENTER)
label1.pack(side=TOP,pady=15)
label1.configure(bg="#80e5ff")

quoteField = Entry(root,font=("verdana",12),justify=CENTER)
quoteField.pack(side=TOP,fill=X,padx=10,pady=20,ipady=40)
# quoteField.config(state='readonly')
quoteField.configure(bg="#66ff66")

label2 = Label(root,text="Author",font=("verdana",18,"bold"),justify=CENTER)
label2.pack(side=TOP,pady=15)
label2.configure(bg="#80e5ff")

authorField = Entry(root,font=("verdana",12),justify=CENTER)
authorField.pack(side=TOP,fill=X,padx=10,pady=10,ipady=20)
# authorField.config(state='readonly')
authorField.configure(bg="#66ff66")

quoteBtn = Button(root, text="Fetch Quote",font=("verdana",18),relief="ridge",command=fetchQuote)
quoteBtn.pack(side=LEFT,padx=30,pady=20)
quoteBtn.configure(bg="#ff1ac6")

clearBtn = Button(root, text="Clear Quote",font=("verdana",18),relief="ridge",command=clearQuote)
clearBtn.pack(side=RIGHT,padx=30,pady=20)
clearBtn.configure(bg="#ff1ac6")


root.mainloop()

