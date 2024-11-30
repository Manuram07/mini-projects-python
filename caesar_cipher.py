alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.
# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.

def encrypt(text,shift):
    for i in text:
        for j in range(0,len(alphabet)):
            if i==alphabet[j] and j<-shift:
                print(alphabet[j+shift],end="")
            elif i==alphabet[j] and j > -shift:
                print(alphabet[j+shift-26],end="")
def decrypt(text,shift):
    for i in text:
        for j in range(0,len(alphabet)):
            if i==alphabet[j] and j >  -shift:
                print(alphabet[j-shift],end="")
            elif i==alphabet[j] and j < -shift:
                print(alphabet[j-shift+26],end="")
if direction =="encode":
    encrypt(text,shift)
elif direction=="decode":
    decrypt(text,shift)
    
    
'''
import art
print(art.cclogo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# TODO-2: What happens if the user enters a number/symbol/space?


def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else:

            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")


# TODO-3: Can you figure out a way to restart the cipher program?
con=True
while(con == True):

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    restart=input("Type 'yes' if you want to go again. Otherwise, type 'no'.").lower()
    if restart=="no":
        con=False
        print("good bye")
    elif restart=="yes":
        con=True
    else:
        print("you have entered a wrong decision")
        con=False

'''