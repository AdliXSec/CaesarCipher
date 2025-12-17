# Caesar Cipher

Sebuah implementasi sederhana dari algoritma enkripsi dan dekripsi Caesar Cipher.

## Tentang Caesar Cipher

Caesar Cipher adalah salah satu teknik enkripsi yang paling sederhana dan dikenal luas. Ini adalah jenis sandi substitusi di mana setiap huruf dalam teks biasa diganti dengan huruf yang posisinya bergeser sejumlah tetap dalam alfabet. Misalnya, dengan pergeseran kiri 3, D akan diganti dengan A, E akan menjadi B, dan seterusnya.

## Fitur

- Mengenkripsi teks menggunakan kunci pergeseran yang ditentukan.
- Mendekripsi teks menggunakan kunci pergeseran yang sama.
- Menangani huruf besar dan huruf kecil.
- Mempertahankan spasi dan karakter non-alfabet.
- Fitur bruteforce tanpa mengetahui key / substitusi

## Cara Menggunakan

1.  **Kloning repositori:**

    ```bash
    git clone https://github.com/AdliXSec/CaesarCipher
    cd CaesarCipher
    ```

2.  **Jalankan skrip:**
    Anda biasanya akan menjalankan skrip dari terminal Anda, dengan menyediakan teks untuk dienkripsi/dekripsi dan kunci pergeseran.

    **Contoh untuk Penggunaan:**

    ```bash
    python main.py

    Masukkan pesan: Kapal berhenti di pelabuhan
    Masukkan key: 19

    Plaintext : Kapal berhenti di pelabuhan
    Ciphertext: Dtite uxkaxgmb wb ixetunatg
    --------------------
    Decode    : Kapal berhenti di pelabuhan
    --------------------
    ```

    **Contoh hasil Bruteforce:**

    ```
    Brute Force

    Cshsd twjzwfla va hwdstmzsf, Key : 1
    Brgrc sviyvekz uz gvcrslyre, Key : 2
    Aqfqb ruhxudjy ty fubqrkxqd, Key : 3
    Zpepa qtgwtcix sx etapqjwpc, Key : 4
    Yodoz psfvsbhw rw dszopivob, Key : 5
    Xncny oreuragv qv crynohuna, Key : 6
    Wmbmx nqdtqzfu pu bqxmngtmz, Key : 7
    Vlalw mpcspyet ot apwlmfsly, Key : 8
    Ukzkv lobroxds ns zovklerkx, Key : 9
    Tjyju knaqnwcr mr ynujkdqjw, Key : 10
    Sixit jmzpmvbq lq xmtijcpiv, Key : 11
    Rhwhs ilyoluap kp wlshibohu, Key : 12
    Qgvgr hkxnktzo jo vkrghangt, Key : 13
    Pfufq gjwmjsyn in ujqfgzmfs, Key : 14
    Oetep fivlirxm hm tipefyler, Key : 15
    Ndsdo ehukhqwl gl shodexkdq, Key : 16
    Mcrcn dgtjgpvk fk rgncdwjcp, Key : 17
    Lbqbm cfsifouj ej qfmbcvibo, Key : 18
    Kapal berhenti di pelabuhan, Key : 19
    Jzozk adqgdmsh ch odkzatgzm, Key : 20
    Iynyj zcpfclrg bg ncjyzsfyl, Key : 21
    Hxmxi yboebkqf af mbixyrexk, Key : 22
    Gwlwh xandajpe ze lahwxqdwj, Key : 23
    Fvkvg wzmcziod yd kzgvwpcvi, Key : 24
    Eujuf vylbyhnc xc jyfuvobuh, Key : 25
    Dtite uxkaxgmb wb ixetunatg, Key : 26
    ```

## Penjelasan Kode (untuk pengembang)

Bagian ini secara singkat menjelaskan logika inti dari implementasi Caesar Cipher:

- `char.isalpha()`: Memeriksa apakah suatu karakter adalah huruf alfabet.
- `ord('A')`: Mengembalikan nilai integer ASCII/Unicode dari karakter 'A'. Digunakan untuk menghitung posisi huruf dalam alfabet (indeks 0).
- `chr()`: Mengonversi integer (nilai ASCII/Unicode) kembali menjadi karakter.

## Penulis

Naufal Syahruradli
