def caesar_cipher(text, shift, mode):
    result = ""

    if mode == "decrypt":
        shift = -shift

    for char in text:

        
        if char.isupper():
            shifted = (ord(char) - ord('A') + shift) % 26
            result += chr(shifted + ord('A'))

        
        elif char.islower():
            shifted = (ord(char) - ord('a') + shift) % 26
            result += chr(shifted + ord('a'))
 
        else:
            result += char

    return result

print("CAESAR CIPHER PROGRAM")
print("-" * 30)

message = input("Enter your message: ")
shift   = int(input("Enter shift value (1-25): "))
mode    = input("Type encrypt or decrypt: ").lower()

output = caesar_cipher(message, shift, mode)

print("\nOriginal :", message)
print("Result   :", output)