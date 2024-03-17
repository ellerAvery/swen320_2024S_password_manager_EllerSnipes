# https://www.tutorialspoint.com/cryptography_with_python/cryptography_with_python_quick_guide.htm

from cryptography.fernet import Fernet

class SecureCipher():
    def __init__(self):
        self.key = Fernet.generate_key()
        self.cipher_suite = Fernet(self.key)

    def encrypt(self, text):
        if not isinstance(text, bytes):
            text = text.encode('utf-8')
        encrypted_text = self.cipher_suite.encrypt(text)
        return encrypted_text.decode('utf-8')

    def decrypt(self, encrypted_text):
        if not isinstance(encrypted_text, bytes):
            encrypted_text = encrypted_text.encode('utf-8')
        decrypted_text = self.cipher_suite.decrypt(encrypted_text)
        return decrypted_text.decode('utf-8')
