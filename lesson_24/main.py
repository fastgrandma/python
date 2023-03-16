# class Nazvanie:
#     def __init__(self):
#         self.money = 1_000
#         self.__zarplata = 100
#
#     def bar(self):
#         if self.__zarplata > 4:
#             return True
#         else:
#             return False
#
#
#     def __sad(self):
#         print("александру грустно")
#
# sanya = Nazvanie()
#
# # sanya.money += 100
# print(sanya.bar())
#
# sanya._Nazvanie__zarplata = 1_000_000

# class Car:
#     def stop(self):
#         return "машина завелся"
#     def go(self):
#         return "jnrk.xbkcz"
#     def
#


#class Alphabet:
#     def __init__(self, lang):
#         self.__lang = lang
#         self.__letters = string.ascii_lowercase
#     def print(self):
#         print(self.__letters)
#     def letters_num(self):
#         print(len(self.__letters))
#
#
# al = Alphabet("eng")
# al.print()
# al.letters_num()



# задача 3

class Clock:
    def __init__(self):
        #self.__time = datetime.datetime.now().strftime("%H:%M:%S")
        self.__time = "08:07:06"
        self.__h,self.__m,self.__s = self.__time.split(":")
        self.__h,self.__m,self.__s = int(self.__h),int(self.__m),int(self.__s)

    def hours(self):
        self.__h += 1
    def minutes(self):
        self.__m += 1
    def seconds(self):
        self.__s += 1
    def test_h(self):
        if self.__h > 23:
            self.__h = 0
    def test_m(self):
        if self.__m > 59:
            self.__m = 0
            self.__h += 1
    def vivod(self):
        print(f"{self.__h}:{self.__m}:{self.__s}")




time_0 = Clock()
time_0.minutes()
