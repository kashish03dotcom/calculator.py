import tkinter as tk

root=tk.Tk()
root.title("My First Calculator")
root.geometry("400x400")
root.resizable(False,False)

expression=""

def update_display(value):
    global expression
    expression += str(value)
    display.delete(0,tk.END)
    display.insert(tk.END,expression)

def clear():
    global expression
    expression=""
    display.delete(0,tk.END)
    
def calculate():
    global expression
    try:
        result=eval(expression)
        display.delete(0,tk.END)
        display.insert(tk.END,result)
        expression  =str(result)
    except:
        display.delete(0,tk.END)
        display.insert(tk.END,"Error")
        expression=""
        
display=tk.Entry(root,font=("Arial",20),justify="right")
display.pack(fill="x",padx=10,pady=10)

buttons =[
    ("7",0,0),("8",0,1),("9",0,2),("/",0,3),
    ("4",1,0),("5",1,1),("6",1,2),("*",1,3),
    ("1",2,0),("2",2,1),("3",2,2),("-",2,3),
    ("0",3,0),(".",3,1),("=",3,2),("+",3,3),
    ]

frame =  tk.Frame(root)
frame.pack()

for (text,row,col) in buttons:
    if text=="=":
        cmd=calculate
    else:
        cmd=lambda x=text:update_display(x)

    tk.Button(frame,text=text,width=5,height=2,command=cmd).grid(row=row,column=col,padx=5,pady=5)

    tk.Button(root,text="clear",font=("arial",14),command=clear).pack(fill="x",padx=10,pady=10)

def key_press(event):
    global expression
    key=event.char

    if key in "0123456789+-*/.":
        update_display(key)

    elif event.keysym=="Return":
        calculate()

    elif event.keysym=="BackSpace":
        expression=expression[:-1]
        display.delete(0,tk.END)
        display.insert(tk.END,expression)

    elif event.keysym=="Escape":
        clear()

root.bind("<Key>",key_press)
root.mainloop()