# class Chelovek:
#     def __init__(self, height=200):
#         self.hi = height
#
# obj = Chelovek()
# print(obj.hi)
#
# obj2 = Chelovek(150)
# print(obj2.hi)

class Human:
    default_name = "Антон"
    default_age = 39
    def __init__(self, name=default_name, age=default_age):
        self.age = age
        self.name = name
        self.__money = 50
        self.__house = False

    def into(self):
        return self.age, self.name, self.__money, self.__house

    def __make_deal(self):
        if self.__money > dom.final_price():
            print("денег оч много")
            return True


    def buy_house(self, dom):
        if self.__make_deal(dom):  # make deal -> ценовой вопрос
            dom.owner = self.name  # владелец дома
            self.__house = dom  # в0000000000ладение домом
            return "с новой будкой бро"
        else:
            return "у тебя : NN. Нужно : MM"

class House:
    def __init__(self, ar="сибирь", pr = 50):
        self.__area = ar
        self.__price = pr
        self.__skidka = randint()


    def final_price(self):
        return self.__price - self.__price * self.__skidka

anton = Human
dom = House
