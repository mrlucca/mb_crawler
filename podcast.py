from MbSpyder import MbSpyder


class Podcast(MbSpyder):
    def __init__(self):
        super().__init__()
        self.urlBase      = "https://montebravo.com.br/blog/categoria/podcasts/"
        self.nameDataFile = "podcasts"


    def getContent(self, elements):
        return [{
            "titulo": element['aria-label'], 
            "link": element.find("iframe")['src']
            } for element in elements.find_all("article")]




start = Podcast()
start()