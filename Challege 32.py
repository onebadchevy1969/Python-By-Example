import math
num_rad = input('Enter the radius of a cylinder: ')
num_dep = input('Enter the depth of a cylinder: ')
num_rad_int = int(num_rad)
num_dep_int = int(num_dep)
area = math.pi * (num_rad_int**2)
volume = area * num_dep_int
print('The volume of the cylinder is: ' + str(round(volume, 3)))