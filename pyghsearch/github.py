import time

_CACHE_DEFAULT_KEY = "default"

class GithubCache(object):
  def __init__(self, filename=None):
    if filename is not None:
      pass # Load cache
      return

    self.cache = {
      "search_code": {},
      "files": {},
      "repos": {},
      _CACHE_DEFAULT_KEY: {}
    }

  def cache_item(self, url, response):
    data = response.json()

    millis = int(round(time.time() * 1000))
    subcache = self.cache[data["type"]]
    subcache[url] = {
      "data": data,
      "headers": response.headers,
      "time_stored": millis,
      "time_accessed": millis
    }

  def get_cache_time(self, url, cache_key):
    try:
      return self.cache[cache_key]["time_stored"]
    except KeyError as e:
      return -1

  def retrieve_item(self, url, cache_key):
    return self.cache[cache_key].get(url)


class GithubRequests(object):
  def __init__(self, api_url, username, password):
    self.api_url = api_url
    self.username = username
    self.password = password

  def _request(self, method, url):
    pass

  def __get_attr__(self, name):
    if name in ["get", "post", "put", "head"]:
      def method(*args, **kwargs):
        return requests.request(method, url *args, **kwargs)

  def resolve(self, ghitem):
    r = self.get(ghitem.url)
    r.raise_for_status()
    ghitem.resolve(r)

