import random
print(dir (random))
from random import *
print(randint (10,30))
print(randrange(90))

item = ['egg', 'mutton', 'chicken']
for i in range (1, 5+1) :
    print(choices (item , k =3))
    print(sample(item , k = 3))
print(item)
shuffle(item)
print(item)


