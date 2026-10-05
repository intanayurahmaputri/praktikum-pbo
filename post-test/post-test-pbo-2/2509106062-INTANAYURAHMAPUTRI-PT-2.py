import os


class Produk:
    total_produk_terdaftar = 0
    kategori_tersedia = ["Skincare", "Makeup"]

    def __init__(self, nama, brand, kategori, harga, stok):
        self._nama = nama
        self._brand = brand
        self._kategori = kategori
        self.__harga = 0
        self.__stok = 0
        self.harga = harga
        self.stok = stok
        Produk.total_produk_terdaftar += 1

    def tampilkan_info(self):
        print(f"  > {self._nama} ({self._brand}) - {self._kategori}")
        print(f"      Harga : Rp{self.__harga:,.0f} | Stok : {self.__stok} unit")

    def kurangi_stok(self, jumlah):
        if jumlah <= 0:
            print("  [GAGAL] Jumlah tidak valid.")
            return False
        if jumlah > self.__stok:
            print(f"  [GAGAL] Stok {self._nama} tidak mencukupi (sisa {self.__stok}).")
            return False
        self.__stok -= jumlah
        print(f"  [BERHASIL] Stok {self._nama} berkurang {jumlah}, sisa {self.__stok}.")
        return True

    @staticmethod
    def validasi_nama_produk(nama):
        return isinstance(nama, str) and len(nama.strip()) >= 3

    @property
    def nama(self):
        return self._nama

    @property
    def brand(self):
        return self._brand

    @property
    def kategori(self):
        return self._kategori

    @property
    def harga(self):
        return self.__harga

    @harga.setter
    def harga(self, nilai_baru):
        if not isinstance(nilai_baru, (int, float)) or nilai_baru <= 0:
            print(f"  [DITOLAK] Harga '{nilai_baru}' tidak valid.")
            return
        self.__harga = nilai_baru

    @property
    def stok(self):
        return self.__stok

    @stok.setter
    def stok(self, nilai_baru):
        if not isinstance(nilai_baru, int) or nilai_baru < 0:
            print(f"  [DITOLAK] Stok '{nilai_baru}' tidak valid.")
            return
        self.__stok = nilai_baru


class Skincare(Produk):
    def __init__(self, nama, brand, harga, stok, jenis_kulit):
        super().__init__(nama, brand, "Skincare", harga, stok)
        self.jenis_kulit = jenis_kulit

    def tampilkan_info(self):
        print(f"  > {self._nama} ({self._brand}) - {self._kategori}")
        print(f"      Harga : Rp{self.harga:,.0f} | Stok : {self.stok} unit")
        print(f"      Jenis Kulit : {self.jenis_kulit}")


class Makeup(Produk):
    def __init__(self, nama, brand, harga, stok, warna):
        super().__init__(nama, brand, "Makeup", harga, stok)
        self.warna = warna

    def tampilkan_info(self):
        print(f"  > {self._nama} ({self._brand}) - {self._kategori}")
        print(f"      Harga : Rp{self.harga:,.0f} | Stok : {self.stok} unit")
        print(f"      Warna       : {self.warna}")


class DetailPembelian:
    def __init__(self, produk, jumlah):
        self.__nama_produk = produk.nama
        self.__harga_satuan = produk.harga
        self.__jumlah = jumlah
        self.__subtotal = self.__harga_satuan * jumlah

    @property
    def subtotal(self):
        return self.__subtotal

    def tampilkan_detail(self):
        print(f"      Produk       : {self.__nama_produk}")
        print(f"      Harga satuan : Rp{self.__harga_satuan:,.0f}")
        print(f"      Jumlah       : {self.__jumlah}")
        print(f"      Subtotal     : Rp{self.__subtotal:,.0f}")


class Transaksi:
    total_transaksi = 0
    mata_uang = "IDR"

    def __init__(self, nomor_transaksi, produk: Produk, jumlah):
        self._nomor_transaksi = nomor_transaksi
        self._produk = produk
        self._jumlah = jumlah
        self.__total_harga = 0

    def proses_transaksi(self):
        if not Transaksi.validasi_jumlah(self._jumlah):
            print(f"  [GAGAL] Transaksi {self._nomor_transaksi}: jumlah tidak valid.")
            return False

        if not self._produk.kurangi_stok(self._jumlah):
            print(f"  [DIBATALKAN] Transaksi {self._nomor_transaksi}.")
            return False

        self.total_harga = self._produk.harga * self._jumlah
        Transaksi.total_transaksi += 1
        print(f"  [BERHASIL] Transaksi {self._nomor_transaksi}")
        print(f"      Produk  : {self._produk.nama}")
        print(f"      Jumlah  : {self._jumlah}")
        print(f"      Total   : {Transaksi.mata_uang} {self.total_harga:,.0f}")
        return True

    def tampilkan_riwayat(self):
        print(f"\n  Nomor    : {self._nomor_transaksi}")
        print(f"  Produk   : {self._produk.nama}")
        print(f"  Jumlah   : {self._jumlah}")
        print(f"  Total    : {Transaksi.mata_uang} {self.total_harga:,.0f}")

    @staticmethod
    def validasi_jumlah(jumlah):
        return isinstance(jumlah, int) and jumlah > 0

    @property
    def nomor_transaksi(self):
        return self._nomor_transaksi

    @property
    def produk(self):
        return self._produk

    @property
    def jumlah(self):
        return self._jumlah

    @property
    def total_harga(self):
        return self.__total_harga

    @total_harga.setter
    def total_harga(self, nilai_baru):
        if not isinstance(nilai_baru, (int, float)) or nilai_baru < 0:
            print("  [DITOLAK] Total harga tidak valid.")
            return
        self.__total_harga = nilai_baru


class Pembelian(Transaksi):
    jumlah_pembelian = 0

    def __init__(self, nomor_transaksi, produk, jumlah, metode_pembayaran):
        super().__init__(nomor_transaksi, produk, jumlah)
        self.metode_pembayaran = metode_pembayaran
        self.__sudah_dibayar = False
        self.__detail = DetailPembelian(produk, jumlah)

    def proses_transaksi(self):
        print("\n  [PROSES PEMBELIAN]")
        print(f"  Metode Pembayaran : {self.metode_pembayaran}")
        berhasil = super().proses_transaksi()
        if berhasil:
            Pembelian.jumlah_pembelian += 1
            print("  Detail Pembelian:")
            self.__detail.tampilkan_detail()
        return berhasil

    def tandai_lunas(self):
        self.__sudah_dibayar = True

    @classmethod
    def buat_nomor(cls):
        return f"T{cls.jumlah_pembelian + 1:04d}"

    @property
    def sudah_dibayar(self):
        return self.__sudah_dibayar

    def tampilkan_riwayat(self):
        super().tampilkan_riwayat()
        status = "Lunas" if self.__sudah_dibayar else "Belum dibayar"
        print(f"  Metode   : {self.metode_pembayaran}")
        print(f"  Status   : {status}")


class Pembayaran(Transaksi):
    def __init__(self, pembelian: Pembelian, uang_dibayar):
        super().__init__(pembelian.nomor_transaksi, pembelian.produk, pembelian.jumlah)
        self._pembelian = pembelian
        self.uang_dibayar = uang_dibayar

    def proses_transaksi(self):
        print("\n  [PROSES PEMBAYARAN]")
        if self._pembelian.sudah_dibayar:
            print(f"  [GAGAL] Pembelian {self._pembelian.nomor_transaksi} sudah lunas.")
            return False

        total = self._pembelian.total_harga
        if self.uang_dibayar < total:
            print(f"  [GAGAL] Uang kurang Rp{total - self.uang_dibayar:,.0f}.")
            return False

        self.total_harga = total
        self._pembelian.tandai_lunas()
        Transaksi.total_transaksi += 1
        print(f"  [BERHASIL] Pembayaran {self._nomor_transaksi} dikonfirmasi")
        print(f"      Produk            : {self._produk.nama}")
        print(f"      Metode Pembayaran : {self._pembelian.metode_pembayaran}")
        print(f"      Total             : {Transaksi.mata_uang} {self.total_harga:,.0f}")
        print(f"      Uang dibayar      : {Transaksi.mata_uang} {self.uang_dibayar:,.0f}")
        print(f"      Kembalian         : {Transaksi.mata_uang} {self.kembalian:,.0f}")
        return True

    @property
    def kembalian(self):
        return self.uang_dibayar - self.total_harga

    def tampilkan_riwayat(self):
        super().tampilkan_riwayat()
        print(f"  Dibayar  : {Transaksi.mata_uang} {self.uang_dibayar:,.0f}")
        print(f"  Kembali  : {Transaksi.mata_uang} {self.kembalian:,.0f}")


class Toko:
    nama_toko = "Aye's Beauty Store"

    def __init__(self):
        self.__produk = []

    def tambah_produk(self, produk):
        self.__produk.append(produk)

    def hapus_produk(self, produk):
        if produk in self.__produk:
            self.__produk.remove(produk)
            Produk.total_produk_terdaftar -= 1

    def tampilkan_produk(self):
        if not self.__produk:
            print("\n  Belum ada produk.")
            return
        for nomor, produk in enumerate(self.__produk, 1):
            print(f"\n  Produk {nomor}")
            produk.tampilkan_info()

    @property
    def daftar_produk(self):
        return list(self.__produk)

    @classmethod
    def ubah_nama_toko(cls, nama_baru):
        cls.nama_toko = nama_baru
        print(f"  [BERHASIL] Nama toko diperbarui menjadi: {cls.nama_toko}")


def bersihkan_layar():
    os.system("cls" if os.name == "nt" else "clear")


def cetak_garis():
    print("=" * 70)


def cetak_tengah(teks, lebar=70):
    print(teks.center(lebar))


def cetak_judul(teks, lebar=70):
    cetak_garis()
    cetak_tengah(teks, lebar)
    cetak_garis()


def jeda():
    input("\n  Tekan enter untuk kembali...")


def input_harga():
    while True:
        try:
            harga = float(input("  Harga       : Rp"))
            if harga <= 0:
                print("  [GAGAL] Harga harus lebih dari 0.")
                continue
            return harga
        except ValueError:
            print("  [GAGAL] Masukkan angka yang valid.")


def input_stok():
    while True:
        try:
            stok = int(input("  Stok        : "))
            if stok < 0:
                print("  [GAGAL] Stok tidak boleh negatif.")
                continue
            return stok
        except ValueError:
            print("  [GAGAL] Masukkan angka yang valid.")


def input_jumlah():
    while True:
        try:
            jumlah = int(input("  Jumlah      : "))
            if not Transaksi.validasi_jumlah(jumlah):
                print("  [GAGAL] Jumlah harus lebih dari 0.")
                continue
            return jumlah
        except ValueError:
            print("  [GAGAL] Masukkan angka yang valid.")


def input_uang():
    while True:
        try:
            uang = float(input("  Uang dibayar : Rp"))
            if uang <= 0:
                print("  [GAGAL] Uang harus lebih dari 0.")
                continue
            return uang
        except ValueError:
            print("  [GAGAL] Masukkan angka yang valid.")


def pilih_produk(daftar_produk):
    if not daftar_produk:
        print("\n  Belum ada produk.")
        return None

    print()
    cetak_tengah("DAFTAR PRODUK")
    for nomor, produk in enumerate(daftar_produk, 1):
        print(f"  {nomor}. {produk.nama} ({produk.kategori}) - Rp{produk.harga:,.0f} | Stok {produk.stok}")

    while True:
        try:
            pilihan = int(input("\n  Pilih produk: "))
            if 1 <= pilihan <= len(daftar_produk):
                return daftar_produk[pilihan - 1]
            print("  [GAGAL] Pilihan tidak tersedia.")
        except ValueError:
            print("  [GAGAL] Masukkan angka.")


def menu_produk(toko):
    while True:
        bersihkan_layar()
        cetak_judul("KELOLA PRODUK")
        print("  1. Tambah Produk")
        print("  2. Edit Produk")
        print("  3. Hapus Produk")
        print("  0. Kembali")

        pilihan = input("\n  Pilih menu: ")

        if pilihan == "1":
            print()
            cetak_tengah("TAMBAH PRODUK")
            print("  1. Skincare")
            print("  2. Makeup")
            kategori = input("\n  Pilih kategori: ")

            if kategori not in ("1", "2"):
                print("  [GAGAL] Kategori tidak tersedia.")
                jeda()
                continue

            nama = input("  Nama produk : ")
            if not Produk.validasi_nama_produk(nama):
                print("  [GAGAL] Nama produk minimal 3 karakter.")
                jeda()
                continue

            brand = input("  Brand       : ")
            harga = input_harga()
            stok = input_stok()

            if kategori == "1":
                jenis_kulit = input("  Jenis kulit : ")
                produk = Skincare(nama, brand, harga, stok, jenis_kulit)
            else:
                warna = input("  Warna       : ")
                produk = Makeup(nama, brand, harga, stok, warna)

            toko.tambah_produk(produk)
            print("\n  [BERHASIL] Produk berhasil ditambahkan.")
            jeda()

        elif pilihan == "2":
            produk = pilih_produk(toko.daftar_produk)
            if produk is None:
                jeda()
                continue

            while True:
                bersihkan_layar()
                cetak_judul("EDIT PRODUK")
                produk.tampilkan_info()
                print("\n  1. Edit Harga")
                print("  2. Edit Stok")
                print("  0. Selesai")
                pilihan_edit = input("\n  Pilih menu: ")
                if pilihan_edit == "1":
                    produk.harga = input_harga()
                    print(f"  [BERHASIL] Harga {produk.nama} menjadi Rp{produk.harga:,.0f}.")
                    jeda()
                elif pilihan_edit == "2":
                    produk.stok = input_stok()
                    print(f"  [BERHASIL] Stok {produk.nama} menjadi {produk.stok} unit.")
                    jeda()
                elif pilihan_edit == "0":
                    break
                else:
                    print("  [GAGAL] Menu tidak tersedia.")
                    jeda()

        elif pilihan == "3":
            produk = pilih_produk(toko.daftar_produk)
            if produk is None:
                jeda()
                continue
            print(f"\n  Apakah yakin ingin menghapus {produk.nama}?")
            konfirmasi = input("  Ketik 'y' untuk menghapus: ")
            if konfirmasi.lower() == "y":
                nama_produk = produk.nama
                toko.hapus_produk(produk)
                print(f"  [BERHASIL] {nama_produk} berhasil dihapus.")
            else:
                print("  [DIBATALKAN] Produk tidak dihapus.")
            jeda()

        elif pilihan == "0":
            break
        else:
            print("  [GAGAL] Menu tidak tersedia.")
            jeda()


def menu_transaksi(toko, daftar_pembelian, daftar_pembayaran):
    while True:
        bersihkan_layar()
        cetak_judul("TRANSAKSI")
        print("  1. Pembelian")
        print("  2. Pembayaran")
        print("  3. Lihat Riwayat Transaksi")
        print("  0. Kembali")
        pilihan = input("\n  Pilih menu: ")

        if pilihan == "1":
            produk = pilih_produk(toko.daftar_produk)
            if produk is None:
                jeda()
                continue

            jumlah = input_jumlah()
            metode_pembayaran = input("  Metode pembayaran (Tunai/Transfer/E-Wallet): ")
            transaksi = Pembelian(Pembelian.buat_nomor(), produk, jumlah, metode_pembayaran)

            if transaksi.proses_transaksi():
                daftar_pembelian.append(transaksi)
            jeda()

        elif pilihan == "2":
            belum_lunas = [p for p in daftar_pembelian if not p.sudah_dibayar]
            if not belum_lunas:
                print("\n  Tidak ada pembelian yang perlu dibayar.")
                jeda()
                continue

            print()
            cetak_tengah("PEMBELIAN BELUM DIBAYAR")
            for nomor, pembelian in enumerate(belum_lunas, 1):
                print(f"  {nomor}. {pembelian.nomor_transaksi} - {pembelian.produk.nama} - Rp{pembelian.total_harga:,.0f}")

            while True:
                try:
                    pilihan_pembelian = int(input("\n  Pilih pembelian: "))
                    if 1 <= pilihan_pembelian <= len(belum_lunas):
                        pembelian_dipilih = belum_lunas[pilihan_pembelian - 1]
                        break
                    print("  [GAGAL] Pilihan tidak tersedia.")
                except ValueError:
                    print("  [GAGAL] Masukkan angka.")

            uang = input_uang()
            pembayaran = Pembayaran(pembelian_dipilih, uang)
            if pembayaran.proses_transaksi():
                daftar_pembayaran.append(pembayaran)
            jeda()

        elif pilihan == "3":
            print()
            cetak_judul("RIWAYAT TRANSAKSI")
            if not daftar_pembelian and not daftar_pembayaran:
                print("  Belum ada transaksi.")
            else:
                print()
                cetak_tengah("--- PEMBELIAN ---")
                for transaksi in daftar_pembelian:
                    transaksi.tampilkan_riwayat()
                print()
                cetak_tengah("--- PEMBAYARAN ---")
                for transaksi in daftar_pembayaran:
                    transaksi.tampilkan_riwayat()
            jeda()

        elif pilihan == "0":
            break
        else:
            print("  [GAGAL] Menu tidak tersedia.")
            jeda()


def menu_informasi():
    while True:
        bersihkan_layar()
        cetak_judul("INFORMASI TOKO")
        print(f"  Nama toko       : {Toko.nama_toko}")
        print(f"  Total produk    : {Produk.total_produk_terdaftar}")
        print(f"  Total transaksi : {Transaksi.total_transaksi}")
        print("\n  Kategori produk:")

        for kategori in Produk.kategori_tersedia:
            print(f"  - {kategori}")

        print("\n  1. Ubah Nama Toko")
        print("  0. Kembali")
        pilihan = input("\n  Pilih menu: ")

        if pilihan == "1":
            nama_baru = input("  Nama toko baru: ")
            if nama_baru.strip():
                Toko.ubah_nama_toko(nama_baru)
            else:
                print("  [GAGAL] Nama toko tidak boleh kosong.")
            jeda()
        elif pilihan == "0":
            break
        else:
            print("  [GAGAL] Menu tidak tersedia.")
            jeda()


def main():
    toko = Toko()
    daftar_pembelian = []
    daftar_pembayaran = []

    while True:
        bersihkan_layar()
        print()
        cetak_judul("SISTEM PENJUALAN TOKO KECANTIKAN 💄", 69)
        print("  1. Kelola Produk")
        print("  2. Transaksi")
        print("  3. Lihat Daftar Produk")
        print("  4. Informasi Toko")
        print("  0. Keluar")
        pilihan = input("\n  Pilih menu: ")

        if pilihan == "1":
            menu_produk(toko)
        elif pilihan == "2":
            menu_transaksi(toko, daftar_pembelian, daftar_pembayaran)
        elif pilihan == "3":
            bersihkan_layar()
            toko.tampilkan_produk()
            jeda()
        elif pilihan == "4":
            menu_informasi()
        elif pilihan == "0":
            bersihkan_layar()
            print("Terima kasih telah menggunakan sistem ini! (˶ᵔ ᵕ ᵔ˶)")
            break
        else:
            print("\n  [GAGAL] Menu tidak tersedia.")
            jeda()


main()