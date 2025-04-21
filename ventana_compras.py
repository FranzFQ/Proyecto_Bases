from codigo import Codigo
from PyQt6.QtWidgets import QApplication ,QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout, QLabel, QLineEdit, QMessageBox, QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem, QHeaderView 
from PyQt6.QtGui import QIcon, QPixmap, QGuiApplication, QLinearGradient, QColor, QBrush, QPalette
from PyQt6.QtCore import Qt, QSize

class Ventana_compras(Codigo):
    def __init__(self, main_layout, botones, base_datos):
        super().__init__()
        self.layout = main_layout
        self.botones = botones
        self.base_datos = base_datos
        self.layout_extra: QVBoxLayout | None = None

    def compras(self):
        self.limpieza_layout(self.layout)
        self.recoloreas_botones(self.botones)
        self.color_boton_oprimido(self.botones[2])
        self.activar_botones(self.botones)
        self.botones[2].setEnabled(False)

        main_layout = QVBoxLayout()

        layout1 = QHBoxLayout()
        layout1.setAlignment(Qt.AlignmentFlag.AlignTop)

        layout2 = QHBoxLayout()

        self.layout3 = QHBoxLayout()
        self.layout3.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.boton_proveedores = QPushButton()
        self.boton_proveedores.setIcon(QIcon(self.imagen("imagenes/proveedores.png", 90, 90)))
        self.boton_proveedores.setIconSize(QSize(100, 100))
        self.color_boton_sin_oprimir(self.boton_proveedores)
        self.boton_proveedores.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.boton_proveedores.clicked.connect(self.proveedores)

        self.boton_pedido = QPushButton()
        self.boton_pedido.setIcon(QIcon(self.imagen("imagenes/pedido.png", 90, 90)))
        self.boton_pedido.setIconSize(QSize(100, 100))
        self.color_boton_sin_oprimir(self.boton_pedido)
        self.boton_pedido.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.boton_pedido.clicked.connect(self.ingreso_pedido)

        informar = QLabel("Oprima uno de los botones que tiene en la parte superior izquierda")
        informar.setStyleSheet("color: Black; font-size: 20px")
        informar.setAlignment(Qt.AlignmentFlag.AlignTop)
        informar.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        layout1.addItem(self.espacio(35, 35))
        layout1.addWidget(self.boton_proveedores)
        layout1.addWidget(self.boton_pedido)
        layout1.addStretch()
        
        self.layout3.addStretch()
        self.layout3.addWidget(informar)
        self.layout3.addStretch()

        layout2.addItem(self.espacio(35, 35))
        layout2.addLayout(self.layout3)

        main_layout.addLayout(layout1)
        main_layout.addLayout(layout2)

        self.layout.addLayout(main_layout)
    
    def proveedores(self):
        self.limpieza_layout(self.layout3)
        self.boton_proveedores.setEnabled(False)
        self.boton_pedido.setEnabled(True)

        layout_main = QVBoxLayout()
        layout_main.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)    

        layout1 = QHBoxLayout()
        layout1.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.layout4 = QHBoxLayout()

        self.boton_agregar = QPushButton()
        self.boton_agregar.setIcon(QIcon(self.imagen("imagenes/agregar.png", 45, 45)))
        self.boton_agregar.setIconSize(QSize(55, 55))
        self.color_boton_sin_oprimir(self.boton_agregar)
        self.boton_agregar.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.boton_agregar.clicked.connect(self.agregar_proveedor)

        self.boton_eliminar = QPushButton()
        self.boton_eliminar.setIcon(QIcon(self.imagen("imagenes/eliminar.png", 45, 45)))
        self.boton_eliminar.setIconSize(QSize(55, 55))
        self.color_boton_sin_oprimir(self.boton_eliminar)
        self.boton_eliminar.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        self.boton_editar = QPushButton()
        self.boton_editar.setIcon(QIcon(self.imagen("imagenes/editar.png", 45, 45)))
        self.boton_editar.setIconSize(QSize(55, 55))
        self.color_boton_sin_oprimir(self.boton_editar)
        self.boton_editar.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.boton_editar.clicked.connect(self.editar_proveedor)

        self.boton_buscar = QPushButton()
        self.boton_buscar.setIcon(QIcon(self.imagen("imagenes/buscar.png", 45, 45)))
        self.boton_buscar.setIconSize(QSize(55, 55))
        self.color_boton_sin_oprimir(self.boton_buscar)
        self.boton_buscar.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        self.ingreso_busqueda = QLineEdit()
        self.ingreso_busqueda.setPlaceholderText("Ingrese el ID del proveedor")
        self.color_linea(self.ingreso_busqueda)
        self.ingreso_busqueda.setFixedSize(400, 60)
        self.ingreso_busqueda.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        #Tabla de proveedores
        proveedores = [["1", "Francisco Queme", "Direccion X", "Ejemplo@gmail.com"]]

        #tabla de proveedores
        self.tabla_proveedores = QTableWidget(len(proveedores), 4)

        self.tabla_proveedores.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)

        self.tabla_proveedores.setHorizontalHeaderLabels(["ID", "Nombre", "Direccion", "Email"]) 

        for fila, valor in enumerate(proveedores):
            item_id = QTableWidgetItem(valor[0])
            item_nombre = QTableWidgetItem(valor[1])
            item_direccion = QTableWidgetItem(valor[2])
            item_email = QTableWidgetItem(valor[3])

            self.tabla_proveedores.setItem(fila, 0, item_id)
            self.tabla_proveedores.setItem(fila, 1, item_nombre)
            self.tabla_proveedores.setItem(fila, 2, item_direccion)
            self.tabla_proveedores.setItem(fila, 3, item_email)

            for col in range(4):
                item = self.tabla_proveedores.item(fila, col)
                item.setFlags(Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable)
        
        self.tabla_proveedores.resizeColumnsToContents()
        self.color_tabla(self.tabla_proveedores)
        self.tabla_proveedores.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.tabla_proveedores.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        layout1.addWidget(self.boton_agregar)
        layout1.addWidget(self.boton_eliminar)
        layout1.addWidget(self.boton_editar)
        layout1.addWidget(self.boton_buscar)
        layout1.addWidget(self.ingreso_busqueda)

        self.layout4.addWidget(self.tabla_proveedores)

        layout_main.addLayout(layout1)
        layout_main.addLayout(self.layout4)

        self.layout3.addLayout(layout_main)
    
    def agregar_proveedor(self):
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
        agregar_label.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        agregar_label.setScaledContents(True)

        self.ingreso_nombre = QLineEdit()
        self.color_linea(self.ingreso_nombre)
        self.ingreso_nombre.setFixedSize(200, 30)
        self.ingreso_nombre.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        self.ingreso_direccion = QLineEdit()
        self.color_linea(self.ingreso_direccion)
        self.ingreso_direccion.setFixedSize(200, 30)
        self.ingreso_direccion.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        self.ingreso_email = QLineEdit()
        self.color_linea(self.ingreso_email)
        self.ingreso_email.setFixedSize(200, 30)
        self.ingreso_email.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        label_nombre = QLabel("Ingrese el nombre: ")
        label_nombre.setStyleSheet("color: Black")
        label_nombre.setFixedWidth(200)
        label_nombre.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        label_direccion = QLabel("Ingrese la dirrecion: ")
        label_direccion.setStyleSheet("color: Black")
        label_direccion.setFixedWidth(200)
        label_direccion.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        label_email = QLabel("Ingrese el email: ")
        label_email.setStyleSheet("color: Black")
        label_email.setFixedWidth(200)
        label_email.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        boton_agregar = QPushButton("Agregar")
        self.color_boton_sin_oprimir(boton_agregar)
        boton_agregar.setFixedWidth(150)
        boton_agregar.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        boton_cancelar = QPushButton("Cancelar")
        self.color_boton_sin_oprimir(boton_cancelar)
        boton_cancelar.setFixedWidth(150)
        boton_cancelar.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        layout1.addWidget(label_nombre, 0, 0)
        layout1.addWidget(self.ingreso_nombre, 0, 1)
        layout1.addWidget(label_direccion, 1, 0)
        layout1.addWidget(self.ingreso_direccion, 1, 1)
        layout1.addWidget(label_email, 2, 0)
        layout1.addWidget(self.ingreso_email, 2, 1)
        layout1.addWidget(boton_agregar, 3, 0)
        layout1.addWidget(boton_cancelar, 3, 1)

        layout2.addWidget(agregar_label)

        self.layout_extra.addLayout(layout2)
        self.layout_extra.addLayout(layout1)

        self.layout4.addLayout(self.layout_extra)


    def editar_proveedor(self):
        # Cada que se complete una insercion o elemiminacion el Layout se tiene que volver a poner como none (esto no es definitivo)
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

        self.ingreso_direccion = QLineEdit()
        self.color_linea(self.ingreso_direccion)
        self.ingreso_direccion.setFixedSize(200, 30)
        self.ingreso_direccion.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        self.ingreso_email = QLineEdit()
        self.color_linea(self.ingreso_email)
        self.ingreso_email.setFixedSize(200, 30)
        self.ingreso_email.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        label_nombre = QLabel("Ingrese el nombre: ")
        label_nombre.setStyleSheet("color: Black")
        label_nombre.setFixedWidth(200)
        label_nombre.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        label_direccion = QLabel("Ingrese la dirrecion: ")
        label_direccion.setStyleSheet("color: Black")
        label_direccion.setFixedWidth(200)
        label_direccion.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        label_email = QLabel("Ingrese el email: ")
        label_email.setStyleSheet("color: Black")
        label_email.setFixedWidth(200)
        label_email.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        boton_confirmar = QPushButton("Confirmar")
        self.color_boton_sin_oprimir(boton_confirmar)
        boton_confirmar.setFixedWidth(150)
        boton_confirmar.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        boton_cancelar = QPushButton("Cancelar")
        self.color_boton_sin_oprimir(boton_cancelar)
        boton_cancelar.setFixedWidth(150)
        boton_cancelar.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        layout1.addWidget(label_nombre, 0, 0)
        layout1.addWidget(self.ingreso_nombre, 0, 1)
        layout1.addWidget(label_direccion, 1, 0)
        layout1.addWidget(self.ingreso_direccion, 1, 1)
        layout1.addWidget(label_email, 2, 0)
        layout1.addWidget(self.ingreso_email, 2, 1)
        layout1.addWidget(boton_confirmar, 3, 0)
        layout1.addWidget(boton_cancelar, 3, 1)

        layout2.addWidget(agregar_label)

        self.layout_extra.addLayout(layout2)
        self.layout_extra.addLayout(layout1)

        self.layout4.addLayout(self.layout_extra)

    def ingreso_pedido(self):
        self.limpieza_layout(self.layout3)
        self.boton_proveedores.setEnabled(True)
        self.boton_pedido.setEnabled(False)

        layout1 = QHBoxLayout()
        layout2 = QHBoxLayout()

        layout_tabla1 = QVBoxLayout()

        layout_tabla2 = QVBoxLayout()

        #Tabla de inventario
        inventario = [["1", "Calculadora", 10, 150]]
        
        self.tabla_inventario = QTableWidget(len(inventario), 4)

        self.tabla_inventario.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)

        self.tabla_inventario.setHorizontalHeaderLabels(["ID", "Nombre", "Existencias", "Costo"]) 

        for fila, valor in enumerate(inventario):
            item_id = QTableWidgetItem(valor[0])
            item_nombre = QTableWidgetItem(valor[1])
            item_existencia = QTableWidgetItem(f"{valor[2]}")
            item_costo = QTableWidgetItem(f"Q{valor[3]:.2f}")

            self.tabla_inventario.setItem(fila, 0, item_id)
            self.tabla_inventario.setItem(fila, 1, item_nombre)
            self.tabla_inventario.setItem(fila, 2, item_existencia)
            self.tabla_inventario.setItem(fila, 3, item_costo)

            for col in range(4):
                item = self.tabla_inventario.item(fila, col)
                item.setFlags(Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable)
        
        self.tabla_inventario.resizeColumnsToContents()
        self.color_tabla(self.tabla_inventario)
        self.tabla_inventario.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.tabla_inventario.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.tabla_inventario.cellDoubleClicked.connect(self.agregar_cantidad)

        self.boton_buscar = QPushButton()
        self.boton_buscar.setIcon(QIcon(self.imagen("imagenes/buscar.png", 45, 45)))
        self.boton_buscar.setIconSize(QSize(55, 55))
        self.color_boton_sin_oprimir(self.boton_buscar)
        self.boton_buscar.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        self.ingreso_busqueda = QLineEdit()
        self.ingreso_busqueda.setPlaceholderText("Ingrese el ID del producto")
        self.color_linea(self.ingreso_busqueda)
        self.ingreso_busqueda.setFixedHeight(60)
        self.ingreso_busqueda.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

        #Tabla de Ingreso de nuevo producto
        ingreso = [["1", "Calculadora", 10, 150]]

        self.tabla_ingreso = QTableWidget(len(ingreso), 4)

        self.tabla_ingreso.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)

        self.tabla_ingreso.setHorizontalHeaderLabels(["ID", "Nombre", "Nueva existencia", "Costo"]) 

        for fila, valor in enumerate(ingreso):
            item_id = QTableWidgetItem(valor[0])
            item_nombre = QTableWidgetItem(valor[1])
            item_existencia = QTableWidgetItem(f"{valor[2]}")
            item_costo = QTableWidgetItem(f"Q{valor[3]:.2f}")

            self.tabla_ingreso.setItem(fila, 0, item_id)
            self.tabla_ingreso.setItem(fila, 1, item_nombre)
            self.tabla_ingreso.setItem(fila, 2, item_existencia)
            self.tabla_ingreso.setItem(fila, 3, item_costo)

            for col in range(4):
                item = self.tabla_ingreso.item(fila, col)
                item.setFlags(Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable)
        
        self.tabla_ingreso.resizeColumnsToContents()
        self.color_tabla(self.tabla_ingreso)
        self.tabla_ingreso.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.tabla_ingreso.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        ingreso_label = QLineEdit()
        ingreso_label.setPlaceholderText("Actualizacion del inventario")
        self.color_linea(ingreso_label)
        ingreso_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        ingreso_label.setFixedHeight(60)
        ingreso_label.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        ingreso_label.setEnabled(False)

        self.total = QLineEdit()
        self.total.setPlaceholderText("Total del ingreso: Q0.00")
        self.color_linea(self.total)
        self.total.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.total.setFixedHeight(50)
        self.total.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.total.setEnabled(False)

        boton_confirmar = QPushButton("Confirmar")
        boton_confirmar.setFixedHeight(50)
        self.color_boton_sin_oprimir(boton_confirmar)
        boton_confirmar.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        
        boton_cancelar = QPushButton("Cancelar")
        boton_cancelar.setFixedHeight(50)
        self.color_boton_sin_oprimir(boton_cancelar)
        boton_cancelar.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

        layout1.addWidget(self.ingreso_busqueda)
        layout1.addWidget(self.boton_buscar)

        layout_tabla1.addLayout(layout1)
        layout_tabla1.addWidget(self.tabla_inventario)

        layout2.addWidget(boton_confirmar)
        layout2.addWidget(boton_cancelar)

        layout_tabla2.addWidget(ingreso_label)
        layout_tabla2.addWidget(self.tabla_ingreso)
        layout_tabla2.addWidget(self.total)
        layout_tabla2.addLayout(layout2)

        self.layout3.addLayout(layout_tabla1)
        self.layout3.addLayout(layout_tabla2)

    def agregar_cantidad(self):
        self.ventana_cantidad = QWidget()
        self.fondo_degradado(self.ventana_cantidad, "#5DA9F5", "#0037FF")
        self.ventana_cantidad.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        main_layout = QGridLayout()
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout1 = QHBoxLayout()
            
        self.cantidad = QLineEdit()
        self.cantidad.setPlaceholderText("Ingrese la cantidad")
        self.color_linea(self.cantidad)
        self.cantidad.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.cantidad.setFixedHeight(30)
        self.cantidad.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)

        boton_confirmar = QPushButton("Confirmar")
        self.color_boton_sin_oprimir(boton_confirmar)
        boton_confirmar.setFixedSize(100, 20)
        boton_confirmar.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.asignacion_tecla(self.ventana_cantidad, "Return", boton_confirmar)

        boton_cancelar = QPushButton("Cancelar")
        self.color_boton_sin_oprimir(boton_cancelar)
        boton_cancelar.setFixedSize(100, 20)
        boton_cancelar.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.asignacion_tecla(self.ventana_cantidad, "Esc", boton_cancelar)
        boton_cancelar.clicked.connect(self.cancelar_cantidad)

        layout1.addWidget(boton_confirmar)
        layout1.addWidget(boton_cancelar)

        main_layout.addWidget(self.cantidad, 0, 0)
        main_layout.addLayout(layout1, 1, 0)

        self.ventana_cantidad.setLayout(main_layout)
        self.ventana_cantidad.showNormal()