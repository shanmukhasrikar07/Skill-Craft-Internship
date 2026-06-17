
def encrypt(message, key):
    encrypted = ""
    for char in message:
        encrypted = encrypted + chr(ord(char) ^ key)
    return encrypted

def decrypt(encrypted_message, key):
    decrypted = ""
    for char in encrypted_message:
        decrypted = decrypted + chr(ord(char) ^ key)
    return decrypted



print("IMAGE ENCRYPTION TOOL")
print("-" * 30)
print("1. Encrypt message")
print("2. Decrypt message")

choice  = input("Enter choice (1 or 2): ")
message = input("Enter your message: ")
key     = int(input("Enter key (1 to 100): "))

if choice == '1':
    result = encrypt(message, key)
    print("Encrypted:", result)

elif choice == '2':
    result = decrypt(message, key)
    print("Decrypted:", result)

else:
    print("Wrong choice!!")