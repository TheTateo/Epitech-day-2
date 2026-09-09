#Calcule de pi par l'approximation de séries - formule de Leibniz
from numpy import around

a = 1
b = 1
pi = 0
_pi_ = 0
for i in range(1000000):
    if i % 2 == 0:
        _pi_ += (a/b)
    else:
        _pi_ -= (a/b)
    b+=2
pi = 4*(_pi_)

print(around(pi, 6)) 