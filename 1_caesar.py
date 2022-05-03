def caesar(string, shift):
    caesar = ''
    for char in string:
        if char == ' ':
            caesar = caesar + char
        elif char.isupper():
            caesar = caesar + chr(((ord(char) -65 ) + shift) % 26 + 65)
        elif char.islower():
            caesar = caesar + chr(((ord(char) -97 ) + shift) % 26 + 97)
        else:
            caesar = caesar + char
    return caesar

text = input ("Enter String to Encrypt: ")
shift = int(input("Enter shift number: "))
print("Caesar Cipher: ", caesar(text, shift))
