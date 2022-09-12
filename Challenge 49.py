compnum = 50
num_guess = 1
guess = int(input('Please enter your guess: '))
while guess != compnum:
    if guess < compnum:
        print('Your guess is too low! ')
        num_guess = num_guess + 1
        guess = int(input('Please enter your guess: '))
    elif guess > compnum:
        print('Your Guess is too high!')
        num_guess = num_guess + 1
        guess = int(input('Please enter your guess: '))


print('Great Job! It took you ' + str(num_guess) + ' attemps')