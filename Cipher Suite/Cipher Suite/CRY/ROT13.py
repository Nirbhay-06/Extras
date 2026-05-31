import string

def Rot13CipherEncryption(text,key=13):

    CharList = string.ascii_uppercase
    CharList = list(CharList)

    text = text.upper()
    text = list(text)
    cipherText = ""

    for char in text:
        if char not in CharList:
            cipherText = cipherText + char
            continue
        index = (CharList.index(char) + key) % 26
        cipherText = cipherText + CharList[index]

    return cipherText

def Rot13CipherDecryption(text,key=13):

    CharList = string.ascii_uppercase
    CharList = list(CharList)

    text = text.upper()
    text = list(text)
    plainText = ""

    for char in text:
        if char not in CharList:
            plainText = plainText + char
            continue
        index = (CharList.index(char) - key) % 26
        plainText = plainText + CharList[index]

    return plainText



def main():
    
    text = input("Enter a Text to Process: ")

    cipherText = Rot13CipherEncryption(text)
    print(cipherText)

    plainText = Rot13CipherDecryption(cipherText)
    print(plainText)


if __name__ == "__main__":
    main()