import requests
import json

class GNews: 
    BASE_URL = "https://gnews.io/api/v3/"
    def __init__(
            self, token: str, lang="en_UK", 
            country="UK", mindate="None", 
            maxdate="None"):
        token = token.strip()
        if not token:
            raise NameError("Gnews constructor: API (str) not defined!")

        self.token = token
        self.lang = lang
        self.country = country
        self.mindate = mindate
        self.maxdate = maxdate

    def search(self, q: str) -> json:
        q = q.strip()
        if not q:
            raise NameError("Gnews search(): No query provided!")

        response = requests.get(
                GNews.BASE_URL + "search?q={0}?country={1}" +
                "mindate={2}?maxdate={3}?lang={4}?token={5}".format(
                        0=q, 1=self.country, 
                        2=self.mindate, 3=self.maxdate, 
                        4=self.lang, 5=self.token
                )
        )

    def top_news(self) -> json:
        return requests.get(GNews.BASE_URL + "top-news?token=%s" % self.token)
