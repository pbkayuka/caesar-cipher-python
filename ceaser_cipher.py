alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','v','w','x','y','z']

def encrypt(plain_text,shift_key):
    cipher_text = ''
    for char in plain_text:
        if char in alphabets:
           position = alphabets.index(char)
           new_position= (position+shift_key) % 26
           cipher_text+=alphabets[new_position]
        else:
            cipher_text+=char
    print(f"The text after the encryption {cipher_text}")

def decrypt(cipher_text,shift_key):
    plain_text = ''
    for char in cipher_text:
        if char in alphabets:
           position = alphabets.index(char)
           new_position= (position-shift_key) % 26
           plain_text+=alphabets[new_position]
        else:
            plain_text+=char
    print(f"The text after decrytion  is {plain_text}")
wanna_end=False
while not wanna_end:
    what_to_do=input("if u wnat to encrypt type as 'encrypt' or type as 'decrypt': ")
    text=input("enter the text: ").lower()
    shift_key=int(input("enter the shift key: "))
    if what_to_do=="encrypt":
        encrypt(text,shift_key)
    elif what_to_do=="decrypt":
        decrypt(text,shift_key)
    play_again=input("if u wnat to play type 'yes' or type 'no': ")
    if play_again=="no":
        wanna_end=True
        print("thank you! have a nice day")