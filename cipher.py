alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
text=input("enter a word:\n").lower()
shift=int(input("enter number:\n"))
def encrypt(inputt,indext):
    cipher=""
    for letter in inputt:
        position=alphabet.index[letter]
        newposition=position+indext
        newletter=alphabet[newposition]
        cipher+=newletter
    print(f"the text is{cipher}")
encrypt(inputt=text,indext=shift)

