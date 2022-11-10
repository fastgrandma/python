import random

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
hand_player = [random.choice(cards)]
hand_computer = [random.choice(cards)]
score_player = 0
score_computer = 0
get_card = "y"
while get_card == "y":
    hand_player.append(random.choice(cards))
    if sum(hand_player) > 21 and 11 in hand_player:
        for i in range(0, len(hand_player)): # перебираем карты
            if hand_player[i] == 11: # ищем туз...
                hand_player[i] = 1 # меняем 11 на 1
                break # только до первого туза

    score_player = sum(hand_player)
    print(f"твоя рука: {hand_player}. очков: {score_player}")
    print(f"Первая карта компутера: {hand_computer[0]}")
    if score_player > 21:
        get_card = "n"
    else:
        get_card = input("берем карту? y - да, n - нет")
