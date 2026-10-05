# Posttest 2 PBO - Relasi UML dan Inheritance

- Nama : Intan Ayu Rahma Putri
- NIM : 2509106062
- Kelas : B1 '25

## Tentang Program

Program ini adalah sistem penjualan untuk toko kecantikan bernama Aye's Beauty Store, dibuat dengan Python dan dijalankan lewat terminal. Menu yang ada di program ini ada 4, yaitu kelola produk (tambah, edit harga dan stok, hapus), transaksi (pembelian, pembayaran, riwayat), lihat daftar produk, dan informasi toko.

Produk yang dijual dibagi jadi dua kategori, Skincare dan Makeup. Class yang saya pakai:

- `Produk` sebagai superclass, turunannya `Skincare` dan `Makeup`
- `Transaksi` sebagai superclass, turunannya `Pembelian` dan `Pembayaran`
- `DetailPembelian` untuk rincian dari satu pembelian
- `Toko` untuk menyimpan daftar produk

## Relasi UML

### Asosiasi

Asosiasi adalah hubungan antar class di mana satu class memakai objek dari class lain, tapi kedua objeknya tetap berdiri sendiri. Di program ini asosiasi ada dua.

Pertama, class `Transaksi` memakai objek `Produk`. Produknya dibuat lebih dulu lewat menu kelola produk, lalu dikirim ke transaksi saat ada pembelian.

```python
class Transaksi:
    def __init__(self, nomor_transaksi, produk: Produk, jumlah):
        self._nomor_transaksi = nomor_transaksi
        self._produk = produk
        self._jumlah = jumlah
        self.__total_harga = 0
```

Kedua, class `Pembayaran` memakai objek `Pembelian`, karena setiap pembayaran pasti untuk satu pembelian. Makanya nomor pembayaran saya samakan dengan nomor pembelian yang dibayar.

```python
class Pembayaran(Transaksi):
    def __init__(self, pembelian: Pembelian, uang_dibayar):
        super().__init__(pembelian.nomor_transaksi, pembelian.produk, pembelian.jumlah)
        self._pembelian = pembelian
        self.uang_dibayar = uang_dibayar
```

### Agregasi

Agregasi juga hubungan "memiliki", tapi bagiannya tetap bisa ada walaupun pemiliknya tidak ada. Di program ini class `Toko` menyimpan kumpulan `Produk` di dalam sebuah list. Objek produk tidak dibuat di dalam `Toko`, tapi dibuat di luar lalu dimasukkan lewat method `tambah_produk()`.

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

### Komposisi

Kalau komposisi, hubungannya lebih kuat dari agregasi. Bagian yang dimiliki dibuat di dalam class pemiliknya dan tidak bisa berdiri sendiri. Contohnya di class `Pembelian`, objek `DetailPembelian` dibuat langsung di dalam `__init__`. Detail pembelian cuma ada kalau pembeliannya ada.

```python
class Pembelian(Transaksi):
    def __init__(self, nomor_transaksi, produk, jumlah, metode_pembayaran):
        super().__init__(nomor_transaksi, produk, jumlah)
        self.metode_pembayaran = metode_pembayaran
        self.__sudah_dibayar = False
        self.__detail = DetailPembelian(produk, jumlah)
```

## Inheritance

### Superclass dan Subclass

Ada dua superclass di program ini. `Produk` punya subclass `Skincare` dan `Makeup`. `Transaksi` punya subclass `Pembelian` dan `Pembayaran`.

### Penggunaan super()

Semua subclass memanggil konstruktor superclass-nya memakai `super().__init__(...)`, seperti di `Skincare` dan `Makeup` berikut.

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

`Pembelian` dan `Pembayaran` juga begitu, bisa dilihat di potongan kode bagian asosiasi dan komposisi di atas.

### Atribut Tambahan

Masing-masing subclass punya atribut sendiri yang tidak ada di class lain:

- `Skincare` punya `jenis_kulit`
- `Makeup` punya `warna`
- `Pembelian` punya `metode_pembayaran`
- `Pembayaran` punya `uang_dibayar`

### Method Overriding

Method `tampilkan_info()` milik `Produk` saya tulis ulang di `Skincare` dan `Makeup`. Di `Skincare` ada tambahan baris jenis kulit, di `Makeup` ada tambahan baris warna.

```python
class Skincare(Produk):
    def tampilkan_info(self):
        print(f"  > {self._nama} ({self._brand}) - {self._kategori}")
        print(f"      Harga : Rp{self.harga:,.0f} | Stok : {self.stok} unit")
        print(f"      Jenis Kulit : {self.jenis_kulit}")
```

Selain itu `proses_transaksi()` dan `tampilkan_riwayat()` dari `Transaksi` juga di-override di `Pembelian` dan `Pembayaran`. Di `Pembelian`, prosesnya menampilkan metode pembayaran dan detail pembelian. Di `Pembayaran`, prosesnya mengecek dulu apakah pembelian sudah lunas, lalu mengecek uangnya cukup atau tidak, baru menghitung kembalian.

### Protected dan Private

Atribut protected (pakai `_`) saya gunakan untuk data yang memang perlu dipakai langsung oleh subclass.

- Di `Produk`: `_nama`, `_brand`, dan `_kategori`, dipakai langsung di `tampilkan_info()` milik `Skincare` dan `Makeup`
- Di `Transaksi`: `_nomor_transaksi`, `_produk`, dan `_jumlah`, dipakai langsung di class `Pembayaran`

Atribut private (pakai `__`) saya gunakan untuk data yang tidak boleh diubah sembarangan dari luar superclass.

- Di `Produk`: `__harga` dan `__stok`, aksesnya lewat property `harga` dan `stok`
- Di `Transaksi`: `__total_harga`, aksesnya lewat property `total_harga`

Setter-nya diberi validasi, misalnya harga tidak boleh nol atau minus dan stok tidak boleh minus.

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