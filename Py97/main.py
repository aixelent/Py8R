vowels = ["a", "e", "i", "o", "u"]

msg = input("Enter string: ")
msg_without_vowels = ""

for letter in msg:
    if letter in vowels:
        msg_without_vowels += letter

print(msg_without_vowels)
