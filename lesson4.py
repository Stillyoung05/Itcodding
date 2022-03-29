
"""@itcodding 4-dars Py1"""



#                                   LISTLAR USTIDA AMALLAR
# ruyhat = ['asus','Apple', 'HP', 'Acer', 'dell']
# print(ruyhat)


# print(ruyhat[4]) # list dan item ni olish. manfiy indeks


# ruyhat[3] = 25 # list itemini boshqasiga almashtirish
# print(ruyhat)


# ruyhat.insert(3, 'yangi item nomi') # indeks buyicha item qushish
# print(ruyhat)


# ruyhat.append('MSI') # list ni oxiriga item qushish
# print(ruyhat)


# ruyhat2 = ['olma', 'banan', 'gilos'] # listlarni bir biriga qushish . + orqali ham
# ruyhat.extend(ruyhat2)
# print(ruyhat)
# list3 = ruyhat + ruyhat2
# print(list3)


# ruyhat.remove('Asus') # listdan item ni chiqarib tashlash
# print(ruyhat)


# ruyhat.pop(4) # list itemini indeks buyicha chiqarib tashlash
# print(ruyhat)


# ruyhat.pop() # oxirgi itemni chiqarib tashlash
# print(ruyhat)


# ruyhat.clear() # listni tozalash
# print(ruyhat)


# ruyhat.sort() # listni alfavit buyicha tartiblash
# print(ruyhat)


# ruyhat.sort(reverse = True) # listni alfavitga teskari tartiblash
# print(ruyhat)


# ruyhat.reverse() # list ni kiritilgan tartibni teskarisiga tartiblaydi
# print(ruyhat)


# r = ruyhat.copy() # 1 listni boshqasiga nusxalash. list() metodi orqali
# print(r)


# print(ruyhat.count('dell')) # list ichidan element necha martta qatnashganini aniqlash


#                                   TUPLELAR USTIDA AMALLAR

# mytuple = ('lorem', 'sit', 'emet', 'dolor', 123.34, False)
# print(mytuple)
# print(len(mytuple)) # elementlar sonini aniqlash
# print(len(mytuple))


# indekslar bilan ishlash list dagi bilan bir xil
# print(mytuple[0:3])


# list_uchun = list(mytuple) # tuple elementini almashtirish
# list_uchun[2] = 'just'
# print(tuple(list_uchun))
# print(mytuple)



# l = list(mytuple) # tuple ga element qushish
# l.append('BU')
# f = tuple(l)
# print(f)


# t = ('asdf', ) # tuple larni bir biriga qoshish
# mytuple += t
# print(mytuple)


# d = list(mytuple) # tuple dan malumot o`chirish
# d.remove('lorem')
# print(tuple(d))


# del mytuple # tuple ni o`chirish
# print(mytuple)


# (qwe, qw, em, do, a, b) = mytuple # tuple dan chiqarish
# print(f"{qwe}{qw}{em}{do}{a}{b}")


# new_tuple = mytuple * 2 # tuple larni ikkilantirish
# print(new_tuple)


# TUPLE USTIDA BAJARILADIGAN METODLAR index() va count()


# print(mytuple.index('emet'))

# 5-dars
print('<-------"Tosh" , "Qaychi" , "Qogoz" o"yini------->')
set={"tosh","qaychi","qogoz"}
l=list(set)
print('O"yinni boshlaysizmi? Tanlang: "start" yoki "stop"')
a=input("Kiriting:")
if a=="start":
    print(f"Quyidagilarning qaysi birini tanlaysiz\n 1.{l[0]}\n 2.{l[1]}\n 3.{l[2]}")
k=0
s=0
while a=="start":
    x=set.pop()
    choose=input("Sizning tanlovingiz:")
    print(f"kompyuter:{x}")
    if choose==x:
        print("Kompyuterga 1 ochko , Sizga 1 ochko!")
        k+=1
        s+=1
    elif (choose=="tosh" and x=="qaychi") or (choose=="qaychi" and x=="qogoz") or (choose=="qogoz" and x=="tosh"):
        print("Sizga 1 ochko!")
        s+=1
    elif (choose=="tosh" and x=="qogoz")  or (choose=="qaychi" and x=="tosh") or (choose=="qogoz" and x=="qaychi"):
        print("Kompyuterga 1 ochko!")
        k+=1
    else:
        print("Notogri tanlov!!!!")
    print('Yana o"ynaysizmi? O"ynasangiz "start" , to"xtatmoqchi bo"lsangiz "stop" kiriting')
    a=input("Kiriting:")
    if a=="stop":
        print(f"NATIJA : Kompyuter--->{k} : {s}<---Siz")
        if k>s:
            print("Siz yutqazdiz!")
        elif k<s:
            print('Siz g"alaba qozondiz!')
        else:
            print("Durrang!")
# Kamolova Iroda













































