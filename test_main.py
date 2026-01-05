import unittest
import io
import sys
from main import caesar_cipher, brute_force

class TestCaesarCipher(unittest.TestCase):

    def test_encrypt_basic(self):
        text, key, expected = "abc", 3, "def"
        sys.stderr.write(f"\n  Process: Encrypt '{text}' with key {key}. Expected: '{expected}'")
        self.assertEqual(caesar_cipher(text, key, 'encrypt'), expected)

    def test_decrypt_basic(self):
        text, key, expected = "def", 3, "abc"
        sys.stderr.write(f"\n  Process: Decrypt '{text}' with key {key}. Expected: '{expected}'")
        self.assertEqual(caesar_cipher(text, key, 'decrypt'), expected)

    def test_encrypt_with_wrapping(self):
        text, key, expected = "xyz", 3, "abc"
        sys.stderr.write(f"\n  Process: Encrypt '{text}' with wrap-around. Expected: '{expected}'")
        self.assertEqual(caesar_cipher(text, key, 'encrypt'), expected)

    def test_decrypt_with_wrapping(self):
        text, key, expected = "abc", 3, "xyz"
        sys.stderr.write(f"\n  Process: Decrypt '{text}' with wrap-around. Expected: '{expected}'")
        self.assertEqual(caesar_cipher(text, key, 'decrypt'), expected)

    def test_case_preservation(self):
        text, key, expected = "HeLLo", 5, "MjQQt"
        sys.stderr.write(f"\n  Process: Preserve case in '{text}'. Expected: '{expected}'")
        self.assertEqual(caesar_cipher(text, key), expected)

    def test_with_spaces_and_punctuation(self):
        text, key, expected = "Hello, World! 123", 5, "Mjqqt, Btwqi! 123"
        sys.stderr.write(f"\n  Process: Preserve non-alpha chars in '{text}'.")
        self.assertEqual(caesar_cipher(text, key), expected)

    def test_no_shift(self):
        text, key, expected = "Hello, World!", 0, "Hello, World!"
        sys.stderr.write(f"\n  Process: No shift (key 0) on '{text}'.")
        self.assertEqual(caesar_cipher(text, key), expected)

    def test_large_shift(self):
        text, key, expected = "abc", 29, "def"
        sys.stderr.write(f"\n  Process: Large shift (key {key}) on '{text}'. Expected: '{expected}'")
        self.assertEqual(caesar_cipher(text, key, 'encrypt'), expected)

    def test_empty_string(self):
        text, key, expected = "", 5, ""
        sys.stderr.write(f"\n  Process: Handle empty string. Expected: ''")
        self.assertEqual(caesar_cipher(text, key), expected)

    def test_non_alphabetic_string(self):
        text, key, expected = "123!@#$%", 5, "123!@#$%"
        sys.stderr.write(f"\n  Process: Handle non-alphabetic string '{text}'.")
        self.assertEqual(caesar_cipher(text, key), expected)

    def test_all_letters_encryption_decryption(self):
        original, key = "The quick brown fox jumps over the lazy dog", 17
        sys.stderr.write(f"\n  Process: Full cycle encrypt/decrypt on '{original[:20]}...'")
        encrypted = caesar_cipher(original, key)
        decrypted = caesar_cipher(encrypted, key, 'decrypt')
        self.assertEqual(decrypted, original)

    def test_negative_shift_encryption(self):
        text, key = "abc", -3
        sys.stderr.write(f"\n  Process: Equivalence of negative shift key {key}.")
        self.assertEqual(caesar_cipher(text, key, 'encrypt'), caesar_cipher(text, abs(key), 'decrypt'))

    def test_brute_force_output(self):
        original_message, key = "this is a secret", 10
        encrypted_message = caesar_cipher(original_message, key)
        sys.stderr.write(f"\n  Process: Brute force on '{encrypted_message}' finds '{original_message}'.")
        
        captured_output = io.StringIO()
        sys.stdout = captured_output
        brute_force(encrypted_message)
        sys.stdout = sys.__stdout__
        
        output = captured_output.getvalue()
        self.assertIn(original_message, output)
        self.assertIn(f"Key {key:2}: {original_message}", output)

if __name__ == '__main__':
    unittest.main()
