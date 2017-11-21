
class GHSearchFileContents(object):
  def __init__(self, query):
    pass # does initial query

  def filter(self, condition):
    pass # strict cut off filter

  def filter_split(self, condition):
    pass

class GHSearchFileContentResults(object):
  def __init__(self, query):
    pass

  def filter(self, condition):
    pass # strict cut off filter, returns GHSearchFileContentResults

  def filter_split(self, condition):
    pass # split into two. returns 2 GHSearchFileContentResults ?

  def sort(self, key):
    pass # in place sort, returns GHSearchFileContentResults

class GHSearchResults(object):
  """
    * it'd be nice to have one object to do it
    * possibly subclasses that understand what key to use in each object
    * somehow chain filters that each apply a "match type" ?
  """

  def __init__(self):
    pass
