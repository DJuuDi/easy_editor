from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from ui import Ui_MainWindow

class Widget(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.noets = {
            "Перша замітка":{
                "текст": "Це текст першої замітки",
                "теги": []
            }
        }
app = QApplication([])
ex = Widget()
ex.show()
app.exec_()
