sayi = int(input("sayi giriniz ="))
toplam=0

for i in range(1,sayi):
    if(sayi%i==0):
        print(i)
        toplam=toplam+i
        
if(sayi==toplam):
    print("mukemmel sayi")
else:
    print("mukemmel sayi degildir")