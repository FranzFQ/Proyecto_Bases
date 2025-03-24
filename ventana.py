import sys
from PyQt6.QtWidgets import QApplication ,QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QMessageBox 
from PyQt6.QtCore import Qt, QSize
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
        self.window2.setWindowIcon(QIcon("logo.ico"))

        self.mesaje_error = QMessageBox()
        self.mesaje_error.setIcon(QMessageBox.Icon.Warning)
        self.mesaje_error.setStyleSheet("QMessageBox { color: black; background-color: #e15f5f;} QPushButton {color: black; background-color: #ff0000;} QLabel{color: black;}")
        self.mesaje_error.setWindowIcon(QIcon("warning.ico")) 


        self.mensaje_informacion = QMessageBox()
        self.mensaje_informacion.setStyleSheet("QMessageBox { color: black; background-color: #36dfea;} QPushButton {color: black; background-color: #22a4ac;} QLabel{color: black;}")
        self.mensaje_informacion.setWindowIcon(QIcon("infomation.ico"))

    def limpieza_layout(self, layout):
        while layout.count():
            item = self.layout2.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.setParent(None)
            else:
                layout_interno = item.layout()
                if layout_interno is not None:
                    self.limpiar_layout_recursivo(layout_interno)
    def imagen(self, ruta, ancho, alto):
        imagen = QPixmap(ruta)
        imagen = imagen.scaled(ancho, alto, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        return imagen

    def inicio(self):
        main_layout = QVBoxLayout()
        layout1 = QHBoxLayout()
        layout2 = QHBoxLayout()
        layout3 = QHBoxLayout()

        usuario_imagen = self.imagen("usuario.png", 150, 150)
        usuario_label = QLabel()
        usuario_label.setPixmap(usuario_imagen)
        usuario_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        usuario = QLabel("Ingrese el usuario:")
        usuario.setAlignment(Qt.AlignmentFlag.AlignCenter)
        usuario.setStyleSheet("Color: black")

        self.ingreso_usuario = QLineEdit()
        self.ingreso_usuario.setStyleSheet("Color: black; background-color: #bf35e1;")
        self.ingreso_usuario.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ingreso_usuario.setFixedWidth(200)

        contraseña = QLabel("Ingrese la contraseña:")
        contraseña.setAlignment(Qt.AlignmentFlag.AlignCenter)
        contraseña.setStyleSheet("Color: black")

        self.ingreso_contraseña = QLineEdit()
        self.ingreso_contraseña.setStyleSheet("Color: black; background-color: #bf35e1;")
        self.ingreso_contraseña.setEchoMode(QLineEdit.EchoMode.Password)
        self.ingreso_contraseña.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ingreso_contraseña.setFixedWidth(200)

        boton_ingresar = QPushButton("Ingresar")
        boton_ingresar.clicked.connect(self.verificacion)
        boton_ingresar.setStyleSheet("Color: black; background-color: #aa35e1;")
        boton_ingresar.setFixedWidth(175)

        boton_cancelar = QPushButton("cancelar")
        boton_cancelar.clicked.connect(self.cancelar_inicio)
        boton_cancelar.setStyleSheet("Color: black; background-color: #aa35e1;")
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
            self.window1.close()
            self.ventana_principal()
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

    def ventana_principal(self):
        self.window2.setWindowTitle("Bienvenido usuario: " + "admin")
        main_layout = QHBoxLayout()

        layout1 = QVBoxLayout()
        layout1.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.layout2 = QVBoxLayout()
        self.layout2.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.boton_usuario = QPushButton()
        self.boton_usuario.setIcon(QIcon(self.imagen("usuarios.png", 150, 150)))
        self.boton_usuario.setIconSize(QSize(150, 150))
        self.boton_usuario.setFixedSize(200, 200)
        self.boton_usuario.setStyleSheet("QPushButton {background-color: white; border: 5px solid black;} QPushButton:hover {background-color: #e1e1e1;} QPushButton:pressed {background-color: #c1c1c1;}")

        self.boton_ventas = QPushButton()
        self.boton_ventas.setIcon(QIcon(self.imagen("ventas.png", 150, 150)))
        self.boton_ventas.setIconSize(QSize(150, 150))
        self.boton_ventas.setFixedSize(200, 200)
        self.boton_ventas.setStyleSheet("QPushButton {background-color: white; border: 5px solid black;} QPushButton:hover {background-color: #e1e1e1;} QPushButton:pressed {background-color: #c1c1c1;}")

        self.boton_compras = QPushButton()
        self.boton_compras.setIcon(QIcon(self.imagen("compras.png", 150, 150)))
        self.boton_compras.setIconSize(QSize(150, 150))
        self.boton_compras.setFixedSize(200, 200)
        self.boton_compras.setStyleSheet("QPushButton {background-color: white; border: 5px solid black;} QPushButton:hover {background-color: #e1e1e1;} QPushButton:pressed {background-color: #c1c1c1;}")

        self.boton_inventario = QPushButton()
        self.boton_inventario.setIcon(QIcon(self.imagen("inventario.png", 150, 150)))
        self.boton_inventario.setIconSize(QSize(150, 150))
        self.boton_inventario.setFixedSize(200, 200)
        self.boton_inventario.setStyleSheet("QPushButton {background-color: white; border: 5px solid black;} QPushButton:hover {background-color: #e1e1e1;} QPushButton:pressed {background-color: #c1c1c1;}")
        self.boton_inventario.clicked.connect(self.ventana_inventario)

        layout1.addWidget(self.boton_usuario)
        layout1.addWidget(self.boton_ventas)
        layout1.addWidget(self.boton_compras)
        layout1.addWidget(self.boton_inventario)
        
        self.principal()
        main_layout.addLayout(layout1)
        main_layout.addLayout(self.layout2)
        self.window2.setLayout(main_layout)
        self.window2.showMaximized()
        pass

    def principal(self):
        logo = QLabel()
        logo.setPixmap(self.imagen("logo_libreria.png", 400, 400))
        logo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout2.addWidget(logo)
    
    def ventana_inventario(self):
        self.limpieza_layout(self.layout2)
        self.boton_inventario.setStyleSheet("QPushButton {background-color: #c1c1c1; border: 5px solid black;} QPushButton:hover {background-color: #e1e1e1;} QPushButton:pressed {background-color: #c1c1c1;}")
        layout3 = QHBoxLayout()
        layout3.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignCenter)

        boton_editar = QPushButton()
        boton_editar.setIcon(QIcon(self.imagen("editar.png", 150, 150)))
        boton_editar.setIconSize(QSize(50, 50))
        boton_editar.setFixedSize(200, 80)
        boton_editar.setStyleSheet("QPushButton {background-color: white; border: 5px solid black;} QPushButton:hover {background-color: #e1e1e1;} QPushButton:pressed {background-color: #c1c1c1;}")

        boton_eliminar = QPushButton()
        boton_eliminar.setIcon(QIcon(self.imagen("eliminar.png", 150, 150)))
        boton_eliminar.setIconSize(QSize(50, 50))
        boton_eliminar.setFixedSize(200, 80)
        boton_eliminar.setStyleSheet("QPushButton {background-color: white; border: 5px solid black;} QPushButton:hover {background-color: #e1e1e1;} QPushButton:pressed {background-color: #c1c1c1;}")

        boton_agregar = QPushButton()
        boton_agregar.setIcon(QIcon(self.imagen("agregar.png", 150, 150)))
        boton_agregar.setIconSize(QSize(50, 50))
        boton_agregar.setFixedSize(200, 80)
        boton_agregar.setStyleSheet("QPushButton {background-color: white; border: 5px solid black;} QPushButton:hover {background-color: #e1e1e1;} QPushButton:pressed {background-color: #c1c1c1;}")


        boton_busqueda = QPushButton()
        boton_busqueda.setIcon(QIcon(self.imagen("buscar.png", 150, 150)))
        boton_busqueda.setIconSize(QSize(50, 50))
        boton_busqueda.setFixedSize(200, 80)
        boton_busqueda.setStyleSheet("QPushButton {background-color: white; border: 5px solid black;} QPushButton:hover {background-color: #e1e1e1;} QPushButton:pressed {background-color: #c1c1c1;}")

        self.ingreso_busqueda = QLineEdit()
        self.ingreso_busqueda.setPlaceholderText("Busqueda")
        self.ingreso_busqueda.setStyleSheet("Color: black; background-color: #77f9ff; border: 5px solid black;")
        self.ingreso_busqueda.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ingreso_busqueda.setFixedSize(400, 80)


        layout3.addWidget(boton_editar)
        layout3.addWidget(boton_eliminar)
        layout3.addWidget(boton_agregar)
        layout3.addWidget(boton_busqueda)
        layout3.addWidget(self.ingreso_busqueda)

        self.layout2.addLayout(layout3)        
        