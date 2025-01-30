from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
import sys 

class Patrimonio(QWidget):
    def __init__(self):
        super().__init__()

        # Vamos configurar a geometria da tela. Setandos valores de posição X e Y,
        # além de largura e altura
        self.setGeometry(500,30,400,600)

        # Texto para a barra de título
        self.setWindowTitle("Patrimônio do Objeto")

        #Gerenciador de layout vertical
        self.layout_v = QVBoxLayout()

        # Labels para o id do objeto
        self.label_id = QLabel("ID do objeto:")
        self.label_id.setStyleSheet("QLabel{font-size:15pt}")
        #LineEdit para o id do objeto
        self.edit_id = QLineEdit()
        self.edit_id.setStyleSheet("QLineEdit{font-size:15pt}")
        #------------------------------------------------------

        # Labels para o número de série do objeto
        self.label_numero = QLabel("Número de série:")
        self.label_numero.setStyleSheet("QLabel{font-size:15pt}")
        #LineEdit para o id do objeto
        self.edit_numero = QLineEdit()
        self.edit_numero.setStyleSheet("QLineEdit{font-size:15pt}")
        #------------------------------------------------------

        # Labels para o nome do patrimônio
        self.label_nome_patrimonio = QLabel("Nome do Patrimônio:")
        self.label_nome_patrimonio.setStyleSheet("QLabel{font-size:15pt}")
        #LineEdit para o nome do patrimônio
        self.edit_nome_patrimonio = QLineEdit()
        self.edit_nome_patrimonio.setStyleSheet("QLineEdit{font-size:15pt}")
        #------------------------------------------------------

        # Labels para o tipo do objeto
        self.label_tipo = QLabel("Tipo do objeto:")
        self.label_tipo.setStyleSheet("QLabel{font-size:15pt}")
        #LineEdit para o tipo do objeto
        self.edit_tipo = QLineEdit()
        self.edit_tipo.setStyleSheet("QLineEdit{font-size:15pt}")
        #------------------------------------------------------

        # Labels para a descrição do objeto
        self.label_descricao = QLabel("Pequena descrição do objeto:")
        self.label_descricao.setStyleSheet("QLabel{font-size:15pt}")
        #LineEdit para o tipo do objeto
        self.edit_descricao = QLineEdit()
        self.edit_descricao.setStyleSheet("QLineEdit{font-size:15pt}")
        #------------------------------------------------------

        # Labels para a localização do objeto
        self.label_local = QLabel("Sua localização:")
        self.label_local.setStyleSheet("QLabel{font-size:15pt}")
        #LineEdit para o tipo do objeto
        self.edit_local = QLineEdit()
        self.edit_local.setStyleSheet("QLineEdit{font-size:15pt}")
        #------------------------------------------------------

        # Labels para a data de fabricação do objeto
        self.label_fabricacao = QLabel("Data de fabricação:")
        self.label_fabricacao.setStyleSheet("QLabel{font-size:15pt}")
        #LineEdit para o tipo do objeto
        self.edit_frabricacao = QLineEdit()
        self.edit_frabricacao.setStyleSheet("QLineEdit{font-size:15pt}")
        #------------------------------------------------------

        # Labels para a data de aquisição do objeto
        self.label_aquisicao = QLabel("Data de aquisição:")
        self.label_aquisicao.setStyleSheet("QLabel{font-size:15pt}")
        #LineEdit para o tipo do objeto
        self.edit_aquisicao = QLineEdit()
        self.edit_aquisicao.setStyleSheet("QLineEdit{font-size:15pt}")
        #------------------------------------------------------

        self.button = QPushButton("Cadastrar")
        self.button.setStyleSheet("QPushButton{background-color:blue;color:white;font-size:20pt;font-weight:bold}")
        # Chamar a função de cadastro do cliente ao clicar no botão
        self.button.clicked.connect(self.cadastrar)
        #------------------------------------------------------

        # Adicionar a Label id e o lineedit ao layout certical
        self.layout_v.addWidget(self.label_id)
        self.layout_v.addWidget(self.edit_id)

        # Adicionar a Label números de série e o lineedit ao layout certical
        self.layout_v.addWidget(self.label_numero)
        self.layout_v.addWidget(self.edit_numero)

        # Acionar a Label nome do patrimônio e o lineedit ao layout certical
        self.layout_v.addWidget(self.label_nome_patrimonio)
        self.layout_v.addWidget(self.edit_nome_patrimonio)

        # Acionar a Label tipo e o lineedit ao layout certical
        self.layout_v.addWidget(self.label_tipo)
        self.layout_v.addWidget(self.edit_tipo)

         # Acionar a Label descrição e o lineedit ao layout certical
        self.layout_v.addWidget(self.label_descricao)
        self.layout_v.addWidget(self.edit_descricao)

         # Acionar a Label localização e o lineedit ao layout certical
        self.layout_v.addWidget(self.label_local)
        self.layout_v.addWidget(self.edit_local)

        # Acionar a Label data de fabricação e o lineedit ao layout certical
        self.layout_v.addWidget(self.label_fabricacao)
        self.layout_v.addWidget(self.edit_frabricacao)

        # Acionar a Label data de aquisição e o lineedit ao layout certical
        self.layout_v.addWidget(self.label_aquisicao)
        self.layout_v.addWidget(self.edit_aquisicao)

        self.layout_v.addWidget(self.button)

        
        
        #adicionar o layout_v a tela
        self.setLayout(self.layout_v)

    def cadastrar(self):
        if(self.edit_id.text()=="" or self.edit_numero.text()=="" or self.edit_nome_patrimonio.text()=="" or self.edit_tipo.text()=="" or self.edit_descricao.text()=="" or self.edit_frabricacao.text()=="" or self.edit_aquisicao.text()==""):
            QMessageBox.critical(self, "Erro", "Você deve preencher todos os campos")
        else:
            # Vamos criar uma variável que fara referencia ao um arquivo de texto
            arquivo = open("Patrimônio.txt","+a", encoding="utf8")
            arquivo.write(f"ID: {self.edit_id.text()}\n")
            arquivo.write(f"Número de série: {self.edit_numero.text()}\n")
            arquivo.write(f"Nome do patrimônio: {self.edit_nome_patrimonio.text()}\n")
            arquivo.write(f"Tipo: {self.edit_tipo.text()}\n")
            arquivo.write(f"Descrição: {self.edit_descricao.text()}\n")
            arquivo.write(f"Localização: {self.edit_local.text()}\n")
            arquivo.write(f"Data de fabricação: {self.edit_frabricacao.text()}\n")
            arquivo.write(f"Data de aquisição: {self.edit_aquisicao.text()}\n")
            arquivo.write("-------------------------------------------\n")
            arquivo.close()
            QMessageBox.information(self, "Salvo", "Os dados do patrimônio foram salvos")


#app = QApplication(sys.argv)
# Instancia da classe CadastroCliente para iniciar a janela
#tela = Patrimonio()
# exibir a tela durante a execução
#tela.show()
# ao clicar no botão fechar a tela deve fechar e sair da memória
#app.exec()