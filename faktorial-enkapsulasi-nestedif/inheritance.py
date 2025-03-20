class Kendaraan:
    def __init__(self, merk, tahun_produksi):
        self.merk = merk
        self.tahun_produksi = tahun_produksi

    def info(self):
        print(f"Merk\t\t\t: {self.merk}\nTahun Produksi\t\t: {self.tahun_produksi}")

class Mobil(Kendaraan):
    def __init__(self, merk, tahun_produksi, jumlah_roda, jenis_bahan_bakar):
        super().__init__(merk, tahun_produksi)
        self.jumlah_roda = jumlah_roda
        self.jenis_bahan_bakar = jenis_bahan_bakar
    
    def info(self):
        super().info()
        print(f"Jumlah roda\t\t: {self.jumlah_roda}\nJenis bahan bakar\t: {self.jenis_bahan_bakar}")

class sepedaMotor(Kendaraan):
    def __init__(self, merk, tahun_produksi, kapasitas_mesin):
        super().__init__(merk, tahun_produksi)
        self.kapasitas_mesin = kapasitas_mesin
    
    def info(self):
        super().info()
        print(f"Kapasitas mesin\t\t: {self.kapasitas_mesin}")


class Truk(Mobil):
    def __init__(self, merk, tahun_produksi, jumlah_roda, jenis_bahan_bakar, kapasitas_muatan):
        super().__init__(merk, tahun_produksi, jumlah_roda, jenis_bahan_bakar)
        self.kapasitas_muatan = kapasitas_muatan

    def info(self):
        super().info()
        

    def muat_barang(self):
        berat = int(input("Berat barang (kg)\t: "))
        muatan = "Kapasitas"
        if berat <= self.kapasitas_muatan:
            print(f"{muatan}\t\t: Cukup")
        else:
            print(f"{muatan}\t\t: Melebihi")

mobil = Mobil("Ferrari",2030,4,"Pertamax")
motor = sepedaMotor("Ducati",2030,"15000 CC")
truk = Truk("Fuso", 2025, 8, "Solar", 1000)
print("\n","="*10,"Mobil","="*10)
mobil.info()
print("\n","="*10,"Motor","="*10)
motor.info()
print("\n","="*10,"Truk","="*10)
truk.info()
truk.muat_barang()