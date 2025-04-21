from codigo import Codigo
from PyQt6.QtWidgets import QApplication ,QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout, QLabel, QLineEdit, QMessageBox, QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem, QHeaderView 
from PyQt6.QtGui import QIcon, QPixmap, QGuiApplication, QLinearGradient, QColor, QBrush, QPalette
from PyQt6.QtCore import Qt, QSize

class Ventana_usuarios(Codigo):
    def __init__(self, main_layout, botones, base_datos):
        super().__init__()
        self.layout = main_layout
        self.botones = botones
        self.base_datos = base_datos
        self.layout_extra: QVBoxLayout | None = None

    def usuario(self):
        self.limpieza_layout(self.layout)
        self.recoloreas_botones(self.botones)
        self.color_boton_oprimido(self.botones[0])
        self.activar_botones(self.botones)
        self.botones[0].setEnabled(False)
        
        main_layout = QHBoxLayout()

        sub_layout = QVBoxLayout()

        layout3 = QHBoxLayout()
        layout3.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        
        self.layout4 = QHBoxLayout()
        self.layout4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.boton_editar = QPushButton()
        self.boton_editar.setIcon(QIcon(self.imagen("imagenes/editar.png", 50, 50)))
        self.boton_editar.setIconSize(QSize(70, 70))
        self.boton_editar.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.color_boton_sin_oprimir(self.boton_editar)
        self.boton_editar.clicked.connect(self.editar_usuario)  

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
        self.boton_agregar.clicked.connect(self.agregar_usuario)

        self.boton_busqueda = QPushButton()
        self.boton_busqueda.setIcon(QIcon(self.imagen("imagenes/buscar.png", 50, 50)))
        self.boton_busqueda.setIconSize(QSize(70, 70))
        self.boton_busqueda.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.color_boton_sin_oprimir(self.boton_busqueda)
        

        self.ingreso_busqueda = QLineEdit()
        self.ingreso_busqueda.setPlaceholderText("Ingrese el nombre del producto...")
        self.color_linea(self.ingreso_busqueda)
        self.ingreso_busqueda.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ingreso_busqueda.setFixedSize(400, 80)
        self.ingreso_busqueda.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        # creacion de tabla,
        usuarios =  [["1", "root", "Ejemplo@gmail.com", "Telefono1", "Vendedora"]] 

        # Crear la tabla con el número correcto de filas y columnas
        self.tabla_usuarios = QTableWidget(len(usuarios), 5)
        self.tabla_usuarios.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)

        # Define los encabezados de las columnas
        self.tabla_usuarios.setHorizontalHeaderLabels(["ID", "Nombre", "Correo", "Telefono", "Puesto"])

        # Llenar la tabla con los datos
        for fila, usuario in enumerate(usuarios):
            id_item = QTableWidgetItem(usuario[0])
            nombre_item = QTableWidgetItem(usuario[1])
            email_item = QTableWidgetItem(usuario[2])
            telefono_item = QTableWidgetItem(usuario[3]) 
            puesto_item = QTableWidgetItem(usuario[4])
            
            # Añadir items a la tabla
            self.tabla_usuarios.setItem(fila, 0, id_item)
            self.tabla_usuarios.setItem(fila, 1, nombre_item)
            self.tabla_usuarios.setItem(fila, 2, email_item)
            self.tabla_usuarios.setItem(fila, 3, telefono_item)
            self.tabla_usuarios.setItem(fila, 4, puesto_item)
            
            # Configurar flags para todos los items
            for col in range(5):
                item = self.tabla_usuarios.item(fila, col)
                item.setFlags(Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable)

        # Opcional: Ajustar el tamaño de las columnas al contenido
        self.tabla_usuarios.resizeColumnsToContents()
        #Modificacion del color, bordes y fondo de la tabla
        self.color_tabla(self.tabla_usuarios)
        self.tabla_usuarios.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.tabla_usuarios.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        layout3.addWidget(self.boton_editar)
        layout3.addWidget(self.boton_eliminar)
        layout3.addWidget(self.boton_agregar)
        layout3.addWidget(self.boton_busqueda)
        layout3.addWidget(self.ingreso_busqueda)

        self.layout4.addWidget(self.tabla_usuarios)
        self.layout4.addItem(self.espacio(20, 20))
        
        sub_layout.addLayout(layout3)
        sub_layout.addLayout(self.layout4)

        main_layout.addItem(self.espacio(35, 35))
        main_layout.addLayout(sub_layout)
        self.layout.addLayout(main_layout)

    def agregar_usuario(self):
        # Cada que se complete una insercion o elemiminacion el Layout se tiene que volver a poner como none (esto no es definitivo)
        if self.layout_extra is not None:
            self.limpieza_layout(self.layout_extra)

        self.layout_extra = QVBoxLayout()
        self.layout_extra.setAlignment(Qt.AlignmentFlag.AlignTop)

        layout1 = QGridLayout()
        layout2 = QHBoxLayout()
        layout2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.boton_agregar.setEnabled(False)
        self.boton_eliminar.setEnabled(True)
        self.boton_editar.setEnabled(True)

        imagen_agregar = self.imagen("imagenes/agregar.png", 90, 90)
        agregar_label = QLabel()
        agregar_label.setPixmap(imagen_agregar)
        agregar_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        agregar_label.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        agregar_label.setScaledContents(True)

        self.ingreso_nombre = QLineEdit()
        self.color_linea(self.ingreso_nombre)
        self.ingreso_nombre.setFixedSize(200, 30)
        self.ingreso_nombre.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        self.ingreso_email = QLineEdit()
        self.color_linea(self.ingreso_email)
        self.ingreso_email.setFixedSize(200, 30)
        self.ingreso_email.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        self.ingreso_telefono = QLineEdit()
        self.color_linea(self.ingreso_telefono)
        self.ingreso_telefono.setFixedSize(200, 30)
        self.ingreso_telefono.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        self.ingreso_puesto = QLineEdit()
        self.color_linea(self.ingreso_puesto)
        self.ingreso_puesto.setFixedSize(200, 30)
        self.ingreso_puesto.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        label_nombre = QLabel("Ingrese el nombre: ")
        label_nombre.setStyleSheet("color: Black")
        label_nombre.setFixedWidth(200)
        label_nombre.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        label_email = QLabel("Ingrese el email: ")
        label_email.setStyleSheet("color: Black")
        label_email.setFixedWidth(200)
        label_email.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        label_telfono = QLabel("Ingrese el telefono: ")
        label_telfono.setStyleSheet("color: Black")
        label_telfono.setFixedWidth(200)
        label_telfono.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        label_puesto = QLabel("Ingrese el puesto: ")
        label_puesto.setStyleSheet("color: Black")
        label_puesto.setFixedWidth(200)
        label_puesto.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        boton_confirmar = QPushButton("Agregar")
        self.color_boton_sin_oprimir(boton_confirmar)
        boton_confirmar.setFixedWidth(150)
        boton_confirmar.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        boton_cancelar = QPushButton("Cancelar")
        self.color_boton_sin_oprimir(boton_cancelar)
        boton_cancelar.setFixedWidth(150)
        boton_cancelar.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        layout2.addWidget(agregar_label)

        layout1.addWidget(label_nombre, 0, 0)
        layout1.addWidget(self.ingreso_nombre, 0, 1)
        layout1.addWidget(label_telfono, 1, 0)
        layout1.addWidget(self.ingreso_telefono, 1, 1)
        layout1.addWidget(label_email, 2, 0)
        layout1.addWidget(self.ingreso_email, 2, 1)
        layout1.addWidget(label_puesto, 3, 0)
        layout1.addWidget(self.ingreso_puesto, 3, 1)
        layout1.addWidget(boton_confirmar, 4, 0)
        layout1.addWidget(boton_cancelar, 4, 1)
        
        self.layout_extra.addLayout(layout2)
        self.layout_extra.addLayout(layout1)

        self.layout4.addLayout(self.layout_extra)


    def editar_usuario(self):
        if self.layout_extra is not None:
            self.limpieza_layout(self.layout_extra)

        self.layout_extra = QVBoxLayout()
        self.layout_extra.setAlignment(Qt.AlignmentFlag.AlignTop)

        layout1 = QGridLayout()
        layout2 = QHBoxLayout()
        layout2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.boton_agregar.setEnabled(True)
        self.boton_eliminar.setEnabled(True)
        self.boton_editar.setEnabled(False)

        imagen_agregar = self.imagen("imagenes/editar.png", 90, 90)
        agregar_label = QLabel()
        agregar_label.setPixmap(imagen_agregar)
        agregar_label.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        agregar_label.setScaledContents(True)

        self.ingreso_nombre = QLineEdit()
        self.color_linea(self.ingreso_nombre)
        self.ingreso_nombre.setFixedSize(200, 30)
        self.ingreso_nombre.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        self.ingreso_email = QLineEdit()
        self.color_linea(self.ingreso_email)
        self.ingreso_email.setFixedSize(200, 30)
        self.ingreso_email.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        self.ingreso_telefono = QLineEdit()
        self.color_linea(self.ingreso_telefono)
        self.ingreso_telefono.setFixedSize(200, 30)
        self.ingreso_telefono.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        self.ingreso_puesto = QLineEdit()
        self.color_linea(self.ingreso_puesto)
        self.ingreso_puesto.setFixedSize(200, 30)
        self.ingreso_puesto.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        label_nombre = QLabel("Ingrese el nombre: ")
        label_nombre.setStyleSheet("color: Black")
        label_nombre.setFixedWidth(200)
        label_nombre.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        label_email = QLabel("Ingrese el email: ")
        label_email.setStyleSheet("color: Black")
        label_email.setFixedWidth(200)
        label_email.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        label_telfono = QLabel("Ingrese el telefono: ")
        label_telfono.setStyleSheet("color: Black")
        label_telfono.setFixedWidth(200)
        label_telfono.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        label_puesto = QLabel("Ingrese el puesto: ")
        label_puesto.setStyleSheet("color: Black")
        label_puesto.setFixedWidth(200)
        label_puesto.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        boton_confirmar = QPushButton("Confirmar")
        self.color_boton_sin_oprimir(boton_confirmar)
        boton_confirmar.setFixedWidth(150)
        boton_confirmar.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        boton_cancelar = QPushButton("Cancelar")
        self.color_boton_sin_oprimir(boton_cancelar)
        boton_cancelar.setFixedWidth(150)
        boton_cancelar.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        
        layout2.addWidget(agregar_label) 

        layout1.addWidget(label_nombre, 0, 0)
        layout1.addWidget(self.ingreso_nombre, 0, 1)
        layout1.addWidget(label_telfono, 1, 0)
        layout1.addWidget(self.ingreso_telefono, 1, 1)
        layout1.addWidget(label_email, 2, 0)
        layout1.addWidget(self.ingreso_email, 2, 1)
        layout1.addWidget(label_puesto, 3, 0)
        layout1.addWidget(self.ingreso_puesto, 3, 1)
        layout1.addWidget(boton_confirmar, 4, 0)
        layout1.addWidget(boton_cancelar, 4, 1)

        self.layout_extra.addLayout(layout2)
        self.layout_extra.addLayout(layout1)

        self.layout4.addLayout(self.layout_extra)