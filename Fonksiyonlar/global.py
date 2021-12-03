# def fonk():
#     a=5
#     print(a)
# fonk()
#print("a nın degeri:",a)  degisken fonksiyon dısında tanımsız

def fonk():
    global a
    a=5
    print(a)
fonk()
print("a nın degeri:",a)




a=10
def fonk():
    a=5
    return a
print("a nın degeri:",fonk())
print("a nın degeri:",a)


