name = input('Please enter your name: ')
num = int(input('Please enter number: '))
if num > 10:
    for i in range(1,4):
        print('Too High')
        i = i+1
else:
    num = num + 1
    for i in range(1,num):
        print(name)
        i =+ 1