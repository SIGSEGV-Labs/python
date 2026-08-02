import string

keyboard_characters = list(string.ascii_letters + string.digits + string.punctuation)
length = len(keyboard_characters)

print('Yo wassup welcome to caesar cipher program by Deva go try it yourself it looks cool right:)')

def encoder():
    key = int(input('Enter the key value for the encoding of the message: '))
    message = input('Enter the message to be encrypted: ')
    encrypted_msg = []

    for i in message:
        if i == ' ':
            encrypted_msg.append(' ')
            continue
        if i in keyboard_characters:
            index = (keyboard_characters.index(i) + key)%length
            encrypted_msg.append(keyboard_characters[index])
        else:
            encrypted_msg.append(i)
    encrypted_msg = "".join(encrypted_msg)
    print('\nThe encrypted message is: ' + encrypted_msg)
    print(f'Key used: {key}')
    print('--> Copy the message above and paste it into option 2 (Decode message) to decrypt it!\n')

def decoder():
    key = int(input('Enter the key value which you used for encoding of the message: '))
    message = input('Enter the encrypted message: ')
    decrypted_msg = []

    for i in message:
        if i == ' ':
            decrypted_msg.append(' ')
            continue
        if i in keyboard_characters:
            index = (keyboard_characters.index(i) - key)%length
            decrypted_msg.append(keyboard_characters[index])
        else:
            decrypted_msg.append(i)
    decrypted_msg = "".join(decrypted_msg)
    print('The decrypted message is: ' + decrypted_msg)

while True:
    print('\n1. Encode message')
    print('2. Decode message')
    res = input('Enter your choice (1 or 2 to continue, any other key to exit): ')

    if res == '1':
        encoder()
    elif res == '2':
        decoder()
    else:
        print('Exiting program. Goodbye!')
        break
