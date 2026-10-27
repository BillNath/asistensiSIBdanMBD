
# ====================================================
# 1. FUNCTION PROCEDURE: MENU
# ====================================================

# Function adalah kumpulan kode yang diberi nama
# dan dapat dipanggil kapan saja ketika dibutuhkan.
#
# Procedure adalah fungsi yang fokus menjalankan
# suatu tindakan, misalnya menampilkan menu.
#
# Fungsi menu() tidak menerima parameter dan tidak
# mengembalikan nilai menggunakan return.
# Tugasnya hanya menampilkan pilihan menu ke layar.

def menu():
    print("\nMenu:")
    print("1. Calculator")
    print("2. Fibonacci")
    print("3. Buat Kotak")
    print("0. Keluar")


# ====================================================
# 2. FUNCTION FIBONACCI
# ====================================================

# Fungsi fibonacci() digunakan untuk menampilkan
# deret Fibonacci sebanyak n bilangan.
#
# Fibonacci adalah deret angka yang setiap angka
# berikutnya merupakan penjumlahan dua angka sebelumnya.
#
# Contoh:
# 0, 1, 1, 2, 3, 5, 8, 13, ...
#
# Parameter n menentukan jumlah bilangan yang ditampilkan.

def fibonacci(n):

    # Memeriksa apakah n kurang dari atau sama dengan 0.
    # Jika benar, tampilkan pesan kesalahan.
    if n <= 0:
        print("n harus lebih dari 0")

        # return tanpa nilai menghentikan fungsi.
        return

    # Menentukan dua angka pertama Fibonacci.
    # a = 0 dan b = 1.
    a, b = 0, 1

    # Perulangan dilakukan sebanyak n kali.
    # Tanda _ digunakan karena kita tidak membutuhkan
    # nilai penghitung perulangannya.
    for _ in range(n):

        # Menampilkan angka a.
        # end=" " membuat angka tetap pada baris yang sama.
        print(a, end=" ")

        # Memperbarui nilai a dan b.
        # a mendapatkan nilai b sebelumnya.
        # b mendapatkan hasil penjumlahan a dan b sebelumnya.
        a, b = b, a + b

    # Berpindah ke baris baru setelah semua angka ditampilkan.
    print()


# ====================================================
# 3. FUNCTION BUAT KOTAK
# ====================================================

# Fungsi buatKotak() digunakan untuk membuat pola kotak
# dari karakter bintang (*).
#
# Parameter a menentukan jumlah baris dan kolom.
#
# Contoh jika a = 3:
# * * *
# * * *
# * * *

def buatKotak(a):

    # Perulangan luar mengatur jumlah baris.
    for i in range(a):

        # Perulangan dalam mengatur jumlah kolom
        # untuk setiap baris.
        for j in range(a):

            # Menampilkan bintang tanpa pindah baris.
            # end=" " memberikan spasi setelah setiap bintang.
            print("*", end=" ")

        # Setelah satu baris selesai, pindah ke baris baru.
        print()


# ====================================================
# 4. FUNCTION PERHITUNGAN
# ====================================================

# Fungsi ini digunakan oleh menu Calculator.
#
# Parameter:
# a  = angka pertama
# b  = angka kedua
# op = operator matematika
#
# Fungsi akan mengembalikan hasil sesuai operator
# yang dipilih oleh pengguna.

def perhitungan(a, b, op):

    # Jika operator adalah "+", lakukan penjumlahan.
    if op == '+':
        return a + b

    # Jika operator adalah "-", lakukan pengurangan.
    elif op == '-':
        return a - b

    # Jika operator adalah "*", lakukan perkalian.
    elif op == '*':
        return a * b

    # Jika operator adalah "/", lakukan pembagian.
    elif op == '/':

        # Pastikan angka kedua bukan nol.
        if b != 0:
            return a / b
        else:
            return "Error: Pembagian dengan nol"

    # Jika operator tidak sesuai dengan pilihan,
    # kembalikan pesan kesalahan.
    else:
        return "Operator tidak valid"


# ====================================================
# 5. PROGRAM UTAMA
# ====================================================

# while digunakan untuk melakukan perulangan
# selama kondisi yang ditentukan bernilai True.
#
# True berarti benar, sehingga while True akan terus
# berjalan sampai dihentikan menggunakan break.
#
# Tujuannya agar menu terus ditampilkan kembali
# setelah pengguna selesai menjalankan suatu fitur.

while True:

    # Memanggil fungsi menu() untuk menampilkan pilihan.
    menu()

    # Meminta pengguna memilih menu dari angka 0 sampai 3.
    #
    # input() menghasilkan teks (string).
    # int() mengubah teks tersebut menjadi bilangan bulat.
    #
    # Contoh:
    # Input "1" diubah menjadi angka 1.
    menuSelect = int(input("Pilih menu (0-3): "))


    # ------------------------------------------------
    # PILIHAN 0: KELUAR DARI PROGRAM
    # ------------------------------------------------

    # Memeriksa apakah pengguna memilih angka 0.
    if menuSelect == 0:

        # Menampilkan pesan sebelum program dihentikan.
        print("Program selesai. Terima kasih!")

        # break menghentikan perulangan while True.
        # Setelah break dijalankan, program keluar
        # dari menu dan melanjutkan ke akhir program.
        break


    # ------------------------------------------------
    # PILIHAN 1: CALCULATOR
    # ------------------------------------------------

    # Jika pilihan bukan 0, Python memeriksa kondisi elif.
    # Jika menuSelect bernilai 1, fitur kalkulator dijalankan.
    elif menuSelect == 1:

        # Meminta angka pertama dari pengguna.
        a = int(input("Masukkan angka pertama: "))

        # Meminta angka kedua dari pengguna.
        b = int(input("Masukkan angka kedua: "))

        # Meminta operator matematika.
        # Tidak perlu menggunakan str() karena input()
        # sudah menghasilkan string.
        op = input("Masukkan operator (+, -, *, /): ")

        # Memanggil fungsi perhitungan() dengan tiga argumen.
        # Hasil yang dikembalikan fungsi disimpan di variabel hasil.
        hasil = perhitungan(a, b, op)

        # Menampilkan hasil perhitungan atau pesan kesalahan.
        print("Hasil perhitungan:", hasil)


    # ------------------------------------------------
    # PILIHAN 2: FIBONACCI
    # ------------------------------------------------

    # Jika menuSelect bernilai 2, fitur Fibonacci dijalankan.
    elif menuSelect == 2:

        # Meminta jumlah angka Fibonacci yang ingin ditampilkan.
        n = int(input(
            "Masukkan jumlah bilangan Fibonacci yang ingin ditampilkan: "
        ))

        # Memanggil fungsi fibonacci() dengan argumen n.
        fibonacci(n)


    # ------------------------------------------------
    # PILIHAN 3: BUAT KOTAK
    # ------------------------------------------------

    # Jika menuSelect bernilai 3, fitur pembuatan kotak dijalankan.
    elif menuSelect == 3:

        # Meminta ukuran kotak dari pengguna.
        ukuran = int(input("Masukkan ukuran kotak: "))

        # Memanggil fungsi buatKotak() dengan argumen ukuran.
        buatKotak(ukuran)


    # ------------------------------------------------
    # PILIHAN SELAIN 0, 1, 2, ATAU 3
    # ------------------------------------------------

    # else dijalankan jika semua kondisi if dan elif
    # sebelumnya tidak terpenuhi.
    #
    # Contoh: pengguna memilih angka 5.
    else:
        print("Pilihan tidak valid, silakan pilih 0-3.")

# Program berakhir setelah pengguna memilih menu 0.
