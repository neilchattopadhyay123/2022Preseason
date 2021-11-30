text = input("Enter your Text: ")
print(text)

for character in text:
  print(str(ord(character)).zfill(3))
