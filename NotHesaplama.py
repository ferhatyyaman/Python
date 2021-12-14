def ortHesapla(isim,ara,final):
    ort = ara*0.4+final*0.6
    sonuc ={ "ogrenci" : isim,
             "araNot" :ara,
             "finalNot" :final,
             "ortalama" :ort }
    return sonuc
isim=input("ogrenci adi giriniz:")
vize=int(input("vize notu gir"))
final=int(input("final notu gir"))
print(ortHesapla(isim,vize,final))