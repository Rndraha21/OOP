class Produk:
    def __init__(self, nama, harga, stok):
        self.nama = nama
        self._harga = harga
        self.__stok = stok
    
    def tampilkan(self):
        print(f'''Nama Barang: {self.nama}
Harga Barang: {self._harga}
Stok Barang: {self.__stok}''')

    def get_stok(self):
        return self.__stok
    
    def set_stok(self, jumlah):
        jumlah = int(input("Masukkan jumlah: "))
        self.__stok = jumlah

barang = Produk("Handphone", 1000000, "Available")
barang.tampilkan()
print(f"Stok barang yang private: {barang.get_stok()}")
barang.set_stok(())
print(f"Jumlah barang yang tersedia: {barang.get_stok()}")


class Pegawai:
    def __init__(self, nama, jabatan, gaji):
        self.nama = nama
        self._jabatan = jabatan
        self.__gaji = gaji
    
    def informasi_pegawai(self):
        print(f'''Nama: {self.nama}
Jabatan: {self._jabatan}
Gaji: {self.__gaji}''')
    
    def get_gaji(self):
        return self.__gaji
        
    def set_gaji(self, gaji):
        gaji = int(input("Masukkan Gaji: "))
        if gaji >= 3:
            self.__gaji = gaji
        else:
            print("Gaji Anda di bawah UMR")

pegawai = Pegawai("Robin", "CEO", 4)
pegawai.informasi_pegawai()
pegawai.set_gaji(4)
print(pegawai.get_gaji())

class RekeningBank:
    def __init__(self, saldo):
        self.__saldo = saldo

    def get_saldo(self):
        return self.__saldo

    def set_setoran(self):
        setoran = int(input("Setor: "))
        if setoran >= 0:
            self.__saldo += setoran 
            print(f"Berhasil di setor {setoran}. total saldo: {self.__saldo}")
        else:
            print("Silahkan setor dengan benar")
    
    def set_tarik(self):
        tarik = int(input("Tarik: "))
        if tarik >= 0 and tarik <= self.__saldo:  
            self.__saldo -= tarik 
            print(f"Berhasil di tarik {tarik}. Sisa saldo: {self.__saldo}")
        else:
            print("Silahkan tarik dengan benar atau saldo tidak cukup")

akun_bank = RekeningBank(20000000)
print(f"Jumlah saldo Anda: {akun_bank.get_saldo()}")
akun_bank.set_setoran()  
print(f"Jumlah saldo Anda setelah setor: {akun_bank.get_saldo()}")
akun_bank.set_tarik() 
print(f"Jumlah saldo Anda setelah tarik: {akun_bank.get_saldo()}")