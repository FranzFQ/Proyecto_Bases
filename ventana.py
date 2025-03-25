import sys
from PyQt6.QtWidgets import QApplication ,QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QMessageBox, QSizePolicy 
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
        self.window1.setWindowIcon(QIcon("imagenes/logo.ico"))

        self.window2.setStyleSheet("background-color: #00fff0;")
        self.window2.setWindowIcon(QIcon("imagenes/logo.ico"))

# Funciones para optimizar el codigo

    def limpieza_layout(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.setParent(None)
            else:
                sub_layout = item.layout()
                if sub_layout is not None:
                    self.limpieza_layout(sub_layout)
    
    def mensaje_error(self, titulo, mensaje):
        self.mesaje_error = QMessageBox()
        self.mesaje_error.setIcon(QMessageBox.Icon.Warning)
        self.mesaje_error.setStyleSheet("QMessageBox { color: black; background-color: #e15f5f;} QPushButton {color: black; background-color: #ff0000;} QLabel{color: black;}")
        self.mesaje_error.setWindowIcon(QIcon("imagenes/warning.ico")) 
        self.mesaje_error.setWindowTitle(titulo)
        self.mesaje_error.setText(mensaje)
        self.mesaje_error.setDefaultButton(QMessageBox.StandardButton.Ok)
        self.mesaje_error.exec()

    def mensaje_informacion(self, titulo, mensaje):
        self.mensaje_informacion = QMessageBox()
        self.mensaje_informacion.setStyleSheet("QMessageBox { color: black; background-color: #36dfea;} QPushButton {color: black; background-color: #22a4ac;} QLabel{color: black;}")
        self.mensaje_informacion.setWindowIcon(QIcon("imagenes/infomation.ico"))
        self.mensaje_informacion.setWindowTitle(titulo)
        self.mensaje_informacion.setText(mensaje)
        self.mensaje_informacion.setIcon(QMessageBox.Icon.Information)
        self.mensaje_informacion.setDefaultButton(QMessageBox.StandardButton.Ok) 
        self.mensaje_informacion.exec()

    def color_boton_sin_oprimir(self, boton):
        boton.setStyleSheet("QPushButton {background-color: white; border: 5px solid black; } QPushButton:hover {background-color: #e1e1e1;} QPushButton:pressed {background-color: #c1c1c1;}")

    def color_boton_oprimido(self, boton):
        boton.setStyleSheet("QPushButton {background-color: #c1c1c1; border: 5px solid black;} QPushButton:hover {background-color: #e1e1e1;} QPushButton:pressed {background-color: #c1c1c1;}")

    def imagen(self, ruta, ancho, alto):
        imagen = QPixmap(ruta)
        imagen = imagen.scaled(ancho, alto, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        return imagen

    def activar_botones(self):
        self.boton_compras.setEnabled(True)
        self.boton_ventas.setEnabled(True)
        self.boton_usuario.setEnabled(True)
        self.boton_inventario.setEnabled(True)

    def recoloreas_botones(self):
        self.color_boton_sin_oprimir(self.boton_compras)
        self.color_boton_sin_oprimir(self.boton_ventas)
        self.color_boton_sin_oprimir(self.boton_usuario)
        self.color_boton_sin_oprimir(self.boton_inventario)

# Inicio de las ventanas del programa

    def inicio(self):
        main_layout = QVBoxLayout()
        layout1 = QHBoxLayout()
        layout2 = QHBoxLayout()
        layout3 = QHBoxLayout()

        usuario_imagen = self.imagen("imagenes/usuario.png", 150, 150)
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

        contrasenia = QLabel("Ingrese la contraseña:")
        contrasenia.setAlignment(Qt.AlignmentFlag.AlignCenter)
        contrasenia.setStyleSheet("Color: black")

        self.ingreso_contrasenia = QLineEdit()
        self.ingreso_contrasenia.setStyleSheet("Color: black; background-color: #bf35e1;")
        self.ingreso_contrasenia.setEchoMode(QLineEdit.EchoMode.Password)
        self.ingreso_contrasenia.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ingreso_contrasenia.setFixedWidth(200)

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
        layout2.addWidget(contrasenia)
        layout2.addWidget(self.ingreso_contrasenia)
        layout3.addWidget(boton_ingresar)
        layout3.addWidget(boton_cancelar) 
        main_layout.addWidget(usuario_label)
        main_layout.addLayout(layout1)
        main_layout.addLayout(layout2)
        main_layout.addLayout(layout3)
        self.window1.setLayout(main_layout)
        self.window1.show()

    def verificacion(self):
        if self.ingreso_usuario.text() == "admin" and self.ingreso_contrasenia.text() == "admin":
            self.window1.close()
            self.ventana_principal()
        else:
            self.mensaje_error("Error", "Usuario o contraseña incorrectos")

    def cancelar_inicio(self):
        self.ingreso_usuario.clear()
        self.ingreso_contrasenia.clear()
        self.mensaje_informacion("Cancelado", "Inicio de sesion cancelado")

    def ventana_principal(self):
        self.window2.setWindowTitle("Bienvenido usuario: " + "admin")
        main_layout = QHBoxLayout()

        layout1 = QVBoxLayout()
        layout1.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.layout2 = QVBoxLayout()
        self.layout2.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.boton_usuario = QPushButton()
        self.boton_usuario.setIcon(QIcon(self.imagen("imagenes/usuarios.png", 150, 150)))
        self.boton_usuario.setIconSize(QSize(150, 150))
        self.boton_usuario.setFixedSize(200, 200)
        self.color_boton_sin_oprimir(self.boton_usuario)
        self.boton_usuario.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.boton_usuario.clicked.connect(self.ventana_usuario)

        self.boton_ventas = QPushButton()
        self.boton_ventas.setIcon(QIcon(self.imagen("imagenes/ventas.png", 150, 150)))
        self.boton_ventas.setIconSize(QSize(150, 150))
        self.boton_ventas.setFixedSize(200, 200)
        self.color_boton_sin_oprimir(self.boton_ventas)
        self.boton_ventas.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.boton_ventas.clicked.connect(self.ventana_ventas)

        self.boton_compras = QPushButton()
        self.boton_compras.setIcon(QIcon(self.imagen("imagenes/compras.png", 150, 150)))
        self.boton_compras.setIconSize(QSize(150, 150))
        self.boton_compras.setFixedSize(200, 200)
        self.color_boton_sin_oprimir(self.boton_compras)
        self.boton_compras.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.boton_compras.clicked.connect(self.ventana_compras)

        self.boton_inventario = QPushButton()
        self.boton_inventario.setIcon(QIcon(self.imagen("imagenes/inventario.png", 150, 150)))
        self.boton_inventario.setIconSize(QSize(150, 150))
        self.boton_inventario.setFixedSize(200, 200)
        self.color_boton_sin_oprimir(self.boton_inventario)
        self.boton_inventario.clicked.connect(self.ventana_inventario)
        self.boton_inventario.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

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
        logo.setPixmap(self.imagen("imagenes/logo_libreria.png", 400, 400))
        logo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout2.addWidget(logo)
    
    def ventana_usuario(self):
        self.limpieza_layout(self.layout2)
        self.recoloreas_botones()
        self.color_boton_oprimido(self.boton_usuario)
        self.activar_botones()
        self.boton_usuario.setEnabled(False)

    def ventana_ventas(self):
        self.limpieza_layout(self.layout2)
        self.recoloreas_botones()
        self.color_boton_oprimido(self.boton_ventas)
        self.activar_botones()
        self.boton_ventas.setEnabled(False)

    def ventana_compras(self):
        self.limpieza_layout(self.layout2)
        self.recoloreas_botones()
        self.color_boton_oprimido(self.boton_compras)
        self.activar_botones()
        self.boton_compras.setEnabled(False)

    
    def ventana_inventario(self):
        self.limpieza_layout(self.layout2)
        self.recoloreas_botones()
        self.color_boton_oprimido(self.boton_inventario)
        self.activar_botones()
        self.boton_inventario.setEnabled(False)
        layout3 = QHBoxLayout()
        layout3.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignCenter)

        boton_editar = QPushButton()
        boton_editar.setIcon(QIcon(self.imagen("imagenes/editar.png", 150, 150)))
        boton_editar.setIconSize(QSize(50, 50))
        boton_editar.setFixedSize(200, 80)
        boton_editar.setStyleSheet("QPushButton {background-color: white; border: 5px solid black;} QPushButton:hover {background-color: #e1e1e1;} QPushButton:pressed {background-color: #c1c1c1;}")

        boton_eliminar = QPushButton()
        boton_eliminar.setIcon(QIcon(self.imagen("imagenes/eliminar.png", 150, 150)))
        boton_eliminar.setIconSize(QSize(50, 50))
        boton_eliminar.setFixedSize(200, 80)
        boton_eliminar.setStyleSheet("QPushButton {background-color: white; border: 5px solid black;} QPushButton:hover {background-color: #e1e1e1;} QPushButton:pressed {background-color: #c1c1c1;}")

        boton_agregar = QPushButton()
        boton_agregar.setIcon(QIcon(self.imagen("imagenes/agregar.png", 150, 150)))
        boton_agregar.setIconSize(QSize(50, 50))
        boton_agregar.setFixedSize(200, 80)
        boton_agregar.setStyleSheet("QPushButton {background-color: white; border: 5px solid black;} QPushButton:hover {background-color: #e1e1e1;} QPushButton:pressed {background-color: #c1c1c1;}")

        boton_busqueda = QPushButton()
        boton_busqueda.setIcon(QIcon(self.imagen("imagenes/buscar.png", 150, 150)))
        boton_busqueda.setIconSize(QSize(50, 50))
        boton_busqueda.setFixedSize(200, 80)
        boton_busqueda.setStyleSheet("QPushButton {background-color: white; border: 5px solid black;} QPushButton:hover {background-color: #e1e1e1;} QPushButton:pressed {background-color: #c1c1c1;}")

        self.ingreso_busqueda = QLineEdit()
        self.ingreso_busqueda.setPlaceholderText("Ingrese el codigo de su producto")
        self.ingreso_busqueda.setStyleSheet("Color: black; background-color: #77f9ff; border: 5px solid black;")
        self.ingreso_busqueda.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ingreso_busqueda.setFixedSize(400, 80)

        layout3.addWidget(boton_editar)
        layout3.addWidget(boton_eliminar)
        layout3.addWidget(boton_agregar)
        layout3.addWidget(boton_busqueda)
        layout3.addWidget(self.ingreso_busqueda)

        self.layout2.addLayout(layout3)        
    