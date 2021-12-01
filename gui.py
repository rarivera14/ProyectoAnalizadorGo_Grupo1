from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt, pyqtSlot
from lexer import *
from sintactico import *
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QMainWindow, QLineEdit, QPushButton, QTextEdit, \
    QPlainTextEdit, QVBoxLayout, QFileDialog, QTreeView
import sys
import os

#------- William Venegas
class MainWindow(QMainWindow):
    '''Clase para la interfaz grafica'''
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setStyleSheet("background-color: #007d9c;")
        self.setWindowIcon(QtGui.QIcon('./img/go.png'))

        self.title= QLabel(self)
        self.title.setText("Puedes probarlo escribiendo tu código aquí")
        self.title.resize(300,50)
        self.title.move(10,10)
        self.title.setStyleSheet("color: white;")

        self.file = QLabel(self)
        self.file.setText("O puedes escoger un archivo...")
        self.file.resize(300, 50)
        self.file.move(10, 180)
        self.file.setStyleSheet("color: white;")

        self.lexical = QLabel(self)
        self.lexical.setText("Lexical analysis")
        self.lexical.resize(300, 50)
        self.lexical.move(10, 330)
        self.lexical.setStyleSheet("color: white;")

        self.sintax = QLabel(self)
        self.sintax.setText("Análisis de sintaxis")
        self.sintax.resize(300, 50)
        self.sintax.move(530, 330)
        self.sintax.setStyleSheet("color: white;")

        self.qline = QPlainTextEdit(self)
        self.qline.setFixedSize(1000, 100)
        self.qline.setPlaceholderText("Ingrese su código aquí ...")
        self.qline.setStyleSheet("border: 3"
                            "px solid gray;outline: none; color: white;")
        self.qline.move(0,50)

        self.lexerbutton = QPushButton(self)
        self.lexerbutton.resize(100, 32)
        self.lexerbutton.move(475, 160)
        self.lexerbutton.setStyleSheet('background-color: #9ED36A')
        self.lexerbutton.setText('Ejecutar lexer')
        self.lexerbutton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lexerbutton.clicked.connect(self.clickLexer)

        self.sintacticobutton = QPushButton(self)
        self.sintacticobutton.resize(100, 32)
        self.sintacticobutton.move(600, 160)
        self.sintacticobutton.setStyleSheet('background-color: #9ED36A')
        self.sintacticobutton.setText('Ejecutar sintactico')
        self.sintacticobutton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sintacticobutton.clicked.connect(self.clickSintactico)

        self.fileButton = QPushButton(self)
        self.fileButton.resize(100, 32)
        self.fileButton.move(10, 220)
        self.fileButton.clicked.connect(self.clickSubirArchivo)
        self.fileButton.setStyleSheet('background-color: #9ED36A')
        self.fileButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.fileButton.setText('Elija el archivo')
        self.qlabel = QPlainTextEdit(self)
        self.qlabel.setStyleSheet("border: 3""px solid gray;outline: none; color: white;")
        self.qlabel.move(0, 370)
        self.qlabel.resize(470, 320)
        self.qlabel.setReadOnly(True)

        self.qlabelResult = QPlainTextEdit(self)
        self.qlabelResult.setStyleSheet("border: 3""px solid gray;outline: none; color: white;")
        self.qlabelResult.move(520, 370)
        self.qlabelResult.resize(470, 320)
        self.qlabelResult.setReadOnly(True)


        self.setWindowTitle("Go Compiler")
        self.setFixedSize(1000, 700)
    
    def clickLexer(self):
        self.qlabel.clear()
        try:
            l_token = ejecutarLexer(self.qline.toPlainText())
            if len(l_token) > 0:
                self.qlabel.insertPlainText("FORMATO: {:5} ---> {:5}\n\n".format("VALOR", "TOKEN"))
                for tok in l_token:
                    self.qlabel.insertPlainText("{:5} ---> {:5}".format(tok.value, tok.type))
                    self.qlabel.insertPlainText("\n")
        except ValueError as e:
            self.qlabel.insertPlainText(str(e))
        self.qlabel.insertPlainText("\n")

    def clickSintactico(self):
        self.qlabelResult.clear()
        try:
            text = self.qline.toPlainText()
            textSet = text.split('\n')
            resultado = p_ejecutar_sintactico(' '.join(textSet))
            if resultado == None:
                self.qlabelResult.insertPlainText("Sintaxis Correcta")
        except ValueError as e:
            self.qlabelResult.insertPlainText(str(e))
        self.qlabelResult.insertPlainText("\n")

    def clickSubirArchivo(self):
        try:
            file, _ = QFileDialog.getOpenFileName(self, 'Buscar Archivo', os.getcwd(), "Text Files (*.go)")
            if file:
                text = "Archivo seleccionado: " + str(file)
                self.qlabel.insertPlainText(text + '\n\n')
                contenido_archivo = open(file, 'r').read()
                l_token = ejecutarLexer(contenido_archivo)
                print(l_token)
                if len(l_token) > 0:
                    self.qlabel.insertPlainText("FORMATO: {:5} ---> {:5}\n\n".format("VALOR", "TOKEN"))
                    for tok in l_token:
                        self.qlabel.insertPlainText("{:5} ---> {:5}".format(tok.value, tok.type))
                        self.qlabel.insertPlainText("\n")
                self.qlabel.insertPlainText("\n")
        except ValueError as e:
            self.qlabel.insertPlainText(str(e))
        self.qlabel.insertPlainText("\n")



#---------- Funcion principal
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()