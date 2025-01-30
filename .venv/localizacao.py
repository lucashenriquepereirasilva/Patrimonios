from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
import sys 

class localizacao(QWidget):
    def __init__(self):
        super().__init__()

        # Vamos ajustar a geometria da tela
        # Setando valores da posição x e y, além da largura e altura
        self.setGeometry(500,150,500,500)

        # Texto para a barra de título
        self.setWindowTitle("localizacao")
        
        # Gerenciador de layout vertical
        self.layout_v = QVBoxLayout()

        # Labels para os dados do ID
        self.label_id = QLabel("ID do Produto:")
        self.label_id.setStyleSheet("QLabel{font-size:12pt}")

        # Labels para empresa
        self.label_empresa = QLabel("Empresa:")
        self.label_empresa.setStyleSheet("QLabel{font-size:12pt}")

        # Labels para Logradouro
        self.label_Logradouro = QLabel("Logradouro:")
        self.label_Logradouro.setStyleSheet("QLabel{font-size:12pt}")

        # Labels para Número
        self.label_Numero = QLabel("Número:")
        self.label_Numero.setStyleSheet("QLabel{font-size:12pt}")

        # Labels para Prédio
        self.label_Predio = QLabel("Prédio:")
        self.label_Predio.setStyleSheet("QLabel{font-size:12pt}")

        # Labels para Andares
        self.label_Andar = QLabel("Andar:")
        self.label_Andar.setStyleSheet("QLabel{font-size:12pt}")

        # Labels para Salas
        self.label_Sala = QLabel("Salas:")
        self.label_Sala.setStyleSheet("QLabel{font-size:12pt}")

###########################################################################

        # LineEdit para ID
        self.edit_id = QLineEdit()
        self.edit_id.setStyleSheet("QLineEdit{font-size:12pt}")

        # LineEdit para Empresa
        self.edit_empresa = QLineEdit()
        self.edit_empresa.setStyleSheet("QLineEdit{font-size:12pt}")

        # LineEdit para o Logradouro
        self.edit_Logradouro = QLineEdit()
        self.edit_Logradouro.setStyleSheet("QLineEdit{font-size:12pt}")

        # LineEdit para Número
        self.edit_Numero = QLineEdit()
        self.edit_Numero.setStyleSheet("QLineEdit{font-size:12pt}")

        # LineEdit para Prédio
        self.edit_Predio = QLineEdit()
        self.edit_Predio.setStyleSheet("QLineEdit{font-size:12pt}")

        # LineEdit para Andares
        self.edit_Andar = QLineEdit()
        self.edit_Andar.setStyleSheet("QLineEdit{font-size:12pt}")

        # LineEdit para Salas
        self.edit_Sala = QLineEdit()
        self.edit_Sala.setStyleSheet("QLineEdit{font-size:12pt}")

##########################################################################

        self.button = QPushButton("Cadastrar")
        self.button.setStyleSheet("QPushButton{background-color:black;color:white;font-size:12pt;font-weight:bold}")

        # Chamar a função de cadastro do cliente ao clicar no botão
        self.button.clicked.connect(self.cadastrar)

        # Adicionar a label o ID e o LineEdit ao layout vertical 
        self.layout_v.addWidget(self.label_id)
        self.layout_v.addWidget(self.edit_id)

        # Adicionar a label da Empresa e o LineEdit ao layout vertical 
        self.layout_v.addWidget(self.label_empresa)
        self.layout_v.addWidget(self.edit_empresa)
        
        # Adicionar a label o Telefone e o LineEdit ao layout vertical 
        self.layout_v.addWidget(self.label_Logradouro)
        self.layout_v.addWidget(self.edit_Logradouro)

        # Adicionar a label do Número e o LineEdit ao layout vertical 
        self.layout_v.addWidget(self.label_Numero)
        self.layout_v.addWidget(self.edit_Numero)

        # Adicionar a label Prédio ao layout vertical
        self.layout_v.addWidget(self.label_Predio)
        self.layout_v.addWidget(self.edit_Predio)

        # Adicionar a label Andares ao layout vertical
        self.layout_v.addWidget(self.label_Andar)
        self.layout_v.addWidget(self.edit_Andar)

        # Adicionar a label Salas ao layout vertical
        self.layout_v.addWidget(self.label_Sala)
        self.layout_v.addWidget(self.edit_Sala)

        self.layout_v.addWidget(self.button)
        

        # Adicionar o layout_v a tela
        self.setLayout(self.layout_v)

###############################################################################
        
    def cadastrar(self):
        
        # Arquivo de ID do Produto
        arquivo = open("clientes.txt" ,"+a")
        arquivo.write(f"Nome: {self.label_id.text()}")
        arquivo.close()
        arquivo = open("clientes.txt" ,"+a")
        arquivo.write(f"Nome: {self.edit_id.text()}")
        arquivo.close()

        # Arquivo da Empresa
        arquivo = open("clientes.txt" ,"+a")
        arquivo.write(f"Nome: {self.label_empresa.text()}")
        arquivo.close()
        arquivo = open("clientes.txt" ,"+a")
        arquivo.write(f"Nome: {self.edit_empresa.text()}")
        arquivo.close()

        # Arquivo de Logradouro
        arquivo = open("clientes.txt" ,"+a")
        arquivo.write(f"Nome: {self.label_Logradouro.text()}")
        arquivo.close()
        arquivo = open("clientes.txt" ,"+a")
        arquivo.write(f"Nome: {self.edit_Logradouro.text()}")
        arquivo.close()

        # Arquivo de Número
        arquivo = open("clientes.txt" ,"+a")
        arquivo.write(f"Nome: {self.label_Numero.text()}")
        arquivo.close()
        arquivo = open("clientes.txt" ,"+a")
        arquivo.write(f"Nome: {self.edit_Numero.text()}")
        arquivo.close()

        # Arquivo do Prédio
        arquivo = open("clientes.txt" ,"+a")
        arquivo.write(f"Nome: {self.label_Predio.text()}")
        arquivo.close()
        arquivo = open("clientes.txt" ,"+a")
        arquivo.write(f"Nome: {self.edit_Predio.text()}")
        arquivo.close()

        # Arquivo do Andar
        arquivo = open("clientes.txt" ,"+a")
        arquivo.write(f"Nome: {self.label_Andar.text()}")
        arquivo.close()
        arquivo = open("clientes.txt" ,"+a")
        arquivo.write(f"Nome: {self.edit_Andar.text()}")
        arquivo.close()

        # Arquivo de Salas
        arquivo = open("clientes.txt" ,"+a")
        arquivo.write(f"Nome: {self.label_Sala.text()}")
        arquivo.close()
        arquivo = open("clientes.txt" ,"+a")
        arquivo.write(f"Nome: {self.edit_Sala.text()}")
        arquivo.close()