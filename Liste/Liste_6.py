#Belirtilen elemanın listenin kaçıncı elemanı olduğu bilgisini verir
Liste=["İstanbul","ankara","izmir","bursa"]
a=Liste.index("izmir")
print("",a,". indis")

# SORT listeyi sıralamak için kullanılır
sayilar=[1,5,9,45,6,78,2,6,88]
sayilar.sort() 
print(sayilar)


# Reverse işlevi listeyi ters çevirmek için kullanılır 
sayilar=[1,5,9,45,6,78,2,6,88]
sayilar.reverse() 
print(sayilar)

# Belirtilen elemanın liste içerisinde kaç kez geçtiği bilgisini verir
sayilar=[1,0,9,45,6,78,2,6,2,2,88]
a=sayilar.count(2) 
b=sayilar.count(5) 
print(a,b)
