#parametre kullanimi

#  def selam(isim):
#      print("merhaba benim adim %s "%isim)
#      print("merhaba benim adim",isim)

#  isim=input("isminizi giriniz")
#  selam(isim)


    
#birden fazla parametre kullanimi
def selam(isim,soyad,numara):
    print("merhaba benim adim: %s soyadım: %s ve numaram: %s "%(isim,soyad,numara))
   

isim=input("isminizi giriniz: ")
soyad=input("soyadinizi giriniz: ")
numara=input("numaranizi giriniz: ")
selam(isim,soyad,numara)