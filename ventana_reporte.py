from codigo import Codigo
from PyQt6.QtWidgets import QApplication ,QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout, QLabel, QLineEdit, QMessageBox, QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem, QHeaderView, QComboBox 
from PyQt6.QtGui import QIcon, QPixmap, QGuiApplication, QLinearGradient, QColor, QBrush, QPalette
from PyQt6.QtCore import Qt, QSize

class Ventana_reporte(Codigo):
    def __init__(self, main_layout, base_datos, botones, nivel):
        super().__init__()
        self.layout = main_layout
        self.base_datos = base_datos
        self.botones = botones
        self.nivel = nivel
        self.nueva_ventana = None
    
    def reportes(self):
        self.limpieza_layout(self.layout)
        self.color_acceso_nivel(self.nivel, self.botones)
        self.color_boton_oprimido(self.botones[4])
        self.activar_botones(self.botones)
        self.botones[4].setEnabled(False)

        main_layot = QVBoxLayout()
        main_layot.setAlignment(Qt.AlignmentFlag.AlignTop)

        layout1 = QHBoxLayout()
        self.layout2 = QHBoxLayout()
        layout3 = QVBoxLayout()

        boton_reporte_ventas = QPushButton()
        boton_reporte_ventas.setIcon(QIcon(self.imagen("imagenes/reporte ventas.png", 90, 90)))
        boton_reporte_ventas.setIconSize(QSize(100, 100))
        self.color_boton_sin_oprimir(boton_reporte_ventas)
        boton_reporte_ventas.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        boton_reporte_ventas.clicked.connect(self.reporte_ventas)

        boton_reporte_compras = QPushButton()
        boton_reporte_compras.setIcon(QIcon(self.imagen("imagenes/reporte compras.png", 90, 90)))
        boton_reporte_compras.setIconSize(QSize(100, 100))
        self.color_boton_sin_oprimir(boton_reporte_compras)
        boton_reporte_compras.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        boton_reporte_compras.clicked.connect(self.reporte_compras)

        boton_generar_reporte = QPushButton()
        boton_generar_reporte.setIcon(QIcon(self.imagen("imagenes/generar reporte.png", 90, 90)))
        boton_generar_reporte.setIconSize(QSize(100, 100))
        self.color_boton_sin_oprimir(boton_generar_reporte)
        boton_generar_reporte.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        boton_generar_reporte.clicked.connect(self.generar_reporte)

        informar = QLabel("Oprima uno de los botones que tiene en la parte superior izquierda")
        informar.setStyleSheet("color: Black; font-size: 20px")
        informar.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        layout1.addItem(self.espacio(35, 35))
        layout1.addWidget(boton_reporte_ventas)
        layout1.addWidget(boton_reporte_compras)
        layout1.addWidget(boton_generar_reporte)
        layout1.addStretch()

        layout3.addStretch()
        layout3.addWidget(informar)
        layout3.addStretch()
        
        self.layout2.addLayout(layout3)

        main_layot.addLayout(layout1)
        main_layot.addLayout(self.layout2)
        self.layout.addLayout(main_layot)

    def reporte_ventas(self):
        if self.nueva_ventana is not None:
            self.nueva_ventana.close()

        self.verificacion = False
        self.limpieza_layout(self.layout2)

        main_layout = QVBoxLayout()

        layout1 = QHBoxLayout()
        layout1.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.orden_tabla = QComboBox()
        self.orden_tabla.addItems(["Dia", "Mes", "Año"])
        self.color_caja_opciones(self.orden_tabla)
        self.orden_tabla.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        orden_label = QLabel("Ingrese la forma en la que desea ordenar las ventas: ")
        orden_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        orden_label.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.color_linea(orden_label)

        registro_ventas = [["2023-10-01", 1000, 5, 500, "Calculadora"], ["2023-10-02", 2000, 10, 1000, "Tijera"]]

        self.tabla = QTableWidget(len(registro_ventas), 5)
        self.tabla.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)

        self.tabla.setHorizontalHeaderLabels(["Fecha", "Ingresos totales", "Total de Productos vendidos", "Ganancias totales", "Producto más vendido"])

        for fila, producto in enumerate(registro_ventas):

            fecha_item = QTableWidgetItem(f"{producto[0]}")
            ingreso_item = QTableWidgetItem(f"Q{producto[1]:.2f}")
            productos_item = QTableWidgetItem(f"{producto[2]}")
            ganancias_item = QTableWidgetItem(f"Q{producto[3]:.2f}") 
            vendido_item = QTableWidgetItem(producto[4])

            self.tabla.setItem(fila, 0, fecha_item)
            self.tabla.setItem(fila, 1, ingreso_item)
            self.tabla.setItem(fila, 2, productos_item)
            self.tabla.setItem(fila, 3, ganancias_item)
            self.tabla.setItem(fila, 4, vendido_item)

            for col in range(5):
                item = self.tabla.item(fila, col)
                item.setFlags(Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable)

        self.color_tabla(self.tabla)
        self.tabla.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.tabla.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.tabla.cellDoubleClicked.connect(self.mostrar_detalles_venta)

        layout1.addWidget(orden_label)
        layout1.addWidget(self.orden_tabla)
        
        main_layout.addLayout(layout1)
        main_layout.addWidget(self.tabla)

        self.layout2.addItem(self.espacio(35, 35))
        self.layout2.addLayout(main_layout)
    
    def mostrar_detalles_venta(self, fila):
        if self.verificacion is False:
            self.verificacion = True
            layout1 = QVBoxLayout()

            cartelera = QLabel("Detalles de la venta")
            self.color_linea(cartelera)
            cartelera.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
            cartelera.setFixedHeight(50)
            cartelera.setAlignment(Qt.AlignmentFlag.AlignCenter)
            cartelera.setEnabled(False)

            boton_cerrar = QPushButton("cerrar")
            self.color_boton_sin_oprimir(boton_cerrar)
            boton_cerrar.setFixedHeight(50)
            boton_cerrar.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
            boton_cerrar.clicked.connect(self.limpieza_detalle_venta)

            fecha = self.tabla.item(fila, 0).text()
            
            detalle_vendidos = [[fecha, "lapicez", 10, 20], [fecha, "Calculadoras", 2, 30]]

            self.detalle_venta = QTableWidget(len(detalle_vendidos), 4)
            self.detalle_venta.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)

            self.detalle_venta.setHorizontalHeaderLabels(["Fecha", "Nombre del producto", "Cantidad vendida", "Ganancia total"])

            for fila, producto in enumerate(detalle_vendidos):

                fecha_item = QTableWidgetItem(f"{producto[0]}")
                nombre_item = QTableWidgetItem(producto[1])
                producto_item = QTableWidgetItem(f"{producto[2]}")
                ganancia_item = QTableWidgetItem(f"Q{producto[3]:.2f}") 
                
                self.detalle_venta.setItem(fila, 0, fecha_item)
                self.detalle_venta.setItem(fila, 1, nombre_item)
                self.detalle_venta.setItem(fila, 2, producto_item)
                self.detalle_venta.setItem(fila, 3, ganancia_item)

                for col in range(4):
                    item = self.detalle_venta.item(fila, col)
                    item.setFlags(Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable)

            self.color_tabla(self.detalle_venta)
            self.detalle_venta.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
            self.detalle_venta.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

            layout1.addWidget(cartelera)
            layout1.addWidget(self.detalle_venta)
            layout1.addWidget(boton_cerrar)

            self.layout2.addLayout(layout1)

    def limpieza_detalle_venta(self):
        self.limpieza_layout(self.layout2)
        self.reporte_ventas()

    def reporte_compras(self):
        if self.nueva_ventana is not None:
            self.nueva_ventana.close()

        self.verificacion = False
        self.limpieza_layout(self.layout2)

        main_layout = QVBoxLayout()

        layout1 = QHBoxLayout()
        layout1.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.orden_tabla = QComboBox()
        self.orden_tabla.addItems(["Dia", "Mes", "Año"])
        self.color_caja_opciones(self.orden_tabla)
        self.orden_tabla.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        orden_label = QLabel("Ingrese la forma en la que desea ordenar las compras: ")
        orden_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        orden_label.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.color_linea(orden_label)

        registro_ventas = [["2023-10-01", 1000, 5, 500], ["2023-10-02", 2000, 10, 1000]]

        self.tabla = QTableWidget(len(registro_ventas), 4)
        self.tabla.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)

        self.tabla.setHorizontalHeaderLabels(["Fecha", "Cantidad ingresada", "Total de Productos comprados", "Total de gastos"])

        for fila, producto in enumerate(registro_ventas):

            fecha_item = QTableWidgetItem(f"{producto[0]}")
            ingreso_item = QTableWidgetItem(f"Q{producto[1]:.2f}")
            productos_item = QTableWidgetItem(f"{producto[2]}")
            ganancias_item = QTableWidgetItem(f"Q{producto[3]:.2f}") 
            
            self.tabla.setItem(fila, 0, fecha_item)
            self.tabla.setItem(fila, 1, ingreso_item)
            self.tabla.setItem(fila, 2, productos_item)
            self.tabla.setItem(fila, 3, ganancias_item)

            for col in range(4):
                item = self.tabla.item(fila, col)
                item.setFlags(Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable)

        self.color_tabla(self.tabla)
        self.tabla.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.tabla.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.tabla.cellDoubleClicked.connect(self.mostrar_detalles_compra)

        layout1.addWidget(orden_label)
        layout1.addWidget(self.orden_tabla)

        main_layout.addLayout(layout1)
        main_layout.addWidget(self.tabla)

        self.layout2.addItem(self.espacio(35, 35))
        self.layout2.addLayout(main_layout)
    
    def mostrar_detalles_compra(self, fila):
        if self.verificacion is False:
            self.verificacion = True
            layout1 = QVBoxLayout()

            cartelera = QLabel("Detalles de la compra")
            self.color_linea(cartelera)
            cartelera.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
            cartelera.setFixedHeight(50)
            cartelera.setAlignment(Qt.AlignmentFlag.AlignCenter)
            cartelera.setEnabled(False)

            boton_cerrar = QPushButton("cerrar")
            self.color_boton_sin_oprimir(boton_cerrar)
            boton_cerrar.setFixedHeight(50)
            boton_cerrar.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
            boton_cerrar.clicked.connect(self.limpieza_detalle_compra)

            fecha = self.tabla.item(fila, 0).text()
            
            detalle_vendidos = [[fecha, "lapicez", 10, 20], [fecha, "Calculadoras", 2, 30]]

            self.detalle_compra = QTableWidget(len(detalle_vendidos), 4)
            self.detalle_compra.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)

            self.detalle_compra.setHorizontalHeaderLabels(["Fecha", "Nombre del producto", "Cantidad comprada", "Gasto total"])

            for fila, producto in enumerate(detalle_vendidos):

                fecha_item = QTableWidgetItem(f"{producto[0]}")
                nombre_item = QTableWidgetItem(producto[1])
                cantidad_item = QTableWidgetItem(f"{producto[2]}")
                gasto_item = QTableWidgetItem(f"Q{producto[3]:.2f}") 
                
                self.detalle_compra.setItem(fila, 0, fecha_item)
                self.detalle_compra.setItem(fila, 1, nombre_item)
                self.detalle_compra.setItem(fila, 2, cantidad_item)
                self.detalle_compra.setItem(fila, 3, gasto_item)

                for col in range(4):
                    item = self.detalle_compra.item(fila, col)
                    item.setFlags(Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable)

            self.color_tabla(self.detalle_compra)
            self.detalle_compra.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
            self.detalle_compra.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
            layout1.addWidget(cartelera)
            layout1.addWidget(self.detalle_compra)
            layout1.addWidget(boton_cerrar)
            self.layout2.addLayout(layout1)

    def limpieza_detalle_compra(self):
        self.limpieza_layout(self.layout2)
        self.reporte_compras()

    def generar_reporte(self):
        self.nueva_ventana = QWidget()
        self.nueva_ventana.setWindowTitle("Generar Reporte")
        self.fondo_degradado(self.nueva_ventana, "#0037FF", "#5DA9F5")
        self.nueva_ventana.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.limpieza_layout(self.layout2)

        main_layout = QVBoxLayout()

        layout1 = QGridLayout()

        layout2 = QVBoxLayout()

        layout3 = QHBoxLayout()

        seleccion_label = QLabel("Escoja el tipo de reporte que requiere")
        self.color_linea(seleccion_label)
        seleccion_label.setAlignment(Qt.AlignmentFlag.AlignCenter)  
        seleccion_label.setFixedHeight(30)
        seleccion_label.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)

        self.opcion = QComboBox()
        self.opcion.addItems(["Generar reporte solo de ventas", "Generar reporte solo de compras", "Generar reporte general"])
        self.color_caja_opciones(self.opcion)
        self.tipo = self.opcion.currentText

        fecha_inicio_label = QLabel("Ingrese la fecha de inicion para el reporte: ")
        fecha_inicio_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        fecha_inicio_label.setFixedHeight(30)
        fecha_inicio_label.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        self.color_linea(fecha_inicio_label)

        fecha_fin_label = QLabel("Ingrese la fecha final para el reporte: ")
        fecha_fin_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        fecha_fin_label.setFixedHeight(30)
        fecha_fin_label.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        self.color_linea(fecha_fin_label)

        self.fecha_inicio = QLineEdit()
        self.fecha_inicio.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.fecha_inicio.setFixedHeight(30)
        self.fecha_inicio.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)        
        self.color_linea(self.fecha_inicio)

        self.fecha_fin = QLineEdit()
        self.fecha_fin.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.fecha_fin.setFixedHeight(30)
        self.fecha_fin.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)        
        self.color_linea(self.fecha_fin)

        boton_confirmar = QPushButton("Confirmar")
        boton_confirmar.setFixedHeight(20)
        boton_confirmar.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        boton_confirmar.clicked.connect(self.creacion_reporte)
        self.asignacion_tecla(self.nueva_ventana, "Return", boton_confirmar)
        self.color_boton_sin_oprimir(boton_confirmar)

        boton_cancelar = QPushButton("Cancelar")
        boton_cancelar.setFixedHeight(20)
        boton_cancelar.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        boton_cancelar.clicked.connect(self.cancelar_reporte)
        self.asignacion_tecla(self.nueva_ventana, "Esc", boton_cancelar) 
        self.color_boton_sin_oprimir(boton_cancelar)

        informar = QLabel("Llene los campos del recuadro")
        informar.setStyleSheet("color: Black; font-size: 20px")
        informar.setAlignment(Qt.AlignmentFlag.AlignAbsolute)
        informar.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        layout1.addWidget(fecha_inicio_label, 0, 0)
        layout1.addWidget(self.fecha_inicio, 0, 1)
        layout1.addWidget(fecha_fin_label, 1, 0)
        layout1.addWidget(self.fecha_fin, 1, 1)

        layout3.addWidget(boton_confirmar)
        layout3.addWidget(boton_cancelar)

        main_layout.addWidget(seleccion_label)
        main_layout.addWidget(self.opcion)
        main_layout.addLayout(layout1)
        main_layout.addLayout(layout3)

        layout2.addStretch()
        layout2.addWidget(informar)
        layout2.addStretch()

        self.layout2.addLayout(layout2)

        self.nueva_ventana.setLayout(main_layout)

        self.nueva_ventana.showNormal()
    
    def creacion_reporte(self):
        #Obtine el texto que se encuntra acualmente en la caja
        self.opcion.currentText()

        self.nueva_ventana.close()

    def cancelar_reporte(self):
        self.nueva_ventana.close()
        self.limpieza_layout(self.layout2)

        layout = QVBoxLayout()
                        
        informar = QLabel("Oprima uno de los botones que tiene en la parte superior izquierda")
        informar.setStyleSheet("color: Black; font-size: 20px")
        informar.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        layout.addStretch()
        layout.addWidget(informar)
        layout.addStretch()

        self.layout2.addLayout(layout)

