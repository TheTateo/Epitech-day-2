#Calcule de pi
from numpy import around

a = 6
fraction = 0
for i in range(99, 0, -2):
    fraction = ((i**2)/(a + fraction))
fraction += 3
print(around(fraction, 6))