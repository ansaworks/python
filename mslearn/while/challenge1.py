import random

count = 0
guess = 0
correct_guess = random.randint(1, 5)
while guess != correct_guess :
    count += 1
    guess = input('Guess a number between 1 and 5 : ')
    if guess.isnumeric() :
        guess = int(guess)
else :
    print(f'You guessed it in {count} tries')
