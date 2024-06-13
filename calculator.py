from tkinter import*
calculation=""
def add_to_calculation(symbol):
    global calculation
    calculation+=str(symbol)
    text_result.delete(1.0,"end")
    text_result.insert(1.0,calculation)
    
    pass

def evaluate_calculation():
    global calculation
    try:
        calculation=str(eval(calculation))
        text_result.delete(1.0,"end")
        text_result.insert(1.0,calculation)
        
    except:
        clear_field()
        text_result.insert(1.0,"error")
    
    
    pass


def clear_field():
    global calculation
    calculation=""
    text_result.delete(1.0,"end")
    
    
    pass
    
    
    
root=Tk()
root.geometry("314x275")


text_result=Text(root,height=2,width=17,font=("arial",24),bg="grey")
text_result.grid(columnspan=5)

b1=Button(root,text="1",command=lambda:add_to_calculation(1),width=5,font=("Arial",14))
b1.grid(row=2,column=1)
b2=Button(root,text="2",command=lambda:add_to_calculation(2),width=5,font=("Arial",14))
b2.grid(row=2,column=2)
b3=Button(root,text="3",command=lambda:add_to_calculation(3),width=5,font=("Arial",14))
b3.grid(row=2,column=3)
b4=Button(root,text="4",command=lambda:add_to_calculation(4),width=5,font=("Arial",14))
b4.grid(row=3,column=1)
b5=Button(root,text="5",command=lambda:add_to_calculation(5),width=5,font=("Arial",14))
b5.grid(row=3,column=2)
b6=Button(root,text="6",command=lambda:add_to_calculation(6),width=5,font=("Arial",14))
b6.grid(row=3,column=3)
b7=Button(root,text="7",command=lambda:add_to_calculation(7),width=5,font=("Arial",14))
b7.grid(row=4,column=1)
b8=Button(root,text="8",command=lambda:add_to_calculation(8),width=5,font=("Arial",14))
b8.grid(row=4,column=2)
b9=Button(root,text="9",command=lambda:add_to_calculation(9),width=5,font=("Arial",14))
b9.grid(row=4,column=3)
b0=Button(root,text="0",command=lambda:add_to_calculation(0),width=5,font=("Arial",14))
b0.grid(row=5,column=2)
ba=Button(root,text="+",command=lambda:add_to_calculation("+"),width=5,font=("Arial",14))
ba.grid(row=2,column=4)
bs=Button(root,text="-",command=lambda:add_to_calculation("-"),width=5,font=("Arial",14))
bs.grid(row=3,column=4)
bm=Button(root,text="*",command=lambda:add_to_calculation("*"),width=5,font=("Arial",14))
bm.grid(row=4,column=4)
bd=Button(root,text="/",command=lambda:add_to_calculation("/"),width=5,font=("Arial",14))
bd.grid(row=5,column=4)
bo=Button(root,text="(",command=lambda:add_to_calculation("("),width=5,font=("Arial",14))
bo.grid(row=5,column=1)
bc=Button(root,text=")",command=lambda:add_to_calculation(")"),width=5,font=("Arial",14))
bc.grid(row=5,column=3)
be=Button(root,text="=",command=evaluate_calculation,width=5,font=("Arial",14),bg="orange")
be.grid(row=6,column=3)
bc=Button(root,text="CE",command=lambda:clear_field(),width=5,font=("Arial",14))
bc.grid(row=6,column=1)
bc=Button(root,text=".",command=lambda:add_to_calculation("."),width=5,font=("Arial",14))
bc.grid(row=6,column=2)

root.mainloop()