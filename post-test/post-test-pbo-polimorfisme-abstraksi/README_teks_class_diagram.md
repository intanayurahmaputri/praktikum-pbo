# Sistem Penjualan Toko Kecantikan

## Deskripsi Program

Program ini merupakan aplikasi berbasis terminal untuk membantu admin/kasir mengelola toko kecantikan Aye's Beauty Store. Fitur yang tersedia meliputi pengelolaan produk skincare dan makeup, pencatatan pembelian, pembayaran, riwayat transaksi, serta informasi toko.

Program dibuat menggunakan Python dengan menerapkan konsep Object-Oriented Programming (OOP), yaitu abstraksi, inheritance, polimorfisme, duck typing, operator overloading, dan relasi antarkelas.

## Class Diagram

Diagram kelas berikut ditampilkan dalam bentuk teks agar dapat dibaca langsung dari README tanpa memerlukan file gambar tambahan.

```text
                         +----------------------+
                         |      Produk (ABC)    |
                         +----------------------+
                         | _nama                |
                         | _brand               |
                         | _kategori            |
                         | __harga              |
                         | __stok               |
                         +----------------------+
                         | tampilkan_info()     |  {abstract}
                         | tampilkan_spesifikasi()| {abstract}
                         | tampilkan_ringkasan()|
                         | ringkasan()          |
                         | __str__()            |
                         +----------------------+
                           ^                  ^
                           | inheritance      | inheritance
              +--------------------+  +--------------------+
              |      Skincare      |  |       Makeup       |
              +--------------------+  +--------------------+
              | jenis_kulit        |  | warna              |
              +--------------------+  +--------------------+
              | tampilkan_info()   |  | tampilkan_info()   |
              | tampilkan_spesifikasi()| tampilkan_spesifikasi()|
              +--------------------+  +--------------------+


 +----------------------+       inheritance       +----------------------+
 |      Transaksi       |<------------------------|      Pembelian       |
 +----------------------+                         +----------------------+
 | _nomor_transaksi     |                         | metode_pembayaran    |
 | _produk              |                         | __sudah_dibayar      |
 | _jumlah              |                         | __detail             |
 | __total_harga        |                         +----------------------+
 +----------------------+                                  |
 | proses_transaksi()   |                                  | composition
 | tampilkan_riwayat()  |                                  v
 | ringkasan()          |                         +----------------------+
 +----------------------+                         |   DetailPembelian   |
          ^                                       +----------------------+
          | inheritance                           | __nama_produk       |
          |                                       | __harga_satuan      |
 +----------------------+                         | __jumlah            |
 |      Pembayaran      |                         | __subtotal          |
 +----------------------+                         +----------------------+
 | _pembelian           |
 | uang_dibayar         |
 +----------------------+

 +----------------------+       aggregation       +----------------------+
 |         Toko         | o---------------------->|        Produk        |
 +----------------------+                         +----------------------+
 | __produk             |
 +----------------------+
 | tambah_produk()      |
 | hapus_produk()       |
 | tampilkan_produk()   |
 +----------------------+

 Relasi asosiasi tambahan:
 Transaksi  ----------------------> Produk
 Pembayaran ----------------------> Pembelian
```

Keterangan simbol:
- `^` menunjukkan inheritance (pewarisan), yaitu kelas anak mewarisi kelas induk.
- `o---->` menunjukkan aggregation (agregasi), yaitu `Toko` menyimpan objek `Produk` yang dapat dibuat secara terpisah.
- `composition` menunjukkan komposisi, yaitu `Pembelian` membuat dan menyimpan objek `DetailPembelian`.
- `------>` menunjukkan asosiasi, yaitu satu kelas menggunakan atau menyimpan referensi ke objek kelas lain.
- `ABC` menunjukkan bahwa `Produk` merupakan abstract class.

### Penjelasan Relasi Kelas

1. Asosiasi — `Transaksi` dengan `Produk`  
   Kelas `Transaksi` menyimpan referensi objek produk melalui atribut `_produk` untuk memproses pembelian dan mengurangi stok. Objek `Produk` dapat dibuat dan dikelola secara terpisah dari objek `Transaksi`.

   Kelas `Pembayaran` juga memiliki asosiasi dengan `Pembelian` melalui atribut `_pembelian`, karena pembayaran mengakses data pembelian yang sudah dibuat.

2. Agregasi — `Toko` dengan `Produk`  
   Kelas `Toko` menyimpan kumpulan objek produk melalui atribut `__produk` dan method `tambah_produk()`. Produk dibuat sebagai objek tersendiri sebelum dimasukkan ke toko, sehingga objek produk tidak bergantung pada keberadaan objek `Toko`.

3. Komposisi — `Pembelian` dengan `DetailPembelian`  
   Kelas `Pembelian` membuat objek `DetailPembelian` langsung di dalam konstruktor dan menyimpannya pada atribut privat `__detail`. Detail tersebut menjadi bagian dari data pembelian dan dibuat khusus untuk pembelian tersebut.

4. Inheritance — `Skincare` dan `Makeup` dengan `Produk`, serta `Pembelian` dan `Pembayaran` dengan `Transaksi`  
   `Skincare` dan `Makeup` mewarisi atribut serta method dari `Produk`. Sementara itu, `Pembelian` dan `Pembayaran` mewarisi atribut serta method dari `Transaksi`.

## Penerapan Abstraksi

Kelas `Produk` merupakan abstract class yang menggunakan `ABC` dan memiliki dua abstract method, yaitu `tampilkan_info()` dan `tampilkan_spesifikasi()`. Oleh karena itu, objek `Produk` tidak dapat dibuat secara langsung.

Kelas `Skincare` dan `Makeup` merupakan subclass dari `Produk` dan mengimplementasikan kedua abstract method tersebut. `Skincare` mempunyai atribut unik `jenis_kulit`, sedangkan `Makeup` mempunyai atribut unik `warna`. Keduanya memanggil `super().__init__(...)` untuk menggunakan konstruktor kelas induk.

Method konkret `tampilkan_ringkasan()` dimiliki kelas `Produk` dan digunakan oleh kedua subclass melalui method `tampilkan_info()`. Method tersebut menampilkan informasi umum produk dan memanggil `tampilkan_spesifikasi()` agar setiap subclass menampilkan detailnya masing-masing.

Program juga mencoba menginstansiasi `Produk` menggunakan `try-except TypeError` pada menu Informasi Toko. Percobaan tersebut menghasilkan pesan bahwa `Produk` tidak dapat diinstansiasi karena masih memiliki abstract method.

## Penerapan Polimorfisme

### 1. Polimorfisme melalui Pewarisan

Method `tampilkan_info()` diimplementasikan pada kelas `Skincare` dan `Makeup`. Method tersebut dipanggil melalui satu loop di `Toko.tampilkan_produk()` untuk objek produk yang berbeda. Setiap objek menjalankan implementasinya sendiri dan menampilkan spesifikasi sesuai kategori produk.

### 2. Duck Typing

Kelas `Produk` dan `Transaksi` tidak memiliki hubungan pewarisan langsung, tetapi keduanya memiliki method bernama `ringkasan()`. Fungsi `tampilkan_objek(objek)` memanggil method tersebut tanpa memeriksa tipe objek. Fungsi yang sama digunakan untuk menampilkan ringkasan produk maupun transaksi.

### 3. Operator Overloading

Kelas `Produk` menerapkan magic method `__str__()`. Method ini menentukan representasi objek ketika objek produk dicetak menggunakan `print()` atau dimasukkan ke dalam f-string.

### 4. Inheritance dan Enkapsulasi

`Skincare` dan `Makeup` mewarisi kelas `Produk`, sedangkan `Pembelian` dan `Pembayaran` mewarisi kelas `Transaksi`. Program juga menggunakan atribut protected seperti `_nama` dan `_produk`, serta atribut private seperti `__harga`, `__stok`, dan `__detail` sesuai kebutuhan kelas.

## Screenshot Output Program

Tambahkan screenshot asli dari program yang dijalankan ke folder `screenshots/`, lalu gunakan nama file berikut atau sesuaikan tautannya dengan nama file screenshot yang disimpan.

### 1. Menu Utama

![Screenshot menu utama](screenshots/menu-utama.png)

### 2. Daftar Produk Skincare dan Makeup

![Screenshot daftar produk](screenshots/daftar-produk.png)

### 3. Proses Pembelian atau Pembayaran

![Screenshot proses transaksi](screenshots/transaksi.png)

### 4. Bukti Abstract Class Tidak Dapat Diinstansiasi

Buka menu Informasi Toko dan ambil screenshot bagian yang menampilkan pesan `[BERHASIL] Produk tidak dapat diinstansiasi.` beserta penyebab `TypeError`.

![Screenshot bukti abstract class](screenshots/bukti-abstract-class.png)

Catatan: Ganti atau lengkapi gambar pada bagian ini dengan screenshot asli dari program. Jangan mengumpulkan README dengan gambar screenshot yang masih belum tersedia.

## Cara Menjalankan Program

1. Pastikan Python 3 sudah terpasang.
2. Simpan file program Python dan README dalam folder proyek yang sama.
3. Jalankan perintah berikut dari terminal:

```bash
python sistem_penjualan_toko_kecantikan_final.py
```

Jika sistem menggunakan perintah `python3`, jalankan:

```bash
python3 sistem_penjualan_toko_kecantikan_final.py
```

## Struktur Berkas

```text
proyek/
├── sistem_penjualan_toko_kecantikan_final.py
├── README.md
└── screenshots/
    ├── menu-utama.png
    ├── daftar-produk.png
    ├── transaksi.png
    └── bukti-abstract-class.png
```
