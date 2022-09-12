name = input('Please enter your name: ')
num = input('Please enter a number: ')
num = int(num) + 1
for i in range(0, num):
    for letter in name:
        print(letter)