# Posttest 2 - Relasi UML dan Inheritance

| | |
|---|---|
| **Nama** | Intan Ayu Rahma Putri |
| **NIM** | 2509106062 |
| **Kelas** | B1 '25 |
| **Program** | Sistem Penjualan Toko Kecantikan (Aye's Beauty Store) |
| **File program** | `posttest2_toko_kecantikan.py` |

## Deskripsi Program

Program berbasis CLI (Python) untuk mengelola penjualan toko kecantikan. Program memiliki empat menu utama:

1. **Kelola Produk**: tambah, edit (harga dan stok), dan hapus produk Skincare atau Makeup.
2. **Transaksi**: membuat pembelian, membayar pembelian (dengan perhitungan kembalian), dan melihat riwayat transaksi.
3. **Lihat Daftar Produk**: menampilkan seluruh produk yang tersimpan di toko.
4. **Informasi Toko**: menampilkan nama toko, total produk, total transaksi, kategori produk, dan mengubah nama toko.

## Daftar Class

| Class | Peran |
|---|---|
| `Produk` | Superclass untuk semua produk |
| `Skincare`, `Makeup` | Subclass dari `Produk` |
| `Transaksi` | Superclass untuk semua transaksi |
| `Pembelian`, `Pembayaran` | Subclass dari `Transaksi` |
| `DetailPembelian` | Rincian pembelian, bagian dari `Pembelian` |
| `Toko` | Pengelola kumpulan produk |

## 1. Relasi UML

### a. Asosiasi

Asosiasi adalah hubungan antar class di mana satu objek memakai objek lain, tetapi masing-masing tetap berdiri sendiri. Pada program ini ada dua asosiasi:

- `Transaksi` berasosiasi dengan `Produk`. Objek `Produk` dibuat di luar, lalu dipakai oleh transaksi.
- `Pembayaran` berasosiasi dengan `Pembelian`. Objek `Pembelian` yang sudah ada dipakai untuk diproses pembayarannya.

```python
class Transaksi:
    def __init__(self, nomor_transaksi, produk: Produk, jumlah):
        self._nomor_transaksi = nomor_transaksi
        self._produk = produk
        self._jumlah = jumlah
        self.__total_harga = 0
```

```python
class Pembayaran(Transaksi):
    def __init__(self, nomor_transaksi, pembelian: Pembelian, uang_dibayar):
        super().__init__(nomor_transaksi, pembelian.produk, pembelian.jumlah)
        self._pembelian = pembelian
        self.uang_dibayar = uang_dibayar
```

### b. Agregasi

Agregasi adalah hubungan "memiliki" yang longgar: objek bagian dibuat di luar dan tetap ada walaupun objek pemiliknya hilang. Class `Toko` menyimpan daftar `Produk`. Produk dibuat terlebih dahulu di menu Kelola Produk, lalu ditambahkan ke `Toko`. Produk bukan bagian yang lahir dan mati bersama `Toko`.

```python
class Toko:
    def __init__(self):
        self.__produk = []

    def tambah_produk(self, produk):
        self.__produk.append(produk)

    def hapus_produk(self, produk):
        if produk in self.__produk:
            self.__produk.remove(produk)
            Produk.total_produk_terdaftar -= 1
```

### c. Komposisi

Komposisi adalah hubungan "memiliki" yang kuat: objek bagian dibuat di dalam objek pemilik dan tidak punya arti tanpa pemiliknya. Class `Pembelian` membuat objek `DetailPembelian` sendiri di dalam `__init__`. Detail tersebut tidak dibuat di tempat lain, sehingga ikut hilang jika `Pembelian` hilang.

```python
class Pembelian(Transaksi):
    def __init__(self, nomor_transaksi, produk, jumlah, metode_pembayaran):
        super().__init__(nomor_transaksi, produk, jumlah)
        self.metode_pembayaran = metode_pembayaran
        self.__sudah_dibayar = False
        self.__detail = DetailPembelian(produk, jumlah)
```

### Ringkasan Relasi

| Relasi | Class yang terlibat | Letak di kode |
|---|---|---|
| Asosiasi | `Transaksi` dengan `Produk` | `Transaksi.__init__` |
| Asosiasi | `Pembayaran` dengan `Pembelian` | `Pembayaran.__init__` |
| Agregasi | `Toko` dengan `Produk` | `Toko.tambah_produk` |
| Komposisi | `Pembelian` dengan `DetailPembelian` | `Pembelian.__init__` |

## 2. Inheritance

### a. Superclass dan Subclass

| Superclass | Subclass |
|---|---|
| `Produk` | `Skincare`, `Makeup` |
| `Transaksi` | `Pembelian`, `Pembayaran` |

### b. Penggunaan `super().__init__(...)`

Setiap subclass memanggil konstruktor superclass-nya.

```python
class Skincare(Produk):
    def __init__(self, nama, brand, harga, stok, jenis_kulit):
        super().__init__(nama, brand, "Skincare", harga, stok)
        self.jenis_kulit = jenis_kulit
```

```python
class Makeup(Produk):
    def __init__(self, nama, brand, harga, stok, warna):
        super().__init__(nama, brand, "Makeup", harga, stok)
        self.warna = warna
```

`Pembelian` dan `Pembayaran` juga memanggil `super().__init__(...)` ke `Transaksi`, seperti pada potongan kode di bagian Asosiasi dan Komposisi.

### c. Atribut Tambahan (Unik)

| Subclass | Atribut unik |
|---|---|
| `Skincare` | `jenis_kulit` |
| `Makeup` | `warna` |
| `Pembelian` | `metode_pembayaran` |
| `Pembayaran` | `uang_dibayar` |

### d. Method Overriding

| Method di superclass | Di-override oleh | Perilaku yang berbeda |
|---|---|---|
| `Produk.tampilkan_info()` | `Skincare` | Menampilkan jenis kulit |
| `Produk.tampilkan_info()` | `Makeup` | Menampilkan warna |
| `Transaksi.proses_transaksi()` | `Pembelian` | Menampilkan metode pembayaran, memanggil `super()`, lalu mencetak detail pembelian |
| `Transaksi.proses_transaksi()` | `Pembayaran` | Mengecek status lunas dan uang yang dibayar, lalu menghitung kembalian |
| `Transaksi.tampilkan_riwayat()` | `Pembelian`, `Pembayaran` | Menambahkan status, uang dibayar, dan kembalian |

```python
class Skincare(Produk):
    def tampilkan_info(self):
        print(f"  > {self._nama} ({self._brand}) - {self._kategori}")
        print(f"      Harga : Rp{self.harga:,.0f} | Stok : {self.stok} unit")
        print(f"      Jenis Kulit : {self.jenis_kulit}")
```

### e. Tingkat Akses (Protected dan Private)

**Protected** dipakai pada data yang perlu diakses langsung oleh subclass.

| Superclass | Atribut protected | Dipakai langsung oleh |
|---|---|---|
| `Produk` | `_nama`, `_brand`, `_kategori` | `Skincare.tampilkan_info()`, `Makeup.tampilkan_info()` |
| `Transaksi` | `_nomor_transaksi`, `_produk`, `_jumlah` | `Pembayaran.proses_transaksi()`, `Pembayaran.tampilkan_riwayat()` |

**Private** dipakai pada data yang hanya boleh diubah lewat superclass, dan diakses subclass melalui getter dan setter (`@property`) yang memiliki validasi.

| Superclass | Atribut private | Akses dari luar |
|---|---|---|
| `Produk` | `__harga`, `__stok` | property `harga` dan `stok` |
| `Transaksi` | `__total_harga` | property `total_harga` |

```python
class Produk:
    def __init__(self, nama, brand, kategori, harga, stok):
        self._nama = nama
        self._brand = brand
        self._kategori = kategori
        self.__harga = 0
        self.__stok = 0
        self.harga = harga
        self.stok = stok
```