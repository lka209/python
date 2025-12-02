import sys
from main_window import MainWindow
from PySide6.QtWidgets import QApplication, QLabel


def temp_label(texto):
   label1 = QLabel(texto)
   label1.setStyleSheet('font-size: 30px;')
   return label1
   
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    window = MainWindow()
    window.addWidgetToVLayout(temp_label('teste 1'))
    
    window.adjustpixedsize()
    
    window.show()
    app.exec()