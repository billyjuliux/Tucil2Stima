# Penjelasan Algoritma Decrease and Conquer
Setelah data input diolah menjadi sebuah graf, Algoritma Decrease and Conquer diimplementasikan pada *Topological Sort* dengan mengurangi instansi persoalan dengan me-*print* edge/elemen yang memiliki *in degree* bernilai 0. Selanjutnya, edge yang ditunjuk oleh edge ini dikurangi *in degree* nya sebanyak 1. Dicari kembali edge yang memiliki *in degree* bernilai 0, seterusnya sampai semua edge ter-*print* keluar.

# Requirement Program dan Instalasi
Project ini tidak menggunakan instalasi tambahan apapun selain bahasa python3.

# Cara Menggunakan Program
Pindah ke direktori **folder src** dari project ini, lalu jalankan **python3 13519094.py <nama_testcase>.txt**. Misal : python3 13519094.py 1.txt.

# Author
Billy Julius - 13519094
