def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    if mode == 'bruteforce':
        for i in range(1, 27):
            for char in text:
                if char.isalpha():
                    start_ascii = ord('A') if char.isupper() else ord('a')
                    new_char = chr((ord(char) - start_ascii + -i) % 26 + start_ascii)
                    result += new_char
                else:
                    result += char
            result += ', Key : ' + str(i) + '\n'

    if mode == 'decrypt':
        shift = -shift
        for char in text:
            if char.isalpha():
                start_ascii = ord('A') if char.isupper() else ord('a')
                # Rumus: (Posisi Awal + Shift) % 26 + Basis
                new_char = chr((ord(char) - start_ascii + shift) % 26 + start_ascii)
                result += new_char
            else:
                result += char

    if mode == 'encrypt':
        for char in text:
            if char.isalpha():
                start_ascii = ord('A') if char.isupper() else ord('a')
                # Rumus: (Posisi Awal + Shift) % 26 + Basis
                new_char = chr((ord(char) - start_ascii + shift) % 26 + start_ascii)
                result += new_char
            else:
                result += char

    return result

pesan_asli = input("Masukkan pesan: ")
key = int(input("Masukkan key: "))

enkripsi = caesar_cipher(pesan_asli, key, mode='encrypt')
print(f"\nPlaintext : {pesan_asli}")
print(f"Ciphertext: {enkripsi}")

print("-" * 20)
dekripsi = caesar_cipher(enkripsi, key, mode='decrypt')
print(f"Decode    : {dekripsi}")

print("-" * 20)
brute = caesar_cipher(enkripsi, key, mode='bruteforce')
print("Brute Force\n")
print(brute)