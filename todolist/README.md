# Tugas 4: Pengimplementasian Form dan Autentikasi Menggunakan Django

[Link Apliasi](https://webggniboss.herokuapp.com/todolist/)

## Apa kegunaan ```{% csrf_token %}``` pada elemen ```<form>?``` Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?

```{% csrf_token %}``` berfungsi untuk melindungi data-data *user* dan *website*. Jika tidak terdapat ```{% csrf_token %}```, maka akan ditemukan *vulnerability* untuk menyerang data *user* dan *website*. 

## Apakah kita dapat membuat elemen ```<form>``` secara manual (tanpa menggunakan generator seperti ```{{ form.as_table }})?``` Jelaskan secara gambaran besar bagaimana cara membuat ```<form>``` secara manual.

Ya, kita sangat mungkin untuk membuat form secara manual. Cara kita untuk membuat form adalah dengan membuat tag ```<form>``` terlebih dahulu. Setelah itu membuat tag ```<input>``` yang berfungsi untuk memasukkan *input user*. Terakhir, buatlah sebuah *trigger* untuk melakukan POST *request*.

## Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada *database*, hingga munculnya data yang telah disimpan pada template HTML.



## Jelaskan bagaimana cara kamu mengimplementasikan *checklist* di atas.

1. Membuat aplikasi ```todolist``` pada proyek Django.

2. Menambahkan path
```python
    path('todolist/', include('todolist.urls'))
```
pada ```urls.py``` di folder ```project_django```

3. 