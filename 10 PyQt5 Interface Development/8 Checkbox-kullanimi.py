import sys
from PyQt5.QtWidgets import QWidget,QApplication,QCheckBox,QLabel,QPushButton,QVBoxLayout


class Pencere(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.checkbox = QCheckBox("Python'u seviyor musun ? ")          #checkbox oluşturma
        self.yazi_alani = QLabel("")
        self.buton = QPushButton("Tıkla")

        v_box = QVBoxLayout()

        v_box.addWidget(self.checkbox)
        v_box.addWidget(self.yazi_alani)
        v_box.addWidget(self.buton)
        v_box.addStretch()

        self.setLayout(v_box)

        self.buton.clicked.connect(lambda : self.click(self.checkbox.isChecked()))      #fonksiyon objesi vermemiz gerektiği için lambda kullanıldı

        self.show()

    def click(self,checkbox):
        if checkbox:
            self.yazi_alani.setText("Ben de seviyorum kanka")
        else:
            self.yazi_alani.setText("Niye sevmiyon şerefsiz")

app = QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())
