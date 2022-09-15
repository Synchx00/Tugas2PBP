# Tugas 2: Pengenalan Aplikasi Django dan Models View Template (MVT) pada Django

[Link Apliasi](https://webggniboss.herokuapp.com/katalog/)

## Bagan request client ke web aplikasi berbasis Django beserta respon

<p align="center"><img src= "https://github.com/Synchx00/Tugas2PBP/tree/main/katalog/images/bagan.png"/></p>

1. ```urls.py``` akan memproses *Request* yang diminta oleh *user* dan dilakukan pencocokan dengan ```urlpatterns```
2. Memanggil fungsi yang ada pada ```views.py```
3. Memanggil *query* ke ```models.py``` jika ada aktivitas yang menggunakan *database*
4. Memproses data pada *database*
5. *Response* data akan dikembalikan ke ```views.py```
6. ```views.py``` akan memilih ```html``` yang sesuai dengan *mapping* sebelumnya
7. *Response* akan diteruskan kembali ke *user* dan memberikan tampilan aplikasi

## kenapa menggunakan *virtual environment*?

*Virtual environment* digunakan untuk melakukan isolasi pada proyek Django kita. Sebut saja jika kita membutuhkan suatu *library* khusus pada proyek kita, jika kita menggunakan *virtual environment* dan melakukan instalasi *library* tersebut pada *virtual environment* maka kita tidak akan memengaruhi proyek lain. Jadi, akan sangat baik jika kita menggunakan *virtual environment*.

Kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan *virtual environment*. Namun, hal ini tidak dianjurkan karena kita tidak dapat mengatur masing-masing proyek Django kita yang berbeda.

## Implementasi

1. Membuat fungsi pada ```views.py```
```
def show_catalog(request):
    data_barang_catalog = CatalogItem.objects.all()
    context = {
    'list_barang': data_barang_catalog,
    'nama': 'Son Sulung Suryahatta Asnan',
    'id' : '2106751455'
    
}
    return render(request, "katalog.html", context)
```

2. Membuat routing pada ```urls.py``` di folder project django dan katalog
    - Menambahkan
    ```
    path('', show_catalog, name='show_catalog')
    ```
    pada ```urlpatterns``` di dalam file ```urls.py``` pada folder katalog
    - Menambahkan
    ```
    path('katalog/', include('katalog.urls'))
    ```
    pada ```urlpatterns``` di dalam file ```urls.py``` pada folder project_django

3. 