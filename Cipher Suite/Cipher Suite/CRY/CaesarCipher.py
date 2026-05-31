import string

def CeaserCipherEncryption(text,key):

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

def CeaserCipherDecryption(text,key):

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
    key = int(input("Enter a Key Rotation Value: "))
    text = input("Enter a Text to Process: ")

    cipherText = CeaserCipherEncryption(text,key)
    print(cipherText)

    plainText = CeaserCipherDecryption(cipherText,key)
    print(plainText)


if __name__ == "__main__":
    main()