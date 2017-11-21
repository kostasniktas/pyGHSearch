
class GHSearchItem(object):
  def resolve(self, response):
    pass

class GHFile(GHSearchItem):
  def __init__(self, name, url):
    self.name = name
    self.url = url

class GHRepo(GHSearchItem):
  def __init__(self, name, url):
    self.name = name
    self.url = url

