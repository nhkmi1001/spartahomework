from pprint import pprint
#
class Calc():
    def set_number(self, a, b):
        self.a = a
        self.b = b

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
        try:
            result = self.a / self.b
            return f"divide: {result}"
        except ZeroDivisionError:
            print("0으로 나눌 수 없습니다.")
while True:
    try:
        a , b = [int(x) for x in input().split()]
        break
    except ValueError:
        print("숫자만 입력 가능합니다")


calc = Calc()
calc.set_number(a, b)
print(calc.plus())  # 더한 값
print(calc.minus())  # 뺀 값
print(calc.multiple())  # 곱한 값
print(calc.divide())  # 나눈 값




#
# people = [
#     ("Blake Howell", "Jamaica", 18, "aw@jul.bw"),
#     ("Peter Bowen", "Burundi", 30, "vinaf@rilkov.il"),
#     ("Winnie Hall", "Palestinian Territories", 22, "moci@pacivhe.net"),
#     ("Alfred Schwartz", "Syria", 29, "ic@tolseuc.pr"),
#     ("Carrie Palmer", "Mauritius", 28, "fenlofi@tor.aq"),
#     ("Rose Tyler", "Martinique", 17, "as@forebjab.et"),
#     ("Katharine Little", "Anguilla", 29, "am@kifez.et"),
#     ("Brent Peterson", "Svalbard & Jan Mayen", 22, "le@wekciga.lr"),
#     ("Lydia Thornton", "Puerto Rico", 19, "lefvoru@itbewuk.at"),
#     ("Richard Newton", "Pitcairn Islands", 17, "da@lasowiwa.su"),
#     ("Eric Townsend", "Svalbard & Jan Mayen", 22, "jijer@cipzo.gp"),
#     ("Trevor Hines", "Dominican Republic", 15, "ev@hivew.tm"),
#     ("Inez Little", "Namibia", 26, "meewi@mirha.ye"),
#     ("Lloyd Aguilar", "Swaziland", 16, "oza@emneme.bb"),
#     ("Erik Lane", "Turkey", 30, "efumazza@va.hn")
#
#
# people = [x for x in people if x[2] >= 20]
# pprint(people)
