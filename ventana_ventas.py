from codigo import Codigo
from PyQt6.QtWidgets import QApplication ,QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout, QLabel, QLineEdit, QMessageBox, QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem, QHeaderView 
from PyQt6.QtGui import QIcon, QPixmap, QGuiApplication, QLinearGradient, QColor, QBrush, QPalette
from PyQt6.QtCore import Qt, QSize
from datetime import datetime

class Ventana_ventas(Codigo):
    def __init__(self, main_layout: QVBoxLayout, botones, base_datos):
        super().__init__()
        self.layout = main_layout
        self.botones = botones
        self.base_datos = base_datos
        self.fila_carrito = 0
        self.carrito = []
        self.total_venta = 0

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
        boton_buscar.clicked.connect(self.buscar_producto)
        
        inventario = self.base_datos.obtener_productos_ventas()

        #Tabla de ventas
        self.tabla1 = QTableWidget(len(inventario), 5)
        self.tabla1.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)

        self.tabla1.setHorizontalHeaderLabels(["ID", "Nombre", "Descripción", "Existencias", "Precio" ]) 

        
        # Llenar la tabla con los datos
        for fila, producto in enumerate(inventario):
            # Convertir los valores a strings (excepto los que ya lo son)
            id_item = QTableWidgetItem(str(producto['id']))
            nombre_item = QTableWidgetItem(producto['nombre'])
            descripcion_item = QTableWidgetItem(producto['descripcion'])
            existencia_item = QTableWidgetItem(str(producto['stock']))
            precio_item = QTableWidgetItem(f"Q{producto['precio']:.2f}")  # Formato con 2 decimales
            
            # Añadir items a la tabla
            self.tabla1.setItem(fila, 0, id_item)
            self.tabla1.setItem(fila, 1, nombre_item)
            self.tabla1.setItem(fila, 2, descripcion_item)
            self.tabla1.setItem(fila, 3, existencia_item)
            self.tabla1.setItem(fila, 4, precio_item)
            
            # Configurar flags para todos los items
            for col in range(5):
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

        #Tabla carrito
        self.tabla2 = QTableWidget(0, 4)
        self.tabla2.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)

        self.tabla2.setHorizontalHeaderLabels(["ID","Nombre", "Cantidad", "Precio"]) 

        self.tabla2.resizeColumnsToContents()
        self.color_tabla(self.tabla2)
        self.tabla2.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.tabla2.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        self.total = QLineEdit()
        self.total.setText(f"Total de compra: Q{self.total_venta:.2f}")
        self.color_linea(self.total)
        self.total.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.total.setFixedHeight(50)
        self.total.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.total.setEnabled(False)

        boton_confirmar = QPushButton("Confirmar")
        boton_confirmar.setFixedHeight(50)
        self.color_boton_sin_oprimir(boton_confirmar)
        boton_confirmar.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        boton_confirmar.clicked.connect(self.confirmar_compra)
        
        boton_cancelar = QPushButton("Cancelar")
        boton_cancelar.setFixedHeight(50)
        self.color_boton_sin_oprimir(boton_cancelar)
        boton_cancelar.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        boton_cancelar.clicked.connect(self.cancelar_compra)

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
        main_layout.addLayout(layout3)
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
        boton_confirmar.clicked.connect(self.confirmar_cantidad)

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

    def confirmar_cantidad(self):
        fila = self.tabla1.currentRow()
        cantidad = self.cantidad.text()

        # Verificar que la cantidad sea menor o igual a la existencia del producto
        # y que sea un número positivo
        if int(cantidad) <= int(self.tabla1.item(fila, 3).text()) and int(cantidad) > 0:
            # Buscar en tabla carrito si el producto ya existe
            nueva_cantidad = 0
            for i in range(self.tabla2.rowCount()):
                if self.tabla2.item(i, 0).text() == self.tabla1.item(fila, 0).text():
                    # Si el producto ya existe, actualizar la cantidad 
                    nueva_cantidad = int(self.tabla2.item(i, 2).text()) + int(cantidad)
                    self.tabla2.setItem(i, 2, QTableWidgetItem(str(nueva_cantidad)))
                    break
            id_producto = int(self.tabla1.item(fila, 0).text())
            precio_producto = float(self.tabla1.item(fila, 4).text()[1:])
            total_producto = int(cantidad) * precio_producto
            nombre_producto = self.tabla1.item(fila, 1).text()
            if nueva_cantidad == 0:
                # 👇 Insertar nueva fila en la tabla2
                self.tabla2.insertRow(self.fila_carrito)

                item_id = QTableWidgetItem(str(id_producto))
                item_nombre = QTableWidgetItem(nombre_producto)
                item_cantidad = QTableWidgetItem(f"{cantidad}")
                item_precio = QTableWidgetItem(f"Q{precio_producto:.2f}")

                self.tabla2.setItem(self.fila_carrito, 0, item_id)
                self.tabla2.setItem(self.fila_carrito, 1, item_nombre)
                self.tabla2.setItem(self.fila_carrito, 2, item_cantidad)
                self.tabla2.setItem(self.fila_carrito, 3, item_precio)

                for col in range(4):
                    item = self.tabla2.item(self.fila_carrito, col)
                    item.setFlags(Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable)

                self.fila_carrito += 1

            self.total_venta += total_producto
            self.total.setText(f"Total de compra: Q{self.total_venta:.2f}")
            # Modificar el stock del producto en la base de datos
            nuevo_stock = int(self.tabla1.item(fila, 3).text()) - int(cantidad)
            self.carrito.append([id_producto, nuevo_stock, cantidad, precio_producto])


            # Actualizar la tabla de ventas
            self.tabla1.setItem(fila, 3, QTableWidgetItem(str(nuevo_stock)))

            # Por simplicidad, solo se muestra un mensaje de éxito
            self.mensaje_informacion("Agregar al carrito", f"Se ha agregado {cantidad} de {nombre_producto} al carrito. Total: Q{total_producto:.2f}")
            
            # Cerrar la ventana de cantidad
            self.ventana_cantidad.close()
            
        else:
            self.mensaje_error("Error", "La cantidad ingresada es mayor a la existencia del producto o no es válida")
            return

    def confirmar_compra(self):
        # Actualizar tabla de ventas en base de datos (id, Empleado_id, fecha, total_venta)
        self.base_datos.agregar_venta(1, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), self.total_venta) # Modificar el id del empleado según sea necesario
        # Obtener el id de la venta recién creada
        id_venta = self.base_datos.obtener_id_ultima_venta()
        # Actualizar la tabla detalle_venta (Producto_id, Venta_id, cantidad, precio)


        # Actualizar el stock de los productos en la base de datos
        for producto in self.carrito:
            id_producto = producto[0]
            nuevo_stock = producto[1]
            stock_venta = producto[2]
            precio = producto[3]
            # Modificar el stock del producto en la base de datos
            self.base_datos.modificar_producto_stock(id_producto, nuevo_stock)
            # Actualizar la tabla detalle_venta (Producto_id, Venta_id, cantidad, precio)
            self.base_datos.agregar_detalle_venta(id_producto, id_venta, stock_venta, precio)

        self.mensaje_informacion("Compra confirmada", "La compra se ha confirmado correctamente")
        self.tabla2.clearContents()
        self.tabla2.setRowCount(0)
        self.tabla2.setColumnCount(4)
        self.carrito.clear()
        self.total.clear()
        self.total.setText("Total de compra: Q0")
        self.fila_carrito = 0

    def llenar_inventario(self):
        # Volver a cargar la tabla de ventas con los productos originales
        inventario = self.base_datos.obtener_productos_ventas()
        self.tabla1.setRowCount(len(inventario))

        # Llenar la tabla con los datos
        for fila, producto in enumerate(inventario):
            id_item = QTableWidgetItem(str(producto['id']))
            nombre_item = QTableWidgetItem(producto['nombre'])
            descripcion_item = QTableWidgetItem(producto['descripcion'])
            existencia_item = QTableWidgetItem(str(producto['stock']))
            precio_item = QTableWidgetItem(f"Q{producto['precio']:.2f}")

            # Añadir items a la tabla
            self.tabla1.setItem(fila, 0, id_item)
            self.tabla1.setItem(fila, 1, nombre_item)
            self.tabla1.setItem(fila, 2, descripcion_item)
            self.tabla1.setItem(fila, 3, existencia_item)
            self.tabla1.setItem(fila, 4, precio_item)

    def cancelar_compra(self):
        # Volver a cargar la tabla de ventas con los productos originales
        self.llenar_inventario()
        self.mensaje_informacion("Compra cancelada", "La compra se ha cancelado")
        self.tabla2.clearContents()
        self.tabla2.setRowCount(0)
        self.tabla2.setColumnCount(4)
        self.carrito.clear()
        self.total.clear()
        self.total.setText("Total de compra: Q0")
        self.total_venta = 0
        self.fila_carrito = 0

    def cancelar_cantidad(self):
        self.ventana_cantidad.close()

    def buscar_producto(self):
        # Buscar el producto por nombre en la base de datos
        nombre_producto = self.ingreso_busqueda.text()
        resultado = self.base_datos.buscar_producto_ventas_por_nombre(nombre_producto)
        
        if len(resultado) != 0:
            # Limpiar la tabla antes de mostrar los resultados
            self.tabla1.clearContents()
            self.tabla1.setRowCount(len(resultado))
            # Llenar la tabla con los resultados de la búsqueda
            for fila, producto in enumerate(resultado):
                id_item = QTableWidgetItem(str(producto['id']))
                nombre_item = QTableWidgetItem(producto['nombre'])
                descripcion_item = QTableWidgetItem(producto['descripcion'])
                existencia_item = QTableWidgetItem(str(producto['stock']))
                precio_item = QTableWidgetItem(f"Q{producto['precio']:.2f}")

                # Añadir items a la tabla
                self.tabla1.setItem(fila, 0, id_item)
                self.tabla1.setItem(fila, 1, nombre_item)
                self.tabla1.setItem(fila, 2, descripcion_item)
                self.tabla1.setItem(fila, 3, existencia_item)
                self.tabla1.setItem(fila, 4, precio_item)

        else:
            self.mensaje_error("Error", "No se encontraron productos con ese nombre")

        self.ingreso_busqueda.clear()


