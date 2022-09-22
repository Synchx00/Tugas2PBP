# Tugas 3: Pengimplementasian Data Delivery Menggunakan Django

[Link Apliasi](https://webggniboss.herokuapp.com/mywatchlist/)

## Jelaskan perbedaan antara JSON, XML, dan HTML!

1. JSON

    JSON adalah singkatan dari JavaScript Object Notation. JSON didesain menjadi self-describing, sehingga JSON sangat mudah untuk dimengerti. Umumnya JSON digunakan untuk menyimpan dang mengirimkan data. Sintaks JSON merupakan turunan dari Object JavaScript. Akan tetapi format JSON berbentuk text, sehingga kode untuk membaca dan membuat JSON banyak terdapat dibanyak bahasa pemrograman. JSON digunakan pada banyak aplikasi web dan *mobile*

2. XML

    XML adalah singkatan dari eXtensible Markup Language. XML didesain menjadi self-descriptive, jadi dengan membaca XML tersebut kita bisa mengerti informasi apa yang ingin disampaikan dari data yang tertulis. Sama seperti JSON, XML juga digunakan untuk menyimpan dan mengirimkan data. Namun XML hanyalah informasi yang dibungkus di dalam tag. Kita perlu menulis program untuk mengirim, menerima, menyimpan, atau menampilkan informasi tersebut. XML digunakan pada banyak aplikasi web dan *mobile*.

3. HTML

    HTML adalah sebuah markup language yang digunakan untuk mendefinisikan layout dari sebuah halaman website. Perlu diingat bahwa HTML bukan merupakan programming language, sehingga HTML dengan sendirinya tidak dapat digunakan untuk mendefinisikan control flow seperti pada Python ataupun Java. HTML sendiri berperan sebagai kerangka sebuah website.

## Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Untuk melakukan implementasi *request* dan *response* terhadap data yang ada di dalam database. Jika tidak ada *data delivey*, maka user tidak dapat melihat konten yang mereka inginkan. Hal ini dikarenakan data hanya tersimpan di dalam database namun tidak dikembalikan ke dalam UI.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

1. Membuat aplikasi ```mywatchlist``` pada proyek Django.
2. Menambahkan path 
    ```python
    path('mywatchlist/', include('mywatchlist.urls'))
    ``` 
    pada ```urls.py``` di folder ```project_django```
3. Membuat model ```Mywatchlist``` dengan beberapa atribut seperti yang ada   pada kode berikut 
    ```python
    from django.db import models

    class WatchListItem(models.Model):
        watched = models.CharField(max_length=255)
        title = models.CharField(max_length=255)
        rating = models.IntegerField()
        release_date = models.TextField()
        review = models.TextField()
    ```
4. Menambahkan 10 data untuk objek ```MyWatchList``` pada file ```initial_watchlist_data.json```
    ```json
    [
        {
            "model": "mywatchlist.watchlistitem",
            "pk": 1,
            "fields": {
                "watched": "Watched",
                "title": "The Fast and The Furious (2001)",
                "rating": 10,
                "release_date": "June 22, 2001",
                "review": "Amazing"
            }
        },
        
        {
            "model": "mywatchlist.watchlistitem",
            "pk": 2,
            "fields": {
                "watched": "Watched",
                "title": "2 Fast 2 Furious (2003)",
                "rating": 10,
                "release_date": "June 6, 2003",
                "review": "Amazing"
            }
        },

        {
            "model": "mywatchlist.watchlistitem",
            "pk": 3,
            "fields": {
                "watched": "Watched",
                "title": "The Fast and the Furious: Tokyo Drift (2006)",
                "rating": 10,
                "release_date": "June 16, 2006",
                "review": "Amazing"
            }
        },

        {
            "model": "mywatchlist.watchlistitem",
            "pk": 4,
            "fields": {
                "watched": "Watched",
                "title": "Fast & Furious (2009)",
                "rating": 10,
                "release_date": "April 3, 2009",
                "review": "Amazing"
            }
        },

        {
            "model": "mywatchlist.watchlistitem",
            "pk": 5,
            "fields": {
                "watched": "Watched",
                "title": "Fast Five (2011)",
                "rating": 10,
                "release_date": "April 29, 2011",
                "review": "Amazing"
            }
        },

        {
            "model": "mywatchlist.watchlistitem",
            "pk": 6,
            "fields": {
                "watched": "Watched",
                "title": "Fast & Furious 6 (2013)",
                "rating": 10,
                "release_date": "May 24, 2013",
                "review": "Amazing"
            }
        },

        {
            "model": "mywatchlist.watchlistitem",
            "pk": 7,
            "fields": {
                "watched": "Watched",
                "title": "Furious 7 (2015)",
                "rating": 10,
                "release_date": "April 3, 2015",
                "review": "Amazing"
            }
        },

        {
            "model": "mywatchlist.watchlistitem",
            "pk": 8,
            "fields": {
                "watched": "Watched",
                "title": "The Fate of the Furious (2017)",
                "rating": 10,
                "release_date": "April 14, 2017",
                "review": "Amazing"
            }
        },

        {
            "model": "mywatchlist.watchlistitem",
            "pk": 9,
            "fields": {
                "watched": "Watched",
                "title": "F9 (2021)",
                "rating": 10,
                "release_date": "June 25, 2021",
                "review": "Amazing"
            }
        },

        {
            "model": "mywatchlist.watchlistitem",
            "pk": 10,
            "fields": {
                "watched": "Not watched",
                "title": "Fast X",
                "rating": 0,
                "release_date": "May 19, 2023",
                "review": "None"
            }
        }
    ]
    ```
5. Menambahkan fitur untuk menyajikan data dalam format ```html```  ```xml``` ```json``` dengan memasukkan kode berikut pada ```views.py```
    ```python
    def show_film_list(request):
        data_watchlist = WatchListItem.objects.all()

        watched = WatchListItem.objects.filter(watched="Watched")
        not_watched = WatchListItem.objects.filter(watched="Not watched")

        watched_count = watched.count()
        not_watched_count = not_watched.count()
        
        watched_status = watched_count >= not_watched_count

        context = {
        'list_film': data_watchlist,
        'nama': 'Son Sulung Suryahatta Asnan',
        'id' : '2106751455',
        'status_check' : watched_status,
    }
        return render(request, "mywatchlist.html", context)

    def show_xml(request):
        data = WatchListItem.objects.all()

        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

    def show_json(request):
        data = WatchListItem.objects.all()

        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    ```


## Postman

1. HTML 
    <p align="center"><img src= "https://user-images.githubusercontent.com/95991754/191644934-f7cdaaad-2a9e-4022-91df-977edba705ec.jpg"/></p>

2. JSON
    <p align="center"><img src= "https://user-images.githubusercontent.com/95991754/191645024-126d2219-2583-4073-a607-a666afbb8971.jpg"/></p>

3. XLM
    <p align="center"><img src= "https://user-images.githubusercontent.com/95991754/191645054-de92b121-eef8-4d32-92d7-c50dc72cffca.jpg"/></p>