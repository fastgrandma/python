import easygui
# import random
#
# def rock_paper_scissors():
#     otvets = {"бумога":"img/33.png","ножница":"img/22.png","каминь":"img/1.png"}
#     easygui.buttonbox(
#         msg="выбрал быстро вайййй",
#         title="каминь, ножница, бумога",
#         image=["img/1.png", "img/22.png", "img/33.png"],
#         choices=("домоййййййййййййййййййййййй",)
#
#     )
# answer_comp = random.choice(list(otvets.keys()))
#
#
# def guess_the_number():
#     easygui.msgbox()
#
#
#
# games = [
#     'Камень, ножницы, бумага',
#     'Угадай число'
# ]
#
# games_entry_points = [
#     rock_paper_scissors,
#     guess_the_number
# ]
#
# while True:
#     res = easygui.buttonbox('Выбери игру!', choices=games)
#     if res is None:
#         break
#     games_entry_points[games.index(res)]()

easygui


def rock_paper_scissors():
    easygui.msgbox('Здесь будет игра "Камень, ножницы, бумага"')


def guess_the_number():
    easygui.msgbox('Здесь будет игра "Угадай число"')


games = [
    'Камень, ножницы, бумага',
    'Угадай число'
]

games_entry_points = [
    rock_paper_scissors,
    guess_the_number
]

while True:
    res = easygui.buttonbox('Выбери игру!', choices=games)
    if res is None:
        break
    games_entry_points[games.index(res)]()