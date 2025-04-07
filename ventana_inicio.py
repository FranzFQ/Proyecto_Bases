import sys
from codigo import Codigo
from ventana_principal import Ventana_principal
from Base_datos import BaseDatos
from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout, QLabel, QLineEdit, QSizePolicy
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt


class Ventana_inicio(Codigo):
    def __init__(self):
        super().__init__()
        self.usuario: list[str]= []


# Inicio de las ventanas del programa
    def inicio(self):
        self.window1 = QWidget()
        self.window1.setWindowTitle("Inicio de sesion")
        self.fondo_degradado(self.window1, "#5DA9F5", "#0037FF")
        self.window1.setWindowIcon(QIcon("imagenes/logo.ico"))
        self.window1.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        main_layout = QVBoxLayout()
        layout1 = QGridLayout()
        layout1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout2 = QHBoxLayout()
        layout2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        usuario_imagen = self.imagen("imagenes/usuario.png", 150, 150)
        usuario_label = QLabel()
        usuario_label.setPixmap(usuario_imagen)
        usuario_label.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        layout2.addWidget(usuario_label)

        usuario = QLabel("Ingrese el usuario:")
        usuario.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        usuario.setStyleSheet("Color: black")

        self.ingreso_usuario = QLineEdit()
        self.color_linea(self.ingreso_usuario)
        self.ingreso_usuario.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.ingreso_usuario.setFixedWidth(200)

        contrasenia = QLabel("Ingrese la contraseña:")
        contrasenia.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        contrasenia.setStyleSheet("Color: black")

        self.ingreso_contrasenia = QLineEdit()
        self.color_linea(self.ingreso_contrasenia)
        self.ingreso_contrasenia.setEchoMode(QLineEdit.EchoMode.Password)
        self.ingreso_contrasenia.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.ingreso_contrasenia.setFixedWidth(200)

        boton_ingresar = QPushButton("Ingresar")
        boton_ingresar.clicked.connect(self.verificacion)
        self.color_boton_sin_oprimir(boton_ingresar)
        boton_ingresar.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        boton_ingresar.setFixedWidth(200)

        boton_salir = QPushButton("Salir")
        boton_salir.clicked.connect(self.cerrar_programa)
        self.color_boton_sin_oprimir(boton_salir)
        boton_salir.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        boton_salir.setFixedWidth(200)

        layout1.addWidget(usuario, 0, 0)
        layout1.addWidget(self.ingreso_usuario, 0, 1)
        layout1.addItem(self.espacio(10, 10), 1, 0, 1, 1)
        layout1.addWidget(contrasenia, 2, 0)
        layout1.addWidget(self.ingreso_contrasenia, 2, 1)
        layout1.addItem(self.espacio(10, 10), 3, 0, 3, 1)
        layout1.addWidget(boton_ingresar, 4, 0)
        layout1.addWidget(boton_salir, 4, 1)

        main_layout.addLayout(layout2)
        main_layout.addLayout(layout1)
        self.window1.setLayout(main_layout)
        self.ventanas[0] = self.window1
        self.window1.showNormal()
        self.window1.activateWindow()

    def verificacion(self):
        user = self.ingreso_usuario.text()
        password = self.ingreso_contrasenia.text()

        try:
            print("Iniciando base de datos...")
            self.base_datos = BaseDatos(user, password)
            #Aquí se inicia base de datos
            if self.base_datos.conexion and self.base_datos.conexion.is_connected():
                print("Base de datos iniciada correctamente")
                if self.ventanas[1] is None:
                    self.window2 = Ventana_principal(self.ventanas, self.base_datos)
                    self.window2.principal()
                    self.window1.close()
                else:
                    self.ventana_maxima(self.ventanas[1])
                    self.window1.close()

            else:
                self.mensaje_error("Error", "No se pudo conectar a la base de datos")
                
        except Exception as e:
          # Error
            print(type(e).__name__ + ": " + str(e))
            self.mensaje_error("Error", f"Usuario o contraseña incorrectos:")
            # Limpiar campos
            self.ingreso_usuario.clear()
            self.ingreso_contrasenia.clear()
            
    def cerrar_programa(self):
        self.ventanas[0].close()
        self.mensaje_informacion("Programa cerrado", "Se ha cerrado el programa exitosamente")
        sys.exit()
