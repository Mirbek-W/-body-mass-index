from tkinter import *

root=Tk()
root.geometry("350x380")
root.resizable(width=False, height=False)
root.title("Индекс массы тела")
root.iconbitmap("logo.ico")




#текст в начале!
iop0=Label(text="Индекс массы тела (ИМТ) - величина, позволяющая оценить \n степень соответствия массы человека и его роста и\n тем самым косвенно судить о том, является ли масса\n недостаточной, нормальной или избыточной. ИМТ важен\n при определении показаний для лечения. ")
iop0.grid(row=0,column=0)

#инпут 01 вес
jkl=Label(text="Ваш вес?")
iop1 = Entry(root,width=20, font=15)
jkl2=Label(text="kg")

iop1.grid (row=1,column=0)
jkl.place(x=1,y=84)
jkl2.place(x=247,y=84)

# инпут 02

jkl1=Label(text="Ваш рост?")
iop2 = Entry(root, width=20, font=15)
jkl4=Label(text="см")


iop2.grid (row=2,column=0)
jkl1.place(x=1,y=104)
jkl4.place(x=247,y=104)

# кнопка проверить !
but1= Button (root,background="#EC5B25" ,text= "проверить!")
but1.place(x=220, y=128)

output1=Label(root,font="14")

def fun1(event):
    input1=float(iop1.get())
    input2=float(iop2.get())

    res=float("{0:.2f}".format(input1/((input2/100)*(input2/100))))


   
    
    if res<=16:
        output1["text"]="Выраженный дефицит массы тела"
        print("все работает!")
    else:
        print("что то нито")

    output1.place(x=3,y=200)

 


# привязка к функции!!
but1.bind("<Button-1>",fun1)











#output


















root.mainloop()