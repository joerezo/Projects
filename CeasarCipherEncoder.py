'''

Your task is to write a program which:

asks the user for one line of text to encrypt;
asks the user for a shift value (an integer number from the range 1..25 - note:
you should force the user to enter a valid shift value (don't give up and don't
let bad data fool you!)
prints out the encoded text.

'''
# Caesar cipher.
text = input("Enter your message: ")
offset = int(input("Enter your message offset: "))
cipher = ''
for char in text:
    if not char.isalpha():
        cipher += char
        continue
    if char == char.upper():
        code = ord(char) + offset
        if code > ord('Z'):
            code = code-26
    elif char ==char.lower():
        code = ord(char) + offset
        if code > ord('z'):
            code = code-26
    cipher += chr(code)

print(cipher)
