alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(msg, s, cipher_type):
    final_text = ""
    if cipher_type == "decode":
        s *= -1
    for letter in msg:
        position = alphabet.index(letter)
        new_position = position + s
        final_text += alphabet[new_position]
    print(f"The {cipher_type}d message is: {final_text}")


caesar(msg=text, s=shift, cipher_type=direction)