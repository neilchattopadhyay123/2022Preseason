text = input("Enter your Text: ")
binary = ''.join(format(ord(i), 'b') for i in text)
print(str(binary))
