import string

keyboard_characters = list(string.ascii_letters + string.digits + string.punctuation)

key = int(input('Enter the key value for the encoding of ther message: '))
message = input('Enter the message to be encrypted: ')
encrypted_msg = []
length = len(keyboard_characters)

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
print('The encrypted message is: ' + encrypted_msg)
print('Give this string and key to the decoder to get your message back :)')
