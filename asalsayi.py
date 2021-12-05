def bolenler(n):
    liste=[]
    for i in range(1,n+1):
        liste.append(i)
    return liste

def asal(n):
    liste=bolenler(n)
    if(len(liste)==2):
        sonuc=True
    else:
        sonuc=False
    return sonuc

def asallar(n):
    liste=[]
    for i in range(1,n):
        if(asal(i)==True):
            liste.append(i)
            liste2=[liste,sum(liste)]
    return liste2