# Sistem Manajemen Penjualan Toko Kecantikan

## Deskripsi

Program ini mensimulasikan sistem penjualan sederhana di toko kecantikan
**Aye's Beauty Store**. Terdapat tiga class utama yang berdiri sendiri
namun saling berinteraksi:

| Class | Peran |
|---|---|
| `Produk` | Menyimpan data produk (nama, brand, kategori, harga, stok) |
| `Pengguna` | Menyimpan data pengguna sistem (admin/pelanggan) |
| `Transaksi` | Mencatat transaksi penjualan, menghubungkan objek `Produk` dan `Pengguna` |

## Struktur Class

### 1. `Produk`
- **Atribut kelas:** `nama_toko`, `total_produk_terdaftar`, `kategori_tersedia`
- **Atribut instance publik:** `nama`, `brand`, `kategori`
- **Atribut instance privat:** `__harga`, `__stok`
- **Instance method:** `tampilkan_info()`, `kurangi_stok(jumlah)`
- **Class method:** `dari_dict(data)` (factory), `ubah_nama_toko(nama_baru)`
- **Static method:** `validasi_nama_produk(nama)`
- **Property:** `harga` (validasi harus angka > 0), `stok` (validasi harus integer ≥ 0)

### 2. `Pengguna`
- **Atribut kelas:** `nama_platform`, `total_pengguna`, `role_tersedia`
- **Atribut instance publik:** `id_pengguna`, `nama`, `role`
- **Atribut instance privat:** `__password`
- **Instance method:** `tampilkan_profil()` (password ditampilkan tersamar `*`)
- **Class method:** `registrasi(...)` (factory), `info_platform()`
- **Static method:** `validasi_password(password)`
- **Property:** `password` (validasi minimal 6 karakter)

### 3. `Transaksi`
- **Atribut kelas:** `nama_toko`, `total_transaksi`, `mata_uang`
- **Atribut instance publik:** `nomor_transaksi`, `pengguna` (objek `Pengguna`), `produk` (objek `Produk`), `jumlah`
- **Atribut instance privat:** `__total_harga`
- **Instance method:** `proses_transaksi()` — memvalidasi jumlah, memanggil `produk.kurangi_stok()`, dan menghitung total harga transaksi jika transaksi berhasil
- **Class method:** `buat_transaksi_cepat(...)` (factory dengan nomor transaksi otomatis berformat T diikuti 4 digit angka)
- **Static method:** `validasi_jumlah(jumlah)`
- **Property:** `total_harga` (validasi harus angka ≥ 0)

### Fungsi bantuan tampilan
- `cetak_judul(judul)` dan `cetak_subjudul(subjudul)` — hanya untuk merapikan
  output di terminal saat program dijalankan, bukan bagian dari class OOP di atas.

## Panduan Pengujian

Bagian `if __name__ == "__main__":` pada `main.py` memuat demonstrasi
lengkap, dibagi menjadi 3 bagian besar (tiap bagian punya beberapa
sub-pengujian bernomor):

**1. CLASS PRODUK**
   - 1.1 Membuat 2 objek `Produk`: `produk1` langsung lewat `__init__`,
     `produk2` lewat factory method `dari_dict`, lalu memanggil
     `tampilkan_info()` (instance method).
   - 1.2 Menampilkan atribut kelas `total_produk_terdaftar` dan memanggil
     class method `ubah_nama_toko()`.
   - 1.3 Menguji static method `validasi_nama_produk()`.
   - 1.4–1.5 Menguji setter `harga` dan `stok` dengan nilai valid lalu
     nilai tidak valid (negatif) — nilai tidak valid harus ditolak
     dengan pesan `[DITOLAK]` dan nilai lama tetap dipertahankan.

**2. CLASS PENGGUNA**
   - 2.1 Membuat 2 objek `Pengguna`: `admin1` langsung, `pelanggan1`
     lewat factory method `registrasi()`, lalu memanggil
     `tampilkan_profil()`.
   - 2.2 Memanggil class method `info_platform()`.
   - 2.3 Menguji static method `validasi_password()`.
   - 2.4 Menguji setter `password` dengan nilai valid (≥6 karakter) lalu
     nilai tidak valid (`123`, harus ditolak).

**3. CLASS TRANSAKSI**
   - 3.1 Membuat 2 objek `Transaksi` yang memakai objek `Produk` dan
     `Pengguna` dari bagian sebelumnya (`transaksi1` langsung,
     `transaksi2` lewat factory method `buat_transaksi_cepat()`), lalu
     memanggil `proses_transaksi()`.
   - 3.2 Menguji static method `validasi_jumlah()`.
   - 3.3 Menguji transaksi dengan jumlah melebihi stok yang tersedia —
     harus gagal/dibatalkan (pesan `[GAGAL]` dan `[DIBATALKAN]`).
   - 3.4 Menguji setter `total_harga` langsung dengan nilai valid lalu
     nilai tidak valid (negatif).