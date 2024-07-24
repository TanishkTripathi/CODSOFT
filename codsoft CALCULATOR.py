from tkinter import*

def click(value):
    x=ent1.get()
    if value=="AC":
        ent1.delete(0,END)
    elif value=="+/-":
        if x:
            if x[0]=="-":
                ent1.delete(0)
            elif x[0]=="+":
                ent1.delete(0)
                ent1.insert(0,"-")
            else:
                ent1.insert(0,"-")
    elif value == "=":
       try:
           b = eval(x)
           ent1.delete(0,END)
           ent1.insert(END,str(b))
       except Exception as e:
           ent1.delete(0,END)
           ent1.insert(END,"Error")
    else:
        ent1.insert(END,value)
root=Tk()        
root.geometry("750x750")
root.title("CALCULATOR")
frame1=LabelFrame(root,text="CALCULATOR")
frame1.pack()
ent1=Entry(frame1,width=15)
ent1.grid(row = 1, column = 0, pady = 2,columnspan=4)
buttons=[
    ("AC",2,0),("+/-",2,1),("%",2,2),("/",2,3),
    ("1",3,0),("2",3,1),("3",3,2),("*",3,3),
    ("4",4,0),("5",4,1),("6",4,2),("-",4,3),
    ("7",5,0),("8",5,1),("9",5,2),("+",5,3),
    ("0",6,0,2),(".",6,2),("=",6,3)
]
for(text,row,col,*span) in buttons:
    width=5 if text=="0" else 4
    columnspan =span[0] if span else 1
    Button(frame1,text=text,width=width,command=lambda t=text: click(t)).grid(row=row,column=col,columnspan=columnspan,pady=2)
root.mainloop()
