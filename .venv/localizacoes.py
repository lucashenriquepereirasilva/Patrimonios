from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton
import sys

class Patrimonio(QWidget):
    def __init__(self):
        super().__init__()

        # Configuração inicial da janela
        self.setWindowTitle('Cadastro de Patrimônio')
        self.setGeometry(300, 300, 400, 300)

        # Layout
        layout = QVBoxLayout()

        # Campos de entrada para dados do patrimônio
        self.id_label = QLabel('ID:')
        self.id_QLineEdit = QLineEdit()

        self.empresa_label = QLabel('empresa')
        self.empresa_QLineEdit = QLineEdit()

        self.logradouro_label = QLabel('logradouro')
        self.logradouro_QLineEdit = QLineEdit()

        self.numero_label = QLabel('Numero')
        self.numero_QLineEdit = QLineEdit()

        self.prédio_label = QLabel('prédio')
        self.prédio_QLineEdit = QLineEdit()

        self.andar_label = QLabel('andar')
        self.andar_QLineEdit = QLineEdit()

        self.sala_label = QLabel('sala')
        self.sala_QLineEdit = QLineEdit()

        self.data_fabricação_label = QLabel('data de fabricação')
        self.data_fabricação_QLineEdit = QLineEdit()

        self.data_label = QLabel('data de aquisição')
        self.data_QLineEdit = QLineEdit()









        # Botão para salvar os dados
        self.salvar_button = QPushButton('Salvar')
        self.salvar_button.clicked.connect(self.salvar_dados)

        # Adicionar widgets ao layout
        layout.addWidget(self.id_label)
        layout.addWidget(self.id_QLineEdit)

        layout.addWidget(self.empresa_label)
        layout.addWidget(self.empresa_QLineEdit)

        layout.addWidget(self.logradouro_label)
        layout.addWidget(self.logradouro_QLineEdit)

        layout.addWidget(self.numero_label)
        layout.addWidget(self.numero_QLineEdit)

        layout.addWidget(self.prédio_label)
        layout.addWidget(self.prédio_QLineEdit)

        layout.addWidget(self.andar_label)
        layout.addWidget(self.andar_QLineEdit)

        layout.addWidget(self.sala_label)
        layout.addWidget(self.sala_QLineEdit)


        # layout.addWidget(self.data_fabricação_label)
        # layout.addWidget(self.data_fabricação_QLineEdit)

        # layout.addWidget(self.data_label)
        # layout.addWidget(self.data_QLineEdit)


        layout.addWidget(self.salvar_button)

        # Definir o layout da janela
        self.setLayout(layout)

    def salvar_dados(self):
        # Exibir uma mensagem simples de confirmação
        id_dado = self.id_QLineEdit.text()
        nome_dado = self.nome_QLineEdit.text()
        numero_serie_dado = self.numero_serie_QLineEdit.text()


# Inicializar o aplicativo PyQt
app = QApplication(sys.argv)
window = Patrimonio()
window.show()
sys.exit(app.exec_())
