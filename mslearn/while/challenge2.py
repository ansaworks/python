import random

result = random.randint(1, 10)
count = 0
guess = 0

print('Guess a number between 1 and 10')
while guess != result :
    count += 1
    guess = input(f'Enter guess #{count}: ')
    if guess.isnumeric() :
        guess = int(guess)
        if guess < result :
            print('Your guess is too low, try again!')
        elif guess > result :
            print('Your guess is too high, try again!')
    else :
        print('Numbers only, please!')
else :
    print(f'You guessed it in {count} tries.')

