# **INSTAGRAM FOLLOWERS CRAWLING**

**Pengantar**
Berikut adalah rigkasan dari kegunaan dan cara menjalankan script yang ada di directory ini.

**Daftar Program:**
Ini adalah list program yang ada dengan versi terbarunya yang ada di directory ini.

1. Program instagram_crawler_v3.ipynb
2. Program instagram_post_crawler_method2.ipynb

## 1. PROGRAM instagram_crawler_v3

**A. Kegunaan Dari Program**
Berikut beberapa hal yang bisa diperoleh melalui program ini:

* Mengambil data username-username yang merupakan followers dari akun Instagram yang dicrawl
* Mengambil data nama lengkap, jumlah following, dan jumlah post dari akun tersebut
* Menyimpan data-data di atas ke dalam file csv dan menyimpannya pada folder Google Drive anda

**B. Hal-Hal Yang Harus Disiapkan**
Pertama-tama, sebelum menjalankan program berikut anda harus menyiapkan:

* Akun Google Drive
* Username Instagram beserta passwordnya
* Username Instagram yang mau dicrawl

**C. Cara Menjalankan Program**
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

## 2. Program instagram_post_crawler_method2.ipynb

**A. Kegunaan Dari Program**
Berikut beberapa hal yang bisa diperoleh melalui program ini:

* Mengambil data url dari foto-foto post akun instagram yang sudah dicrawl sebelumnya, menggunakan program instagram_crawler_v3
* Menyimpan data-data tersebut ke dalam file JSON dan menyimpannya pada folder Google Drive anda

**B. Hal-Hal Yang Harus Disiapkan**
Sebelum menjalankan program berikut anda harus menyiapkan:

* Akun Google Drive
* Username Instagram beserta passwordnya
* File csv dari hasil program instagram_crawler_v3 yang sudah dijalankan sebelumnya

**C. Cara Menjalankan Program**
Untuk menjalankan program ini, berikut langkah-langkah yang harus dilalui

* Jalankan sel pertama, untuk mounting program ke folder Google Drive akun anda.
* Masuk ke url yang muncul setelah menjalankan sel tersebut. Lalu, login dengan menggunakan akun Google anda.
* Setelah itu salin kode yang muncul setelah sign in, lalu tempelkan pada program instagram_crawler_v3 dan tekan enter.
* Selanjutnya, jalankan sel kedua yang akan meng-import beberapa library yang dibutuhkan program.
* Lalu, masukkan username dan password Instagram ke dalam textbox yang akan muncul setelah menjalankan sel yang ketiga. Login agar dapat mengakses profil username yang akan dicrawl.
* Selanjutnya jalankan sel keempat, maka secara otomatis program akan mengambil data username yang ada pada file csv di '/content/gdrive/My Drive/instagram-crawling/instagram-usernames' dan mengumpulkan url dari semua post yang dimiliki oleh username-username tersebut.
