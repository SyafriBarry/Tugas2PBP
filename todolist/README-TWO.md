# Tugas 6: 

Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023 

## Nama : Syafri Barry Salim
## NPM  : 2106752136
#

### Link Heroku
https://sbarrystugas2pbp.herokuapp.com/todolist/
#

### Jelaskan perbedaan antara asynchronous programming dengan synchronous programming?
#

Penjelasan :

Synchronous adalah proses jalannya program secara sequential , disini yang dimaksud sequential ada berdasarkan antrian ekseskusi program

Asynchronous adalah proses jalannya program bisa dilakukan secara bersamaan tanpa harus menunggu proses antrian

#


### Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
#
paradigma pemrograman yang alur programnya ditentukan oleh suatu event / peristiwa yang merupakan keluaran atau tindakan pengguna atau bisa berupa pesan dari program lainnya. penerapan pada tugas ini yaitu saat pengguna melakukan perintah dengan mengklik tambah task baru, maka pop up task baru langsung keluar saat di klik/saat terjadi event. 
 

### Jelaskan penerapan asynchronous programming pada AJAX
#
Pada Javascript, Asynchronous JavaScript and XMLHTTP atau biasa disebut AJAX merupakan salah satu konsep yang menerapkan metode asynchronous dalam menjalankan pekerjaannya. Biasa nya AJAX digunakan untuk melakukan permintaan data (request) dan menangani sebuah tanggapan (handling response), baik response dalam bentuk XML, Javascript ataupun JSON dari sebuah Rest API.
#
## JJelaskan bagaimana cara kamu mengimplementasikan checklist di atas
#
1. pertama saya membuat html baru yaitu todolist_ajax.html untuk menampilkan todolist dalam bentuk json
2. kemudian menambahkanfungsi pada file views.py, todolist_ajax, add_task dan todolist_json
3. lalu saya me routing fungsi tersebut di urls.py pada folder todolist 
4. saya mengimport Jquery Ajax dengan `<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>`.  Kemudian menambahkan modal dan script yang berisi asynchronus function pada bagian body html pada todolist_ajax.html untuk mengimplementasikan asynchronus programming yang terdapat pada file views.py.
5. melakukan deploy






