import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QStackedWidget

class VentanaPrincipal(QWidget):
    def __init__(self):
        super().__init__()

        self.stacked_widget = QStackedWidget(self)

        self.ventana1 = QWidget()
        layout1 = QVBoxLayout(self.ventana1)
        layout1.addWidget(QPushButton("Ventana 1"))

        self.ventana2 = QWidget()
        layout2 = QVBoxLayout(self.ventana2)
        layout2.addWidget(QPushButton("Ventana 2"))

        self.stacked_widget.addWidget(self.ventana1)
        self.stacked_widget.addWidget(self.ventana2)

        self.boton_cambiar = QPushButton("Cambiar Ventana", self)
        self.boton_cambiar.clicked.connect(self.cambiar_ventana)

        layout_principal = QVBoxLayout(self)
        layout_principal.addWidget(self.stacked_widget)
        layout_principal.addWidget(self.boton_cambiar)

    def cambiar_ventana(self):
        if self.stacked_widget.currentIndex() == 0:
            self.stacked_widget.setCurrentIndex(1)
        else:
            self.stacked_widget.setCurrentIndex(0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())