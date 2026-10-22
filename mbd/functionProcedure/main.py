def tambah(a, b):
    hasil = a + b
    return hasil

def sapa(nama):
    print(f"Halo, {nama}! Selamat datang.")

def perhitungan(a,b,operator):
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

def fibonacci(n):
    if n <= 0:
        print("n harus lebih dari 0")
        return

    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()

fibonacci(10)

#=======================================================
value1 = int(input("Masukkan angka pertama: "))
operator = str(input("Masukkan operator (+, -, *, /): "))
value2 = int(input("Masukkan angka kedua: "))

output = float(perhitungan(value1, value2, operator))
print("Hasil perhitungan:", output)

ukuran = int(input("Masukkan ukuran kotak: "))
kotak = buatKotak(ukuran)
print(kotak)