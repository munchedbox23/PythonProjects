from tkinter import *
import smtplib


email_send = "example@gmail.com"
password = "your_password"

def send():
    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(email_send,password)
        message = f"Subject:NIKITA MELNIKOV KRUT!\n\n{send_text.get('1.0', END)}"
        for i in range(30):
            connection.sendmail(
                from_addr = email_send,
                to_addrs = email_entry.get(),
                msg = message
                )
            
window = Tk()
window.title("Birthday wisher")
window.geometry("500x450")
window.config(padx = 50,pady = 10,bg = "#48D1CC")
send_photo = PhotoImage(file ="Birthday wisher/send_emails.png")
canvas = Canvas(width = send_photo.width(),height = send_photo.height(),bg = "#48D1CC",highlightthickness=0)
canvas.create_image(send_photo.width() / 2, send_photo.height() / 2, image = send_photo)
canvas.place(x = 100,y = 0)



email_label = Label(window,text = "Почта адресата:",bg = "#48D1CC",font = ("Arial",14,"italic"),fg = "#000000")
email_label.place(x = 0,y = 220)

email_entry = Entry(width = 40)
email_entry.place(x = 180, y = 227)

text_label = Label(window,text = "Текст отправления:",bg = "#48D1CC",font = ("Arial",12,"italic"))
text_label.place(x = 0, y = 300)

send_text = Text(width = 30,height=4)
send_text.place(x = 180,y = 280)

letter_img = PhotoImage(file = "Birthday wisher/png-transparent-letter-cleaner-icon-envelope-miscellaneous-blue-angle (1) (1).png")
letter_button = Button(image = letter_img,width = 200,bg = "#DEB887",command = send)
letter_button.place(x = 0,y = 380)

def rubbish():
    email_entry.delete(0, 'end')
    send_text.delete('1.0', 'end')

delete_img = PhotoImage(file = "Birthday wisher/png-transparent-rubbish-bins-waste-paper-baskets-recycling-bin-trash-can-recycling-waste-sticker (1).png")
delete_button = Button(image = delete_img,width = 200,bg = "#DEB887",command = rubbish)
delete_button.place(x = 210,y = 380)

window.mainloop()
