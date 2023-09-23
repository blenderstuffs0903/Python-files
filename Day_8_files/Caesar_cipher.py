alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cypher_direction):
    end_text = ''
    if cypher_direction == "decode":
        shift_amount *= -1
    for letter in start_text:
        if letter not in alphabet:
            end_text += letter
        else:
            index = alphabet.index(letter)
            if index + shift_amount > len(alphabet) - 1:
                end_text += alphabet[(index + shift_amount) - len(alphabet)]
            elif cypher_direction == "encode" or "decode":
                end_text += alphabet[index + shift_amount]
    print(end_text)


while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt\n").lower().strip()

    text = input("Type your message\n").lower().strip()
    shift = int(input("Type the shift number\n"))

    if shift > 25:
        shift %= 25
    caesar(text, shift, direction)
    go_again = input("Type 'yes' if you want to go again, otherwise type 'no'.").strip().lower()
    if go_again[0] == 'n':
        print("Goodbye")
        break





