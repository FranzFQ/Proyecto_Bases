import sys
from PyQt6.QtWidgets import QApplication ,QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QMessageBox 
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QPixmap

class Ventana:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.window1 = QWidget()
        self.window2 = QWidget()

        self.window1.setStyleSheet("background-color: #72cee9;")
        self.window1.setWindowTitle("Inicio de sesion")
        self.window1.setFixedSize(400, 275)
        self.window1.setWindowIcon(QIcon("logo.ico"))

        self.window2.setStyleSheet("background-color: #00fff0;")
        self.window2.setWindowTitle("Programa V1.0")
        self.window2.setWindowIcon(QIcon("logo.ico"))

        self.mesaje_error = QMessageBox()
        self.mesaje_error.setIcon(QMessageBox.Icon.Warning)
        self.mesaje_error.setStyleSheet("QMessageBox { color: black; background-color: #e15f5f;} QPushButton {color: black; background-color: #ff0000;} QLabel{color: black;}")
        self.mesaje_error.setWindowIcon(QIcon("warning.ico")) 


        self.mensaje_informacion = QMessageBox()
        self.mensaje_informacion.setStyleSheet("QMessageBox { color: black; background-color: #36dfea;} QPushButton {color: black; background-color: #22a4ac;} QLabel{color: black;}")
        self.mensaje_informacion.setWindowIcon(QIcon("infomation.ico"))


    def Ingreso_de_datos(self):

        
        self.window2.showMaximized()
        pass
        

    def inicio(self):
        main_layout = QVBoxLayout()
        layout1 = QHBoxLayout()
        layout2 = QHBoxLayout()
        layout3 = QHBoxLayout()

        usuario_imagen = QPixmap("usuario.png")
        usuario_imagen = usuario_imagen.scaled(150, 150, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        usuario_label = QLabel()
        usuario_label.setPixmap(usuario_imagen)
        usuario_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        usuario = QLabel("Ingrese el usuario:")
        usuario.setAlignment(Qt.AlignmentFlag.AlignCenter)
        usuario.setStyleSheet("Color: black")

        self.ingreso_usuario = QLineEdit()
        self.ingreso_usuario.setStyleSheet("Color: white; background-color: #bf35e1;")
        self.ingreso_usuario.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ingreso_usuario.setFixedWidth(200)

        contraseña = QLabel("Ingrese la contraseña:")
        contraseña.setAlignment(Qt.AlignmentFlag.AlignCenter)
        contraseña.setStyleSheet("Color: black")

        self.ingreso_contraseña = QLineEdit()
        self.ingreso_contraseña.setStyleSheet("Color: white; background-color: #bf35e1;")
        self.ingreso_contraseña.setEchoMode(QLineEdit.EchoMode.Password)
        self.ingreso_contraseña.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ingreso_contraseña.setFixedWidth(200)

        boton_ingresar = QPushButton("Ingresar")
        boton_ingresar.clicked.connect(self.verificacion)
        boton_ingresar.setStyleSheet("Color: white; background-color: #aa35e1;")
        boton_ingresar.setFixedWidth(175)

        boton_cancelar = QPushButton("cancelar")
        boton_cancelar.clicked.connect(self.cancelar_inicio)
        boton_cancelar.setStyleSheet("Color: white; background-color: #aa35e1;")
        boton_cancelar.setFixedWidth(175)

        layout1.addWidget(usuario)
        layout1.addWidget(self.ingreso_usuario)
        layout2.addWidget(contraseña)
        layout2.addWidget(self.ingreso_contraseña)
        layout3.addWidget(boton_ingresar)
        layout3.addWidget(boton_cancelar) 
        main_layout.addWidget(usuario_label)
        main_layout.addLayout(layout1)
        main_layout.addLayout(layout2)
        main_layout.addLayout(layout3)
        self.window1.setLayout(main_layout)
        self.window1.show()

    def verificacion(self):
        if self.ingreso_usuario.text() == "admin" and self.ingreso_contraseña.text() == "admin":
            self.Ingreso_de_datos()
        else:
            self.mesaje_error.setWindowTitle("Error")
            self.mesaje_error.setText("Datos incorrectos")

            self.mesaje_error.setDefaultButton(QMessageBox.StandardButton.Ok)
            self.mesaje_error.exec()

    def cancelar_inicio(self):
        self.ingreso_usuario.clear()
        self.ingreso_contraseña.clear()
        self.mensaje_informacion.setWindowTitle("Cancelado")
        self.mensaje_informacion.setText("Inicio de sesion cancelado")
        self.mensaje_informacion.setIcon(QMessageBox.Icon.Information)
        self.mensaje_informacion.setDefaultButton(QMessageBox.StandardButton.Ok) 
        self.mensaje_informacion.exec()