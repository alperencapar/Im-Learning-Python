import sys
from PyQt5.QtWidgets import QWidget, QApplication, QTextEdit, QRadioButton, QLabel, QPushButton, QVBoxLayout, QHBoxLayout


class Pencere(QWidget):
    
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.yazi_alani = QTextEdit()
        self.temizle = QPushButton("Temizle")

        v_box = QVBoxLayout()
        v_box.addWidget(self.yazi_alani)
        v_box.addWidget(self.temizle)

        self.setLayout(v_box)

        self.temizle.clicked.connect(self.butonTemizle)

        self.show()

    def butonTemizle(self):
        self.yazi_alani.clear()

app = QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())