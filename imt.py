from cProfile import label
from tkinter import *
from tkinter import font

root=Tk()
root.geometry("350x380")
root.resizable(width=False, height=False)
root.title("Индекс массы тела -W")
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

output1=Label(root,font="14",fg="#FF0000")
output2=Label(root,fg="#EC5B25")
output_V=Label(root,font="14")


def fun1(event):
    try:
        input1=float(iop1.get())
        input2=float(iop2.get())
        res=float("{0:.2f}".format(input1/((input2/100)*(input2/100))))


    


   
    
        if res<=16:
            output1["text"]="   Выраженный дефицит массы тела"
            output2["text"]="ИМТ ниже 18,5 кг/м2 определяется как недостаточная\n масса (16–18,5 кг/м2), ниже 16 кг/м2 — выраженный\n дефицит массы тела"
            output_V["text"]=res 
        elif res<=18.5:
            output1["text"]="Недостаточная масса тела (дефицит)"
            output2["text"]="В соответствии с классификацией ВОЗ нормальным (здоровым)\nпоказателем ИМТ считается диапазон 18,5–24,99 кг/м2.\nИМТ ниже 18,5 кг/м2 определяется как недостаточная масса\n тела (16–18,5 кг/м2), ниже 16 кг/м2 — выраженный дефицит\n массы тела."
            output_V["text"]=res

        elif res<=24:
            output1["text"]="Нормальная масса тела"
            output2["text"]="Для взрослых нормальной массой тела считается\nтакая, при которой ИМТ находится в интервале\n от 18,5 до 25."
            output_V["text"]=res

        elif res<=30:
            output1["text"]="Избыточная масса тела (предожирение)"
            output2["text"]="сравнить с нормативными показателями – если\n получится небольше 25 единиц – то масса тела не\n превышает норму,при ожирении ИМТ больше 30\n единиц, а состояние с ИМТ в диапазоне\n25-30 называется избыточным весом (предожирением)"
            output_V["text"]=res

        elif res<=35:
            output1["text"]="Ожирение I степени"
            output2["text"]="При первой степени ожирения избыточная \nтела превышает идеальную, или нормальную на 10 – 30%.\nПри 2 степени ожирения – на 30 – 50%. 3 степень\n ожирения – это превышения массы тела на 50 – 100%."
            output_V["text"]=res

        elif res<=40:
            output1["text"]="Ожирение II степени"
            output2["text"]="Ожирение 2 степени — это серьезная патология,\nкоторая несет серьезные эстетические\n изменения тела"
            output_V["text"]=res

        elif res>40:
            output1["text"]="Ожирение III степени"
            output2["text"]="Ожирение третьей степени — значительное повышение\nмассы тела, при котором индекс массы тела (ИМТ)\nсоставляет более 40. Как правило, накопление такой массы\nидет постепенно, т. е. это результат прогрессирующего\n ожирения предыдущих степеней."
            output_V["text"]=res

        else:
            output1["text"]=" "
            output2["text"]=" "

    except ValueError:
        output1["text"]="не верное значение !"  
        output2["text"]=" "   
        output_V["text"]=" " 
    except UnboundLocalError:
        output1["text"]="не верное значение !"  
        output2["text"]=" "   
        output_V["text"]=" " 
    
    output_V.place(x=40,y=180)
    output1.place(x=3,y=200)
    output2.place(x=0,y=220)

 


# привязка к функции!!
but1.bind("<Button-1>",fun1)




























root.mainloop()