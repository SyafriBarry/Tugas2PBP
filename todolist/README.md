# Tugas 4: 

Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023 

## Nama : Syafri Barry Salim
## NPM  : 2106752136
#

### Link Heroku
https://sbarrystugas2pbp.herokuapp.com/todolist/
#

### Apa kegunaan {% csrf_token %} pada elemen <.form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <.form>?
#

Penjelasan :

{% csrf_token %} pada elemen <.form> berguna untuk mencegah serangan CSRF. Dikarena penyerang tidak dapat menentukan atau memprediksi nilai token CSRF pengguna, sehingga tidak dapat membuat permintaan dengan semua parameter yang diperlukan aplikasi untuk memenuhi permintaan tersebut.

yang terjadi apabila tidak ada {% csrf_token %} pada elemen <.form> website yang sudah kita buat rentan diserang oleh pengguna internet dengan mengubah link/code yang terdapat diwebsite tersebut diganti dengan malicious code/ kode berbahaya dan membuat perubahan perubahan tertentu tanpa kita sadari 

#


### Apakah kita dapat membuat elemen <.form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.
#
ya kita bisa membuat form tanpa menggunakan generator dengan membuat tag <.form> dengan attribute action & method kemudian membuat Tag <.input> dan harus memiliki attribute name contoh : <.input name=”nama_inputan” /> fungsinya untuk memberi nama variable yang akan digunakan dengan bantuan method get().

 

## Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML
#
1. mengakses halaman request kepada pengguna, dan akan diarahkan ke form registrasi apabila pengguna tersebut adalah request yang pertama kalinya.  
2. kemudian setelah pengguna mengisi form tersebut dan mengklik submit  maka data itu akan dibawa pada views.py jika form tersebut isvalid maka akan tersave dengan bantuan form.save()
3. terakhir file views.py akan mengambil data model yang terdapat pada models.py dan dikirimkan ke template HTML agar dapat ditampilkan
#
## JJelaskan bagaimana cara kamu mengimplementasikan checklist di atas
#
1. Membuat suatu aplikasi baru bernama todolist di proyek tugas Django dengan menjalankan python manage.py startapp todolist
2. menambahkan  'todolist' ke file setting.py dan menambahkan path todolist ke file urls.py  yang terdapat pada file project_django
3. membuat beberapa models pada models.py seperti user, date, title, description dan is_finished
4. membuat fungsi register, login dan logout pada views.py dan membuat template html bernama login.html dan register.html
5. membuat template halaman todolist.html yang memuat username pengguna, tombol Tambah Task Baru, tombol logout, serta tabel berisi tanggal pembuatan task, judul task, dan deskripsi task
6. membuat template creat-task.html dan membuat fungsi create-task pada file views.py
7. melakukan routing pada file urls.py  dengan fungsi yang terdapat pada file views.py
8. melakukan deploy


### Akun Dummy
1. Username : Barry1
   Password : Tangcity123

2. Username : Barry2
   Password : Tangerang123





