# WRite a program to perform encryptiona nd Decryption Using Playfair technique.
# Take user input for plain text and key from user.

# Importing Modules

import string

# GLOBAL VARIABLE
MAX_ROW = 5
MAX_COLUMN = 5


# FUnctions

#   Function to Generate the KEY matrix
def keyGeneration(keyword):

    character = string.ascii_uppercase
    character = list(character)

 

    #keyString = keyword + character

    for char in keyword:
        if keyword.count(char) != 1:
            index = keyword.rfind(char)
            keyword = keyword[:index] + keyword[index+1:]

    row = 5
    column = 5

    Key = []

    counter = 0



    for i in range(row):
        temp_row = []
        for j in range(column):
            if counter < len(keyword) :
                #print(keyword[counter])
                temp_row.append(keyword[counter])
                counter += 1
            else:
                temp = 0
                for char in character:
                    if char not in keyword:
                        if char == "J":
                            pass
                        else:
                            
                            temp_row.append(char)
                            character[temp] = keyword[0]

                            break;
                    
                    temp += 1

        Key.append(temp_row)

   # for x in Key:
    #    for y in x:
     #       print(f"{y} ",end="")
      #  print()

    return Key

# Function to Balance the Plaintext
def Text_Processing(Plain_text):


    if len(Plain_text)%2 != 0:
        Plain_text = Plain_text + "X"
    
    
    
    Plain = []
    counter = 0
    while counter < (len(Plain_text) - 1):
        temp_row = []

        if (Plain_text[counter] == " "):
            counter += 1
        
        temp_row.append(Plain_text[counter])
        if (Plain_text[counter + 1] == " "):
            counter += 1
            
            
        if Plain_text[counter] == Plain_text[counter+1]:
            temp_row.append("X")
            counter += 1
        else:
            temp_row.append(Plain_text[counter + 1])
            counter += 2 
        Plain.append(temp_row)
        #print(counter)
        
    return Plain

#Function to Convert PlainText to ciphertext
def Encryption(Plain_Text,Key):
    #print(Plain_Text)
    #print(Key)
    cipher_text = []
    for group in Plain_Text:
        char1 = group[0]
        char2 = group[1]

        cipherChar1,CipherChar2 = "",""

        Char1_row,Char1_column = IndexOf(char=char1,Key=Key)
        Char2_row,Char2_column = IndexOf(char=char2,Key=Key)

        if Char1_row == Char2_row:
            if (Char1_column + 1) == MAX_COLUMN:
                cipherChar1 = Key[Char1_row][0]
            else:
                cipherChar1 = Key[Char1_row][Char1_column + 1]
            if (Char2_column + 1) == MAX_COLUMN:
                cipherChar2 = Key[Char1_row][0]
            else:
                cipherChar2 = Key[Char1_row][Char2_column + 1]
        elif Char1_column == Char2_column:
            if (Char1_row + 1) == MAX_ROW:
                cipherChar1 = Key[0][Char1_column]
            else:
                cipherChar1 = Key[Char1_row + 1][Char1_column]
            if (Char2_row + 1) == MAX_ROW:
                cipherChar2 = Key[0][Char1_column]
            else:
                cipherChar2 = Key[Char2_row + 1][Char1_column]
        
        else:
            cipherChar1 = Key[Char1_row][Char2_column]
            cipherChar2 = Key[Char2_row][Char1_column]
        
        temp_row = []
        temp_row.append(cipherChar1)
        temp_row.append(cipherChar2)

        cipher_text.append(temp_row)
    
    return cipher_text

# Functrion to convert list to string.      
def ListToText(LIST):
    Text = ""

    for group in LIST:
        for char in group:
            Text = Text + char
    
    return Text
        
#   Function to find the index of the character from the KEY matix
def IndexOf(char,Key):
    row = 0
    

    for x in Key:
        column = 0
        for y in x:
            if y == char:
                return int(row),int(column)
            column += 1
        row += 1

    return -1, -1

# Function to Decrypt the Ciphertext
def Decryption(CipherText,Key):
    #print(Plain_Text)
    #print(Key)
    PlainText = []
    for group in CipherText:
        char1 = group[0]
        char2 = group[1]

        cipherChar1,CipherChar2 = "",""

        Char1_row,Char1_column = IndexOf(char=char1,Key=Key)
        Char2_row,Char2_column = IndexOf(char=char2,Key=Key)

        if Char1_row == Char2_row:
            if (Char1_column - 1) < 0:
                cipherChar1 = Key[Char1_row][4]
            else:
                cipherChar1 = Key[Char1_row][Char1_column - 1]
            if (Char2_column - 1) < 0:
                cipherChar2 = Key[Char1_row][4]
            else:
                cipherChar2 = Key[Char1_row][Char2_column - 1]
        elif Char1_column == Char2_column:
            if (Char1_row - 1) == -1:
                cipherChar1 = Key[0][Char1_column]
            else:
                cipherChar1 = Key[Char1_row - 1][Char1_column]
            if (Char2_row + 1) == -1:
                cipherChar2 = Key[0][Char1_column]
            else:
                cipherChar2 = Key[Char2_row - 1][Char1_column]
        
        else:
            cipherChar1 = Key[Char1_row][Char2_column]
            cipherChar2 = Key[Char2_row][Char1_column]
        
        temp_row = []
        temp_row.append(cipherChar1)
        temp_row.append(cipherChar2)

        PlainText.append(temp_row)
    
    return PlainText

#   Function to remove the X that is used to Banance the Plain text.
def PlainTextProcessing(Plaintext):
    counter = 0
    length = len(Plaintext)
    Plaintext = list(Plaintext)


    while counter <= length - 1:
        if Plaintext[counter] == "X":
            if counter == length - 1:
                Plaintext[counter] = ""
            
            elif Plaintext[counter - 1] == Plaintext[counter + 1]:
                Plaintext = Plaintext[0:counter] +Plaintext[counter+1:]

            
            else:
                pass
        counter += 1

    return Plaintext

#   Function to encrypt while importing.
def PlayFairEncrypt(plaintext,keyword="MONARCHY"):

    Keyword = keyword.upper()
    print(f"Key: {Keyword}")
    PlainText = plaintext.upper()
    print(f"PlainText: {PlainText}")

    key = keyGeneration(Keyword)
    
    Plain_Text = Text_Processing(PlainText)
    
    Cipher_Text = Encryption(Plain_Text,key)
    

    Cipher_Text = ListToText(Cipher_Text)
    

    return Cipher_Text

# Function to Decrypt while importing.
def PlayFairDecrypt(cipherText,keyword="MONARCHY"):
   
    KeyWord = keyword.upper()

    print(f"Key: {KeyWord}")

    

    CipherText = cipherText.upper()
    print(f"Cipher text: {CipherText}")

    CipherText = Text_Processing(CipherText)
    print(CipherText)

    key = keyGeneration(KeyWord)
    PlainText = Decryption(CipherText,key)

    PlainText = ListToText(PlainText)
    PlainText = PlainTextProcessing(PlainText)
    PlainText = ListToText(PlainText)

    return PlainText


#     MAIN
def main():
    keyword = input("Enter the Keyword: ").upper()
    Key = keyGeneration(keyword)
    Plain_Text = input("Enter the plain text: ").upper()
    Plain_Text = Text_Processing(Plain_Text)
    print()
    print()
    print(f"Text after processing: ",end=" ")

    for row in Plain_Text:
        for char in row:
            print(char,end="")


    Cipher_Text = Encryption(Plain_Text,Key)
    print(f"\n\nCipher Text: ",end=" ")

    Cipher_Text = ListToText(Cipher_Text)
            

    print(f"Cipher Text: {Cipher_Text}")
    Cipher_Text = Text_Processing(Cipher_Text)

    PlainText = Decryption(CipherText=Cipher_Text,Key=Key)

    PlainText = ListToText(PlainText)
    
    PlainText = PlainTextProcessing(PlainText)

    PlainText = ListToText(PlainText)


    print(f"Plain text: {PlainText}")

    
# this is used to only run the Main code if this file is executed from the current file.
if __name__ == "__main__":
    main()


