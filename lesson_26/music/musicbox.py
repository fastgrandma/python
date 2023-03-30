# import random
# import playsound
#
#
# class MusicBox:
#     def __init__(self):
#         self.variants = "b"  # Варианты звуков
#         self.score = 0  # Очки
#         self.sequence = random.choice(self.variants)  # Последовательность
#
#     def __sledushiy(self):
#         dlina = len(self.sequence)
#         self.sequence += random.choice(self.variants)
#
#     def proverit(self, otvet):
#         if otvet == self.sequence:
#             playsound.playsound("sounds/correct.wav")
#             self.__sledushiy()
#             self.score += 1
#         else:
#             playsound.playsound("sounds/incorrect.wav")
#             self.score -= 1
#
#     def igraem(self):
#         for bukva in self.sequence:
#             playsound.playsound(f"sounds/{bukva}.mp3")

