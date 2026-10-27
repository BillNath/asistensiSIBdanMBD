
# ====================================================
# 1. MEMBUAT LIST UNTUK MENYIMPAN DATA NAMA
# ====================================================

# List kosong untuk menyimpan daftar nama.
nama = []


# ====================================================
# 2. MEMBUAT LIST UNTUK MENYIMPAN DATA AKUN
# ====================================================

# List untuk menyimpan username yang didaftarkan.
users = []

# List untuk menyimpan password yang didaftarkan.
passwords = []

# Username dan password dengan indeks yang sama
# merupakan pasangan akun yang sama.
# Contoh:
# users[0] = "budi"
# passwords[0] = "12345"


# ====================================================
# 3. PROGRAM UTAMA
# ====================================================

# Perulangan agar menu utama terus ditampilkan
# sampai pengguna memilih menu keluar.
while True:

    # Menampilkan pilihan menu utama.
    print("\nMenu:")
    print("1. Tambah Nama")
    print("2. Tampilkan Nama")
    print("3. Hapus Nama")
    print("4. Register / Login")
    print("0. Keluar")

    # Meminta pengguna memilih menu.
    # input() menghasilkan data bertipe string.
    pilihan = input("Pilih menu (0-4): ")


    # ====================================================
    # MENU 1: TAMBAH NAMA
    # ====================================================

    if pilihan == "1":

        # Meminta nama yang ingin ditambahkan.
        nama_baru = input("Masukkan nama baru: ")

        # Menambahkan nama ke akhir list.
        nama.append(nama_baru)

        # Menampilkan pesan bahwa nama berhasil ditambahkan.
        print(f"{nama_baru} berhasil ditambahkan.")


    # ====================================================
    # MENU 2: MENAMPILKAN DAFTAR NAMA
    # ====================================================

    elif pilihan == "2":

        # Memeriksa apakah list nama masih kosong.
        if len(nama) == 0:

            # Pesan jika belum ada nama yang disimpan.
            print("Belum ada nama yang ditambahkan.")

        else:

            # Menampilkan judul daftar nama.
            print("Daftar Nama:")

            # enumerate() mengambil indeks dan nilai setiap item.
            # start=1 membuat nomor tampilan dimulai dari 1.
            for i, n in enumerate(nama, start=1):

                # Menampilkan nomor dan nama.
                print(f"{i}. {n}")


    # ====================================================
    # MENU 3: MENGHAPUS NAMA
    # ====================================================

    elif pilihan == "3":

        # Memeriksa apakah list nama kosong.
        if len(nama) == 0:

            # Pesan jika tidak ada nama yang bisa dihapus.
            print("Belum ada nama yang ditambahkan.")

        else:

            # Meminta nama yang ingin dihapus.
            nama_hapus = input("Masukkan nama yang ingin dihapus: ")

            # Memeriksa apakah nama tersebut ada di dalam list.
            if nama_hapus in nama:

                # Menghapus nama yang cocok dari list.
                nama.remove(nama_hapus)

                # Menampilkan pesan berhasil.
                print(f"{nama_hapus} berhasil dihapus.")

            else:

                # Pesan jika nama tidak ditemukan.
                print(f"{nama_hapus} tidak ditemukan dalam daftar.")


    # ====================================================
    # MENU 4: REGISTER DAN LOGIN
    # ====================================================

    elif pilihan == "4":

        # Menampilkan submenu akun.
        print("\nMenu Akun:")
        print("1. Register")
        print("2. Login")
        print("0. Kembali ke Menu Utama")

        # Meminta pengguna memilih fitur akun.
        pilihan_akun = input("Pilih menu akun (0-2): ")


        # ------------------------------------------------
        # SUBMENU 1: REGISTER
        # ------------------------------------------------

        if pilihan_akun == "1":

            # Meminta username baru dari pengguna.
            username_baru = input("Buat username: ")

            # Variabel penanda untuk memeriksa username.
            # False berarti username belum ditemukan.
            username_ada = False

            # Memeriksa seluruh username yang sudah terdaftar.
            for username in users:

                # Membandingkan username yang dimasukkan
                # dengan username yang sudah tersimpan.
                if username == username_baru:

                    # Mengubah penanda menjadi True
                    # jika username sudah digunakan.
                    username_ada = True

                    # Menghentikan perulangan karena
                    # username sudah ditemukan.
                    break

            # Memeriksa hasil pengecekan username.
            if username_ada:

                # Menolak pendaftaran jika username sudah ada.
                print("Username sudah digunakan!")

            else:

                # Meminta password jika username belum digunakan.
                password_baru = input("Buat password: ")

                # Menyimpan username ke dalam list users.
                users.append(username_baru)

                # Menyimpan password ke dalam list passwords.
                # Posisi password harus sama dengan posisi username.
                passwords.append(password_baru)

                # Menampilkan pesan bahwa pendaftaran berhasil.
                print("Register berhasil!")


        # ------------------------------------------------
        # SUBMENU 2: LOGIN
        # ------------------------------------------------

        elif pilihan_akun == "2":

            # Meminta username untuk proses login.
            username_login = input("Masukkan username: ")

            # Meminta password untuk proses login.
            password_login = input("Masukkan password: ")

            # Variabel penanda bahwa login belum berhasil.
            login_berhasil = False

            # Memeriksa setiap username yang terdaftar.
            # i adalah indeks akun, sedangkan username
            # adalah nilai username pada indeks tersebut.
            for i, username in enumerate(users):

                # Memeriksa apakah username cocok
                # dan password pada indeks yang sama juga cocok.
                if (
                    username == username_login
                    and passwords[i] == password_login
                ):

                    # Mengubah penanda jika kedua data cocok.
                    login_berhasil = True

                    # Menghentikan perulangan karena akun ditemukan.
                    break

            # Menampilkan hasil proses login.
            if login_berhasil:

                # Pesan jika username dan password benar.
                print(
                    f"Login berhasil! "
                    f"Selamat datang, {username_login}."
                )

            else:

                # Pesan jika akun tidak ditemukan
                # atau password tidak sesuai.
                print("Login gagal! Username atau password salah.")


        # ------------------------------------------------
        # SUBMENU 0: KEMBALI KE MENU UTAMA
        # ------------------------------------------------

        elif pilihan_akun == "0":

            # Tidak perlu break karena kita hanya ingin
            # mengakhiri submenu dan kembali ke menu utama.
            print("Kembali ke menu utama.")

        else:

            # Pesan jika pilihan submenu tidak tersedia.
            print("Pilihan akun tidak valid.")


    # ====================================================
    # MENU 0: KELUAR DARI PROGRAM
    # ====================================================

    elif pilihan == "0":

        # Menampilkan pesan sebelum program berhenti.
        print("Program selesai. Terima kasih!")

        # Menghentikan perulangan utama.
        break


    # ====================================================
    # PILIHAN MENU TIDAK VALID
    # ====================================================

    else:

        # Pesan jika pengguna memasukkan pilihan
        # selain menu yang tersedia.
        print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")
