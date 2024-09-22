def main():
    print("1:Encryption")
    print("2:Decryption")
    choice=int(input("Enter your choice: "))
    message=input("Enter your message: ")
    shift=int(input("Enter required shift value: "))
    if choice==1:
        encrypted_message=caesar_cipher(message, shift)
        print("The Encrypted Message is: ", encrypted_message)
    else:
        decrypted_message=caesar_cipher(message, -shift)
        print("The Decrypted Message is:", decrypted_message)
def caesar_cipher(text, shift):
    result=""
    for char in text:
        if char.isalpha():
            is_upper=char.isupper()
            shifted_char=chr((ord(char) - ord('A'if is_upper else 'a') + shift) %26 + ord('A' if is_upper else 'a'))
            result+=shifted_char
        else:
            result+=char
    return result
if __name__=="__main__":
    main()