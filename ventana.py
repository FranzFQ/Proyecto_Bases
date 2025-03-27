import sys
from PyQt6.QtWidgets import QApplication ,QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QMessageBox, QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem, QHeaderView 
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QPixmap, QGuiApplication

class Ventana:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.window1 = QWidget()
        self.window2 = QWidget()

        self.window1.setStyleSheet("background-color: #72cee9;")
        self.window1.setWindowTitle("Inicio de sesion")
        self.window1.setWindowIcon(QIcon("imagenes/logo.ico"))

        self.window2.setStyleSheet("background-color: #00fff0;")
        self.window2.setWindowIcon(QIcon("imagenes/logo.ico"))
        self.ventana_maxima(self.window2)

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
        mesaje_error = QMessageBox()
        mesaje_error.setIcon(QMessageBox.Icon.Warning)
        mesaje_error.setStyleSheet("QMessageBox { color: black; background-color: #e15f5f;} QPushButton {color: black; background-color: #ff0000;} QLabel{color: black;}")
        mesaje_error.setWindowIcon(QIcon("imagenes/warning.ico")) 
        mesaje_error.setWindowTitle(titulo)
        mesaje_error.setText(mensaje)
        mesaje_error.setDefaultButton(QMessageBox.StandardButton.Ok)
        mesaje_error.exec()

    def mensaje_informacion(self, titulo, mensaje):
        mensaje_informacion = QMessageBox()
        mensaje_informacion.setStyleSheet("QMessageBox { color: black; background-color: #36dfea;} QPushButton {color: black; background-color: #22a4ac;} QLabel{color: black;}")
        mensaje_informacion.setWindowIcon(QIcon("imagenes/infomation.ico"))
        mensaje_informacion.setWindowTitle(titulo)
        mensaje_informacion.setText(mensaje)
        mensaje_informacion.setIcon(QMessageBox.Icon.Information)
        mensaje_informacion.setDefaultButton(QMessageBox.StandardButton.Ok) 
        mensaje_informacion.exec()

    def color_boton_sin_oprimir(self, boton):
        boton.setStyleSheet("QPushButton {background-color: white; border: 5px solid black; color: black} QPushButton:hover {background-color: #e1e1e1;} QPushButton:pressed {background-color: #c1c1c1;}")

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
        self.boton_inicio.setEnabled(True)

    def recoloreas_botones(self):
        self.color_boton_sin_oprimir(self.boton_compras)
        self.color_boton_sin_oprimir(self.boton_ventas)
        self.color_boton_sin_oprimir(self.boton_usuario)
        self.color_boton_sin_oprimir(self.boton_inventario)

    def color_tabla(self, tabla):
        tabla.setStyleSheet("QTableWidget {background-color: white; border: 5px solid black;} QTableWidget::item {background-color: 00f4ff; color: black;} QTableWidget::item:selected {background-color: #1fdde5; color: black;} QTableWidget::item:hover {background-color: #4cd9df; color: black;} QHeaderView::section {background-color: #94fbff; color: black;}")

    def ventana_maxima(self, window):
        pantalla = QGuiApplication.primaryScreen() 
        screen_rect = pantalla.availableGeometry()
        window.setGeometry(screen_rect)

# Inicio de las ventanas del programa

    def inicio(self):
        main_layout = QVBoxLayout()
        layout1 = QHBoxLayout()
        layout1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout2 = QHBoxLayout()
        layout2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout3 = QHBoxLayout()
        layout3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout4 = QVBoxLayout()
        layout4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        espacio = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        usuario_imagen = self.imagen("imagenes/usuario.png", 150, 150)
        usuario_label = QLabel()
        usuario_label.setPixmap(usuario_imagen)
        usuario_label.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        layout4.addWidget(usuario_label)

        usuario = QLabel("Ingrese el usuario:")
        usuario.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        usuario.setStyleSheet("Color: black")

        self.ingreso_usuario = QLineEdit()
        self.ingreso_usuario.setStyleSheet("Color: black; background-color: #bf35e1;")
        self.ingreso_usuario.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.ingreso_usuario.setFixedWidth(200)

        contrasenia = QLabel("Ingrese la contraseña:")
        contrasenia.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        contrasenia.setStyleSheet("Color: black")

        self.ingreso_contrasenia = QLineEdit()
        self.ingreso_contrasenia.setStyleSheet("Color: black; background-color: #bf35e1;")
        self.ingreso_contrasenia.setEchoMode(QLineEdit.EchoMode.Password)
        self.ingreso_contrasenia.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.ingreso_contrasenia.setFixedWidth(200)

        boton_ingresar = QPushButton("Ingresar")
        boton_ingresar.clicked.connect(self.verificacion)
        boton_ingresar.setStyleSheet("background-color: white; color: black")
        boton_ingresar.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        boton_ingresar.setFixedWidth(175)

        boton_cancelar = QPushButton("cancelar")
        boton_cancelar.clicked.connect(self.cancelar_inicio)
        boton_cancelar.setStyleSheet("background-color: white; color: black")
        boton_cancelar.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        boton_cancelar.setFixedWidth(175)

        layout1.addWidget(usuario)
        layout1.addItem(espacio)
        layout1.addWidget(self.ingreso_usuario)
        layout2.addWidget(contrasenia)
        layout2.addItem(espacio)
        layout2.addWidget(self.ingreso_contrasenia)
        layout3.addWidget(boton_ingresar)
        layout3.addItem(espacio)
        layout3.addWidget(boton_cancelar) 
        main_layout.addLayout(layout4)
        main_layout.addLayout(layout1)
        main_layout.addLayout(layout2)
        main_layout.addLayout(layout3)
        self.window1.setLayout(main_layout)
        self.window1.showNormal()
        self.window1.activateWindow()

    def verificacion(self):
        print(self.ingreso_usuario.text(), self.ingreso_contrasenia.text())
        if self.ingreso_usuario.text() == "admin" and self.ingreso_contrasenia.text() == "admin":
            self.window1.close()
            self.ventana_principal()
        else:
            self.mensaje_error("Error", "Usuario o contraseña incorrectos")

    def cancelar_inicio(self):
        self.ingreso_usuario.clear()
        self.ingreso_contrasenia.clear()
        self.mensaje_informacion("Cancelado", "Inicio de sesion cancelado")

    def regreso(self):
        aviso = QMessageBox()
        aviso.setStyleSheet("QMessageBox { color: black; background-color: #36dfea;} QPushButton {color: black; background-color: #22a4ac;} QLabel{color: black;}")
        aviso.setWindowIcon(QIcon("imagenes/infomation.ico"))
        aviso.setWindowTitle("¿Cerrar sesion?")
        aviso.setText("Seguro que quiere cerrar la sesion actual")
        aviso.setIcon(QMessageBox.Icon.Information)
        aviso.addButton("Si", QMessageBox.ButtonRole.YesRole)
        aviso.addButton("No", QMessageBox.ButtonRole.NoRole)
        respuesta = aviso.exec()
        if respuesta == 2:
            self.window2.close()
            self.inicio()
            self.mensaje_informacion("Sesion cerrada", "La sesion se ha cerrado correctamente")
        
        elif respuesta == 3:
            self.mensaje_informacion("Cierre de sesion cancelada", "La sesion se a cancelado correctamente")

    def ventana_principal(self):
        self.window2.setWindowTitle("Bienvenido usuario: " + "admin")
        main_layout = QHBoxLayout()

        layout1 = QVBoxLayout()
        layout1.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)

        self.layout2 = QVBoxLayout()
        self.layout2.setAlignment(Qt.AlignmentFlag.AlignLeft)

        sub_layout2 = QHBoxLayout()

        espacio = QSpacerItem(10, 10, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        espacio_layout2 = QSpacerItem(100, 100, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)

        self.boton_inicio = QPushButton()
        self.boton_inicio.setIcon(QIcon(self.imagen("imagenes/inicio.png", 80, 80)))
        self.boton_inicio.setIconSize(QSize(150, 100))
        self.color_boton_sin_oprimir(self.boton_inicio)
        self.boton_inicio.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.boton_inicio.clicked.connect(self.regreso)

        self.boton_usuario = QPushButton()
        self.boton_usuario.setIcon(QIcon(self.imagen("imagenes/usuarios.png", 100, 100)))
        self.boton_usuario.setIconSize(QSize(150, 150))
        self.color_boton_sin_oprimir(self.boton_usuario)
        self.boton_usuario.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.boton_usuario.clicked.connect(self.ventana_usuario)

        self.boton_ventas = QPushButton()
        self.boton_ventas.setIcon(QIcon(self.imagen("imagenes/ventas.png", 100, 100)))
        self.boton_ventas.setIconSize(QSize(150, 150))
        self.color_boton_sin_oprimir(self.boton_ventas)
        self.boton_ventas.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.boton_ventas.clicked.connect(self.ventana_ventas)

        self.boton_compras = QPushButton()
        self.boton_compras.setIcon(QIcon(self.imagen("imagenes/compras.png", 100, 100)))
        self.boton_compras.setIconSize(QSize(150, 150))
        self.color_boton_sin_oprimir(self.boton_compras)
        self.boton_compras.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.boton_compras.clicked.connect(self.ventana_compras)

        self.boton_inventario = QPushButton()
        self.boton_inventario.setIcon(QIcon(self.imagen("imagenes/inventario.png", 100, 100)))
        self.boton_inventario.setIconSize(QSize(150, 150))
        self.color_boton_sin_oprimir(self.boton_inventario)
        self.boton_inventario.clicked.connect(self.ventana_inventario)
        self.boton_inventario.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        logo = QLabel()
        logo.setPixmap(self.imagen("imagenes/logo_libreria.png", 400, 400))
        logo.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sub_layout2.addWidget(logo)

        sub_layout2.addItem(espacio_layout2)

        self.layout2.addLayout(sub_layout2)

        layout1.addWidget(self.boton_inicio)
        layout1.addItem(espacio)
        layout1.addWidget(self.boton_usuario)
        layout1.addItem(espacio)
        layout1.addWidget(self.boton_ventas)
        layout1.addItem(espacio)
        layout1.addWidget(self.boton_compras)
        layout1.addItem(espacio)
        layout1.addWidget(self.boton_inventario)
        
        main_layout.addLayout(layout1)
        main_layout.addLayout(self.layout2)
        self.window2.setLayout(main_layout)
        self.ventana_maxima(self.window2)
        self.window2.show()
        self.window2.activateWindow()

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
        
        self.main_layout_ventana_inventario = QHBoxLayout()

        sub_layout = QVBoxLayout()

        layout3 = QHBoxLayout()
        layout3.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        
        layout4 = QHBoxLayout()
        layout4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        espacio = QSpacerItem(60, 60, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        self.boton_editar = QPushButton()
        self.boton_editar.setIcon(QIcon(self.imagen("imagenes/editar.png", 50, 50)))
        self.boton_editar.setIconSize(QSize(70, 70))
        self.boton_editar.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.color_boton_sin_oprimir(self.boton_editar)
        self.boton_editar.clicked.connect(self.editar_elemento)

        self.boton_eliminar = QPushButton()
        self.boton_eliminar.setIcon(QIcon(self.imagen("imagenes/eliminar.png", 50, 50)))
        self.boton_eliminar.setIconSize(QSize(70, 70))
        self.boton_eliminar.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.color_boton_sin_oprimir(self.boton_eliminar)

        self.boton_agregar = QPushButton()
        self.boton_agregar.setIcon(QIcon(self.imagen("imagenes/agregar.png", 50, 50)))
        self.boton_agregar.setIconSize(QSize(70, 70))
        self.boton_agregar.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.color_boton_sin_oprimir(self.boton_agregar)

        self.boton_busqueda = QPushButton()
        self.boton_busqueda.setIcon(QIcon(self.imagen("imagenes/buscar.png", 50, 50)))
        self.boton_busqueda.setIconSize(QSize(70, 70))
        self.boton_busqueda.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.color_boton_sin_oprimir(self.boton_busqueda)

        self.ingreso_busqueda = QLineEdit()
        self.ingreso_busqueda.setPlaceholderText("Ingrese el codigo de su producto")
        self.ingreso_busqueda.setStyleSheet("Color: black; background-color: #77f9ff; border: 5px solid black;")
        self.ingreso_busqueda.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ingreso_busqueda.setFixedSize(400, 80)
        self.ingreso_busqueda.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

    # creacion de tabla
        #Matriz de ejemplo
        inventario = [["1", "Caja de lapices","2","15Q", "Descripcion 1"], ["2", "Caja de boradores","5" ,"20Q", "Descripcion 2"], ["3", "Resma de hojas","10" ,"25Q", "Descripcion 3"]]
        tabla = QTableWidget(len(inventario), len(inventario[0]))

        #Define el indice de las columnas
        tabla.setHorizontalHeaderLabels(["ID", "Nombre", "Existencias", "Precio", "Descripcion"])
        
        #Se ingresan los datos a la tabla con base a la posicion en (x, y) junto con itme
        for fila in range(len(inventario)):
            for columna in range(len(inventario[0])):
                tabla.setItem(fila, columna, QTableWidgetItem(inventario[fila][columna]))

        #Modificacion del color, bordes y fondo de la tabla
        self.color_tabla(tabla)
        tabla.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        tabla.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)

        layout3.addWidget(self.boton_editar)
        layout3.addWidget(self.boton_eliminar)
        layout3.addWidget(self.boton_agregar)
        layout3.addWidget(self.boton_busqueda)
        layout3.addWidget(self.ingreso_busqueda)

        layout4.addWidget(tabla)
        
        sub_layout.addLayout(layout3)
        sub_layout.addLayout(layout4)
        self.main_layout_ventana_inventario.addItem(espacio)
        self.main_layout_ventana_inventario.addLayout(sub_layout)
        self.layout2.addLayout(self.main_layout_ventana_inventario)

    def editar_elemento(self):
        self.boton_editar.setEnabled(False)
        self.main_layout_editar_elemento = QHBoxLayout()
        layout1 = QVBoxLayout()
        layout2 = QHBoxLayout()
        layout3 = QHBoxLayout()
        layout4 = QHBoxLayout()
        layout5 = QHBoxLayout()
        layout6 = QHBoxLayout()

        espacio = QSpacerItem(60, 60, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        image_editar = self.imagen("imagenes/editar.png", 150, 150)
        imagen = QLabel()
        imagen.setPixmap(image_editar)
        imagen.setAlignment(Qt.AlignmentFlag.AlignCenter)
        imagen.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        layout1.addWidget(imagen)

        nombre_producto = QLabel("Nombre del producto: ")
        nombre_producto.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        nombre_producto.setStyleSheet("Color: black")

        self.ingreso_nombre_producto = QLineEdit()
        self.ingreso_nombre_producto.setStyleSheet("Color: black; background-color: #bf35e1;")
        self.ingreso_nombre_producto.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.ingreso_nombre_producto.setFixedWidth(200)

        existencia_producto = QLabel("Existencias del producto")
        existencia_producto.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        existencia_producto.setStyleSheet("Color: black")

        self.ingreso_existencia_producto = QLineEdit()
        self.ingreso_existencia_producto.setStyleSheet("Color: black; background-color: #bf35e1;")
        self.ingreso_existencia_producto.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.ingreso_existencia_producto.setFixedWidth(200)

        precio_producto = QLabel("Precio del producto: ")
        precio_producto.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        precio_producto.setStyleSheet("Color: black")

        self.ingreso_precio_producto = QLineEdit()
        self.ingreso_precio_producto.setStyleSheet("Color: black; background-color: #bf35e1;")
        self.ingreso_precio_producto.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.ingreso_precio_producto.setFixedWidth(200)

        descripcion_producto = QLabel("Descripcion del producto")
        descripcion_producto.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        descripcion_producto.setStyleSheet("Color: black")

        self.ingreso_descripcion_producto = QLineEdit()
        self.ingreso_descripcion_producto.setStyleSheet("Color: black; background-color: #bf35e1;")
        self.ingreso_descripcion_producto.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.ingreso_descripcion_producto.setFixedWidth(200)

        boton_confirmar = QPushButton("Confirmar")
        self.color_boton_sin_oprimir(boton_confirmar)
        boton_confirmar.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        boton_cancelar = QPushButton("Cancelar")
        self.color_boton_sin_oprimir(boton_cancelar)
        boton_cancelar.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        layout2.addWidget(nombre_producto)
        layout2.addWidget(self.ingreso_nombre_producto)

        layout3.addWidget(existencia_producto)
        layout3.addWidget(self.ingreso_existencia_producto)

        layout4.addWidget(precio_producto)
        layout4.addWidget(self.ingreso_precio_producto)

        layout5.addWidget(descripcion_producto)
        layout5.addWidget(self.ingreso_descripcion_producto)

        layout6.addWidget(boton_confirmar)
        layout6.addWidget(boton_cancelar)

        layout1.addLayout(layout2)
        layout1.addLayout(layout3)
        layout1.addLayout(layout4)
        layout1.addLayout(layout5)
        layout1.addLayout(layout6)

        self.main_layout_editar_elemento.addItem(espacio)
        self.main_layout_editar_elemento.addLayout(layout1)
        self.main_layout_ventana_inventario.addLayout(self.main_layout_editar_elemento)
        