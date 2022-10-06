# Tugas 4: Pengimplementasian Form dan Autentikasi Menggunakan Django

[Link Apliasi](https://webggniboss.herokuapp.com/todolist/)

## Apa kegunaan ```{% csrf_token %}``` pada elemen ```<form>?``` Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?

```{% csrf_token %}``` berfungsi untuk melindungi data-data *user* dan *website*. Jika tidak terdapat ```{% csrf_token %}```, maka akan ditemukan *vulnerability* untuk menyerang data *user* dan *website*. 

## Apakah kita dapat membuat elemen ```<form>``` secara manual (tanpa menggunakan generator seperti ```{{ form.as_table }})?``` Jelaskan secara gambaran besar bagaimana cara membuat ```<form>``` secara manual.

Ya, kita sangat mungkin untuk membuat form secara manual. Cara kita untuk membuat form adalah dengan membuat tag ```<form>``` terlebih dahulu. Setelah itu membuat tag ```<input>``` yang berfungsi untuk memasukkan *input user*. Terakhir, buatlah sebuah *trigger* untuk melakukan POST *request*.

## Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada *database*, hingga munculnya data yang telah disimpan pada template HTML.

Ketika user menekan *submit button*, maka *request* POST akan dikirimkan ke server. POST *request* ini akan merubah data pada database. Lalu *request* tersebut akan direspon oleh Django ```views``` dan mengembalikan data yang diinginkan oleh *user*. Setelah itu akan dilakukan *redirect* ke ```views``` sebelumnya dengan melakukan update data terlebih dahulu.

## Jelaskan bagaimana cara kamu mengimplementasikan *checklist* di atas.

1. Membuat aplikasi ```todolist``` pada proyek Django.

2. Menambahkan path
    ```python
    path('todolist/', include('todolist.urls'))
    ```
    pada ```urls.py``` di folder ```project_django```

3. Membuat model ```Task``` dengan beberapa atribut seperti yang ada pada kode berikut
    ```python
    class *Task* (models.Model):
        user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,blank=True, null=True,)
        date = models.DateField(auto_now=True)
        title = models.TextField()
        description = models.TextField()
        is_finished = models.BooleanField(default=False)
    ```

4. Menjalankan perintah ```python manage.py makemingrations``` dan ```python manage.py migrate```

5. Membuat fungsi-fungsi untuk implementasi ```form registrasi```, ```login```, dan ```logout``` agar ```todolist``` dapat digunakan oleh *user* dengan baik.

6. Membuat halaman utama ```todolist``` yang memuat *username user*, ```tombol Tambah *Task* Baru```, ```tombol logout```, serta tabel berisi tanggal pembuatan *task*, judul *task*, dan deskripsi *task*.

7. Membuat halaman form untuk pembuatan *task*. Data yang perlu dimasukkan pengguna hanyalah judul *task* dan deskripsi *task*.

8. Membuat routing
    ```python
    urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('createtask/', create_task,  name='create_task'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'), 
    path('update_task/<str:key>/', update_task, name='update_task'),
    path('delete_task/<str:key>/', delete_task, name="delete_task"),
    ]
    ```

9. Deploy aplikasi ke heroku (Pada tugas ini aplikasi ```mywatchlist``` sudah automatis ter-deploy karena pada tugas sebelumnya kita sudah melakukan deploy ```project_django``` yang merupakan *parent* dari ```mywatchlist```)

10. Membuat dua akun *user* dan tiga *dummy data* menggunakan model ```Task``` pada akun masing-masing di situs web Heroku.

11. Membuat ```README.md``` ini

12. Menambahkan fitur bonus yang berisi ```status``` dari ```task``` dan tombol untuk mengubah ```status``` dan tombol untuk menghapus ```task```

# Tugas 5: Web Design Using HTML, CSS, and CSS Framework

##  Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?

1.  Inline CSS

Inline CSS adalah kode CSS yang ditulis langsung pada atribut elemen HTML. Setiap elemen HTML memiliki atribut style, di situ lah inline CSS ditulis.

Cara ini kurang efisien karena setiap tag HTML yang diberikan harus memiliki style masing-masing. Anda akan lebih sulit dalam mengatur website jika hanya menggunakan inline style CSS. Sebab, Inline CSS digunakan hanya untuk mengubah satu elemen saja.

- Manfaat Inline CSS:
    Sangat membantu ketika Anda hanya ingin menguji dan melihat perubahan pada satu elemen, Berguna untuk memperbaiki kode dengan cepat, dan Proses permintaan HTTP yang lebih kecil dan proses load website akan lebih cepat.
- Kekurangan Inline CSS:
    Tidak efisien karena Inline style CSS hanya bisa diterapkan pada satu elemen HTML.

2. Internal CSS

Internal CSS adalah kode CSS yang ditulis di dalam tag `<style>` dan kode HTML dituliskan di bagian atas (header) file HTML. Internal CSS dapat digunakan untuk membuat tampilan pada satu halaman website dan tidak digunakan pada halaman website yang lain.

Cara ini akan sangat cocok dipakai untuk menciptakan halaman web dengan tampilan yang berbeda. Dengan kata lain, Internal CSS ini bisa dipakai untuk menciptakan tampilan yang unik, pada setiap halaman website.

- Manfaat Internal CSS:
    Perubahan pada Internal CSS hanya berlaku pada satu halaman saja, Anda tidak perlu melakukan upload beberapa file karena HTML dan CSS berada dalam satu file, dan Class dan ID bisa digunakan oleh internal stylesheet.
- Kekurangan Internal CSS:
    Tidak efisien apabila Anda ingin menggunakan CSS yang sama dalam beberapa file dan Membuat performa website lebih lambat. Sebab, CSS yang berbeda-beda akan mengakibatkan loading ulang setiap kali Anda ganti halaman website.

3. External CSS

Eksternal CSS adalah kode CSS yang ditulis terpisah dengan kode HTML Eksternal CSS ditulis di sebuah file khusus yang berekstensi .css. File eksternal CSS biasanya diletakkan setelah bagian `<head>` pada halaman.

Cara ini lebih sederhana dan simpel daripada menambahkan kode CSS di setiap elemen HTML yang ingin Anda atur tampilannya. 

- Manfaat External CSS:
    Ukuran file HTML akan menjadi lebih kecil dan struktur dari kode HTML jadi lebih rapi, Loading website menjadi lebih cepat, dan File CSS dapat digunakan di beberapa halaman website sekaligus. 
- Kekurangan External CSS:
    Halaman akan menjadi berantakan, ketika file CSS gagal dipanggil oleh file HTML. Hal ini terjadi disebabkan karena koneksi internet yang lambat.
    

## Jelaskan tag HTML5 yang kamu ketahui.

1. `<audio>`, Memasukkan audio ke dokumen HTML
2. `<video>`, Memasukkan video ke dokumen HTML
3. `<time>`, Menampilkan hari dan atau tanggal

## Jelaskan tipe-tipe CSS selector yang kamu ketahui.

1. `*`, Memilih semua elemen

2. element, Memilih semua `<p>` elemen

3. .class, emilih semua elemen dengan class="intro"

##  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

1. Mencari contoh template di internet
2. Menjadikan template tersebut sebagai referensi
3. *Coding*-in