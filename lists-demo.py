# 1- "BMW, Mercedes, Opel, Mazda" elemanlarına sahip bir liste oluşturunuz.
arabalar = ['BMW', 'Mercedes', 'Opel', 'Mazda']

# 2- Liste kaç elemanlıdır?
result = len(arabalar)
# 3- Listenin ilk ve son elemanı nedir?
result = arabalar[0]
result = arabalar[1]
# 4- Mazda değerini Toyota ile değiştirin.
arabalar[-1] = 'Toyota'
result = arabalar
# 5- Mercedes listenin bir elemanı mıdır?
result = 'Mercedes' in arabalar
result = 'Ford' in arabalar
# 6- Listenin -2 indeksindeki değer nedir?
result = arabalar[-2]
# 7- Listenin ilk 3 elemanını alın.
result = arabalar[0:3]
# 8- Listenin son 2 elemanını yerine "Toyota" ve "Renault" değerlerini ekleyin.
arabalar[-2:] = ['Toyota', 'Renault'] 
result = arabalar
# 9- Listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin.
arabalar += ['Audi', 'Nissan']
result = arabalar
# 10- Listenin son elemanını silin.
del arabalar[-1]
result = arabalar
# 11- Liste elemanlarını tersten yazdırın.
result = arabalar[::-1]
# 12- Aşağıdaki verileri bir liste içinde saklayınız.

      #  studentA: Yiğit Bilgi 2010, (70,60,70)
      #  studentB: Sena Turan 1999, (80,80,70)
      #  studentC: Ahmet Turan 1998, (80,70,90)

studentsA = ['Yiğit Bilgi', 2010, (70,60,70)]
studentsB = ['Sena Turan', 1999, (80,80,70)]
studentsC = ['Ahmet Turan', 1998, (80,70,90)]

# 13- Liste elemanlarını tek tek ekrana yazdırınız.

result = studentsA[0]
result = studentsB[1]
result = studentsC[2][1]

result = f"{studentsA[0]} {studentsA[1]} {studentsA[2]} yaşında ve not ortalaması {(studentsA[2][0] + studentsA[2][1] + studentsA[2][2]) / 3}"

print(result) 