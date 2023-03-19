from tkinter import *

image_list = ["first_ex.png","Second.png","fourth.png","4.png","5.png","6.png","7.png","8.png","9.png","10.png",""]
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
otveti = ["-100","2.35","3.5","2","6","10","100","60000","2400","0.9"," "]
count = 1
index = 0
plus = 0

window = Tk()
window.title("Математический тренажёр")
window.geometry("720x500+100-100")
window.config(padx=50,pady=50)
window.resizable(False, False)
window.config(padx=50,pady=50,bg = YELLOW)


text = Label(text = f"Задание №{count}",font = ("Arial",35,"bold"),bg = YELLOW)
text.place(x = 180, y = 0)

canvas = Canvas(bg = YELLOW,highlightthickness = 0)
exer_image = PhotoImage(file = image_list[index])
canvas.config(width=exer_image.width(), height=exer_image.height())
canvas.create_image(exer_image.width() / 2, exer_image.height() / 2, image=exer_image)
canvas.image = exer_image
canvas.place(x =85, y = 100)

text1 = Label(text = "Введите ответ)",font = ("Arial",15,"bold"),bg = YELLOW)
text1.place(x = 35,y = 320)

y = Label(text = "НЕ ПРАВИЛЬНО",font = ("Arial",50,"bold"),bg = YELLOW,fg = "#FF2400")
x = Label(text = "ПРАВИЛЬНО",font = ("Arial",50,"bold"),bg = YELLOW)
text2 = Label(text = f"Правильный ответ:{otveti[index]}",bg = YELLOW,font = ("Arial",16,"bold"))

def prav_otvet():
    global index
    global plus
    if otvet.get() == otveti[index]:
        plus += 1
        result = Label(text = f"Решено правильно : {plus}/{count}",font = ("Arial",7,"bold"),bg = YELLOW)
        result.place(x = 0,y = 0)
        x.config(text = "ПРАВИЛЬНО")
        x.place(x = 130, y = 200)
    else:
        result = Label(text = f"Решено правильно : {plus}/{count}",font = ("Arial",7,"bold"),bg = YELLOW)
        result.place(x = 0,y = 0)
        y.config(text = "НЕ ПРАВИЛЬНО")
        text2.config(text = f"Правильный ответ:{otveti[index]}")
        text2.place(x = 190,y = 405)
        y.place(x = 130, y = 200)

def next(): 
    global count 
    global index
    count += 1
    index += 1
    canvas.delete("all")
    y.config(text="")
    x.config(text="")
    otvet.delete(0,END)
    text2.config(text="")
    text.config(text=f"Задание №{count}")
    exer_image = PhotoImage(file=image_list[index])
    canvas.config(width=exer_image.width(), height=exer_image.height())
    canvas.create_image(exer_image.width() / 2, exer_image.height() / 2, image=exer_image)
    canvas.image = exer_image
    if(count == 11):
        canvas.delete("all")
        y.config(text="")
        x.config(text="")
        otvet.delete(0,END)
        text2.config(text="")
        text.config(text = "")
        nazad.destroy()
        next_button.destroy()
        proverka.destroy()
        otvet.destroy()
        text1.config(text = "")
        new_text = Label(text = "На сегодня всё",font = ("Arial",24,"bold"),bg = YELLOW)
        new_text.place(x = 200,y = 150)

    
def after():
    global count 
    global index
    count -= 1
    index -= 1
    canvas.delete("all")
    y.config(text="")
    x.config(text="")
    otvet.delete(0,END)
    text2.config(text="")
    text.config(text=f"Задание №{count}")
    exer_image = PhotoImage(file=image_list[index])
    canvas.config(width=exer_image.width(), height=exer_image.height())
    canvas.create_image(exer_image.width() / 2, exer_image.height() / 2, image=exer_image)
    canvas.image = exer_image
    

otvet = Entry(window,width=20)
otvet.place(x = 50, y = 352)

next_button = Button(text = "Дальше",width = 15,height= 2,command=next)
next_button.place(x = 550,y = 345)

nazad = Button(text = "Назад",width = 15,height= 2,command=after)
nazad.place(x = 440,y = 345)


proverka = Button(window,text = "Проверить ответ",width = 15,height= 2, command = prav_otvet)
proverka.place(x = 50,y = 400)



window.mainloop()
