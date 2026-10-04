class Karyawan:
    def __init__(self, nama, nip, posisi):
        self.nama = nama
        self.nip = nip
        self.posisi = posisi

    @property
    def info_singkat(self):
        return f"{self.nama} ({self.posisi}) - NIP: {self.nip}"
    def __str__(self):
        return f"Karyawan: {self.nama} | NIP: {self.nip} | Posisi: {self.posisi}"

class Bank:
    def __init__(self, nama_bank, kode):
        self.nama_bank = nama_bank
        self.kode = kode
        self._karyawan = [] # Agregasi: menampung referensi objek Karyawan dari luar
        
    def tambah_karyawan(self, karyawan):
        """Karyawan dibuat di luar dan didaftarkan ke dalam bank."""
        if isinstance(karyawan, Karyawan):
            self._karyawan.append(karyawan)
            print(f" [+] {karyawan.nama} mulai bekerja di {self.nama_bank}")
            
    def keluarkan_karyawan(self, nip):
        """Melepas referensi karyawan tanpa memusnahkan objek karyawan
        aslinya."""
        awal = len(self._karyawan)
        self._karyawan = [k for k in self._karyawan if k.nip != nip]
        if len(self._karyawan) < awal:
            print(f" [-] Karyawan dengan NIP {nip} telah berhenti dari {self.nama_bank}")
            
    @property
    def total_karyawan(self):
            return len(self._karyawan)
        
    def tampilkan_daftar_karyawan(self):
        print(f"\n Daftar Pegawai {self.nama_bank} (Kode: {self.kode})")
        print(f" Total: {self.total_karyawan} orang")
        
        for k in self._karyawan:
            print(f" - {k.info_singkat}")

# Objek Karyawan dibuat secara mandiri
teller = Karyawan("Andi Wijaya", "EMP01", "Teller")
manager = Karyawan("Dewi Lestari", "EMP02", "Branch Manager")
# Objek Bank menampung karyawan
bank_mandiri = Bank("Bank Nasional Mandiri", "BNM")
bank_mandiri.tambah_karyawan(teller)
bank_mandiri.tambah_karyawan(manager)
bank_mandiri.tampilkan_daftar_karyawan()
# Bukti siklus hidup agregasi: Bank dibubarkan
del bank_mandiri
# Objek karyawan tetap utuh di memori dan dapat bekerja di tempat lain
print(f"\n Data karyawan setelah entitas bank dihapus:")
print(f" {teller}")
print(f" {manager}")

class CatatanTransaksi:
    """Objek ini tidak memiliki arti mandiri tanpa rekening tempat mutasi
    terjadi."""
    
    def __init__(self, id_transaksi, tipe, nominal, keterangan):
        self.id_transaksi = id_transaksi
        self.tipe = tipe
        self.nominal = nominal
        self.keterangan = keterangan
    
    def __str__(self):
        simbol = "+" if self.tipe == "KREDIT" else "-"
        return f"[{self.id_transaksi}] {self.tipe:<6} {simbol}Rp{self.nominal:,} | Ket: {self.keterangan}"

class Rekening:
    """
    Rekening terdiri dari CatatanTransaksi.
    Catatan dibuat di dalam rekening dan musnah bersama rekening tersebut.
    """
    
    def __init__(self, nomor_rekening, nama_pemilik, saldo_awal=0):
        self.nomor_rekening = nomor_rekening
        self.nama_pemilik = nama_pemilik
        self.saldo = saldo_awal
        self._riwayat = []
        if saldo_awal > 0:
            self._buat_catatan("KREDIT", saldo_awal, "Setoran awal pembukaan rekening")
        
    def _buat_catatan(self, tipe, nominal, keterangan):
        """Objek bagian dibuat langsung di dalam induk."""
        id_baru = f"TRX-{len(self._riwayat) + 1:04d}"
        catatan = CatatanTransaksi(id_baru, tipe, nominal, keterangan)
        self._riwayat.append(catatan)
    
    def setor(self, nominal, keterangan="Setor tunai"):
        self.saldo += nominal
        self._buat_catatan("KREDIT", nominal, keterangan)
        print(f" Setoran Rp{nominal:,} berhasil dicatat.")
    
    def tarik(self, nominal, keterangan="Tarik tunai"):
        if nominal <= self.saldo:
            self.saldo -= nominal
            self._buat_catatan("DEBET", nominal, keterangan)
            print(f" Penarikan Rp{nominal:,} berhasil dicatat.")
        else:
            print(" Saldo tidak mencukupi untuk transaksi.")
    
    def cetak_rekening_koran(self):
        print(f"\n Rekening Koran: {self.nomor_rekening} an {self.nama_pemilik}")
        print(f" Saldo Akhir: Rp{self.saldo:,}")
        print(" Riwayat Mutasi Transaksi:")
        for trx in self._riwayat:
            print(f" {trx}")

# Pembuatan objek induk secara otomatis merakit bagian-bagian internalnya
tabungan = Rekening("554-900-112", "Rina Marlina", 2000000)
tabungan.setor(500000, "Transfer masuk dari klien")
tabungan.tarik(300000, "Pembayaran listrik")
tabungan.cetak_rekening_koran()
# Bukti komposisi: Ketika rekening ditutup dan dihapus
del tabungan
# Riwayat CatatanTransaksi ikut terhapus karena berada di dalam instance rekening tersebut.