
# =========================================================
# 1. FUNCTION TAMBAH
# =========================================================

# Fungsi untuk menjumlahkan dua angka.
# a dan b disebut parameter, yaitu tempat menerima nilai.
# return digunakan untuk mengembalikan hasil fungsi.

def tambah(a, b):
    hasil = a + b
    return hasil


# =========================================================
# 2. FUNCTION SAPA
# =========================================================

# Fungsi untuk menyapa seseorang.
# Parameter nama menerima teks nama pengguna.
# f-string memungkinkan kita memasukkan variabel ke teks.

def sapa(nama):
    print(f"Halo, {nama}! Selamat datang.")


# =========================================================
# 3. FUNCTION PERHITUNGAN
# =========================================================

# Kalkulator sederhana untuk penjumlahan, pengurangan,
# perkalian, dan pembagian.
#
# a        = angka pertama
# b        = angka kedua
# operator = simbol matematika

def perhitungan(a, b, operator):

    if operator == '+':
        return a + b

    elif operator == '-':
        return a - b

    elif operator == '*':
        return a * b

    elif operator == '/':
        # Memastikan angka kedua bukan nol.
        if b != 0:
            return a / b
        else:
            return "Error: Pembagian dengan nol"

    else:
        return "Operator tidak valid"


# =========================================================
# 4. FUNCTION BUAT KOTAK
# =========================================================

# Membuat kotak dari karakter "*".
# Parameter a menentukan jumlah baris dan kolom.
#
# Contoh jika a = 3:
# * * *
# * * *
# * * *

def buatKotak(a):

    # Perulangan luar menentukan jumlah baris.
    for i in range(a):

        # Menyiapkan string kosong untuk satu baris.
        baris = ""

        # Perulangan dalam menentukan jumlah kolom.
        for j in range(a):

            # Menambahkan karakter bintang ke baris.
            baris += "* "

        # Menampilkan baris yang sudah selesai.
        print(baris)


# =========================================================
# 5. FUNCTION FIBONACCI
# =========================================================

# Menampilkan deret Fibonacci sebanyak n angka.
# Setiap angka merupakan penjumlahan dua angka sebelumnya.
#
# Contoh:
# 0, 1, 1, 2, 3, 5, 8, 13, ...

def fibonacci(n):

    # Memastikan n harus lebih besar dari nol.
    if n <= 0:
        print("n harus lebih dari 0")
        return

    # Nilai awal deret Fibonacci.
    a, b = 0, 1

    # Mengulang sebanyak n kali.
    for _ in range(n):

        # Menampilkan angka tanpa pindah baris.
        print(a, end=" ")

        # Memperbarui dua angka Fibonacci.
        a, b = b, a + b

    # Berpindah ke baris baru setelah selesai.
    print()


# =========================================================
# 6. FUNCTION TAMBAH BANYAK ANGKA MENGGUNAKAN *args
# =========================================================

# *args memungkinkan fungsi menerima jumlah argumen
# posisi yang fleksibel, tanpa menentukan jumlahnya
# satu per satu di dalam parameter.
#
# Contoh:
# tambahBanyak(10, 20)
# tambahBanyak(10, 20, 30)
# tambahBanyak(1, 2, 3, 4, 5)
#
# Semua argumen akan dikumpulkan ke dalam tuple bernama args.
# Tuple adalah kumpulan nilai yang dapat menampung banyak item.

def tambahBanyak(*args):

    # Menampilkan seluruh angka yang diterima.
    # args berbentuk tuple, contohnya (10, 20, 30).
    print("Angka yang diterima:", args)

    # Variabel untuk menyimpan hasil penjumlahan.
    total = 0

    # Mengambil setiap angka dari tuple args.
    for angka in args:

        # Menambahkan angka ke total sebelumnya.
        # Sama seperti: total = total + angka
        total += angka

    # Mengembalikan hasil akhir penjumlahan.
    return total


# =========================================================
# 7. MENJALANKAN FUNCTION FIBONACCI
# =========================================================

# Memanggil fungsi fibonacci dengan argumen 10.
# Artinya, tampilkan 10 angka Fibonacci.

fibonacci(10)


# =========================================================
# 8. MENJALANKAN FUNCTION TAMBAH BANYAK ANGKA
# =========================================================

# Contoh pemanggilan dengan dua angka.
print("Hasil penjumlahan:", tambahBanyak(10, 20))

# Contoh pemanggilan dengan tiga angka.
print("Hasil penjumlahan:", tambahBanyak(10, 20, 30))

# Contoh pemanggilan dengan lima angka.
print("Hasil penjumlahan:", tambahBanyak(1, 2, 3, 4, 5))


# =========================================================
# 9. INPUT KALKULATOR
# =========================================================

# input() menerima masukan pengguna dalam bentuk teks.
# int() mengubah teks angka menjadi bilangan bulat.

value1 = int(input("Masukkan angka pertama: "))

# Operator tetap berupa string, misalnya "+", "-", "*", "/".
operator = input("Masukkan operator (+, -, *, /): ")

value2 = int(input("Masukkan angka kedua: "))

# Memanggil fungsi kalkulator.
output = perhitungan(value1, value2, operator)

# Memeriksa apakah hasil berupa angka atau pesan kesalahan.
# Hal ini mencegah error ketika hasil berupa teks.
if isinstance(output, (int, float)):
    print("Hasil perhitungan:", output)
else:
    print(output)


# =========================================================
# 10. INPUT UKURAN KOTAK
# =========================================================

# Meminta pengguna menentukan ukuran kotak.
ukuran = int(input("Masukkan ukuran kotak: "))

# Memanggil fungsi untuk menampilkan kotak.
# Tidak perlu menyimpan hasilnya ke variabel karena
# buatKotak() menggunakan print() dan tidak memiliki return.
buatKotak(ukuran)
