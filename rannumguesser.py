import random
ran_num = random.choice(range(0,10))
user_num = int(input('guess the secret number--'))

if ran_num == int(user_num):
    print('Great Guess')
elif ran_num > int(user_num):
    print('your guess is to low')
else:
    print('youe guess is to high')

