from tkinter import *

root=Tk()
root.geometry("350x380")
root.resizable(width=False, height=False)
root.title("Индекс массы тела")
root.iconbitmap("logo.ico")





iop0=Label(text="Индекс массы тела (ИМТ) - величина, позволяющая оценить \n степень соответствия массы человека и его роста и\n тем самым косвенно судить о том, является ли масса\n недостаточной, нормальной или избыточной. ИМТ важен\n при определении показаний для лечения. ")


iop1 = Entry(root,width=26, font=15)
iop2 = Entry(root, width=26, font=15)
but1= Button (root,background="#EC5B25" ,text= "проверить!")
iop0.grid(row=0,column=0)
iop1.grid (row=1,column=0)
iop2.grid (row=2,column=0)
but1.place(x=220, y=128)


















root.mainloop()