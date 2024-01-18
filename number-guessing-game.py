# Tasks
# User selects a range that belongs to Integer
# Some random integer will be selected and the user has to guess that integer in the minimum number of guesses
# Minimum number of guesses (MNG) depends upon range. Formula: MNG = log2(Upper bound - lower bound + 1)

import sys
import random
import math

# Using the behavior of a do-while loop
while(True):
    sys.stdout.buffer.write(b'Enter lower bound: ')
    sys.stdout.flush()
    lower = int(sys.stdin.buffer.readline())

    sys.stdout.buffer.write(b'Enter upper bound: ')
    sys.stdout.flush()
    upper = int(sys.stdin.buffer.readline())

    if(lower >= upper):
        sys.stdout.buffer.write(b'Please make sure the lower bound is bigger than the upper bound!\n')
        sys.stdout.flush()
        continue
    else:
        break


random_number = random.randint(lower, upper)
minimum_number_guess = math.ceil(math.log2(upper - lower + 1))

# encode strings to bytes before writing them to the buffer
sys.stdout.buffer.write(b'\nYou have only ' + str(minimum_number_guess).encode() + b' chances to guess the number\n')

count = 1

while count < minimum_number_guess:
    sys.stdout.buffer.write(b'Count: ' + str(count).encode())
    sys.stdout.flush()

    sys.stdout.buffer.write(b'\nGuess a number: ')
    sys.stdout.flush()
    
    try:
        guess = int(sys.stdin.buffer.readline().decode().strip())
    except ValueError:
        sys.stdout.buffer.write(b'Invalid input. Please enter an integer.\n')
        sys.stdout.flush()
        continue

    if guess == random_number:
        sys.stdout.buffer.write(b'Congratulations! You did it in ' + str(count).encode() + b' try!\n')
        sys.stdout.flush()
        sys.exit()
    elif guess > random_number:
        sys.stdout.buffer.write(b'You guessed too high!\n')
        sys.stdout.flush()
    elif guess < random_number:
        sys.stdout.buffer.write(b'You guessed too small!\n')
        sys.stdout.flush()

    count += 1


sys.stdout.buffer.write(b'\nThe number was ' + str(random_number).encode() + b'\n')
sys.stdout.flush()


