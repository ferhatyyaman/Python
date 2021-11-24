kisiler=("ahmet","salih",1998,5450)


print(type(kisiler))
isim=kisiler[0]
print(type(isim))
dogumt=kisiler[2]
print(type(dogumt))

#demeti çözümleme
kisiler1=("ahmet","salih",1998,5450)
isim,soyisim,dogumt,maas=kisiler1
print(isim)
print(soyisim)
print(dogumt)
print(maas)


#Demetler listelerin aksine değişiklik yapmaya müsait olmadıklarından listelere göre daha güvenlidirler 
#Değiştirilmemesi gereken veriler içeren bir durumda liste yerine demetler kullanılmalıdır 
#Demetler listelere göre daha hızlı çalışır