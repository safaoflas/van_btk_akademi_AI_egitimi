# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 12:32:34 2018

@author: user
"""

# %%
# variable (degisken)
# variable
var1 = 10 # Tamsayı = int
var2 = 15 
gun = "pazartesi" # string = metinsel ifade
var3 = 10.0 # double (float) = Kesirli ifade
var5 = 10
# 5var = 10  # hata verir
var6 = 10
Var7 = 19  # standart convention of python'a gore buyuk harfle baslamasi uygun degil

# %%
# string 

s = "bugun gunlerden pazartesi"

variable_type = type(s)   # str = string

print(s)

var1 = "ankara"
var2 = "ist"
var3 = var1+var2

var4 = "100"
var5 = "200"
var6 = var4+var5

uzunluk = len(var6) 

# var6[3]

# %% numbers
# int
integer_deneme = -50
# double = float = ondalikli sayi
float_deneme = -30.7


# %% built in functions
str1= "deneme"
float1 = 10.6 
# float(10)
# int(float1)
# round(float1)
str2 = "1005"

# %% user defined functions

var1 = 20
var2 = 50

output = (((var1+var2)*50)/100.0)*var1/var2

# fonksiyon parametresi = input
def benim_ilk_func(a,b):
    
    """
    bu benim ilk denemem
    
    parametre: 
        
    return: 
    """
    output = (((a+b)*50)/100.0)*a/b
    
    return output
    
sonuc = benim_ilk_func(var1,var2)

def deneme1():
    print("bu benim ikinci denemem")

# %% default ve flexible functionları

# default f: cemberin cevre uzunlugu = 2*pi*r
    
def cember_cevresi_hesapla(r,pi=3.14):
    
    """
    cember cevresi hesapla
    input(parametre): r,pi
    output = cemberin cevresi
    """
    
    output = 2*pi*r
    return output

# flexible
    
def hesapla(boy,kilo,*args):
    print(args)
    output = (boy+kilo)*args[0]
    return output

#def hesapla(boy,kilo,yas):
#    output = (boy+kilo)*yas
#    return output
    

# %% QUIZ
    
# int variable yas
# string name isim
# fonksiyonu olacak
# fonksiyon print(type(),len,float()) 
# *args soyisim
# default parametre ayakkabi numarasi
    
yas = 10
name = "ali"
soyisim = "veli"

def function_quiz(yas,name,*args,ayakkabi_numarasi=35):
    print("Cocugun ismi: ",name, " yasi: ",yas," ayak numarasi: ",ayakkabi_numarasi)
    print(type(name))
    print(float(yas))
    
    output = args[0]*yas
    
    return output

sonuc = function_quiz(yas,name,soyisim)

print("args[0]*yas: ",sonuc)


# %% 
# lambda function

def hesapla(x):
    return x*x
sonuc = hesapla(3)


sonuc2 = lambda x: x*x
print(sonuc2(3))

# %% String fonksiyonları 

isim = 'Nisa Güney'

#len fonksiyonu string ifadesinin  uzunluğunu ölçen hazır bir fonksiyondur.
len(isim)

isim[0]

isim[4]

isim[-1]

isim[1:4:2]

isim[0] + isim[-3]

yenistring = "Halil HEYBETOĞLU"

yenistring[0:]

yenistring[1:]

yenistring[:3]

#string ifadede stringe bakıyor atlama değeri negatif yani ters yönlü olduğu için ve başlangıç ve bitiş index'leri verilmediği için stringi tersten ydazdırmış oluyor.
yenistring[::-1]


# .capitalize() -> Sadece stringdeki ilk farhi büyültür.
name = "muhammed ikbal lac"

print(name.capitalize())


# .split() fonksiyonu boşluk sayısına göre yada belirtilen parametredeki ifadeye göre string parçalayıp liste yapısına dönüştürüyor

print(name.split())

# .upper() -> Stringde bulunan bütün karakterleri büyültür.

print(name.upper())