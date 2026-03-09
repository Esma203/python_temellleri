# 1-Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.
#sayi = int(input('sayı: '))
#result = (sayi >= 0) and (sayi <= 100)
#print(f'girilen sayı 0-100 arasında olma durumu: {result}')
# 2-Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.
#sayi = int(input('sayı: '))
#result = (sayi > 0) and (sayi % 2 == 0)
#print(f'girilen sayı pozitif çift sayı olma durumu: {result}')
# 3- Email ve parola bilgileri ile giriş kontrolü yapınız.
#email ='email@esmauslu.com'
#password = 'parola123'

#girilenEmail = input('email: ')
#girilenPassword = input('parola: ')

#result = (girilenEmail == email) and (girilenPassword == password)
#print(f'giriş başarılı olma durumu: {result}')
# 4-Girilen 3 sayıdan en büyüğünü bulunuz.
#sayi1 = int(input('sayı 1: '))  
#sayi2 = int(input('sayı 2: '))
#sayi3 = int(input('sayı 3: '))
#result = (sayi1 > sayi2) and (sayi1 > sayi3)
#print(f'sayı 1 en büyük olma durumu: {result}')
#result = (sayi2 > sayi1) and (sayi2 > sayi3)
#print(f'sayı 2 en büyük olma durumu: {result}')
#result = (sayi3 > sayi1) and (sayi3 > sayi2)
#print(f'sayı 3 en büyük olma durumu: {result}') 
# 5- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
#    Formül: (kilo / boy ** 2)
#    Aşağıdaki tabloya göre kişi hangi gruba girmektedir?
#    0-18.4 => Zayıf    
#    18.5-24.9 => Normal
#    25.0-29.9 => Fazla Kilolu
#    30.0-34.9 => Şişman (Obez)

#name = input('adınız: ')
#kg = float(input('kilonuz: '))
#hg = int(input('boyunuz: '))

#index = kg / (hg ** 2)
#print(f'kilo indeksiniz: {index} ve durumunuz: {"zayıf" if index < 18.5 else "normal" if index < 25 else "fazla kilolu" if index < 30 else "şişman (obez)"}')

