#숫자야구게임
from random import randint
import time

a = int(input())


def generate_numbers():
    numbers = []

    while len(numbers) < a:
        num = randint(1, 9)
        if num not in numbers:
            numbers.append(num)
    return numbers

def user():
    user_guess = []
    while len(user_guess) < a:
        num = int(input(f'{len(user_guess)+1}번째 숫자를 입력하세요:'))

        if num < 1 or num > 9:
            print("범위 외 숫자입니다.")
        elif num in user_guess:
            print("중복되는 숫자입니다.")
        else:
            user_guess.append(num)
    return user_guess

def get_score(guess, answer_list):
    strike_count=0
    ball_count=0

    for i in range(a):
        if guess[i] == answer_list[i]:
            strike_count += 1
        elif guess[i] in answer_list:
            ball_count += 1

    return strike_count, ball_count

start_time = time.time()
answer = generate_numbers()
tries = 0

while True:
    user_guess = user()
    s, b = get_score(user_guess, answer)

    print(f'{s}s {b}b \n')
    tries += 1

    if s == a:
        break
end_time = time.time()

print(f'{tries}트만에 성공')
print(f'총게임시간: {end_time - start_time:.5f}초')


