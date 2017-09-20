import random

dash = '-' * 20
print(dash)
print('  Guess the Number')
print(dash)
print()

the_number = random.randint(0, 100)
guess = -1

while guess != the_number:
    guess_text = int(input('Guess a number between 0 and 100:  '))
    guess = guess_text

    if the_number < guess:
        print('Sorry {} was too high...  try again'.format(guess))
    elif the_number > guess:
        print('Sorry {} was too low... try again'.format(guess))
    else:
        print("You got it!")
