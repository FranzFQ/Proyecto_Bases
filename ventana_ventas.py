from codigo import Codigo
from PyQt6.QtWidgets import QApplication ,QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout, QLabel, QLineEdit, QMessageBox, QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem, QHeaderView 
from PyQt6.QtGui import QIcon, QPixmap, QGuiApplication, QLinearGradient, QColor, QBrush, QPalette
from PyQt6.QtCore import Qt, QSize

class Ventana_ventas(Codigo):
    def __init__(self, main_layout: QVBoxLayout, botones, base_datos):
        super().__init__()
        self.layout = main_layout
        self.botones = botones
        self.base_datos = base_datos

    def ventas(self):
        self.limpieza_layout(self.layout)
        self.recoloreas_botones(self.botones)
        self.color_boton_oprimido(self.botones[1])
        self.activar_botones(self.botones)
        self.botones[1].setEnabled(False)

        main_layout = QHBoxLayout()
        layout1 = QVBoxLayout()

        layout2 = QHBoxLayout()
        layout2.setAlignment(Qt.AlignmentFlag.AlignLeft)

        layout3 = QVBoxLayout()

        layout4 = QVBoxLayout()
        layout4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout5 = QHBoxLayout()
        layout5.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.ingreso_busqueda = QLineEdit()
        self.ingreso_busqueda.setPlaceholderText("Ingrese el nombre del producto...")
        self.color_linea(self.ingreso_busqueda)
        self.ingreso_busqueda.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ingreso_busqueda.setFixedHeight(80)
        self.ingreso_busqueda.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

        boton_buscar = QPushButton()
        boton_buscar.setIcon(QIcon(self.imagen("imagenes/buscar.png", 65, 65)))
        boton_buscar.setIconSize(QSize(75, 75))
        self.color_boton_sin_oprimir(boton_buscar)
        boton_buscar.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        
        #Inventario de prueba
        inventario = [["2", "Calculadora", 12]]

        #Tabla de ventas
        self.tabla1 = QTableWidget(len(inventario), 3)
        self.tabla1.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)

        self.tabla1.setHorizontalHeaderLabels(["ID", "Nombre", "Precio"]) 

        for fila, valor in enumerate(inventario):
            item_nombre = QTableWidgetItem(valor[0])
            item_cantidad = QTableWidgetItem(valor[1])
            item_precio = QTableWidgetItem(f"Q{valor[2]:.2f}")

            self.tabla1.setItem(fila, 0, item_nombre)
            self.tabla1.setItem(fila, 1, item_cantidad)
            self.tabla1.setItem(fila, 2, item_precio)

            for col in range(3):
                item = self.tabla1.item(fila, col)
                item.setFlags(Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable)
        
        self.tabla1.resizeColumnsToContents()
        self.color_tabla(self.tabla1)
        self.tabla1.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.tabla1.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.tabla1.cellDoubleClicked.connect(self.agregar_cantidad)

        carrito_label = QLineEdit()
        carrito_label.setPlaceholderText("Carrito")
        self.color_linea(carrito_label)
        carrito_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        carrito_label.setFixedHeight(80)
        carrito_label.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        carrito_label.setEnabled(False)

        #carrito de prueba
        carrito = [["Calculadora", 10, 12]]

        #Tabla carrito
        self.tabla2 = QTableWidget(len(carrito), 3)
        self.tabla2.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)

        self.tabla2.setHorizontalHeaderLabels(["Nombre", "Cantidad", "Precio"]) 

        for fila, valor in enumerate(carrito):
            item_nombre = QTableWidgetItem(valor[0])
            item_cantidad = QTableWidgetItem(f"{valor[1]}")
            item_precio = QTableWidgetItem(f"Q{valor[2]:.2f}")

            self.tabla2.setItem(fila, 0, item_nombre)
            self.tabla2.setItem(fila, 1, item_cantidad)
            self.tabla2.setItem(fila, 2, item_precio)

            for col in range(3):
                item = self.tabla2.item(fila, col)
                item.setFlags(Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable)
        
        self.tabla2.resizeColumnsToContents()
        self.color_tabla(self.tabla2)
        self.tabla2.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.tabla2.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        self.total = QLineEdit()
        self.total.setPlaceholderText("Total de compra: Q12")
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

        layout2.addWidget(self.ingreso_busqueda)
        layout2.addWidget(boton_buscar)

        layout1.addLayout(layout2)
        layout1.addWidget(self.tabla1)

        layout5.addWidget(boton_confirmar)
        layout5.addWidget(boton_cancelar)

        layout4.addWidget(self.total)
        layout4.addLayout(layout5)

        layout3.addWidget(carrito_label)
        layout3.addWidget(self.tabla2)
        layout3.addLayout(layout4)

        main_layout.addItem(self.espacio(35, 35))
        main_layout.addLayout(layout1)
        main_layout.addItem(self.espacio(100, 100))
        main_layout.addLayout(layout3)
        main_layout.addItem(self.espacio(35, 35))
        self.layout.addLayout(main_layout)

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


    def cancelar_cantidad(self):
        self.ventana_cantidad.close()
        self.mensaje_informacion("Cancelar", "Se a cancelado correctamente el ingreso de la cantidad")