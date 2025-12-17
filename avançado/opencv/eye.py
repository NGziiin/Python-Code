import sys
import cv2
from PySide6.QtWidgets import QApplication, QLabel, QWidget

class MyApp(QWidget):
    def __init__(self):
        super().__init__()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyApp()
    widget.resize(400, 200)
    widget.show()
    sys.exit(app.exec())