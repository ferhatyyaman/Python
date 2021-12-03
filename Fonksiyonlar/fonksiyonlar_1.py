def selamla():
    dil="python"
    print(dil)

selamla()


#tek-cift ornegi
def tek():
    print("sayi tektir")
def cift():
    print("sayi cifttir")

sayi=input("sayi giriniz: ")

if int(sayi) %2==0:
    cift()
else:
    tek()

