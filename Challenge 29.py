import math
number = input('Enter a WHOLE number over 500: ')
number_int = int(number)
sqrt_number = math.sqrt(number_int)
print('The square root of ' + number + '-rounded two places- equals: ' + str(round(sqrt_number, 2)))
