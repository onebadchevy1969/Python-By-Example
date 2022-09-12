num = int(input('Please enter a number: '))
stop = 0
while num < 10:
    print('Too low')
    num = int(input('Please enter a number: '))

while num > 20:
    print('Too high')
    num = int(input('Please enter a number: '))

while num > 10 and num < 20:
    if stop == 0:
        print('Thank you')
        stop = stop + 1
