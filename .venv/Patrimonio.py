from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton, QMessageBox, QTextEdit
import sys

class Patrimonio(QWidget):
    def __init__(self):
        super().__init__()

        # Configuração da janela
        self.setGeometry(400, 150, 500, 400)
        self.setWindowTitle("Sistema de Patrimônio")

        # Layout vertical
        self.layout_v = QVBoxLayout()


        self.label_valor = QLabel("Id do objeto")
        self.label_valor.setStyleSheet("QLabel {font-size: 12px;}")
        self.edit_valor = QLineEdit()
        self.edit_valor.setStyleSheet("QLineEdit {font-size: 12px;}")
        self.layout_v.addWidget(self.label_valor)
        self.layout_v.addWidget(self.edit_valor)


        # Nome do patrimônio
        self.label_nome = QLabel("Nome do Patrimônio")
        self.label_nome.setStyleSheet("QLabel {font-size: 12px;}")
        self.edit_nome = QLineEdit()
        self.edit_nome.setStyleSheet("QLineEdit {font-size: 12px;}")
        self.layout_v.addWidget(self.label_nome)
        self.layout_v.addWidget(self.edit_nome)

        # Descrição do patrimônio
        self.label_descricao = QLabel("tipo do patrimonio")
        self.label_descricao.setStyleSheet("QLabel {font-size: 12px;}")
        self.edit_descricao = QLineEdit()
        self.edit_descricao.setStyleSheet("QLineEdit {font-size: 12px;}")
        self.layout_v.addWidget(self.label_descricao)
        self.layout_v.addWidget(self.edit_descricao)

        # Valor do patrimônio
        self.label_valor = QLabel("Desçrição")
        self.label_valor.setStyleSheet("QLabel {font-size: 12px;}")
        self.edit_valor = QLineEdit()
        self.edit_valor.setStyleSheet("QLineEdit {font-size: 12px;}")
        self.layout_v.addWidget(self.label_valor)
        self.layout_v.addWidget(self.edit_valor)


         # Valor do patrimônio
        self.label_valor = QLabel("Localizção")
        self.label_valor.setStyleSheet("QLabel {font-size: 12px;}")
        self.edit_valor = QLineEdit()
        self.edit_valor.setStyleSheet("QLineEdit {font-size: 12px;}")
        self.layout_v.addWidget(self.label_valor)
        self.layout_v.addWidget(self.edit_valor)

        # Valor do patrimônio
        self.label_valor = QLabel("Data de fabrição")
        self.label_valor.setStyleSheet("QLabel {font-size: 12px;}")
        self.edit_valor = QLineEdit()
        self.edit_valor.setStyleSheet("QLineEdit {font-size: 12px;}")
        self.layout_v.addWidget(self.label_valor)
        self.layout_v.addWidget(self.edit_valor)


        # Data de aquisição
        self.label_data = QLabel("Data de Aquisição ")
        self.label_data.setStyleSheet("QLabel {font-size: 12px;}")
        self.edit_data = QLineEdit()
        self.edit_data.setStyleSheet("QLineEdit {font-size: 12px;}")
        self.layout_v.addWidget(self.label_data)
        self.layout_v.addWidget(self.edit_data)

        # Botão Cadastrar
        self.button_Cadastrar = QPushButton("Cadastrar Patrimônio")
        self.button_Cadastrar.setStyleSheet(
            "QPushButton {background-color: green; color: white; font-size: 12pt; font-weight: bold;}"
        )
        self.layout_v.addWidget(self.button_Cadastrar)

        # Botão para visualizar os patrimônios cadastrados
        self.button_ver_patrimonios = QPushButton("Ver Patrimônios Cadastrados")
        self.button_ver_patrimonios.setStyleSheet(
            "QPushButton {background-color: blue; color: white; font-size: 12pt; font-weight: bold;}"
        )
        self.layout_v.addWidget(self.button_ver_patrimonios)

        # Área para mostrar os patrimônios cadastrados
        self.text_area = QTextEdit()
        self.text_area.setStyleSheet("QTextEdit {font-size: 12px;}")
        self.text_area.setReadOnly(True)
        self.layout_v.addWidget(self.text_area)

        # Conectar os botões às funções
        self.button_Cadastrar.clicked.connect(self.cadastrar_patrimonio)
        self.button_ver_patrimonios.clicked.connect(self.ver_patrimonios)

        # Adicionar o Layout na Tela
        self.setLayout(self.layout_v)

    # Função de cadastro
    def cadastrar_patrimonio(self):
        # Validar os campos
        if not self.edit_nome.text() or not self.edit_descricao.text() or not self.edit_valor.text() or not self.edit_data.text():
            self.show_message("Erro", "Todos os campos são obrigatórios!")
            return

        # Salvar dados no arquivo
        with open("patrimonios.txt", "+a" , encoding= "utf8") as arquivo:
            arquivo.write(f"Nome: {self.edit_nome.text()}\n")
            arquivo.write(f"Descrição: {self.edit_descricao.text()}\n")
            arquivo.write(f"Valor: {self.edit_valor.text()}\n")
            arquivo.write(f"Data de Aquisição: {self.edit_data.text()}\n")
            arquivo.write("----------------------------------------\n")

        # Exibir mensagem de sucesso
        self.show_message("Sucesso", "Patrimônio cadastrado com sucesso!")

        # Limpar os campos após cadastro
        self.edit_nome.clear()
        self.edit_descricao.clear()
        self.edit_valor.clear()
        self.edit_data.clear()

    # Função para visualizar os patrimônios cadastrados
    def ver_patrimonios(self):
        try:
            with open("patrimonios.txt", "r") as arquivo:
                # Exibir os patrimônios na área de texto
                self.text_area.setText(arquivo.read())
        except FileNotFoundError:
            self.show_message("Erro", "Nenhum patrimonio cadastrado ainda!")

    def show_message(self, title, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.exec()

# Inicializar aplicação
# app = QApplication(sys.argv)
# tela = Patrimonio()
# tela.show()
# app.exec()
