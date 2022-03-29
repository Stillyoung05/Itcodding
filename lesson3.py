# a = 'kompyuter'
# print(a.capitalize()) # ATRIBUT.  butun stringni faqat birinchi harfini kattaga alishtiradi


# print('OlmA'.casefold()) # str ni butunlay kichik harfli qiladi


# print('Mani Ismim : Jamshid'.count('a')) # str ichidan qiymatni necha martta qatnashganini beradi


# print('Jamshid'.endswith('d')) # str berilgan qiymat bn tugaydimi? aniqlovchi atribut


# print('kitob'.find('k')) # str dan berilgan qiymatni izlab indeksini ciqarib beradi, index
# print('NOutbuk'.index('uk'))


# print('sadsajbajsbdf'.isalpha()) # True beradi agar, str faqat harfdan tashkil topgan bo`sa


# print('1203912'.isdigit()) # True beradi agar, str faqat raqamdan iborat bo`sa


# print('qweqwe'.isspace())  #True beradi agar, str faqat bo`shliqdan iborat bo`lsa


# print('AsD'.lower()) # str ni polnostyu kichkina harflarga alishtiradi


# print('ITcodding'.swapcase()) # str dagi harflarni kattani kichikga kichik ni kattaga alishtiradi


# print('man on uch yoshman'.title()) # str ning ha rbir so`zini katta bn boshlaydi kak sarlavha


"""Python Booleans"""
# print(bool(False))
# print(bool(None))
# print(bool(0))
# print(bool(""))
# print(bool())
# print(bool([]))
# print(bool({}))
# print(bool(12<=25))

# if 12<=25:
#     print(
#         '25 raqami 12 raqamidan kattaroq'
#     )
# else:
#     print('12 raqami yigirma beshdan kattaroq')


"""Python Operators"""
# Arithmetic operators    --    Arifmetik operatorlar
# Assignment operators    --    Belgilash operatorlari
# Comparison operators    --    Taqqoslash operatorlari
# Logical operators       --    Mantiqiy operatorlar
# Identity operators      --    Identifikatsiya operatorlari
# Membership operators    --    A'zolik operatorlari
# Bitwise operators       --    Bitli operatorlar
"""Arithmetic operators"""
# +
# -
# *
# /
# %
# **
# //

"""Assignment Operators"""
# a = 10
# a += 3
# print(a)
# +=	a += 3	a = a + 3
# -=	a -= 3	a = a - 3
# *=	a *= 3	a = a * 3
# /=	a /= 3	a = a / 3
# %=	a %= 3	a = a % 3
# //=	a //= 3	a = a // 3
# **=	a **= 3	a = a ** 3

"""Logical operators"""

# and - mantiqiy kupaytirish. ikki shart bir vaqtsa teng bajarilganda True natija qaytaradi.
# s = 90
# if s<100 and s > 200:
#     print("S ideal son")
# elif s<100 and s<101:
#     print('To`ri mulohaza')
# else:
#     print("Noto`ri mulohaza")
# f = 12
# print(f>10 and f<1)
# OR operatori. ikki shartdan kamida bittasi to`ri bolganda True qaytaradi.
# print(12/5<2 or 12/1>2)

# NOT operatori. shartning bool qaiymatini teskarisini beradi.
# print(not(len("ASus")==4))

"""Identity Operators"""
# def fuk():
#     """Mening funksiyam"""
#     print("qweqweqwe")
# fuk()
# is operatori. O`zgaruvchilar o`zaro teng bo`bolganda True qaytaruvchi operator. == bilan ten kuchli
# s = 1203912
# e = 1203912
# if s is e:
#     print('Siz bir xil son kiritdingiz')
# else:
#     print('Siz turli xil sonlar kiritdingiz')
# print("ona va bola" is not 'ona')

"""Membership Operators"""
# IN operatori. bu operator qachonki bir uzgaruvchi ikkinchi uzgaruvchi tarkibida bolganda True qaytaradi
# Not IN.
"""Bitwise Operators"""
# and = &
# or = |
# not = ~






















