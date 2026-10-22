def menu():
    print("\nMenu:")
    print("1. Calculator")
    print("2. Fibonacci")
    print("3. Buat Kotak")
    print("0. Keluar")


def fibonacci(n):
    if n <= 0:
        print("n harus lebih dari 0")
        return

    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()

def perhitungan(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b != 0:
            return a / b
        else:
            return "Error: Pembagian dengan nol"
    else:
        return "Operator tidak valid"


def buatKotak(a):
    for i in range(a):
        print("* " * a)


while True:
    menu()
    menuSelect = int(input("Pilih menu (0-3): "))

    if menuSelect == 0:
        print("Program selesai. Terima kasih!")
        break

    elif menuSelect == 1:
        a = int(input("Masukkan angka pertama: "))
        b = int(input("Masukkan angka kedua: "))
        op = input("Masukkan operator (+, -, *, /): ")
        hasil = perhitungan(a, b, op)
        print("Hasil perhitungan:", hasil)

    elif menuSelect == 2:
        n = int(input("Masukkan jumlah bilangan Fibonacci yang ingin ditampilkan: "))
        fibonacci(n)

    elif menuSelect == 3:
        ukuran = int(input("Masukkan ukuran kotak: "))
        buatKotak(ukuran)

    else:
        print("Pilihan tidak valid, silakan pilih 0-3.")