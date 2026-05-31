import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget
from PyQt5.QtGui import QRegion
from PyQt5.QtCore import QRect

# Create a reusable styled label to save lines of code
class StyledLabel(QLabel):
    def __init__(self, text, size=20, is_heading=False):
        super().__init__(text)
        weight = "bold" if is_heading else "normal"
        self.setStyleSheet(f"font-family: Impact; font-size: {size}px; font-weight: {weight};")

# Refined Theme Logic in mainWindow
class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CipherSuite")
        self.setMinimumSize(800, 600)
        self.darkTheme = True
        self.apply_theme() # Set initial theme
        
        self.initBtn()
        self.initUI()

    def apply_theme(self):
        if self.darkTheme:
            self.setStyleSheet("""
                QMainWindow, QWidget { background-color: #381932; color: #FFF3E6; }
                QPushButton { background-color: #000080; color: white; padding: 8px; border-radius: 4px; }
                QLineEdit, QTextEdit, QPlainTextEdit { background-color: #4a2342; border: 1px solid #FFF3E6; color: white; }
            """)
        else:
            self.setStyleSheet("""
                QMainWindow, QWidget { background-color: #FFF3E6; color: #381932; }
                QPushButton { background-color: #d1d1ff; color: #381932; padding: 8px; border-radius: 4px; border: 1px solid #000080; }
                QLineEdit, QTextEdit, QPlainTextEdit { background-color: white; border: 1px solid #381932; color: black; }
            """)

    def themeBtn_clicked(self):
        self.darkTheme = not self.darkTheme
        self.themeBtn.setText("☀️" if not self.darkTheme else "🌙")
        self.apply_theme()
        

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
