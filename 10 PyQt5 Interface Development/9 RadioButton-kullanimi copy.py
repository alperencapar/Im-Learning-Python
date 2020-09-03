import sys
from PyQt5.QtWidgets import QWidget,QApplication,QCheckBox,QLabel,QPushButton,QVBoxLayout,QRadioButton

class Pencere(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.radio_yazi = QLabel("Hangi dili daha çok kullanıyorsun ?")
        self.python = QRadioButton("Python")
        self.java = QRadioButton("Java")
        self.php = QRadioButton("Php")

        self.yazi_alani = QLabel("")

        self.buton = QPushButton("Gönder")


        v_box = QVBoxLayout()

        v_box.addWidget(self.radio_yazi)
        v_box.addWidget(self.python)
        v_box.addWidget(self.java)
        v_box.addWidget(self.php)

        v_box.addStretch()
        v_box.addWidget(self.buton)
        v_box.addWidget(self.yazi_alani)
        
        self.setLayout(v_box)

        self.buton.clicked.connect(lambda: self.click(self.python.isChecked(),self.java.isChecked(),self.php.isChecked()))

        self.show()

    def click(self,python,java,php):

        if(python):
            self.yazi_alani.setText("Python'u seçtin")

        if(java):
            self.yazi_alani.setText("Java'yı seçtin")
        if(php):
            self.yazi_alani.setText("Php'yi seçtin")       

            

app = QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())
