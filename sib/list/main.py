
# ====================================================
# 1. MEMBUAT LIST
# ====================================================

# List adalah struktur data untuk menyimpan banyak nilai
# dalam satu variabel.
#
# List ditandai dengan tanda kurung siku [].
# Setiap data di dalam list disebut elemen.
# Setiap elemen dipisahkan menggunakan tanda koma.
#
# Contoh:
# ["apel", "mangga", "jeruk"]
#
# List dapat menyimpan data dengan tipe yang sama
# maupun tipe data yang berbeda.

buah = ["apel", "mangga", "jeruk"]

# List berisi angka.
angka = [10, 20, 30, 40]

# List berisi berbagai tipe data:
# string (teks), integer (bilangan bulat),
# boolean (True/False), dan float (desimal).
campuran = ["Budi", 20, True, 3.14]


# Menampilkan seluruh isi list.
print("Isi list buah:", buah)
print("Isi list angka:", angka)
print("Isi list campuran:", campuran)


# ====================================================
# 2. INDEXING PADA LIST
# ====================================================

# Index adalah nomor posisi setiap elemen di dalam list.
#
# PENTING:
# Index list Python dimulai dari 0, bukan 1.
#
# buah = ["apel", "mangga", "jeruk"]
#
# Index 0 = "apel"
# Index 1 = "mangga"
# Index 2 = "jeruk"

print("\n")
print("Elemen pertama dari list buah:", buah[0])
print("Elemen kedua dari list buah:", buah[1])
print("Elemen ketiga dari list buah:", buah[2])

# Jika mengakses index yang tidak tersedia,
# Python akan menghasilkan IndexError.
#
# Contoh:
# print(buah[10])  # IndexError


# ====================================================
# 3. MENAMBAHKAN DATA MENGGUNAKAN APPEND()
# ====================================================

# append() digunakan untuk menambahkan elemen baru
# ke bagian paling akhir list.
#
# Sintaks:
# nama_list.append(data_baru)

print("\n")
print("Tambah data baru pada list buah")

# Menampilkan list sebelum ditambahkan.
print("Sebelum ditambah:", buah)

# Menambahkan "pisang" ke akhir list.
buah.append("pisang")

# Menampilkan list setelah ditambahkan.
print("Setelah ditambah:", buah)


# ====================================================
# 4. MENAMBAHKAN DATA MENGGUNAKAN INSERT()
# ====================================================

# insert() digunakan untuk menambahkan elemen
# pada posisi index tertentu.
#
# Sintaks:
# nama_list.insert(index, data_baru)
#
# Contoh:
# buah.insert(1, "semangka")
#
# Artinya, masukkan "semangka" pada index 1.
# Elemen yang sebelumnya berada di index 1
# dan elemen setelahnya akan bergeser ke kanan.

print("\n")
print("Tambah data baru pada list buah")

print("Sebelum ditambah:", buah)

buah.insert(1, "semangka")

print("Setelah ditambah:", buah)


# ====================================================
# 5. MENGHAPUS DATA MENGGUNAKAN REMOVE()
# ====================================================

# remove() digunakan untuk menghapus elemen berdasarkan
# NILAI yang ingin dihapus, bukan berdasarkan index.
#
# Sintaks:
# nama_list.remove(nilai)
#
# Contoh:
# buah.remove("mangga")
#
# Artinya, hapus elemen dengan nilai "mangga".
#
# Jika nilai yang dicari tidak ada di dalam list,
# Python akan menghasilkan ValueError.

print("\n")
print("Hapus data pada list buah")

print("Sebelum dihapus:", buah)

buah.remove("mangga")

print("Setelah dihapus:", buah)


# ====================================================
# 6. MENAMPILKAN LIST MENGGUNAKAN FOR
# ====================================================

# for digunakan untuk melakukan perulangan.
#
# Pada contoh ini, variabel item akan mengambil
# setiap nilai dari list buah secara bergantian.
#
# Contoh:
# Iterasi pertama: item = "apel"
# Iterasi kedua:   item = "semangka"
# Iterasi ketiga:  item = "jeruk"
# Iterasi keempat: item = "pisang"

print("\n")
print("Menampilkan list data menggunakan looping")

for item in buah:
    print(item)


# ====================================================
# 7. MENAMPILKAN LIST MENGGUNAKAN INDEX
# ====================================================

# len() digunakan untuk menghitung jumlah elemen list.
#
# range(len(buah)) menghasilkan urutan index
# mulai dari 0 sampai sebelum jumlah elemen.
#
# Misalnya, jika ada 4 elemen:
# range(4) menghasilkan 0, 1, 2, 3.
#
# Variabel item di sini adalah index,
# bukan nilai buah secara langsung.
#
# buah[item] digunakan untuk mengambil nilai
# berdasarkan index tersebut.

print("\n")
print("Menampilkan list data menggunakan looping dengan index")

for item in range(len(buah)):
    # item + 1 digunakan agar nomor yang ditampilkan
    # dimulai dari 1, bukan 0.
    #
    # buah[item] mengambil nama buah pada index item.
    print(f"{item + 1}. Nama buah: {buah[item]}")


# ====================================================
# 8. CONTOH PENGGUNAAN LIST UNTUK REGISTER DAN LOGIN
# ====================================================

# List dapat digunakan untuk menyimpan data pengguna
# dalam contoh program sederhana.
#
# Pada contoh ini:
# users menyimpan username.
# passwords menyimpan password.
#
# Index username dan password harus sesuai.
#
# Contoh:
# users[0] = "budi"
# passwords[0] = "12345"
#
# Artinya, akun pada index 0 memiliki:
# Username = budi
# Password = 12345
#
# CATATAN:
# Ini hanya contoh pembelajaran.
# Program nyata sebaiknya menggunakan database
# dan menyimpan password dalam bentuk hash,
# bukan menyimpan password asli seperti ini.

users = ["budi"]
passwords = ["12345"]


# ====================================================
# 9. FUNCTION REGISTER
# ====================================================

# Register digunakan untuk membuat akun baru.
#
# Fungsi menerima username dan password baru.
# Sebelum menyimpan akun, program memeriksa
# apakah username sudah digunakan.

def register():

    # Meminta pengguna memasukkan username baru.
    username = input("Buat username: ")

    # Memeriksa apakah username sudah ada di list users.
    if username in users:
        print("Username sudah digunakan!")

    else:
        # Meminta password jika username belum digunakan.
        password = input("Buat password: ")

        # Menambahkan username ke list users.
        users.append(username)

        # Menambahkan password ke list passwords.
        # Kedua data ditambahkan pada index yang bersesuaian.
        passwords.append(password)

        print("Register berhasil!")


# ====================================================
# 10. FUNCTION LOGIN
# ====================================================

# Login digunakan untuk memeriksa apakah username
# dan password yang dimasukkan cocok dengan data akun.
#
# Program mencari username di list users.
# Jika ditemukan, index username digunakan untuk
# mengambil password yang sesuai dari list passwords.

def login():

    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    # Memeriksa apakah username terdaftar.
    if username in users:

        # Mencari posisi username di dalam list.
        index = users.index(username)

        # Memeriksa password pada index yang sama.
        if passwords[index] == password:
            print("Login berhasil! Selamat datang,", username)
        else:
            print("Password salah!")

    else:
        print("Username tidak ditemukan!")


# ====================================================
# 11. MENU REGISTER DAN LOGIN
# ====================================================

# while True membuat menu terus ditampilkan.
# Program berhenti ketika pengguna memilih 0.

while True:

    print("\n=== MENU AKUN ===")
    print("1. Register")
    print("2. Login")
    print("0. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":

        # Memanggil fungsi register().
        register()

    elif pilihan == "2":

        # Memanggil fungsi login().
        login()

    elif pilihan == "0":

        print("Program selesai.")
        break

    else:

        print("Pilihan tidak valid!")
