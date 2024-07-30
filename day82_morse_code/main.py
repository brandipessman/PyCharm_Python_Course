
done = False
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}
while not done:
    decision = str(input('Would you like to encrypt or decrypt? To finish, type "done". : ').upper())

    if decision == 'ENCRYPT':
        english_message = str(input('Enter the message: ').upper())
        cipher = ''
        for char in english_message:
            if char == ' ':
                cipher += " "
            elif char not in MORSE_CODE_DICT.keys():
                cipher += char
            else:
                cipher += MORSE_CODE_DICT[char] + ' '
        print(f'The encrypted message is: {cipher}')


    elif decision == 'DECRYPT':
        cipher_message = str(input('Enter the message: ').upper()) + ' '
        decipher = ''
        cipher_letter = ''
        for char in cipher_message:
            if char != ' ':
                i=0
                cipher_letter += char
            else:
                i += 1
                if i == 2:
                    decipher += ' '
                else:
                    if cipher_letter not in MORSE_CODE_DICT.values():
                        decipher += cipher_letter
                    else:
                        decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(cipher_letter)]
                    cipher_letter = ''
        print(f'The decrypted message is: {decipher}')

    elif decision == "DONE":
        done = True
        print("Goodbye")
    else:
        print('Sorry, that is not an option. Please type "encrypt" or "decrypt".')

