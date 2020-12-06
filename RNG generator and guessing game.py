#importing stuff and setting it up
import random

print('What is your name')
name = input()

print('Okay, ' + name + " I'm thinking of a number between 1 and twenty")
secret = random.randint(1, 20)

for guesses in range(1, 7):
    print('Guess the number')
    guess = int(input())
    if guess > secret:
        print('Too high. Guess again.')
    elif guess < secret:
        print('Too low. Guess again.')
    else:
        break # breaks out when correct number is guessed.
            
if guess == secret:
    print('Good job, ' + name + ', you got it.')
    print('You took ' + str(guesses) + ' guesses.')
else:
    print('No. I was thinking of ' + str(secret))
