class Cookie:
    def __init__(self,color):
        self.color = color

    def get_color(self):
        return self.color

    def set_color(self,color):
        self.color = color


cookie_one = Cookie("Green")
print(cookie_one.get_color())
cookie_one.set_color("orange")
print(cookie_one.get_color())

cookie_two = Cookie("Blue")
print(cookie_two.color)
