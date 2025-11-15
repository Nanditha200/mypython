  # encapsulation
  class me:
    def __init__(self):
      self.public="i am public"
      self.__private="i am private"
    def display(self):
      print(self.__private)
  obj=me()
  obj.display()
