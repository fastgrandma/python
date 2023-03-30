import requests
import random
resp = requests.get("https://api.randomdatatools.ru/").json()
print(resp)
class User:
    def __init__(self):
        self.__lorem = ""
        self.login = self.__data["login"]
        self.__password = self.__data["password"]
        self.imya = self.__data["imya"]
        self.familiya = self.__data["Password"]
        self.posts = []