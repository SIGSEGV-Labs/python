import string

keyboard_characters = list(string.ascii_letters + string.digits + string.punctuation)

key = int(input('Enter the key value which you used for encoding of ther message: '))
message = input('Enter the encrypted message: ')
decrypted_msg = []
length = len(keyboard_characters)

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
