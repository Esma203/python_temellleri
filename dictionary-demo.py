'''
   ogrenciler = {
        '120': {
            'ad': 'Esma',
            'soyad': 'Uslu',
            'yas': 21
            
        },
        '125': {
            'ad': 'Sumeyra',
            'soyad': 'Uslu',
            'yas': 15
        },
        '128': {
            'ad': 'Asli',
            'soyad': 'Uslu',
            'yas': 43
        },            
}

1- Bilgileri verilen öğrenciler kullanıcıdan aldığınız bilgilerle dictionary içinde saklayınız.
2- Öğrenci numarasını kullanıcıdan alıp ilgili öğrenci bilgisini gösterin.

'''
ogrenciler = {}
number = input("Ogrenci numarası: ")
name = input("Ogrenci adı: ")
surname = input("Ogrenci soyadı: ")
age = int(input("Ogrenci yas: "))

#ogrenciler[number] = {
 #   "ad": name,
  #  "soyad": surname,
   # "yas": age
#}

ogrenciler.update({
    number: {
        "ad": name,
        "soyad": surname,
        "yas": age
    }
})

ogrenciler = {}
number = input("Ogrenci numarası: ")
name = input("Ogrenci adı: ")
surname = input("Ogrenci soyadı: ")
age = int(input("Ogrenci yas: "))


ogrenciler.update({
    number: {
        "ad": name,
        "soyad": surname,
        "yas": age
    }
})



print(ogrenciler)



ogrNo = input("Ogrenci numarası: ")
ogrenci = ogrenciler[ogrNo]
print(ogrenci)
