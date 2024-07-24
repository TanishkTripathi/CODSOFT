#PASSWORD GENERATOR
import random
import string
from tkinter import*
root=Tk()                 #GUI
root.geometry("750x750")
root.title("PASSWORD GENERATOR")
myframe=LabelFrame(root,text="PASSWORD GENERATOR",bg="light grey")
myframe.pack()
mylabel=Label(myframe,text="Enter length",bg="white")
mylabel.grid(row = 0, column = 0, pady = 2)
ent=Entry(myframe,width=10,borderwidth=3,bg="white")
ent.grid(row = 0, column = 1, pady = 2)
l=list(string.ascii_lowercase)
u=list(string.ascii_uppercase)
n=['0','1','2','3','4','5','6','7','8','9','0']
s=list(string.punctuation)
password=[]
def easy():               #function for easy password
    x=int(ent.get())
    if x<6:
        mylabel6=Label(myframe,text="Length should be more than 5")
        mylabel6.grid(row=4,column=1)
    elif x>12:
        mylabel7=Label(myframe,text="Length should be less than 13")
        mylabel7.grid(row=4,column=1)
    else:
        password.append(random.choice(u))
        password.append(random.choice(n))
        password.append(random.choice(s))
        for i in range(3,x):
            password.append(random.choice(l))
        random.shuffle(password)
        y=''.join(password)
        label5.config(text=y)
def medium():               #function for medium password
    x=int(ent.get())
    if x<6:
        mylabel6=Label(myframe,text="Length should be more than 5")
        mylabel6.grid(row=4,column=1)
    elif x>12:
        mylabel7=Label(myframe,text="Length should be less than 13")
        mylabel7.grid(row=4,column=1)
    else:
        password.append(random.choice(s))
        for i in range(2):
            password.append(random.choice(u))
            password.append(random.choice(n))
        for i in range(x-5):
            password.append(random.choice(l))
        random.shuffle(password)
        y=''.join(password)
        label5.config(text=y)
def hard():                 #function for hard password
    x=int(ent.get()) 
    x=int(ent.get())
    if x<6:
        mylabel6=Label(myframe,text="Length should be more than 5")
        mylabel6.grid(row=4,column=1)
    elif x>12:
        mylabel7=Label(myframe,text="Length should be less than 13")
        mylabel7.grid(row=4,column=1)
    else:
        for i in range(x//4):
            password.append(random.choice(u))
            password.append(random.choice(n))
            password.append(random.choice(l))
            password.append(random.choice(s))
        for i in range(x%4):
            password.append(random.choice(l))
        random.shuffle(password)
        y=''.join(password)
        label5.config(text=y)

#to use the button
bt=Button(myframe,text="Easy",command=easy,bg="white",borderwidth=3)
bt.grid(row=2,column=0,pady=2)
bt2=Button(myframe,text="Medium",command=medium,bg="white",borderwidth=3)
bt2.grid(row=2,column=1,pady=2)
bt3=Button(myframe,text="Hard",command=hard,bg="white",borderwidth=3)
bt3.grid(row=2,column=2,pady=2)
label4=Label(myframe,text="Password",borderwidth=5)
label4.grid(row=3,column=0,pady=2)
label5=Label(myframe,text="             ",bg="white")
label5.grid(row=3,column=1,pady=2)
root.mainloop()

