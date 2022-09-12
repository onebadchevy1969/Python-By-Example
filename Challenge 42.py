total = 0
for i in range(0,6):
    num = input('please enter a number: ')
    add = input('Would you like to add it to the total? (Y/N): ')
    if add.lower() == 'y':
        total = total + int(num)
        i=+ 1
    elif add.lower() == 'n':
        print('OK, I will not add it to the total. ')
        i =+ 1

    else:
        print('I am sorry, I do not understand. :( ')


print(total)