class Area():
    def __init__(self, a, b):  # 가로 , 세로 , 반지름
        self.a = int(a)
        self.b = int(b)
        self.PIE = 3.14

    def square(self):
        result = self.a * self.b
        return f"squr: {result}"

    def circle(self):
        result = self.PIE * self.a * self.a * 0.25
        return f"circle: {result}"

    def triangle(self):
        result = 0.5 * self.a * self.b
        return f"tri: {result}"

class Calculator():
    def __init__(self, a, b):
        self.a = int(a)
        self.b = int(b)

    def plus(self):
        result = self.a + self.b
        return f"plus: {result}"

    def minus(self):
        result = self.a - self.b
        return f"minus: {result}"

    def multiple(self):
        result = self.a * self.b
        return f"multiple: {result}"

    def divide(self):
        result = self.a / self.b
        return f"divide: {result}"

class Profile():
    def set_profile(self, profile):
        self.profile = profile
    def get_name(self):
        return self.profile["name"]
    def get_gender(self):
        return self.profile["gender"]
    def get_birthday(self):
        return self.profile["birthday"]
    def get_phone(self):
        return self.profile["phone"]
    def get_email(self):
        return self.profile["email"]
    def get_age(self):
        return self.age["age"]



