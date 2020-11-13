import requests
import os
from bs4 import BeautifulSoup as bs


class MbSpyder:
    def __init__(self):
        self.nameDataFile = None
        self.urlBase = "https://montebravo.com.br/blog/categoria/podcasts/"


    @abstractmethod
    def __initCrawler(self):
        return requests.get(self.urlBase) 


    @abstractmethod
    def __getPagination(self, elements):
        return elements.find("div", 
            {"class":"pagination"}).find("li").text.split(" ")[-1] 


    @abstractmethod
    def __getContent(self, elements):
        return [{
            "titulo": element['aria-label'], 
            "link": element.find("iframe")['src']
            } for element in elements.find_all("article")]


    @abstractmethod
    def __saveData(self, data):
        if self.nameDataFile:
            row = ';'.join(data.values()).replace('\n', '').replace('\r', '')
            if not os.path.isdir("./data"):
                os.mkdir("./data")

            with open(f"./data/{self.nameDataFile}.csv", "a+") as dt:
                dt.write(row + "\n")
        else:   
            raise Exception("The file name has not been defined!")

    @abstractmethod
    def __call__(self):
        print("Pegando o número de páginas!")
        res = self.__initCrawler()

        elements = bs(res.text,'html.parser')
        pags = self.__getPagination(elements)
  
        for index in range(1, int(pags)+1):
            print(f"pág:: {index}")
            res = requests.get(f"{self.urlBase}page/{index}/")
            elements = bs(res.text,'html.parser')
            contents = self.__getContent(elements)
            print(f"Gravando dados da pág {index}")

            for content in contents:
                self.__saveData(content)