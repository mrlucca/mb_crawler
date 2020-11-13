from MbSpyder import MbSpyder
class Artigos(MbSpyder):
    def __init__(self):
        super().__init__()
        self.urlBase      = "https://montebravo.com.br/blog/artigos/"
        self.nameDataFile = "artigos"


    def getContent(self, elements):
        return [{
        "categoria":element.find("div", {"class": "categories"}).text,
        "titulo":element.find("h3").text,
        "conteudo":element.find("p").text
        } for element in elements.find_all("article")]


start = Artigos()
start()