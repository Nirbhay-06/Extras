#------PYQT5 Files
import sys

from PyQt5.QtWidgets import (
    QLineEdit,QApplication,QMainWindow,
    QLabel,QPushButton,QWidget,
    QHBoxLayout,QVBoxLayout,QGridLayout,
    QStackedWidget,QPlainTextEdit,QSpinBox,QTextEdit,
    QScrollArea
)
from PyQt5.QtCore import Qt

#----MY FILES
from CRY import (
    Playfair as PF,
    CaesarCipher as CC,
    VigenereCipher as VC,
    ROT13 as RT
)



#-------- Home Page
class HomePage(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):    
        MainLayout = QVBoxLayout(self)
        MainLayout.setSpacing(15)

        Heading = QLabel("Information About CryptoGraphy")
        Heading.setStyleSheet(
            "font-family: OCR-A;"
            "font-size: 25px;"
            "font-weight: bold;"
        )
        MainLayout.addWidget(Heading)


        #------------Information About Playfair Cipher Technique
        
        playfairTitle = QLabel("PlayFair Cipher")
        playfairTitle.setStyleSheet(
            "font-size: 20px;"
            "font-weight: bold;"
            
        )
        MainLayout.addWidget(playfairTitle)

        playfairInfo = QLabel("The Playfair Cipher is a classical symmetric encryption technique that encrypts pairs of letters (digraphs) instead of single letters. This makes it stronger than simple substitution ciphers like Caesar.")
        playfairInfo.setWordWrap(True)
        playfairInfo.setStyleSheet(
            "font-size: 15px;"
            
        )
        MainLayout.addWidget(playfairInfo)
        

        #------------ INformation About Caesar Cipher

        caesarTitle = QLabel("Caesar Cipher")
        caesarTitle.setStyleSheet(
            "font-size: 20px;"
            "font-weight: bold;"
        )
        MainLayout.addWidget(caesarTitle)


        caesarInfo = QLabel("The Caesar Cipher is one of the simplest encryption techniques in cryptography. It’s a substitution cipher where each letter in the message is shifted by a fixed number of positions in the alphabet.")
        caesarInfo.setWordWrap(True)
        caesarInfo.setStyleSheet(
            "font-size: 15px;"
            
        )
        MainLayout.addWidget(caesarInfo)

        vigenereTitle = QLabel("Vigenere Cipher")
        vigenereTitle.setStyleSheet(
            "font-size: 20px;"
            "font-weight: bold;"
            
        )
        MainLayout.addWidget(vigenereTitle)

        vigenereInfo = QLabel("The Vigenère cipher is a polyalphabetic substitution method using a repeating keyword. Each plaintext letter is shifted by the numerical value of the corresponding key letter (A=0 to Z=25). Encryption adds values modulo 26; decryption subtracts them. It improves security over Caesar cipher but remains vulnerable to statistical cryptanalysis techniques.")
        vigenereInfo.setWordWrap(True)
        vigenereInfo.setStyleSheet(
            "font-size: 15px;"
            
        )
        MainLayout.addWidget(vigenereInfo)

        rot13Info = QLabel("ROT 13")
        rot13Info.setStyleSheet(
            "font-size: 20px;"
            "font-weight: bold;"
            
        )
        MainLayout.addWidget(rot13Info)

        rot13Info = QLabel("The algorithm replaces each letter in the alphabet with the one that stands 13 positions after it. Since the English alphabet has 26 letters, applying ROT13 twice brings you right back to the original text. This makes the encryption and decryption processes identical.")
        rot13Info.setWordWrap(True)
        rot13Info.setStyleSheet(
            "font-size: 15px;"
            
        )
        MainLayout.addWidget(rot13Info)







#---------Playfair Cipher Page
class PlayFairCipher(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        layout = QVBoxLayout(self)
        layout.setSpacing(10)

    

        #----------Title
        heading = QLabel("PLayFair Cipher",self)
        heading.setAlignment(Qt.AlignCenter)
        heading.setStyleSheet(
            "font-family: Impact;"
            "font-weight: bold;"
            "font-style: italic;"
            "font-size:40px;"
        )
        layout.addWidget(heading)
        layout.addSpacing(5)


        #----------Text Input for Keyword

        KeywordLayout = QHBoxLayout()
        self.Keyword = QLineEdit()
        self.Keyword.setPlaceholderText("")
        
        label2 = QLabel("Enter a Keyword",self)
        label2.setStyleSheet(
            "font-family: Impact;"
            "font-size:20px;"
        )

        KeywordLayout.addWidget(label2)
        KeywordLayout.addWidget(self.Keyword)

        layout.addLayout(KeywordLayout)

        #-----------Text Box for PlainText or CipherText

        label3 = QLabel("Enter Text ")
        label3.setStyleSheet(
            "font-family: Impact;"
            "font-size:20px;"
        )

        self.Text = QPlainTextEdit()
        self.Text.setPlaceholderText("Plain Text / Cipher Text")
        self.Text.setMinimumHeight(60)

        textLayout = QHBoxLayout()
        
        textLayout.addWidget(label3)
        textLayout.addWidget(self.Text)

        layout.addLayout(textLayout)

        #---------Buttons 
        buttonLayout = QVBoxLayout()


        #-----For encryption
        encrypt = QPushButton("Encrypt")
        buttonLayout.addWidget(encrypt)

        encrypt.clicked.connect(self.encryption)


        #-----For Decryption
        decrypt = QPushButton("Decrypt")
        buttonLayout.addWidget(decrypt)
        decrypt.clicked.connect(self.decryption)

        layout.addLayout(buttonLayout)


        #---------OUTPUT

        OutputLayout = QHBoxLayout()

        label4 = QLabel("Output ")
        label4.setStyleSheet(
            "font-family: Impact;"
            "font-size:20px;"
        )

        self.OutputLabel = QPlainTextEdit()
        self.OutputLabel.setMinimumHeight(60)
        OutputLayout.addWidget(label4)
        OutputLayout.addWidget(self.OutputLabel)

        layout.addLayout(OutputLayout)

    
    def encryption(self):

        key = self.Keyword.text()
        text = self.Text.toPlainText()

        Ciphertext = PF.PlayFairEncrypt(keyword=key,plaintext=text)
        self.OutputLabel.setPlainText(Ciphertext)

    def decryption(self):

        key = self.Keyword.text()
        text = self.Text.toPlainText()

        PlainText = PF.PlayFairDecrypt(keyword=key,cipherText=text)
        self.OutputLabel.setPlainText(PlainText)


#-------------Caesar Cipher Page
class CaesarCipher(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    
    def initUI(self):

        mainLayout = QVBoxLayout(self)

        #------Heading
        heading = QLabel("Caesar Cipher",self)
        heading.setAlignment(Qt.AlignCenter)
        heading.setStyleSheet(
            "font-family: Impact;"
            "font-weight: bold;"
            "font-style: italic;"
            "font-size:40px;"
        )
        mainLayout.addWidget(heading)
        #mainLayout.addSpacing(5)

        #-------Rotation Value 
        rotationValueLayout = QHBoxLayout()
        ROT_label = QLabel("Enter a Rotation Value ")
        ROT_label.setStyleSheet(
            "font-family: Impact;"
            "font-size:20px;"
        )
        self.key = QSpinBox()

        rotationValueLayout.addWidget(ROT_label)
        rotationValueLayout.addWidget(self.key)

        mainLayout.addLayout(rotationValueLayout)

        #---------- Text Input for processing
        textLayout = QHBoxLayout()
        textLabel = QLabel("Enter Text ")
        textLabel.setStyleSheet(
            "font-family: Impact;"
            "font-size:20px;"
        )

        self.textInput = QTextEdit()
        self.textInput.setPlaceholderText("Plain Text/ Cipher text")
        self.textInput.setMinimumHeight(60)

        textLayout.addWidget(textLabel)
        textLayout.addWidget(self.textInput)

        mainLayout.addLayout(textLayout)

        #---------- Encrypt Button

        encrypt = QPushButton("Encrypt",self)
        encrypt.clicked.connect(self.encrypt_Clicked)

        mainLayout.addWidget(encrypt)

        #--------- Decrypt Button
        decrypt = QPushButton("Decrypt",self)
        decrypt.clicked.connect(self.decrypt_Clicked)

        mainLayout.addWidget(decrypt)

        #---------Output
        outputLayout = QHBoxLayout()
        
        outputLabel = QLabel("Output ")
        outputLayout.addWidget(outputLabel)

        self.outputText = QTextEdit()
        self.outputText.setMinimumHeight(60)
        self.outputText.setPlaceholderText("Output ")
        outputLayout.addWidget(self.outputText)

        mainLayout.addLayout(outputLayout)
        


        
    def encrypt_Clicked(self):
        Key = self.key.value()
        Text = self.textInput.toPlainText()

        plainText = CC.CeaserCipherEncryption(text=Text,key=Key)
        self.outputText.setPlainText(plainText)


    def decrypt_Clicked(self):
        Key = self.key.value()
        Text = self.textInput.toPlainText()

        cipherText = CC.CeaserCipherDecryption(text=Text,key=Key)
        self.outputText.setPlainText(cipherText)
        

#--------Veginere Cipher
class VigenereCipher(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        mainLayout = QVBoxLayout(self)

        #----------------Heading
        heading = QLabel("Vigenere Cipher")
        heading.setAlignment(Qt.AlignCenter)
        mainLayout.addWidget(heading)
        heading.setStyleSheet(
            "font-family: Impact;"
            "font-weight: bold;"
            "font-style: italic;"
            "font-size:40px;"
        )

        #--------------Key
        keywordLabel = QLabel("Enter a Keyword ")
        keywordLabel.setStyleSheet(
            "font-family: Impact;"
            "font-size:20px;"
        )
        self.keyword = QLineEdit()

        keywordLayout = QHBoxLayout()
        keywordLayout.addWidget(keywordLabel)
        keywordLayout.addWidget(self.keyword)

        mainLayout.addLayout(keywordLayout)

        #--------------Text Input
        textLabel = QLabel("Enter Text ")
        textLabel.setStyleSheet(
            "font-family: Impact;"
            "font-size:20px;"
        )
        self.text = QTextEdit()
        self.text.setPlaceholderText("Plain Text / Cipher Text")
        self.text.setMinimumHeight(40)

        textLayout = QHBoxLayout()
        textLayout.addWidget(textLabel)
        textLayout.addWidget(self.text)

        mainLayout.addLayout(textLayout)

        #--------Encryption
        encrypt = QPushButton("Encrypt")
        mainLayout.addWidget(encrypt)
        encrypt.clicked.connect(self.encrypt_Clicked)


        #-------Decryption
        decrypt = QPushButton("Decrypt")
        mainLayout.addWidget(decrypt)
        decrypt.clicked.connect(self.decrypt_Clicked)

        #-------Output
        outputLabel = QLabel("Output ")
        outputLabel.setStyleSheet(
            "font-family: Impact;"
            "font-size:20px;"
        )
        self.output = QTextEdit()
        self.output.setPlaceholderText("Output") 
        self.output.setMinimumHeight(40)

        outputLayout = QHBoxLayout()
        outputLayout.addWidget(outputLabel)
        outputLayout.addWidget(self.output)

        mainLayout.addLayout(outputLayout)
        

    def encrypt_Clicked(self):
        keyword = self.keyword.text()
        text = self.text.toPlainText()

        cipherText = VC.Encryption(keyword,text)

        self.output.setText(cipherText)

    
    def decrypt_Clicked(self):
        keyword = self.keyword.text()
        text = self.text.toPlainText()

        plainText = VC.Decryption(keyword,text)

        self.output.setText(plainText)


#--------- ROT 13
class Rot13(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        mainLayout = QVBoxLayout(self)

        heading = QLabel("ROT 13")
        heading.setAlignment(Qt.AlignCenter)
        heading.setStyleSheet(
            "font-family: Impact;"
            "font-weight: bold;"
            "font-style: italic;"
            "font-size:40px;"
        )
        mainLayout.addWidget(heading)

        #------- Text Input 
        inputLayout = QHBoxLayout()
        textInputLabel = QLabel("Enter Text ")
        inputLayout.addWidget(textInputLabel)

        self.input = QTextEdit()
        self.input.setPlaceholderText("Plain / Cipher Text")
        inputLayout.addWidget(self.input)

        mainLayout.addLayout(inputLayout)

        #--------Encryption
        encrypt = QPushButton("Encrypt")
        mainLayout.addWidget(encrypt)
        encrypt.clicked.connect(self.encrypt_Clicked)


        #-------Decryption
        decrypt = QPushButton("Decrypt")
        mainLayout.addWidget(decrypt)
        decrypt.clicked.connect(self.decrypt_Clicked)

        #--------- Output
        outputLayout = QHBoxLayout()
        outputLabel = QLabel("Output")
        outputLayout.addWidget(outputLabel)

        self.outputText = QTextEdit()
        self.outputText.setPlaceholderText("")
        outputLayout.addWidget(self.outputText)

        mainLayout.addLayout(outputLayout)


    #------ Function to Perform Encryption
    def encrypt_Clicked(self):
        inputText = self.input.toPlainText()
        cipherText = RT.Rot13CipherEncryption(inputText)

        self.outputText.setText(cipherText)


    #------ Function to Perform Encryption
    def decrypt_Clicked(self):
        inputText = self.input.toPlainText()
        plainText = RT.Rot13CipherDecryption(inputText)

        self.outputText.setText(plainText)


#-----Main Window
class mainWindow(QMainWindow):

    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CipherSuite")
        super().setStyleSheet(
            "background-color : #381932;"
            "color : #FFF3E6;"
            )
        self.darkTheme = False
        
        
        self.initBtn()
        self.initUI()



    def initBtn(self):

        self.themeBtn = QPushButton("🌙")
        
        self.themeBtn.setStyleSheet(
            "color: white;"
            "background-color: #000080;"
        )
        self.themeBtn.clicked.connect(self.themeBtn_clicked)

        self.playFairBtn = QPushButton("Playfair Cipher",self)
        self.playFairBtn.setStyleSheet(
            "color: white;"
            "background-color: #000080;"
        )
        self.playFairBtn.clicked.connect(self.playFairBtn_Clicked)

        self.Home = QPushButton("Home",self)
        self.Home.setStyleSheet(
            "color: white;"
            "background-color: #000080;"
        )
        self.Home.clicked.connect(self.HomeBtn_Clicked)

        self.caesarCipherBtn = QPushButton("Caesar Cipher",self)
        self.caesarCipherBtn.setStyleSheet(
            "color: white;"
            "background-color: #000080;"
        )
        self.caesarCipherBtn.clicked.connect(self.caesarCipherBtn_clicked)

        self.vigenereCipherBtn = QPushButton("Vegenere Cipher")
        self.vigenereCipherBtn.setStyleSheet(
            "color: white;"
            "background-color: #000080;"
        )
        self.vigenereCipherBtn.clicked.connect(self.vigenereCipher_clicked)

        self.rot13CipherBtn = QPushButton("ROT 13")
        self.rot13CipherBtn.setStyleSheet(
            "color: white;"
            "background-color: #000080;"
        )
        self.rot13CipherBtn.clicked.connect(self.rot13CipherBtn_clicked)

        




    def initUI(self):

        scroll_area = QScrollArea()
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll_area.setWidgetResizable(True)

        central = QWidget()
        scroll_area.setWidget(central)
        self.setCentralWidget(scroll_area)

        mainLayout = QVBoxLayout(central)

        navBar = QHBoxLayout()
        
        
        navBar.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        navBar.addWidget(self.Home)
        navBar.addWidget(self.playFairBtn)
        navBar.addWidget(self.caesarCipherBtn)
        navBar.addWidget(self.vigenereCipherBtn)
        navBar.addWidget(self.rot13CipherBtn)
        navBar.addWidget(self.themeBtn)
        

        mainLayout.addLayout(navBar)


        self.stackedWindow = QStackedWidget()

        self.HomePage = HomePage()
        self.stackedWindow.addWidget(self.HomePage)
        

        self.playFairPage = PlayFairCipher()
        self.stackedWindow.addWidget(self.playFairPage)

        self.caesarCipherPage = CaesarCipher()
        self.stackedWindow.addWidget(self.caesarCipherPage)

        self.vigenereCipher = VigenereCipher()
        self.stackedWindow.addWidget(self.vigenereCipher)
        
        self.rot13Cipher = Rot13()
        self.stackedWindow.addWidget(self.rot13Cipher)
        

        
        
        
        mainLayout.addWidget(self.stackedWindow)

    def themeBtn_clicked(self):
        if(self.darkTheme == True):
            
            self.setStyleSheet("""

                QWidget {
                    background-color : #381932;
                    color : #FFF3E6;
                }

                
            
            """)
            self.themeBtn.setText("🌙")
        else:
            

            self.setStyleSheet("""

                QWidget {
                    background-color : #FFF3E6;
                    color : #381932;
                }

                
            """)
            self.themeBtn.setText("☀️")
        self.darkTheme = not self.darkTheme
        
    def HomeBtn_Clicked(self):
        self.stackedWindow.setCurrentIndex(0)

    def playFairBtn_Clicked(self):
        self.stackedWindow.setCurrentIndex(1)

    def caesarCipherBtn_clicked(self):
        self.stackedWindow.setCurrentIndex(2)

    def vigenereCipher_clicked(self):
        self.stackedWindow.setCurrentIndex(3)

    def rot13CipherBtn_clicked(self):
        self.stackedWindow.setCurrentIndex(4)
        



def main():

    app = QApplication(sys.argv)

    window = mainWindow()
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()