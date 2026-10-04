# Posttest 2 - Relasi UML dan Inheritance

| Keterangan   | Detail                                                |
| ------------ | ----------------------------------------------------- |
| Nama         | Intan Ayu Rahma Putri                                 |
| NIM          | 2509106062                                            |
| Kelas        | B1 '25                                                |
| Program      | Sistem Penjualan Toko Kecantikan (Aye's Beauty Store) |
| File Program | `2509106062-INTANAYURAHMAPUTRI-PT-2.py`               |

## Deskripsi Program

Aye's Beauty Store adalah program berbasis CLI menggunakan Python yang dibuat untuk mengelola produk dan transaksi pada toko kecantikan.

Program memiliki beberapa menu utama, yaitu:

1. Kelola Produk, untuk menambah, mengedit, dan menghapus produk.
2. Transaksi, untuk melakukan pembelian, pembayaran, dan melihat riwayat transaksi.
3. Lihat Daftar Produk, untuk melihat semua produk yang tersedia.
4. Informasi Toko, untuk melihat informasi toko dan mengubah nama toko.

Program ini dibuat menggunakan konsep OOP, seperti inheritance, encapsulation, polymorphism, dan abstraction. Selain itu, terdapat beberapa relasi antarclass yang dapat digambarkan menggunakan UML.

## Daftar Class

| Class             | Peran                                 |
| ----------------- | ------------------------------------- |
| `Produk`          | Class induk untuk produk              |
| `Skincare`        | Subclass dari `Produk`                |
| `Makeup`          | Subclass dari `Produk`                |
| `DetailPembelian` | Menyimpan detail dari suatu pembelian |
| `Transaksi`       | Class induk untuk transaksi           |
| `Pembelian`       | Subclass dari `Transaksi`             |
| `Pembayaran`      | Subclass dari `Transaksi`             |
| `Toko`            | Mengelola daftar produk               |

## 1. Relasi UML

Pada program ini terdapat tiga jenis relasi UML, yaitu asosiasi, agregasi, dan komposisi.

### a. Asosiasi

Asosiasi merupakan hubungan antara dua class yang saling menggunakan atau berinteraksi, tetapi objek dari kedua class tetap dapat berdiri sendiri.

Pada program ini terdapat asosiasi antara `Transaksi` dengan `Produk`.

Pada class `Transaksi`, objek produk diterima sebagai parameter dan disimpan ke dalam atribut `_produk`.

```python
class Transaksi:
    def __init__(self, nomor_transaksi, produk: Produk, jumlah):
        self._nomor_transaksi = nomor_transaksi
        self._produk = produk
        self._jumlah = jumlah
        self.__total_harga = 0
```

Objek `Produk` dibuat terlebih dahulu melalui class `Skincare` atau `Makeup`, kemudian digunakan oleh `Transaksi`.

Selain itu, terdapat asosiasi antara `Pembayaran` dengan `Pembelian`. Class `Pembayaran` menerima objek `Pembelian` sebagai parameter.

```python
class Pembayaran(Transaksi):
    def __init__(self, nomor_transaksi, pembelian: Pembelian, uang_dibayar):
        super().__init__(nomor_transaksi, pembelian.produk, pembelian.jumlah)
        self._pembelian = pembelian
        self.uang_dibayar = uang_dibayar
```

Objek `Pembayaran` menggunakan data dari objek `Pembelian`, seperti produk, jumlah, total harga, dan status pembayaran.

### b. Agregasi

Agregasi merupakan hubungan ketika suatu class memiliki atau menyimpan objek dari class lain, tetapi objek tersebut masih dapat dibuat dan digunakan secara terpisah.

Pada program ini, agregasi terdapat antara `Toko` dengan `Produk`.

Class `Toko` memiliki atribut `__produk` yang digunakan untuk menyimpan kumpulan objek produk.

```python
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
```

Produk dibuat terlebih dahulu di menu tambah produk menggunakan class `Skincare` atau `Makeup`. Setelah itu, objek tersebut dimasukkan ke dalam daftar produk milik `Toko`.

Karena produk dibuat di luar class `Toko`, produk tidak bergantung pada proses pembuatan objek `Toko`. Hal tersebut menunjukkan hubungan agregasi.

### c. Komposisi

Komposisi merupakan hubungan yang lebih kuat karena objek bagian dibuat oleh objek utama dan menjadi bagian dari objek tersebut.

Pada program ini, komposisi terdapat antara `Pembelian` dengan `DetailPembelian`.

Pada saat objek `Pembelian` dibuat, objek `DetailPembelian` langsung dibuat di dalam konstruktor `Pembelian`.

```python
class Pembelian(Transaksi):
    def __init__(self, nomor_transaksi, produk, jumlah, metode_pembayaran):
        super().__init__(nomor_transaksi, produk, jumlah)
        self.metode_pembayaran = metode_pembayaran
        self.__sudah_dibayar = False
        self.__detail = DetailPembelian(produk, jumlah)
```

`DetailPembelian` tidak dibuat dari menu atau proses terpisah. Objek tersebut langsung dibuat oleh `Pembelian` untuk menyimpan nama produk, harga satuan, jumlah, dan subtotal.

Karena itu, hubungan antara `Pembelian` dan `DetailPembelian` termasuk komposisi.

### Ringkasan Relasi

| Relasi    | Class yang Terlibat             | Penerapan dalam Program                       |
| --------- | ------------------------------- | --------------------------------------------- |
| Asosiasi  | `Transaksi` - `Produk`          | Transaksi menggunakan objek produk            |
| Asosiasi  | `Pembayaran` - `Pembelian`      | Pembayaran menggunakan objek pembelian        |
| Agregasi  | `Toko` - `Produk`               | Toko menyimpan daftar produk                  |
| Komposisi | `Pembelian` - `DetailPembelian` | Pembelian membuat detail pembeliannya sendiri |

## 2. Inheritance

Inheritance adalah konsep pewarisan dari superclass ke subclass. Dengan inheritance, subclass dapat menggunakan atribut dan method yang sudah ada pada superclass.

Pada program ini terdapat dua kelompok inheritance, yaitu `Produk` dan `Transaksi`.

### a. Superclass dan Subclass

| Superclass  | Subclass                  |
| ----------- | ------------------------- |
| `Produk`    | `Skincare`, `Makeup`      |
| `Transaksi` | `Pembelian`, `Pembayaran` |

`Skincare` dan `Makeup` mewarisi class `Produk`.

Sedangkan `Pembelian` dan `Pembayaran` mewarisi class `Transaksi`.

### b. Penggunaan `super().__init__(...)`

Setiap subclass memanggil konstruktor superclass menggunakan `super().__init__(...)`.

Contohnya pada class `Skincare`:

```python
class Skincare(Produk):
    def __init__(self, nama, brand, harga, stok, jenis_kulit):
        super().__init__(nama, brand, "Skincare", harga, stok)
        self.jenis_kulit = jenis_kulit
```

`Skincare` memanggil konstruktor `Produk` untuk mengisi data nama, brand, kategori, harga, dan stok. Setelah itu, `Skincare` menambahkan atribut khusus berupa `jenis_kulit`.

Pada class `Makeup`:

```python
class Makeup(Produk):
    def __init__(self, nama, brand, harga, stok, warna):
        super().__init__(nama, brand, "Makeup", harga, stok)
        self.warna = warna
```

Sedangkan pada class `Pembelian`:

```python
class Pembelian(Transaksi):
    def __init__(self, nomor_transaksi, produk, jumlah, metode_pembayaran):
        super().__init__(nomor_transaksi, produk, jumlah)
        self.metode_pembayaran = metode_pembayaran
        self.__sudah_dibayar = False
        self.__detail = DetailPembelian(produk, jumlah)
```

Class `Pembayaran` juga memanggil konstruktor `Transaksi`:

```python
class Pembayaran(Transaksi):
    def __init__(self, nomor_transaksi, pembelian: Pembelian, uang_dibayar):
        super().__init__(nomor_transaksi, pembelian.produk, pembelian.jumlah)
        self._pembelian = pembelian
        self.uang_dibayar = uang_dibayar
```

### c. Atribut Tambahan pada Subclass

Setiap subclass mempunyai atribut tambahan yang sesuai dengan fungsi masing-masing.

| Subclass     | Atribut Tambahan                                   |
| ------------ | -------------------------------------------------- |
| `Skincare`   | `jenis_kulit`                                      |
| `Makeup`     | `warna`                                            |
| `Pembelian`  | `metode_pembayaran`, `__sudah_dibayar`, `__detail` |
| `Pembayaran` | `_pembelian`, `uang_dibayar`                       |

Atribut tambahan tersebut membuat setiap subclass mempunyai karakteristik yang berbeda walaupun tetap mewarisi data dan method dari superclass.

### d. Method Overriding

Method overriding terjadi ketika subclass membuat kembali method yang sudah dimiliki oleh superclass dengan isi atau proses yang disesuaikan.

Pada program ini, method yang di-override adalah `tampilkan_info()`, `proses_transaksi()`, dan `tampilkan_riwayat()`.

#### Overriding `tampilkan_info()`

Class `Skincare` dan `Makeup` meng-override method `tampilkan_info()` dari class `Produk`.

Contoh pada `Skincare`:

```python
def tampilkan_info(self):
    print(f"  > {self._nama} ({self._brand}) - {self._kategori}")
    print(f"      Harga : Rp{self.harga:,.0f} | Stok : {self.stok} unit")
    print(f"      Jenis Kulit : {self.jenis_kulit}")
```

Perbedaannya dengan `Produk.tampilkan_info()` adalah `Skincare` menampilkan tambahan informasi `jenis_kulit`.

Sedangkan `Makeup` menampilkan tambahan informasi `warna`.

#### Overriding `proses_transaksi()`

Class `Pembelian` dan `Pembayaran` meng-override method `proses_transaksi()` dari class `Transaksi`.

Pada `Pembelian`, method tersebut memanggil `super().proses_transaksi()` untuk menjalankan proses transaksi dasar, kemudian menampilkan detail pembelian.

```python
def proses_transaksi(self):
    print("\n  [PROSES PEMBELIAN]")
    print(f"  Metode Pembayaran : {self.metode_pembayaran}")
    berhasil = super().proses_transaksi()

    if berhasil:
        print("  Detail Pembelian:")
        self.__detail.tampilkan_detail()

    return berhasil
```

Sementara itu, `Pembayaran` mempunyai proses sendiri untuk mengecek apakah pembelian sudah lunas, mengecek jumlah uang yang dibayar, menghitung kembalian, dan mengubah status pembelian menjadi lunas.

```python
def proses_transaksi(self):
    print("\n  [PROSES PEMBAYARAN]")

    if self._pembelian.sudah_dibayar:
        print(f"  [GAGAL] Pembelian {self._pembelian.nomor_transaksi} sudah lunas.")
        return False

    total = self._pembelian.total_harga

    if self.uang_dibayar < total:
        print(f"  [GAGAL] Uang kurang Rp{total - self.uang_dibayar:,.0f}.")
        return False
```

#### Overriding `tampilkan_riwayat()`

Class `Pembelian` dan `Pembayaran` juga meng-override method `tampilkan_riwayat()` dari `Transaksi`.

Pada `Pembelian`, method tersebut memanggil `super().tampilkan_riwayat()` kemudian menambahkan metode pembayaran dan status pembayaran.

Pada `Pembayaran`, method tersebut juga memanggil method dari superclass lalu menambahkan informasi pembelian, uang yang dibayar, dan kembalian.

### e. Tingkat Akses Protected dan Private

Program juga menggunakan atribut protected dan private.

#### Protected

Protected ditandai dengan satu garis bawah (`_`) pada awal nama atribut.

Pada class `Produk`, atribut protected yang digunakan adalah:

* `_nama`
* `_brand`
* `_kategori`

Atribut tersebut digunakan secara langsung oleh subclass `Skincare` dan `Makeup`, contohnya pada method `tampilkan_info()`.

Pada class `Transaksi`, terdapat beberapa atribut protected:

* `_nomor_transaksi`
* `_produk`
* `_jumlah`

Atribut tersebut digunakan oleh subclass seperti `Pembelian` dan `Pembayaran`.

Contohnya pada `Pembayaran`:

```python
print(f"      Produk            : {self._produk.nama}")
```

#### Private

Private ditandai dengan dua garis bawah (`__`) pada awal nama atribut.

Pada class `Produk`, terdapat:

* `__harga`
* `__stok`

Kedua atribut tersebut tidak diakses secara langsung dari luar class. Aksesnya dilakukan melalui property `harga` dan `stok`.

```python
@property
def harga(self):
    return self.__harga

@harga.setter
def harga(self, nilai_baru):
    if not isinstance(nilai_baru, (int, float)) or nilai_baru <= 0:
        print(f"  [DITOLAK] Harga '{nilai_baru}' tidak valid.")
        return
    self.__harga = nilai_baru
```

Dengan menggunakan setter, nilai harga dapat divalidasi sebelum disimpan.

Hal yang sama diterapkan pada stok:

```python
@property
def stok(self):
    return self.__stok

@stok.setter
def stok(self, nilai_baru):
    if not isinstance(nilai_baru, int) or nilai_baru < 0:
        print(f"  [DITOLAK] Stok '{nilai_baru}' tidak valid.")
        return
    self.__stok = nilai_baru
```

Pada class `Transaksi`, atribut `__total_harga` juga bersifat private dan diakses melalui property `total_harga`.

Selain itu, class `Pembelian` memiliki beberapa atribut private, yaitu `__sudah_dibayar` dan `__detail`.

Class `DetailPembelian` juga menggunakan atribut private:

* `__nama_produk`
* `__harga_satuan`
* `__jumlah`
* `__subtotal`

Sedangkan class `Toko` mempunyai atribut private `__produk` untuk menyimpan daftar produk.

## Kesimpulan

Program Aye's Beauty Store sudah menerapkan inheritance dengan dua superclass, yaitu `Produk` dan `Transaksi`, serta beberapa subclass yaitu `Skincare`, `Makeup`, `Pembelian`, dan `Pembayaran`.

Setiap subclass mempunyai atribut tambahan dan melakukan overriding pada method tertentu sesuai dengan kebutuhannya. Penggunaan `super().__init__(...)` juga diterapkan pada setiap subclass untuk memanggil konstruktor superclass.

Selain inheritance, program mempunyai beberapa relasi UML. Asosiasi digunakan pada hubungan `Transaksi` dengan `Produk` dan `Pembayaran` dengan `Pembelian`. Agregasi digunakan pada hubungan `Toko` dengan `Produk`, sedangkan komposisi digunakan pada hubungan `Pembelian` dengan `DetailPembelian`.

Program juga menerapkan protected dan private untuk mengatur akses atribut. Atribut private seperti harga, stok, dan total harga menggunakan property agar nilainya dapat divalidasi sebelum diubah.