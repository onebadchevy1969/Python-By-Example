import math
num_1 = input('Enter a WHOLE number: ')
num_2 = input('Enter another WHOLE number: ')
result = int(num_1) // int(num_2)
remain = int(num_1) % int(num_2)
if remain == 0:
    print(num_1 + ' divided by ' + num_2 + ' equals ' + str(result) + ' with no remainder.' )
else:
    print(num_1 + ' divided by ' + num_2 + ' equals ' + str(result) + ' with a remainder of ' + str(remain))
