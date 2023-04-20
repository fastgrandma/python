import tkinter as tk
root = tk.Tk()
root.geometry("600x500")
# # def kak_hochesh():
# #     if btn["state"] == "disabled":
# #         btn["state"] = "normal"
# #         btn["text"] = "активен"
# #     else:
# #         btn["state"] = "disabled"
# #         btn["text"] = "не активен"
# #
# #
# #
# #

# # cb = tk.Checkbutton(root,
# #                     text="активировать",
# #                     command=kak_hochesh)
# #
# #
# #
# #
# # cb.pack()
# # cb.select()
# # btn = tk.Button(root,
# #                text="НЕ активен",
# #                state=tk.DISABLED)
# #
# #
# #
# #
# #
# #
# #
# # btn.pack()
# #
# #
# #


# № 2

def bold():
    if cb1_val.get():
        lab["font"] += "bold"
    else:
        lab["font"] = lab["font"].replace


lab = tk.Label(root,
               text="abc",
               font="Arial 12")
lab.pack
# ==========================
cb1_val = tk.BooleanVar()

cb1 = tk.Checkbutton(root,
                     text="Жирный",
                     variable=cb1_val,
                     onvalue=True,
                     offvalue=False,
                     command=bold
                     )
# ==========================
def italic():
    if cb2_val.get():
        lab["font"] += "italic"
    else:
        lab["font"] = lab["font"].replace




cb2_val = tk.BooleanVar()




cb2 = tk.Checkbutton(root,
                     text="Курсив",
                     variable=cb2_val,
                     onvalue=True,
                     offvalue=False,
                     command=italic
                     )

# ==========================
def overstrike():
    if cb3_val.get():
        lab["font"] += "overstrike"
    else:
        lab["font"] = lab["font"].replace



cb3_val = tk.BooleanVar()



cb3 = tk.Checkbutton(root,
                     text="Жирный",
                     variable=cb3_val,
                     onvalue=True,
                     offvalue=False,
                     command=overstrike
                     )

# ==========================





cb4_val = tk.BooleanVar()



cb4 = tk.Checkbutton(root,
                     text="Жирный",
                     variable=cb4_val,
                     onvalue=True,
                     offvalue=False,
                     command=
                     )







root.mainloop()