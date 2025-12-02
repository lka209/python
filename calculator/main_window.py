from PySide6.QtWidgets import QWidget, QMainWindow, QVBoxLayout

class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args , **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        self.cw = QWidget()
        self.v_layout = QVBoxLayout()

        self.cw.setLayout(self.v_layout)
        self.setCentralWidget(self.cw)

        self.setWindowTitle('Calculator')

    def adjustpixedsize(self):
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())
    
    def addwidget(self, widget: QWidget) -> None:
        self.v_layout.addWidget(widget)
        self.adjustpixedsize()
