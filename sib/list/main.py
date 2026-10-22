buah = ["apel", "mangga", "jeruk"]
angka = [10, 20, 30, 40]
campuran = ["Budi", 20, True, 3.14]

print("Isi list buah:", buah)
print("Isi list angka:", angka)
print("Isi list campuran:", campuran)

#indexing
print("\n")
print("Elemen pertama dari list buah:", buah[0])
print("Elemen kedua dari list buah:", buah[1])
print("Elemen ketiga dari list buah:", buah[2])

#penambahan data pada list
print("\n")
print("tambah data baru pada list buah")
print("sebelum di tambah:", buah)
buah.append("pisang")
print("setelah di tambah:", buah)

print("\n")
print("tambah data baru pada list buah")
print("sebelum di tambah:", buah)
buah.insert(1, "semangka")
print("setelah di tambah:", buah)

#penghapusan data pada list
print("\n")
print("hapus data pada list buah")
print("sebelum di hapus:", buah)
buah.remove("mangga")
print("setelah di hapus:", buah)

#menampilkan list data menggunakan looping
print("\n")
print("menampilkan list data menggunakan looping")
for item in buah:
    print(item)

print("\n")
print("menampilkan list data menggunakan looping dengan index")
for item in range(len(buah)):
    print(f"{item + 1}. Nama buah: {buah[item]}")