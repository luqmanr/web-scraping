# Process Crawling

# A. Untuk melakukan scraping, pertama ada beberapa hal yang perlu dijelaskan
## Pertama, scraping atau crawling dilakukan menggunakan Selenium Webdriver
## https://www.selenium.dev/about/
## Kedua, secara top-down, cara kerja program ini adalah untuk mengekstrak
## data-data yang dikembalikan oleh instagram.com ke browser kita
## dimana data tersebut berbentuk html

# B. Get username followers
## Ada beberapa hal yang perlu disiapkan untuk menggunakan program scraping ini
## 1. akun instagram
## 2. daftar username / username yang ingin diambil data followersnya

## Secara proses demikian
## 1. selenium webdriver pergi ke halaman login instagram
## 2. anda akan diminta untuk memasukkan username dan password akun instagram anda
## 3. program akan membaca daftar username yang ingin anda scraping
## 4. program akan membuka halaman profile username yang telah anda masukkan
## 5. di halaman ini selenium webdriver akan mencoba untuk mengekstrak data followers
## 6. data followers yang telah didapatkan bisa disimpan secara lokal ke dalam sebuah file

a. csv
b. json
c. txt
d. dsb

## 7. (to do) mengirim data followers yang telah didapatkan ke queue database, untuk disimpan
### dengan bentuk data

{username_scraper, username_scraped, username_found}

### a. username_scraper = adalah hanya sebagai penanda siapa yang melakukan scraping
### b. username_scraped = adalah username yang anda ingin cari data followersnya
### c. username_found = adalah username-username yang telah anda dapatkan dari username_scraped