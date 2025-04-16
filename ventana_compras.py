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

        boton_proveedores = QPushButton()
        boton_proveedores.setIcon(QIcon(self.imagen("imagenes/proveedores.png", 90, 90)))
        boton_proveedores.setIconSize(QSize(100, 100))
        self.color_boton_sin_oprimir(boton_proveedores)
        boton_proveedores.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        boton_pedido = QPushButton()
        boton_pedido.setIcon(QIcon(self.imagen("imagenes/pedido.png", 90, 90)))
        boton_pedido.setIconSize(QSize(100, 100))
        self.color_boton_sin_oprimir(boton_pedido)
        boton_pedido.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        informar = QLabel("Oprima uno de los botones que tiene en la parte superior izquierda")
        informar.setStyleSheet("color: Black; font-size: 20px")
        informar.setAlignment(Qt.AlignmentFlag.AlignTop)
        informar.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        layout1.addItem(self.espacio(35, 35))
        layout1.addWidget(boton_proveedores)
        layout1.addWidget(boton_pedido)
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
        pass

    def ingreso_pedido(self):
        pass
