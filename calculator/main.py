from calculator import a

print('뭐할래?')
print('1.더하기')
print('2.뺴기')
print('3.곱하기')
print('4.나누기')

choice = input("선택(1/2/3/4):")

num1 = int(input("처음숫자 : "))
num2 = int(input("두번째숫자 : "))

if choice == '1':
    print(f"{num1} + {num2} = ", a.plus(num1, num2))
elif choice == '2':
    print(f"{num1} - {num2} = ", a.minus(num1, num2))
elif choice == '3':
    print(f"{num1} * {num2} = ", a.multiply(num1, num2))
elif choice == '4':
    print(f"{num1} / {num2} = ", a.divide(num1, num2))
else:
    print("땡")
