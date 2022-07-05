# from the book of 'python trick'.

class Repeater:
  def __init__(self, value):
    self.value = value
  
  def __iter__(self):
    return RepeaterIterator(self)
