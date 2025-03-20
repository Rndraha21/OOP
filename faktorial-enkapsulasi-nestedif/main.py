print("Usia")
usia = int(input("Masukkan usia anda: "))

if usia >= 18:
    print("Anda sudah dewasa")
else:
    print("Anda belum dewasa")

print("\nKelipatan 15")
kelipatan = int(input("Masukkan bilangan: "))
if kelipatan % 15 == 0:
    print("Bilangan anda adalah bilangan kelipatan 15")
else:
    print("Bilangan anda bukan kelipatan 15")

print("\nBilangan bulat")
bilangan_bulat = int(input("Masukkan bilangan bulat: "))
if bilangan_bulat > 0:
    print("Bilangan positif")
elif bilangan_bulat == 0:
    print("Bilangan nol")
else:
    print("Bilangan negatif")

print("\nDiskon")
total = int(input("Masukkan total belanja: "))
diskon = total/(100*10)
if total >= 100000:
    print(f"Anda mendapatkan diskon sebesar {diskon} rupiah")
else:
    print("Anda tidak mendapatkan diskon")


print("\nTahun kabisat")
tahun = int(input("Masukkan tahun: "))
if tahun % 4 == 0:
    print("Tahun kabisat")
else:
    print("Bukan tahun kabisat")


print("\nSegitiga")
sisi1 = int(input("Masukkan sisi pertama: "))
sisi2 = int(input("Masukkan sisi kedua: "))
sisi3 = int(input("Masukkan sisi ketiga: "))
if sisi1==sisi2==sisi3:
    print("Segitiga sama sisi")
elif sisi1==sisi2!=sisi3 or sisi1!=sisi2==sisi3:
    print("Segitiga sama kaki")
else:
    print("Segitiga sembarang")

print("\nBMI")
berat_badan = float(input("Masukkan berat badan: "))
tinggi_badan = float(input("Masukkan tinggi badan dalam meter: "))
bmi = berat_badan/(tinggi_badan**2)
if bmi < 18.5:
    print("Kurus")
elif 18.5 <= bmi <= 24.9:
    print("Normal")
elif 25 <= bmi <=29.9:
    print("Gemuk")
else:
    print("Obesitas")