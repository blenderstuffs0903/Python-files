alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt\n").lower().strip()

text = input("Type your message\n").lower().strip()
shift = int(input("Type the shift number\n"))


def caesar(start_text, shift_amount, cypher_direction):
    end_text = ''
    if cypher_direction == "decode":
        shift_amount *= -1
    for letter in start_text:
        if letter.isspace():
            end_text += letter
        else:
            index = alphabet.index(letter)
            if index + shift_amount > len(alphabet) - 1:
                while index + shift_amount > len(alphabet) - 1:
                    shift_amount -= len(alphabet)
                end_text += alphabet[(index + shift_amount)]
            elif index - shift_amount < -26:
                while index - shift_amount < -26:
                    end_text += len(alphabet)
                end_text += alphabet[(index - shift_amount)]
            elif cypher_direction == "encode" or "decode":
                end_text += alphabet[index + shift_amount]
    print(end_text)


def encrypt(text, shift):
    s_text = ''
    for char in text:
        if char.isspace():
            s_text += char
        else:
            index = alphabet.index(char)
            if index + shift > len(alphabet) - 1:
                s_text += alphabet[(index + shift) - len(alphabet)]
            else:
                s_text += alphabet[index + shift]
    print(s_text)


def decrypt(text, shift):
    s_text = ''
    for char in text:
        if char.isspace():
            s_text += char
        else:
            index = alphabet.index(char)
            s_text += alphabet[index - shift]
    print(s_text)


caesar(text, shift, direction)

