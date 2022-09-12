import math
num = input('Please enter the RADIUS of a circle: ')
num_int = int(num)
area = math.pi * (num_int**2)
print('The area of the circle is: ' + str(area))