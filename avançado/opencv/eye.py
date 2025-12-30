import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from PySide6.QtGui import QGuiApplication
import cv2


class ConfigSystem:
    """Responsável por obter informações de tela e ajustar tamanho de janelas."""

    def __init__(self, gui_app: QGuiApplication):
        self.gui_app = gui_app

    def resize_window_by_ratio(self, window: QWidget, width_ratio: float = 0.7, height_ratio: float = 0.7):
        """
        Redimensiona a janela com base em percentage da tela principal.
        Ex.: 0,7 → 70% da largura/altura.
        """
        if not (0.1 <= width_ratio <= 1.0 and 0.1 <= height_ratio <= 1.0):
            raise ValueError("As razões de largura/altura devem estar entre 0.1 e 1.0")

        screen = self.gui_app.primaryScreen()
        size = screen.size()
        target_w = int(size.width() * width_ratio)
        target_h = int(size.height() * height_ratio)
        window.resize(target_w, target_h)


class MyApp(QWidget):
    def __init__(self, config: ConfigSystem):
        super().__init__()
        self.config = config

        """
        Essa função redimensiona a janela do app de acordo com o monitor
        """
        self.config.resize_window_by_ratio(self, 0.7, 0.7)

        self.setWindowTitle("Estudo PySide6 & OpenCV – WebCam e Olhos")

        # Layout organizado
        layout = QVBoxLayout(self)
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(8)

        self.lbl_info = QLabel("Estudo com Webcam")
        self.btn_start = QPushButton("Clique aqui para iniciar a webcam")

        layout.addWidget(self.lbl_info)
        layout.addWidget(self.btn_start)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Use QGuiApplication de forma segura (QApplication herda dele, então podemos passar o mesmo “app”)
    config = ConfigSystem(QGuiApplication.instance() or QGuiApplication(sys.argv))

    widget = MyApp(config)
    widget.show()
    sys.exit(app.exec())
