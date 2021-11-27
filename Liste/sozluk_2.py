#GET ile bir değerin sözlükte olup olmadığı kontrol edilebilir

sozluk={"istanbul":"sehir", "kadikoy":"ilce", "turkiye":"ulke"}
print(sozluk.get("istanbul")) #key yazılmalı

deger=input("sorgulanacak degeri giriniz")
print(sozluk.get(deger,"deger bulanamadı"))



sehirler={"istanbul":"34", "ankara":"06", "antalya":"07", "adana":"01", "trabzon":"61"}
soru=input("sehirin adini gir plakasini verelim: ")
print(sehirler.get(soru))



#Sözlüklerde herhangi bir sıra kavramı bulunmaz
#from collections import OrderedDict sıra ile erişmek istersek
from collections import OrderedDict
sehirler={"ali":"1", "mehmet":"2", "sedat":"3"}
print(sehirler)

