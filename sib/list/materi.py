nama = []

while True:
    print("\nMenu:")
    print("1. Tambah Nama")
    print("2. Tampilkan Nama")
    print("3. Hapus Nama")
    print("0. Keluar")

    pilihan = input("Pilih menu (0-3): ")

    if pilihan == "1":
        nama_baru = input("Masukkan nama baru: ")
        nama.append(nama_baru)
        print(f"{nama_baru} berhasil ditambahkan.")

    elif pilihan == "2":
        if len(nama) == 0:
            print("Belum ada nama yang ditambahkan.")
        else:
            print("Daftar Nama:")
            for i, n in enumerate(nama, start=1):
                print(f"{i}. {n}")

    elif pilihan == "3":
        if len(nama) == 0:
            print("Belum ada nama yang ditambahkan.")
        else:
            nama_hapus = input("Masukkan nama yang ingin dihapus: ")
            if nama_hapus in nama:
                nama.remove(nama_hapus)
                print(f"{nama_hapus} berhasil dihapus.")
            else:
                print(f"{nama_hapus} tidak ditemukan dalam daftar.")

    elif pilihan == "0":
        print("Program selesai. Terima kasih!")
        break

    else:
        print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")