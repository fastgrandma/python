import tkinter as tk

def show_message():
     # прием значения
     message = ent.get()
     ent.delete(0, 'end')

     print(message)


window = tk.Tk()
window.geometry("600x800")
lab = tk.Label(window, text="ваш адрес", font="Verdana 18", fg="Black", bg="Wheat")
lab.pack()

ent = tk.Entry(bd=10, width=30, )
ent.pack()

lab = tk.Label(window, text="комментарий:", font="Verdana 18", fg="Black", bg="Wheat")
lab.pack()

window.configure(background='CadetBlue2')

txt = tk.Text()
txt.pack()
txt['width'] = 50
txt['height'] = 20

window.configure(background='wheat')



btn = tk.Button(command=show_message())
btn.pack()
btn['width'] = 30
btn['height'] = 3
btn['text'] = "отправить"
btn['background'] = "blue"
btn['foreground'] = "Black"



window.mainloop()