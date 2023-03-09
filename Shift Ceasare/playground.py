from tkinter import *
from for_shifr import alphabet

def ceaser_encode(start_text, shift_amount):
    end_text = ""
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift_amount) % len(alphabet)
            end_text += alphabet[new_position]
        else:
            end_text += char
    return end_text

def ceaser_decode(start_text, shift_amount):
    end_text = ""
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position - shift_amount) % len(alphabet)
            end_text += alphabet[new_position]
        else:
            end_text += char
    return end_text

def reset():
    text.delete('1.0', END)
    finish_text.delete('1.0', END)
    shifts.delete(0, END)

def encode_text():
    start = text.get('1.0', END)
    shift = int(shifts.get())
    encoded = ceaser_encode(start, shift)
    finish_text.delete('1.0', END)
    finish_text.insert(END, encoded)

def decode_text():
    start = text.get('1.0', END)
    shift = int(shifts.get())
    decoded = ceaser_decode(start, shift)
    finish_text.delete('1.0', END)
    finish_text.insert(END, decoded)

window = Tk()
window.geometry("400x400+100+200")
window.title("Шифр Цезаря")
window.config(bg="#DEB3E0")

start_text = Label(window, text="""Введите текст для
кодировки/раскодировки""", font=("Arial", 9, "bold"))
start_text.config(bg="#DEB3E0", fg="#04021C")
start_text.place(x=130, y=0)

text = Text(window, width=37, height=5)
text.focus()
text.place(x=50, y=35)

reset_button = Button(text="Сбросить", font=("Arial", 7, 'bold'), padx=1, pady=1, command=reset)
reset_button.place(x=170, y=350)

finish_text = Text(window, width=37, height=5)
finish_text.place(x=50, y=210)

end_text = Label(window, text="Полученный текст", font=("Arial", 9, "bold"))
end_text.config(bg="#DEB3E0", fg="#04021C")
end_text.place(x=150, y=180)

shift_text = Label(window, text="Смещение = ", font=("Arial", 7, "bold"))
shift_text.place(x=227, y=131)

shifts = Entry(window, width=5)
shifts.place(x=300, y=130)

decode_button = Button(text="Расшифровывать", font=("Arial", 7, 'bold'), padx=1, pady=1, command=decode_text)
decode_button.place(x=260, y=350)

encode_button = Button(text="Зашифровать", font=("Arial", 7, 'bold'), padx=1, pady=1, command=encode_text)
encode_button.place(x=50, y=350)

window.mainloop()
