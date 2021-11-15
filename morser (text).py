""""""
MORSE_CODE_DICT = {
    'A':'.-',
    'B':'-...',
    'C':'-.-.',
    'D':'-..',
    'E':'.',
    'F':'..-.',
    'G':'--.',
    'H':'....',
    'I':'..',
    'J':'.---',
    'K':'-.-',
    'L':'.-..',
    'M':'--',
    'N':'-.',
    'O':'---',
    'P':'.--.',
    'Q':'--.-',
    'R':'.-.',
    'S':'...',
    'T':'-',
    'U':'..-',
    'V':'...-',
    'W':'.--',
    'X':'-..-',
    'Y':'-.--',
    'Z':'--..',
    '1':'.----',
    '2':'..---',
    '3':'...--',
    '4':'....-',
    '5':'.....',
    '6':'-....',
    '7':'--...',
    '8':'---..',
    '9':'----.',
    '0':'-----',
}


def encryptor(text):
    encrypted_text = ""
    try:
        for letters in text:
            if letters != " ":
                encrypted_text = encrypted_text + MORSE_CODE_DICT.get(letters) + " "
            else:
                encrypted_text += " "
        print(encrypted_text)
    except TypeError:
        print("Please enter only Alphabets [A-Z] and Numbers [0-9]")


def decryptor(text):
    text += " "
    key_list = list(MORSE_CODE_DICT.keys())
    val_list = list(MORSE_CODE_DICT.values())
    morse = ""
    normal = ""
    try:
        for letters in text:
            if letters != " ":
                morse += letters
                space_found = 0
            else:
                space_found += 1
                if space_found == 2:
                    normal += " "
                else:
                    normal = normal + key_list[val_list.index(morse)]
                    morse = ""
        print(normal)
    except ValueError:
        print("Please enter only DOTS [.] and DASHES [-]")

print("\nWelcome to Morser\nDeveloped by Ayan Saha \nv1.0.0, 2021\n")
ch = input("SELECT \n [E] To Encrypt \n [D] To Decrypt : ")
if ch == 'E' or ch == 'e':
    text_to_encrypt = input("Enter Text To Encrypt : ").upper()
    encryptor(text_to_encrypt)
elif ch == 'D' or ch == 'd':
    text_to_decrypt = input("Enter Morse Code to Decrypt : ")
    decryptor(text_to_decrypt)
else:
    print("Incorrect option chosen!!")