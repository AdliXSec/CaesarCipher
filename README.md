<center><h1>Caesar Cipher</h1></center>

<center>

[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

</center>

Sebuah implementasi modular dan teruji dari algoritma enkripsi dan dekripsi Caesar Cipher dengan antarmuka baris perintah (CLI) yang interaktif.

## Tentang Proyek

Caesar Cipher adalah salah satu teknik enkripsi substitusi yang paling sederhana dan dikenal luas. Dalam sandi ini, setiap huruf dalam teks biasa diganti dengan huruf yang posisinya bergeser sejumlah langkah tetap dalam alfabet.

Proyek ini menyediakan alat baris perintah yang bersih, efisien, dan mudah digunakan untuk melakukan enkripsi, dekripsi, dan serangan _brute-force_ pada sandi Caesar.

---

## Fitur

- **Enkripsi**: Mengenkripsi teks menggunakan pergeseran kunci yang ditentukan.
- **Dekripsi**: Mendekripsi teks menggunakan pergeseran kunci yang sama.
- **Brute Force**: Mencoba semua kemungkinan kunci (1-26) untuk mendekripsi pesan secara otomatis.
- **Interaktif**: Dilengkapi antarmuka baris perintah (CLI) yang ramah pengguna.
- **Preservasi Karakter**: Menangani huruf besar dan kecil, serta mempertahankan spasi, angka, dan tanda baca.
- **Teruji**: Dilengkapi dengan suite _unit testing_ yang komprehensif untuk memastikan keandalan.

---

## Instalasi dan Penggunaan

#### 1. Prasyarat

- Python 3.6 atau yang lebih baru.

#### 2. Instalasi

Kloning repositori ini ke mesin lokal Anda:

```bash
git clone https://github.com/AdliXSec/CaesarCipher
cd CaesarCipher
```

#### 3. Menjalankan Aplikasi

Untuk menjalankan aplikasi, gunakan perintah berikut di terminal Anda:

```bash
python main.py
```

Anda akan disambut dengan menu interaktif:

```
Caesar Cipher Program
1. Encrypt
2. Decrypt
3. Brute Force
4. Exit
Choose an option (1-4):
```

Pilih opsi yang diinginkan dan ikuti instruksi yang diberikan di layar.

#### 4. Menjalankan Unit Test

Proyek ini dilengkapi dengan serangkaian tes untuk memastikan semua fungsi berjalan dengan benar. Untuk menjalankan tes, gunakan perintah berikut:

```bash
python -m unittest -v test_main.py
```

Anda akan melihat output yang merinci setiap proses pengujian yang dijalankan.

---

## Struktur Proyek

```
ChaesarChiper/
│
├── .git/
├── main.py         # Skrip utama aplikasi dengan logika dan CLI
├── test_main.py    # Unit test untuk semua fungsionalitas
└── README.md       # Anda sedang membacanya :)
```

---

## Kontribusi

Kontribusi untuk pengembangan proyek ini sangat diterima! Jika Anda memiliki ide untuk perbaikan atau menemukan bug, silakan buka _issue_ atau kirim _pull request_.

1.  _Fork_ repositori ini.
2.  Buat _branch_ fitur baru (`git checkout -b fitur/FiturBaru`).
3.  _Commit_ perubahan Anda (`git commit -m 'Menambahkan FiturBaru'`).
4.  _Push_ ke _branch_ tersebut (`git push origin fitur/FiturBaru`).
5.  Buka _Pull Request_.

---

## Lisensi

Proyek ini dilisensikan di bawah Lisensi MIT. Lihat file `LICENSE` untuk detailnya. (Catatan: Anda mungkin perlu menambahkan file `LICENSE` jika belum ada).

---

## Penulis

- **Naufal Syahruradli**
