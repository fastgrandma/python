import requests
import random
class User:
    def __init__(self):
        self.__lorem = ""
        self.__data = requests.get("https://api.randomdatatools.ru/").json()
        self.login = self.__data["login"] if not log else log
        self.__password = self.__data["password"] if not pas else pas
        self.imya = self.__data["Firstname"] if not log else log
        self.familiya = self.__data["Lastname"] if not log else log
        self.posts = [self.__lorem[random.randint(0,35):random.randint(36, )]]