"""VARIABLE"""
#soal nomor 1
data_string = "john"
print("nama :",data_string)

#soal nomor 2
x = 10
data_string = "sepuluh"
print("nilai x =",data_string, x)

#soal nomor 3
data_string1 = "Hello"
data_string = "World"

#soal nomor 4 (dijawab)
print(data_string1, data_string)

a = 10
b = 5

a, b = b,a
print("a =", a)
print("b =", b)

#soal nomor 5 (dijawab)
nama = "alice"
umur = 25
print(f"Nama saya {nama} dan saya berumur {umur} tahun")

"""OPERASI ARITMATIKA"""
#luas alas seigitiga
ti = 25
alas = 10
Luas = 1/2 * alas * ti
print("luas segitiga =", Luas)

#menghitung volume tabung (Hampir benar)
pi =float(input("masukan nilai pi ="))
jari_jari =float(input("masukan nilai jari jari** ="))
tinggi2 =float(input("masukan nilai tinggi ="))

Volume = pi * jari_jari** 2 * tinggi2
print("Volume =",pi,'*', jari_jari** 2,'*',tinggi2, '=', Volume)

"""Menghitung volume yang benar"""
# Menghitung volume tabung
pi = 3.14  # Nilai pi tetap
jari_jari = float(input("Masukkan nilai jari-jari: "))
tinggi = float(input("Masukkan nilai tinggi: "))

# Menghitung volume tabung
volume = pi * (jari_jari ** 2) * tinggi

# Menampilkan hasil
print(f"Volume = {pi} * {jari_jari}² * {tinggi} = {volume}")

#menentukan bilangan ganjil atau genap
angka = int(input("masukan sebuah bilangan :"))

if angka % 2 == 0:
    print("ini bilangan genap")

else:
    print("ini bilangan ganjil")

#menghitung pangkat 2
bilangan = float(input("masukan sebuah bilangan ="))
hasil = bilangan ** 2
print("hasil pangkat dua dari", bilangan, "adalah", hasil)

#menghitung modulus
angka1 = int(input("masukan bilangan pertama :"))
angka2 = int(input("masukan bilangan kedua :"))

sisa = angka1 % angka2

print("sisa dari", angka1, "dibagi", angka2, "adalah", sisa)

"""KOMPARASI"""
#Menentukan Bilangan Positif dan Negatif
bilangan = float(input("Masukan sebuah angka : "))

if bilangan > 0:
    print("Ini bilangan positif")
elif bilangan < 0:
    print("Bilangan ini negatif")
else:
    print("bilangan ini adalah nol")

#Membandingkan dua bilangan bulat (Int)
bilangan = int(input("Masukan bilangan bulat :"))
bilangan2 = int(input("Masukan bilangan bulat :"))

bilangan0 = bilangan > bilangan2
print(bilangan,'>',bilangan2, '=', bilangan0)

#Cek kelipatan 5
bilangan = int(input("Masukan sebuah bilangan bulat :"))

if bilangan % 5 == 0:
    print("bilangan kelipatan lima")
else:
    print("bukan kelipatan lima")

#cek usia dewasa
umur =int(input("Masukan usia Anda :"))

if umur >= 18:
    print("Anda sudah memasuki usia dewasa.")
else:
    print("Anda belum dewasa.")

#Validasi nilai ujian
nilai =int(input("Masukan hasil Nilai Ujian Anda :"))
if 0 <= nilai <= 100:

    if nilai >= 76:
        print("Nilai Anda di atas KKM")
    else:
        print("Nilai Anda dibawah KKM")
else:
    print("Nilai yang dimasukan tidak valid harap masukkan nilai antara 0")
