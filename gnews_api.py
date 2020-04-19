import requests
import json


class GNews:
    BASE_URL = "https://gnews.io/api/v3/"
    COMMON_URL_PARAMS = "?lang={}?country={}?max={}?image={}?token={}?"
    AVAILABLE_TOPICS = [
        "world",
        "nation",
        "business",
        "technology",
        "entertainment",
        "sports",
        "science",
        "health",
    ]

    def __init__(
        self,
        token,
        lang="en_UK",
        country="UK",
        mindate="None",
        maxdate="None",
        max_results=10,
        image="Optional",
        in_search="all",
    ):

        token = token.strip()
        if not token:
            raise NameError("Gnews constructor: API (str) not defined!")

        self.token = token
        self.lang = lang
        self.country = country
        self.mindate = mindate
        self.maxdate = maxdate
        self.max_results = max_results
        self.image = image
        self.in_search = in_search

    def search(
        self,
        query: str,
        lang=None,
        country=None,
        mindate=None,
        maxdate=None,
        max_results=None,
        image=None,
        in_search=None,
    ) -> requests.models.Response:

        if not query:
            raise NameError("Gnews search(): No query provided!")

        return requests.get(
            GNews.BASE_URL
            + "search"
            + GNews.COMMON_URL_PARAMS
            + "mindate={}?maxdate={}?in={}?q={}".format(
                lang if lang else self.lang,
                country if country else self.country,
                max_results if max_results else self.max_results,
                image if image else self.image,
                self.token,
                mindate if mindate else self.mindate,
                maxdate if maxdate else self.maxdate,
                in_search if in_search else self.in_search,
                '"' + query + '"',
            )
        )

    def top_news(
        self, lang=None, country=None, max_results=None, image=None
    ) -> requests.models.Response:

        return requests.get(
            GNews.BASE_URL
            + "top-news"
            + GNews.COMMON_URL_PARAMS.format(
                lang if lang else self.lang,
                country if country else self.country,
                max_results if max_results else self.max_results,
                image if image else self.image,
                self.token,
            )
        )

    def topic(
        self, query: str, lang=None, country=None, max_results=None, image=None
    ) -> requests.models.Response:

        if query not in GNews.AVAILABLE_TOPICS:
            raise NameError("Gnews topic(): the provided topic is not avaible!")

        return requests.get(
            GNews.BASE_URL
            + query
            + GNews.COMMON_URL_PARAMS.format(
                lang if lang else self.lang,
                country if country else self.country,
                max_results if max_results else self.max_results,
                image if image else self.image,
                self.token,
            )
        )
