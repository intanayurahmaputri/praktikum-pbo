# Sistem Manajemen Penjualan Toko Kecantikan

## Deskripsi

Program ini merupakan simulasi sederhana sistem penjualan pada toko kecantikan Aye's Beauty Store. Program dibuat menggunakan konsep Pemrograman Berorientasi Objek (PBO) dengan tiga class utama, yaitu `Produk`, `Pengguna`, dan `Transaksi`.

Ketiga class tersebut memiliki fungsi yang berbeda, tetapi dapat saling berinteraksi dalam proses penjualan.

| Class       | Fungsi                                                                                      |
| ----------- | ------------------------------------------------------------------------------------------- |
| `Produk`    | Menyimpan informasi produk seperti nama, brand, kategori, harga, dan stok.                  |
| `Pengguna`  | Menyimpan data pengguna sistem yang terdiri dari admin dan pelanggan.                       |
| `Transaksi` | Menyimpan data transaksi dan menghubungkan produk dengan pengguna yang melakukan pembelian. |

## Struktur Class

### 1. Class `Produk`

Class `Produk` digunakan untuk menyimpan dan mengelola data produk yang tersedia di toko.

Atribut kelas yang digunakan adalah `nama_toko`, `total_produk_terdaftar`, dan `kategori_tersedia`. Untuk setiap objek produk, terdapat atribut publik `nama`, `brand`, dan `kategori`. Harga dan stok dibuat sebagai atribut privat, yaitu `__harga` dan `__stok`.

Class ini memiliki beberapa method, yaitu:

* `tampilkan_info()` untuk menampilkan informasi produk.
* `kurangi_stok(jumlah)` untuk mengurangi stok setelah terjadi pembelian.
* `dari_dict(data)` sebagai class method untuk membuat objek `Produk` dari dictionary.
* `ubah_nama_toko(nama_baru)` sebagai class method untuk mengubah nama toko.
* `validasi_nama_produk(nama)` sebagai static method untuk memeriksa apakah nama produk valid.
* Property `harga` digunakan untuk mengakses dan mengubah harga dengan validasi angka lebih dari 0.
* Property `stok` digunakan untuk mengakses dan mengubah stok dengan validasi bahwa nilainya harus berupa integer dan tidak boleh negatif.

### 2. Class `Pengguna`

Class `Pengguna` digunakan untuk menyimpan data orang yang menggunakan sistem, baik sebagai admin maupun pelanggan.

Atribut kelas pada class ini adalah `nama_platform`, `total_pengguna`, dan `role_tersedia`. Setiap objek memiliki atribut publik `id_pengguna`, `nama`, dan `role`. Password disimpan sebagai atribut privat `__password` agar tidak diakses secara langsung.

Method yang digunakan antara lain:

* `tampilkan_profil()` untuk menampilkan data pengguna dengan password yang disamarkan.
* `registrasi(...)` sebagai class method untuk membuat pengguna baru setelah password divalidasi.
* `info_platform()` sebagai class method untuk menampilkan informasi platform dan jumlah pengguna.
* `validasi_password(password)` sebagai static method untuk memeriksa panjang password.
* Property `password` digunakan untuk mengakses dan mengubah password melalui setter dengan validasi minimal 6 karakter.

### 3. Class `Transaksi`

Class `Transaksi` digunakan untuk mencatat proses pembelian. Class ini menggunakan objek `Pengguna` dan `Produk` sehingga sebuah transaksi dapat mengetahui siapa yang melakukan pembelian dan produk yang dibeli.

Atribut kelas yang digunakan yaitu `nama_toko`, `total_transaksi`, dan `mata_uang`. Setiap transaksi memiliki `nomor_transaksi`, `pengguna`, `produk`, dan `jumlah`. Total harga disimpan dalam atribut privat `__total_harga`.

Method yang terdapat pada class ini adalah:

* `proses_transaksi()` untuk memeriksa jumlah pembelian, mengurangi stok produk, dan menghitung total harga apabila transaksi berhasil.
* `buat_transaksi_cepat(...)` sebagai class method untuk membuat transaksi dengan nomor otomatis menggunakan format `T` diikuti empat digit angka.
* `validasi_jumlah(jumlah)` sebagai static method untuk memeriksa apakah jumlah pembelian lebih dari 0.
* Property `total_harga` digunakan untuk mengakses dan mengubah total harga dengan validasi agar nilainya tidak negatif.

## Fungsi Bantuan

Selain ketiga class tersebut, terdapat dua fungsi tambahan, yaitu `cetak_judul(judul)` dan `cetak_subjudul(subjudul)`. Kedua fungsi ini hanya digunakan untuk membuat tampilan output di terminal menjadi lebih rapi dan tidak termasuk ke dalam class PBO.

## Pengujian Program

Pengujian program dilakukan pada bagian `if __name__ == "__main__":`. Pengujian dibagi menjadi tiga bagian sesuai dengan class yang digunakan.

### 1. Class Produk

Pada bagian ini dibuat dua objek `Produk`. `produk1` dibuat secara langsung menggunakan constructor, sedangkan `produk2` dibuat menggunakan class method `dari_dict()`. Setelah itu, informasi kedua produk ditampilkan menggunakan `tampilkan_info()`.

Selanjutnya dilakukan pengujian terhadap atribut kelas dan method pada `Produk`. Jumlah produk yang sudah dibuat ditampilkan melalui `total_produk_terdaftar`, kemudian nama toko diubah menggunakan `ubah_nama_toko()`.

Static method `validasi_nama_produk()` juga diuji menggunakan nama produk yang valid dan string kosong.

Terakhir, property `harga` dan `stok` diuji dengan memasukkan nilai yang valid dan tidak valid. Nilai negatif akan ditolak dan nilai sebelumnya tetap digunakan.

### 2. Class Pengguna

Pada bagian `Pengguna`, dibuat dua objek, yaitu `admin1` secara langsung dan `pelanggan1` menggunakan class method `registrasi()`.

Setelah objek dibuat, data pengguna ditampilkan melalui `tampilkan_profil()`. Password yang ditampilkan sudah disamarkan menggunakan karakter `*`.

Kemudian class method `info_platform()` digunakan untuk menampilkan informasi platform dan jumlah pengguna. Static method `validasi_password()` juga diuji menggunakan password yang kurang dari 6 karakter dan password yang memenuhi syarat.

Pengujian terakhir dilakukan pada property `password`. Password baru yang memenuhi syarat dapat disimpan, sedangkan password `123` ditolak karena jumlah karakternya kurang dari 6.

### 3. Class Transaksi

Pada bagian ini dibuat dua objek transaksi menggunakan produk dan pengguna yang sudah dibuat sebelumnya. `transaksi1` dibuat secara langsung, sedangkan `transaksi2` dibuat menggunakan class method `buat_transaksi_cepat()`.

Kedua transaksi kemudian diproses menggunakan `proses_transaksi()`. Jika jumlah pembelian valid dan stok mencukupi, stok produk akan berkurang dan total harga transaksi akan dihitung.

Static method `validasi_jumlah()` kemudian diuji menggunakan jumlah pembelian yang valid dan tidak valid.

Pengujian berikutnya dilakukan dengan membuat transaksi yang jumlah pembeliannya melebihi stok produk. Transaksi tersebut akan gagal dan dibatalkan karena stok tidak mencukupi.

Terakhir, property `total_harga` diuji dengan memasukkan nilai yang valid dan nilai negatif. Nilai negatif akan ditolak sehingga nilai total harga sebelumnya tetap dipertahankan.