
import string

# Funcction to convert cipherText to PlainText
def Decryption(keyword,cipherText):
    charList = list(string.ascii_uppercase)
    cipherText = list(textProcessing(cipherText.upper()))
    keyword = list(keyword.upper())
    plainText = []

    counter = 0
    for char in cipherText:
        plainText.append(charList[(charList.index(char) - charList.index(keyword[counter])) % 26])
        counter += 1
        if counter == len(keyword):
            counter = 0
        
    
    return listTOstring(plainText)
    

# Function to convert the plaintext into cipherText
def Encryption(keyword,plainText):
    plainText = list(textProcessing(plainText))
   # keyword = keywordProcessing(keyword.upper(),plainText)
    keyword = list(keyword.upper())
    charList = list(string.ascii_uppercase)
    cipherText = []
    counter = 0
    for char in plainText:
        cipherText.append(charList[(charList.index(char) + charList.index(keyword[counter])) % 26])
        counter += 1
        if counter == len(keyword):
            counter = 0
    

    return listTOstring(cipherText)


def listTOstring(List):
    text = ""

    for char in List:
        text += char
    
    return text


# this function is used to remove the spaces and any Symbol
def textProcessing(text):
    text = text.upper()
    charList = string.ascii_uppercase

    P_text = ""

    
    for char in text:
        if char not in charList:
            continue
        P_text = P_text + char

    return P_text


def main():
    keyword = input("Enter a Keyword: ")
    plaintext = input("Enter Plain text: ")

    #plaintext = textProcessing(plaintext)
    #key = keywordProcessing(keyword,plaintext)

    ciphertext = Encryption(keyword,plaintext)
    

    print(keyword)
    print(plaintext)
    print(ciphertext)

    PlainText = Decryption(keyword,ciphertext)
    print(PlainText)

if __name__ == "__main__":
    main()