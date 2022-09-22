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
2. Menambahkan path ```path('mywatchlist/', include('mywatchlist.urls'))``` pada ```urls.py``` di folder ```project_django```

## Postman

1. HTML 
    <p align="center"><img src= "https://user-images.githubusercontent.com/95991754/191644934-f7cdaaad-2a9e-4022-91df-977edba705ec.jpg"/></p>

2. JSON
    <p align="center"><img src= "https://user-images.githubusercontent.com/95991754/191645024-126d2219-2583-4073-a607-a666afbb8971.jpg"/></p>

3. XLM
    <p align="center"><img src= "https://user-images.githubusercontent.com/95991754/191645054-de92b121-eef8-4d32-92d7-c50dc72cffca.jpg"/></p>