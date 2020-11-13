import requests
import os
from bs4 import BeautifulSoup as bs
from pprint import pprint

class Artigos:
    def __init__(self):
        self.urlBase = "https://montebravo.com.br/blog/artigos/"


    def __initCrawler(self):
        return requests.get(self.urlBase) 


    def __getPagination(self, elements):
        return elements.find("div", 
            {"class":"pagination"}).find("li").text.split(" ")[-1] 


    def __getContent(self, elements):
        return [{
        "categoria":element.find("div", {"class": "categories"}).text,
        "titulo":element.find("h3").text,
        "conteudo":element.find("p").text
        } for element in elements.find_all("article")]


    def __saveData(self, data):
        row = ';'.join(data.values()).replace('\n', '').replace('\r', '')
        if not os.path.isdir("./data"):
            os.mkdir("./data")

        with open("./data/artigod.csv", "a+") as dt:
            dt.write(row + "\n")
    

    def __call__(self):
        print("Pegando o número de páginas!")
        res = self.__initCrawler()
        elements = bs(res.text,'html.parser')
        pags = self.__getPagination(elements)
        print(f"Número de págs:: {pags}")
        print("Pegando os dados dás paǵinas!")
        for index in range(1, int(pags)+1):
            print(f"pág:: {index}")
            res = requests.get(f"{self.urlBase}page/{index}/")
            elements = bs(res.text,'html.parser')
            contents = self.__getContent(elements)
            print(f"Gravando dados da pág {index}")

            for content in contents:
                self.__saveData(content)



start = Artigos()
start()