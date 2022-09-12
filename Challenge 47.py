
num_1 = int(input('Please enter a number: '))
num_2 = int(input('Please enter another number: '))
answer = input('Would you like to add another number? Yes or No?')
total = num_2 + num_1
while answer.lower() == 'yes':
    num = int(input('Please enter a number: '))
    total = total + num
    answer = input('Would you like to add another number? Yes or No?')

print(total)