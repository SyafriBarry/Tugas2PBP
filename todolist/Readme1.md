# Tugas 5: 

Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023 

## Nama : Syafri Barry Salim
## NPM  : 2106752136
#

### Link Heroku
https://sbarrystugas2pbp.herokuapp.com/todolist/
#

1.	Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?

    ### Inline Style CSS : 
    Style yang di tulis langsung pada
    atribut style di elemen HTML Kode CSS ditulis langsung
    tanpa menggunakan kurung kurawal{ ... }. Kemudian
    properti tetap dipisah dengan titik koma. 
    Kelebihan dari inline CSS :

        1. memperbaiki kode dengan cepat,
        2. Proses permintaan HTTP yang lebih kecil dan proses load website akan lebih cepat
        3. Sangat membantu ketika Anda hanya ingin menguji dan melihat perubahan pada satu elemen
    Kekurangan dari inline css:
    Tidak efisien karena Inline style CSS hanya bisa diterapkan pada satu elemen HTML
    #
    ### Internal Style CSS: 
    kode CSS yang ditulis di dalam tag <'style>. 
    Tag <'style> bisa ditulis di dalam tag <'head>, bisa juga ditulis di dalam tag <'body>. Namun Sering sekali menulisnya di dalam <'head>.  Penulisan css di dalam tag <'head> akan lebih dahulu dibaca dibandingkan di <'body>. Karena lebih dahulu dibaca, style yang akan dipakai adalah yang terakhir.

    Kelebihan Internal CSS
    1. Perubahan pada Internal CSS hanya berlaku pada satu halaman saja.
    2. Anda tidak perlu melakukan upload beberapa file karena HTML dan CSS
       berada dalam satu file
    3. Class dan ID bisa digunakan oleh internal stylesheet

    Kekurangan Internal CSS:
    1. Tidak efisien apabila Anda ingin menggunakan CSS yang sama dalam beberapa file.
    2. Membuat performa website lebih lemot. Sebab, CSS yang berbeda-beda akan mengakibatkan loading ulang setiap kali Anda ganti halaman website
    #
    ### Eksternal Style CSS : 
    kode CSS yang ditulis terpisah dengan kode HTML. Eksternal CSS ditulis di dalam file khusus yang berekstensi .css. kemudian cara menghubungkannya ada 2 cara yaitu dengan menggunakan tag <'link> atau dengan @import

Kelebihan Eksternal CSS: 
1. Ukuran file HTML akan menjadi lebih kecil dan struktur dari kode HTML jadi lebih rapi.
2. Loading website menjadi lebih cepat.
3. File CSS dapat digunakan di beberapa halaman website sekaligus
Kekurangan Internal CSS:
Halaman akan menjadi berantakan, ketika file CSS gagal dipanggil oleh file HTML. Hal ini terjadi disebabkan karena koneksi internet yang lambat
#
### Jelaskan tag HTML5 yang kamu ketahui
HTML5 merupakan perbaruan terbaru dari HTML, syntax yang digunakan pada HTML5 lebih sederhana dan spesifik dari pendahulunya. Sebagai contoh dahulu harus mendefinisikan <'div> untuk berbagai macam elemen, tapi dengan HTML5 penandaan section dengan syntax lebih sederhana <'nav> untuk membuat navigasi. 

Jelaskan tipe-tipe CSS selector yang kamu ketahui.
1.	Selektor Tag = selector yang memilih elemen berdasarkan nama tag
2.	Selektor Class = selector yang memilih elemen berdasarkan nama class
3.	Selektor ID = selector yang memilih elemen berdasarkan nama class namun digunakan pada satu elemen saja. Selector id ditandai dengan tanda pagar (#)
4.	Selektor Atribut = selector yang memilih elemen berdasarkan atribut
5.	Selektor Universal yaitu selector yang digunakan untuk semua elemen Selector universal ditandai dengan tanda bintang (*)
6.	Psedeu Selector = psedeu selector memiliki 2 macam psedeu selector yaitu psedeu-class selektor untuk memilih state pada elemen. Contohnya seperti elemen saat diklik, saat fokus, saat disentuh, dan lain sebagainya. Dan psedeu-element selector selector untuk memilih state pada elemen tertentu dengan bantuan <'span>
#
### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. langkah pertama yang saya lakukan yaitu mendownload framewwork Bootstrap, kemudian menyimpan file bootstrap pada folder fixtures yang terdapat di folder project_django
2. Kemudian saya menyalin Link bootstrap pada index.html, dan menaruhnya pula pada halaman login, register, create-task dan todolist.




