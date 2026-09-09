from math import gcd

def ppcm(a, b):
    return a * b // gcd(a, b)

def plus_petit_diviseur(n):
    resultat = 1

# Boucle pour calculer le plus petit commun multiple  
    for i in range(1, n + 1):
        resultat = ppcm(resultat, i)

    return resultat

print(plus_petit_diviseur(4))
print(plus_petit_diviseur(7))

print(plus_petit_diviseur(20))
#print(plus_petit_divisible(200))
#print(plus_petit_divisible(2000))
