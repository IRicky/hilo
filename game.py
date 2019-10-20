import random

num = random.randint(1, 100)
guess=0
print('Welcome to the Hi - Lo game')

while guess != num:
    guess = int(input('Guess a number between 1 & 100:'))
    if guess < num:
        print('Too low')
    elif guess == num:
        print('Got it: the number is: ', num)
    else:
        print('Too high')

