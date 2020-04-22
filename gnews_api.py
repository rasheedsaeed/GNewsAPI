import requests

# Documentation: https://gnews.io/docs/v3#introduction


class GNews:
    BASE_URL = "https://gnews.io/api/v3/"
    COMMON_URL_PARAMS = "&lang={}&country={}&max={}&image={}&token={}&"
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
        lang="en",
        country="uk",
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

        try:
            response = requests.get(
                GNews.BASE_URL
                + "search?"
                + "&q={}&mindate={}&maxdate={}&in={}".format(
                    '"' + query + '"',
                    mindate if mindate else self.mindate,
                    maxdate if maxdate else self.maxdate,
                    in_search if in_search else self.in_search,
                )
                + GNews.COMMON_URL_PARAMS.format(
                    lang if lang else self.lang,
                    country if country else self.country,
                    max_results if max_results else self.max_results,
                    image if image else self.image,
                    self.token,
                )
            )
            response.raise_for_status()
        except requests.exceptions.Timeout as error:
            raise requests.exceptions.Timeout(error)
        except requests.exceptions.ConnectionError as error:
            raise requests.exceptions.ConnectionError(error)
        except requests.exceptions.RequestException as error:
            raise requests.exceptions.RequestException(error)
        except requests.exceptions.HTTPError as error:
            raise requests.exceptions.HTTPError(error)

        return response

    def top_news(
        self, lang=None, country=None, max_results=None, image=None
    ) -> requests.models.Response:

        try:
            response = requests.get(
                GNews.BASE_URL
                + "top-news?"
                + GNews.COMMON_URL_PARAMS.format(
                    lang if lang else self.lang,
                    country if country else self.country,
                    max_results if max_results else self.max_results,
                    image if image else self.image,
                    self.token,
                )
            )
            response.raise_for_status()
        except requests.exceptions.Timeout as error:
            raise requests.exceptions.Timeout(error)
        except requests.exceptions.ConnectionError as error:
            raise requests.exceptions.ConnectionError(error)
        except requests.exceptions.RequestException as error:
            raise requests.exceptions.RequestException(error)
        except requests.exceptions.HTTPError as error:
            raise requests.exceptions.HTTPError(error)

        return response

    def topic(
        self, query: str, lang=None, country=None, max_results=None, image=None
    ) -> requests.models.Response:

        if query.lower() not in GNews.AVAILABLE_TOPICS:
            raise NameError("Gnews topic(): the provided topic is not available!")

        try:
            response = requests.get(
                GNews.BASE_URL
                + "topics/"
                + query
                + "?"
                + GNews.COMMON_URL_PARAMS.format(
                    lang if lang else self.lang,
                    country if country else self.country,
                    max_results if max_results else self.max_results,
                    image if image else self.image,
                    self.token,
                )
            )
            response.raise_for_status()
        except requests.exceptions.Timeout as error:
            raise requests.exceptions.Timeout(error)
        except requests.exceptions.ConnectionError as error:
            raise requests.exceptions.ConnectionError(error)
        except requests.exceptions.RequestException as error:
            raise requests.exceptions.RequestException(error)
        except requests.exceptions.HTTPError as error:
            raise requests.exceptions.HTTPError(error)

        return response
