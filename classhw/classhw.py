# class Area():
#     def __init__(self, a, b):  # 가로 , 세로 , 반지름
#         self.a = int(a)
#         self.b = int(b)
#         self.PIE = 3.14
#
#     def square(self):
#         result = self.a * self.b
#         return f"squr: {result}"
#
#     def circle(self):
#         result = self.PIE * self.a * self.a * 0.25
#         return f"circle: {result}"
#
#     def triangle(self):
#         result = 0.5 * self.a * self.b
#         return f"tri: {result}"

# class Calculator():
#     def __init__(self, a, b):
#         self.a = int(a)
#         self.b = int(b)
#
#     def plus(self):
#         result = self.a + self.b
#         return f"plus: {result}"
#
#     def minus(self):
#         result = self.a - self.b
#         return f"minus: {result}"
#
#     def multiple(self):
#         result = self.a * self.b
#         return f"multiple: {result}"
#
#     def divide(self):
#         result = self.a / self.b
#         return f"divide: {result}"
#
# calc = Calculator()
# clac.set_number(20, 10)
# print(calc.plus()) # 더한 값
# print(calc.minus()) # 뺀 값
# print(calc.multiple()) # 곱한 값
# print(calc.divide()) # 나눈 값

class Profile():
    def __init__(self):
        self.profile = {
            "name": "lee",
            "gender": "man",
            "birthday": "01/01",
            "age": 32,
            "phone": "01012341234",
            "email": "python@sparta.com",
        }