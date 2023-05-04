from tkinter import *
root = Tk()
root.geometry("550x650")


c = Canvas(root, width=500, height=600, bg="lightblue")
c.pack(anchor=CENTER, expand=True)
# ============================================ Работа с текстом
# c.create_text(0, 0,
#               text="Пельмени * 8",
#               font="Arial 25",
#               fill="gold2",
#               anchor=NW)

# ============================================ Прямоугольник
# c.create_rectangle(10, 10,
#                    200, 150,
#                    fill='red',
#                    width=10,
#                    outline="darkred"
#                    )


# ========================================== окружность
# c.create_oval(10, 10,
#               150, 150)


# # ============================================ arc
# c.create_oval(10, 10,
#              150, 150,
#              fill='green2')
#
# c.create_arc(10, 10,
#             150, 150,
#              fill='gold2',
#              start=30,
#              extent=-45,
#              style=CHORD)
#
# c.create_arc(10, 10,
#             150, 150,
#              fill='orange',
#              start=90,
#              extent=135,
#              style=ARC,
#              width=10)

# ==================================== Линии
# c.create_line(10, 10,
#               150, 150,
#               arrow="both",
#               arrowshape=(50, 50, 50),
#               width=20)

# ================================== DASH
c.create_rectangle(10, 10,
                   200, 150,
                   fill='red',
                   width=10,
                   outline="darkred",
                   dash="-..",
                   activefill="blue",
                   activewidth=20)













root.mainloop()