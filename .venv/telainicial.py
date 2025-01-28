import sys 
from PyQt5.QtWidgets import QApplication, QWidget , QLabel,   QPushButton, QVBoxLayout


from Patrimonio import Patrimonio

class telainicial (QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("gerenciar")
        self.setGeometry(300,200,150,150)
        self.layout_v = QVBoxLayout()

        self.label_titulo = QLabel ("Clique para abrir a janela")
        self.button = QPushButton("Abrir Patrimônio")

        self.layout_v.addWidget(self.label_titulo)
        self.layout_v.addWidget(self.button)

        self.button.clicked.connect(self.abrir_cadastro)
        self.setLayout(self.layout_v)
    def abrir_cadastro(self):
        self.pat = Patrimonio()
        self.pat.show()
app = QApplication (sys.argv)
tela = telainicial()
tela.show()
app.exec() 