import random

dash = '-' * 20
print(dash)
print('  Guess the Number')
print(dash)
print()

the_number = random.randint(0, 100)

guess_text = int(input('Guess a number between 0 and 100:  '))
guess = guess_text

while guess != the_number:
    if the_number < guess:
        print('Lower... Sorry try again:  ')
    elif the_number > guess:
        print('Higher... Sorry try again:  ')
    else:
        print("You got it!")
        break