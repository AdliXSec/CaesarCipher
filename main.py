import sys

"""
Plaintext saya : Kapal berhenti di pelabuhan
Chipertext saya :

Plaintext kelompok lain :
Chipertext kelompok lain : lcncpmcmkdgtucocvgocp
"""


def caesar_cipher(text, shift, mode='encrypt'):
    if mode == 'decrypt':
        shift = -shift

    result = ""
    for char in text:
        if char.isalpha():
            start_ascii = ord('A') if char.isupper() else ord('a')
            # Formula: (Start Position + Shift) % 26 + Base
            new_char = chr((ord(char) - start_ascii + shift) % 26 + start_ascii)
            result += new_char
        else:
            result += char
    return result

def brute_force(text):
    print("\n--- Brute Force Results ---")
    for i in range(1, 27):
        decrypted_text = caesar_cipher(text, i, mode='decrypt')
        print(f"Key {i:2}: {decrypted_text}")

def main():
    print("Caesar Cipher Program")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Brute Force")
    print("4. Exit")

    while True:
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            message = input("Enter the message: ")
            try:
                key = int(input("Enter the key (1-26): "))
                encrypted = caesar_cipher(message, key, 'encrypt')
                print(f"\nPlaintext: {message}")
                print(f"Ciphertext: {encrypted}\n")
            except ValueError:
                print("Invalid key. Please enter a number.\n")
        
        elif choice == '2':
            message = input("Enter the message: ")
            try:
                key = int(input("Enter the key (1-26): "))
                decrypted = caesar_cipher(message, key, 'decrypt')
                print(f"\nCiphertext: {message}")
                print(f"Decoded text: {decrypted}\n")
            except ValueError:
                print("Invalid key. Please enter a number.\n")

        elif choice == '3':
            message = input("Enter the ciphertext to brute force: ")
            brute_force(message)
            print()

        elif choice == '4':
            print("Exiting the program.")
            sys.exit()

        else:
            print("Invalid option. Please choose between 1 and 4.\n")

if __name__ == "__main__":
    main()