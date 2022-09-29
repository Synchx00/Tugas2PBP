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