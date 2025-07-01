# Caesar Cipher — Python Encryption & Decryption Tool

This project is a simple command-line tool for encrypting and decrypting messages using the **Caesar Cipher** algorithm. The Caesar Cipher is a classic substitution cipher where each letter in the plaintext is shifted by a fixed number of positions down the alphabet.

## Features

- Encrypt any message by shifting its letters by a user-defined value
- Decrypt messages by reversing the shift
- Preserves case (uppercase/lowercase)
- Non-alphabetic characters (spaces, punctuation) remain unchanged
- Easy-to-use menu-driven interface

## How It Works

- **Encryption:** Each letter is shifted forward in the alphabet by the given number (the "shift value").
- **Decryption:** Each letter is shifted backward by the same value.
- The script uses modulo arithmetic to wrap around the alphabet as needed.

## Example

```
1:Encryption
2:Decryption
Enter your choice: 1
Enter your message: Hello World!
Enter required shift value: 1
The Encrypted Message is:  Ifmmp Xpsme!
```

```
1:Encryption
2:Decryption
Enter your choice: 2
Enter your message: Ifmmp Xpsme!
Enter required shift value: 1
The Decrypted Message is: Hello World!
```

## Usage

1. **Clone or download this repository.**
2. **Run the script:**
    ```bash
    python caesar_cipher.py
    ```
3. **Follow the prompts** to choose encryption or decryption, enter your message, and specify the shift value.

## Requirements

- Python 3.x (no external dependencies)

## Algorithm Reference

- **Encryption:**  
  For each letter:  
  encrypted = original position + shift \mod 26 
- **Decryption:**  
  For each letter:  
  decrypted = original position - shift\mod 26

## Security Note

The Caesar Cipher is a basic cryptographic technique and **not suitable for securing sensitive information**. It is best used for educational purposes and simple puzzles.

