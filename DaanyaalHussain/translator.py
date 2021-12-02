text = input("Enter your Text: ")
print(text)
final_output = ''

for character in text:
  newcharacter = str(ord(character)).zfill(3)
  final_output += newcharacter + ' '
  
print(final_output)
