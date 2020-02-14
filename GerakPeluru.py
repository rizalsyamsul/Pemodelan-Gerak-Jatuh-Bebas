import math
import matplotlib.pyplot as plt
import numpy

arrayOfXNumerik = []
arrayOfYNumerik = []
arrayOfXAnalitik = []
arrayOfYAnalitik = []
#input
kecepatan = float(input('Masukkan Kecepatan : '))
sudut = float(input('Masukkan Sudut Kemiringan : '))
perubahanwaktu = float(input('Masukkan Perubahan Waktu/delta waktu : '))
posisiXNumerik = float(input('Masukkan x(0) numerik : '))
posisiYNumerik = float(input('Masukkan y(0) numerik : '))
posisiXAnalitik = float(input('Masukkan x(0) analitik : '))
posisiYAnalitik = float(input('Masukkan y(0) analitik: '))

print('\n')
#merubah sudut menjadi sin dan cos menggunakan radian
Sin = round(math.sin(math.radians(sudut)),2)
Cos = math.cos(math.radians(sudut))

#rumus
g = 9.8
waktu = float((2 * kecepatan * Sin) / g)
hAtas = float(math.pow(kecepatan,2) * math.pow(Sin,2))
hBawah = float(2*g)
hMax = float(hAtas/hBawah)
R = kecepatan * Cos * waktu
g = -9.8

# v(0)
kecepatanNumerikX = float(kecepatan * Cos)
kecepatanNumerikY = float(kecepatan * Sin)
kecepatanAnalitikX = float(kecepatan * Cos)
kecepatanAnalitikY = float(kecepatan * Sin)

#memasukan data ke dalam array
arrayOfXNumerik.append(posisiXNumerik)
arrayOfYNumerik.append(posisiYNumerik)
arrayOfXAnalitik.append(posisiXAnalitik)
arrayOfYAnalitik.append(posisiYAnalitik)

#perhitungan numerik  
for t in numpy.arange(0,waktu+perubahanwaktu,perubahanwaktu):
    #vy
    kecepatanNumerikY = kecepatanNumerikY + (g * perubahanwaktu)
    #y(t+delta t)
    posisiYNumerik = posisiYNumerik + (kecepatanNumerikY * perubahanwaktu)
    arrayOfYNumerik.append(posisiYNumerik)
    #x konstan
    posisiXNumerik = posisiXNumerik + (kecepatanNumerikX * perubahanwaktu)
    arrayOfXNumerik.append(posisiXNumerik)
    
    if posisiYNumerik < 0:
        print('Numerik')    
        print('Waktu Total : ',t)    
        print ('Jarak Maksimum : ',posisiXNumerik)
        print ('Tinggi Maksimum : ',hMax)
        print('\n')
        break


#perhitungan analitik
for t in numpy.arange(0,waktu+perubahanwaktu,perubahanwaktu):
     # x konstan
     posisiXAnalitik = kecepatanAnalitikX * t
     arrayOfXAnalitik.append(posisiXAnalitik)
     # y(t)
     posisiYAnalitik = (0.5 * g * math.pow(t,2)) + kecepatanAnalitikY * t
     arrayOfYAnalitik.append(posisiYAnalitik)
     
     if posisiYAnalitik < 0:
        print('Analitik')    
        print('Waktu Total : ',t)    
        print ('Jarak Maksimum : ',R)
        print ('Tinggi Maksimum : ',hMax)
        print('\n')
        break
      
# penggambaran    
plt.xlabel('Jarak')
plt.ylabel('Ketinggian')
plt.plot(arrayOfXAnalitik,arrayOfYAnalitik,'r')
plt.plot(arrayOfXNumerik,arrayOfYNumerik,'b')
plt.legend(['Analitik','Numerik'],loc = 'best')
plt.ylim(0,hMax+0.1)
plt.show()
