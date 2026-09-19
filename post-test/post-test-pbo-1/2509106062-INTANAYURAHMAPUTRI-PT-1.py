class Produk:
    nama_toko = "Aye's Beauty Store"
    total_produk_terdaftar = 0
    kategori_tersedia = ["Skincare", "Makeup", "Haircare"]

    def __init__(self, nama, brand, kategori, harga, stok):
        self.nama = nama
        self.brand = brand
        self.kategori = kategori

        self.__harga = 0
        self.__stok = 0
        self.harga = harga
        self.stok = stok

        Produk.total_produk_terdaftar += 1

    def tampilkan_info(self):
        print(f"  > {self.nama} ({self.brand}) - {self.kategori}")
        print(f"      Harga : Rp{self.__harga:,.0f}")
        print(f"      Stok  : {self.__stok} unit")

    def kurangi_stok(self, jumlah):
        if jumlah <= 0:
            print(f"  [GAGAL] Kurangi stok {self.nama}: jumlah tidak valid.")
            return False
        if jumlah > self.__stok:
            print(f"  [GAGAL] Stok {self.nama} tidak mencukupi (sisa {self.__stok}).")
            return False
        self.__stok -= jumlah
        print(f"  [BERHASIL] Stok {self.nama} berkurang {jumlah}, sisa {self.__stok}.")
        return True

    @classmethod
    def dari_dict(cls, data):
        return cls(
            data["nama"],
            data["brand"],
            data["kategori"],
            data["harga"],
            data["stok"],
        )

    @classmethod
    def ubah_nama_toko(cls, nama_baru):
        cls.nama_toko = nama_baru
        print(f"  [BERHASIL] Nama toko diperbarui menjadi: {cls.nama_toko}")

    @staticmethod
    def validasi_nama_produk(nama):
        return isinstance(nama, str) and len(nama.strip()) >= 3

    @property
    def harga(self):
        return self.__harga

    @harga.setter
    def harga(self, nilai_baru):
        if not isinstance(nilai_baru, (int, float)) or nilai_baru <= 0:
            print(f"  [DITOLAK] Harga '{nilai_baru}' tidak valid, harga tidak diubah.")
            return
        self.__harga = nilai_baru

    @property
    def stok(self):
        return self.__stok

    @stok.setter
    def stok(self, nilai_baru):
        if not isinstance(nilai_baru, int) or nilai_baru < 0:
            print(f"  [DITOLAK] Stok '{nilai_baru}' tidak valid, stok tidak diubah.")
            return
        self.__stok = nilai_baru


class Pengguna:
    nama_platform = "Aye's POS System"
    total_pengguna = 0
    role_tersedia = ["Admin", "Pelanggan"]

    def __init__(self, id_pengguna, nama, role, password):
        self.id_pengguna = id_pengguna
        self.nama = nama
        self.role = role

        self.__password = None
        self.password = password

        Pengguna.total_pengguna += 1

    def tampilkan_profil(self):
        print(f"  > [{self.id_pengguna}] {self.nama} - Role: {self.role}")
        print(f"      Password : {'*' * len(self.__password)}")

    @classmethod
    def registrasi(cls, id_pengguna, nama, role, password):
        if not cls.validasi_password(password):
            print("  [GAGAL] Pengguna tidak dapat didaftarkan.")
            return None

        pengguna_baru = cls(id_pengguna, nama, role, password)
        print(f"  [BERHASIL] Pengguna baru terdaftar: {nama} ({role})")
        return pengguna_baru

    @classmethod
    def info_platform(cls):
        print(f"  Platform      : {cls.nama_platform}")
        print(f"  Total pengguna: {cls.total_pengguna}")

    @staticmethod
    def validasi_password(password):
        return isinstance(password, str) and len(password) >= 6

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password_baru):
        if not Pengguna.validasi_password(password_baru):
            print("  [DITOLAK] Password minimal 6 karakter, password tidak diubah.")
            return
        self.__password = password_baru


class Transaksi:
    nama_toko = "Aye's Beauty Store"
    total_transaksi = 0
    mata_uang = "IDR"

    def __init__(self, nomor_transaksi, pengguna: Pengguna, produk: Produk, jumlah):
        self.nomor_transaksi = nomor_transaksi
        self.pengguna = pengguna
        self.produk = produk
        self.jumlah = jumlah

        self.__total_harga = 0

        Transaksi.total_transaksi += 1

    def proses_transaksi(self):
        if not Transaksi.validasi_jumlah(self.jumlah):
            print(f"  [GAGAL] Transaksi {self.nomor_transaksi}: jumlah tidak valid.")
            return False

        berhasil = self.produk.kurangi_stok(self.jumlah)
        if not berhasil:
            print(f"  [DIBATALKAN] Transaksi {self.nomor_transaksi}.")
            return False

        self.total_harga = self.produk.harga * self.jumlah
        print(
            f"  [BERHASIL] Transaksi {self.nomor_transaksi}: "
            f"{self.pengguna.nama} membeli {self.jumlah}x {self.produk.nama} "
            f"= {Transaksi.mata_uang} {self.total_harga:,.0f}"
        )
        return True

    @classmethod
    def buat_transaksi_cepat(cls, pengguna, produk, jumlah):
        nomor_otomatis = f"T{cls.total_transaksi + 1:04d}"
        return cls(nomor_otomatis, pengguna, produk, jumlah)

    @staticmethod
    def validasi_jumlah(jumlah):
        return isinstance(jumlah, int) and jumlah > 0

    @property
    def total_harga(self):
        return self.__total_harga

    @total_harga.setter
    def total_harga(self, nilai_baru):
        if not isinstance(nilai_baru, (int, float)) or nilai_baru < 0:
            print("  [DITOLAK] total_harga tidak valid, nilai tidak diubah.")
            return
        self.__total_harga = nilai_baru


def cetak_judul(judul):
    print()
    print("=" * 70)
    print(judul)
    print("=" * 70)


def cetak_subjudul(subjudul):
    print()
    print(f"{subjudul}")


if __name__ == "__main__":

    cetak_judul("1. CLASS PRODUK")

    cetak_subjudul("1.1 Membuat objek")
    produk1 = Produk("Facial Wash Aloe Vera", "Somethinc", "Skincare", 45000, 50)
    produk2 = Produk.dari_dict({
        "nama": "Matte Lip Cream",
        "brand": "Emina",
        "kategori": "Makeup",
        "harga": 35000,
        "stok": 30,
    })
    produk1.tampilkan_info()
    produk2.tampilkan_info()

    cetak_subjudul("1.2 Atribut kelas & class method")
    print(f"  Total produk terdaftar : {Produk.total_produk_terdaftar}")
    Produk.ubah_nama_toko("Aye's Beauty Store - Cabang Samarinda")

    cetak_subjudul("1.3 Static method: validasi_nama_produk")
    print("  'Facial Wash' ->", Produk.validasi_nama_produk("Facial Wash"))
    print("  ''            ->", Produk.validasi_nama_produk(""))

    cetak_subjudul("1.4 Setter harga")
    produk1.harga = 47000
    produk1.harga = -1000
    print("  Harga produk1 sekarang:", produk1.harga)

    cetak_subjudul("1.5 Setter stok")
    produk2.stok = 25
    produk2.stok = -5
    print("  Stok produk2 sekarang:", produk2.stok)
    print()

    cetak_judul("2. CLASS PENGGUNA")

    cetak_subjudul("2.1 Membuat objek")
    admin1 = Pengguna("U001", "Aya", "Admin", "admin123")
    pelanggan1 = Pengguna.registrasi("U002", "Julpa", "Pelanggan", "julpa123")
    admin1.tampilkan_profil()
    pelanggan1.tampilkan_profil()

    cetak_subjudul("2.2 Class method: info_platform")
    Pengguna.info_platform()

    cetak_subjudul("2.3 Static method: validasi_password")
    print("  'abc'    ->", Pengguna.validasi_password("abc"))
    print("  'abc123' ->", Pengguna.validasi_password("abc123"))

    cetak_subjudul("2.4 Setter password")
    pelanggan1.password = "sandiBaru99"
    pelanggan1.password = "123"
    pelanggan1.tampilkan_profil()
    print()

    cetak_judul("3. CLASS TRANSAKSI")

    cetak_subjudul("3.1 Membuat objek")
    transaksi1 = Transaksi("T0001", pelanggan1, produk1, 2)
    transaksi2 = Transaksi.buat_transaksi_cepat(admin1, produk2, 5)
    transaksi1.proses_transaksi()
    transaksi2.proses_transaksi()
    print(f"  Total transaksi tercatat: {Transaksi.total_transaksi}")

    cetak_subjudul("3.2 Static method: validasi_jumlah")
    print("  Jumlah 3  ->", Transaksi.validasi_jumlah(3))
    print("  Jumlah -2 ->", Transaksi.validasi_jumlah(-2))

    cetak_subjudul("3.3 Transaksi dengan jumlah melebihi stok")
    transaksi3 = Transaksi("T0003", pelanggan1, produk1, 999)
    transaksi3.proses_transaksi()

    cetak_subjudul("3.4 Setter total_harga")
    transaksi1.total_harga = 100000
    transaksi1.total_harga = -500
    print("  Total harga transaksi1 sekarang:", transaksi1.total_harga)