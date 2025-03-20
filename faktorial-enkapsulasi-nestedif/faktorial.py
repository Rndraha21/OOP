

def faktorial(angka):
    if angka == 0 or angka == 1:
        return 1
    else:
        return angka*faktorial(angka-1)

def main():
    while True:
        print("+"*10)
        print("FAKTORIAL")
        print("+"*10)
        try:
            pilihan = int(input('''\nPilihan
1. Hitung faktorial
2. Keluar
Masukkan Pilihan: '''))
            if pilihan == 1:
                n = int(input("Masukkan angka: "))
                print(f"Faktorial dari {n} adalah {faktorial(n)}")
            else:
                print("Terima kasih telah mencoba program saya!")
                break
        except ValueError:
            print("Silahkan masukkan angka yang valid!!!")

if __name__ == "__main__":
    main()