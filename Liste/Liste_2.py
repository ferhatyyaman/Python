#Eklemek, iliştirmek anlamına gelen Append bir listenin sonuna eleman eklemek için kullanılır
Liste=["İstanbul","ankara","izmir","bursa"]
Liste.append("antalya")
Liste.append("kars")
print(Liste)

# İnsert işlevi ile Listenin istenilen indisler arasına eleman eklenir
Liste=["İstanbul","ankara","izmir","bursa"]
Liste.insert(4,"antalya")
Liste.insert(0,"kars")
print(Liste)