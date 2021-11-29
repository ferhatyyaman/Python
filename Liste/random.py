import random

# print(random.randint(1,100)) #bu aralıktan rastgele deger verir (min max dahil)
# print(random.randint(1,100)-10)

# print(random.randrange(1,101)) # max dahil degil aralıktan rstgele deger verir
# print(random.randrange(1,101,3))#1-100 arasinda 3 e bolundugunde 1 kalan sayıyı verir

deger1=range(10)
deger2=range(10,50)
deger3=range(10,50,2)
print(random.sample(deger1,5))
print(random.sample(deger2,5))
print(random.sample(deger3,5))

deger1=range(10)
deger2=range(10,50)
deger3=range(10,50,2)
print(random.choice(deger1))
print(random.choice(deger2))
print(random.choice(deger3))