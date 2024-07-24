from tkinter import*
import random
root=Tk()
root.geometry("750x750")
root.title("Game")
myframe=LabelFrame(root,text="STONE PAPER SCISSOR")
myframe.pack()
label1=Label(myframe,text="STONE PAPER SCISSOR")
label1.grid(row=0,column=2,pady=2)

c=["ROCK","PAPER","SCISSOR"]
x=""
comp=0
you=0
def sci():
    global x
    x="SCISSOR"
    label5.config(text=x)   
    winlose(x)   
def rock():
    global x
    x="ROCK"
    label5.config(text=x)
    winlose(x)    
def pap():
    global x
    x="PAPER"
    label5.config(text=x)
    winlose(x)
def winlose(x):
    global comp
    global you
    y=random.choice(c)
    label3.config(text=y)
    if x==y:
        pass    
    elif x=="ROCK" and y=="PAPER":
        comp=comp+1   
    elif x=="ROCK" and y=="SCISSOR":
        you=you+1   
    elif x=="PAPER" and y=="ROCK":
        you=you+1       
    elif x=="PAPER" and y=="SCISSOR":
        comp=comp+1   
    elif x=="SCISSOR" and y=="ROCK":
        comp=comp+1    
    elif x=="SCISSOR" and y=="PAPER":
        you=you+1    
    a=str(comp)
    b=str(you)
    label8.config(text=a)
    label9.config(text=b)
    button1.config(state=DISABLED)
    button2.config(state=DISABLED)
    button3.config(state=DISABLED)
def replay():
    global x
    x=""
    label5.config(text="                   ")
    label3.config(text="                   ")
    button1.config(state=NORMAL)
    button2.config(state=NORMAL)
    button3.config(state=NORMAL)

photo = PhotoImage(file = r"C:\Users\Tanishk\Downloads\scissor.jpeg").subsample(5,5)
button1=Button(myframe,text="SCISSOR",image=photo,command=sci)
button1.grid(row=1,column=0,padx=10,pady=10)

photo2=PhotoImage(file=r"C:\Users\Tanishk\Downloads\paper.jpeg").subsample(5,5)
button2=Button(myframe,text="PAPER",image=photo2,command=pap)
button2.grid(row=1,column=2,pady=2)

photo3=PhotoImage(file=r"C:\Users\Tanishk\Downloads\rock2.png").subsample(2,2)
button3=Button(myframe,text="ROCK",image=photo3,command=rock)
button3.grid(row=1,column=4,padx=20,pady=2)

label2=Label(myframe,text="Computer choose")
label2.grid(row=3,column=0,padx=55,columnspan=3)
label3=Label(myframe,text="                   ",bg="pink")
label3.grid(row=3,column=3,columnspan=2)
label4=Label(myframe,text="You choose")
label4.grid(row=5,column=0,padx=55,pady=10,columnspan=3)
label5=Label(myframe,text="                   ",bg="sky blue")
label5.grid(row=5,column=3,columnspan=2)
label6=Label(myframe,text="COMPUTER")
label6.grid(row=6,column=1,columnspan=2,pady=10)
label7=Label(myframe,text="You")
label7.grid(row=6,column=3,columnspan=2)
label8=Label(myframe,text="     0      ",bg="pink")
label8.grid(row=7,column=1,columnspan=2)
label9=Label(myframe,text="     0        ",bg="sky blue")
label9.grid(row=7,column=3,columnspan=2)

button4=Button(myframe,text="Play again",command=replay)
button4.grid(row=8,column=2,pady=30,padx=50,columnspan=2)
button5=Button(myframe,text="EXIT",command=root.destroy)
button5.grid(row=9,column=2,padx=50,pady=10,columnspan=2)

root.mainloop()
