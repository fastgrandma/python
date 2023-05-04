from tkinter import *
#
win = Tk()
win.geometry('700x600')
#
#
# def poop():
#     global timer
#     c.delete('all')
#     timer += 1
#     c.create_image(300, 250, image=img)
#     c.create_text(300, 255, text=timer, font='Arial 25')
#     c.after(1000, poop)
#
#
# img = PhotoImage(file='CHASI.png').subsample(4, 4)
#
c = Canvas(win, width=600, height=300, bg='silver')
c.pack(anchor=CENTER, expand=True)
# timer = 0
#
# poop()



c.create_text(10, 10, anchor=NW, text="Школа", font="Arial 20")
c.create_text(150, 25, 250, 25, arrow=LAST)
c.create_text(10, 10, anchor=NW, text="Школа", font="Arial 20")
c.create_text(150, 25, 250, 25, arrow=LAST)























win.mainloop()








