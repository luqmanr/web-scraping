# **INSTAGRAM FOLLOWERS CRAWLING**

## 1. PROGRAM instagram_crawler_v3

**A. Pengantar**
.

**B. Kegunaan Dari Program**
Berikut beberapa hal yang bisa diperoleh melalui program ini:

* Mengambil data username-username yang merupakan followers dari akun Instagram yang dicrawl
* Mengambil data nama lengkap, jumlah following, dan jumlah post dari akun tersebut
* Menyimpan data-data di atas ke dalam file csv dan menyimpannya pada folder Google Drive anda

**C. Hal-Hal Yang Harus Disiapkan**
Pertama-tama, sebelum menjalankan program berikut anda harus menyiapkan:

* Akun Google Drive
* Username Instagram beserta passwordnya
* Username Instagram yang mau dicrawl

**D. Cara Menjalankan Program**
Untuk menjalankan program ini, berikut langkah-langkah yang harus dilalui

* Jalankan sel pertama, untuk mounting program ke folder Google Drive akun anda.
* Masuk ke url yang muncul setelah menjalankan sel tersebut. Lalu, login dengan menggunakan akun Google anda.
* Setelah itu salin kode yang muncul setelah sign in, lalu tempelkan pada program instagram_crawler_v3 dan tekan enter.
* Selanjutnya, jalankan sel kedua yang akan meng-import beberapa library yang dibutuhkan program.
* Lalu, masukkan username dan password Instagram ke dalam textbox yang akan muncul setelah menjalankan sel yang ketiga. Login agar dapat mengakses profil username yang akan dicrawl.
* Selanjutnya, isi list pada sel keempat dengan username yang ingin anda crawl, lalu jalankan sel tersebut. Contoh format penulisannya adalah sebagai berikut: (apabila ingin crawl username tyogotest2)

'''
usernames_target = [
  "tyogotest2"
]
'''

* Setelah itu jalankan sel kelima, dan secara otomatis program akan crawling username yang anda berikan, lalu diikuti dengan juga meng-crawl username-username yang merupakan follower dari akun tersebut.
* Hasil crawl bisa anda lihat di directory berikut:
'/content/gdrive/My Drive/instagram-crawling/instagram-usernames'
