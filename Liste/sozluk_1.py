#Bir anahtar(key) yardımı ile verilere erişme mümkün
sozluk={"istanbul":"sehir", "kadikoy":"ilce", "turkiye":"ulke"}
print(sozluk["istanbul"])

sozluk["göztepe"]="mahalle" #ekleme
print(sozluk)

sozluk["kadikoy"]="cadde" #degisiklik
print(sozluk)

print(sozluk.keys())    #anahtarlar
print(sozluk.values())  #degerler
print(sozluk.items())   #tum varlıklar



sozluk.clear() #tum degerleri siler

