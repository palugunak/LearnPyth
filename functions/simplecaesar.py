import string


shift =3
choice = input("would you like encode or decode?")
word = input("please enter the text")
letters = string.ascii_letters + string.punctuation + string.digits

encoded =""
if choice == "encode":
    for letter in word:
        if letter == "":
            encoded = encoded + ""
        else:
            x = letters.index(letter) + shift
            encoded = encoded + letter(x)

