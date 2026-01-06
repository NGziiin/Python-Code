import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QFrame
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QGuiApplication


class WindowResizer:
    def __init__(self, app: QGuiApplication):
        self.app = app

    def resize_by_ratio(self, window: QWidget, width_ratio=0.4, height_ratio=0.55):
        screen = self.app.primaryScreen()
        size = screen.size()
        window.resize(
            int(size.width() * width_ratio),
            int(size.height() * height_ratio)
        )


class LoginWindow(QWidget):
    def __init__(self, resizer: WindowResizer):
        super().__init__()
        self.resizer = resizer
        self.resizer.resize_by_ratio(self)

        self.setWindowTitle("Login do Sistema")
        self.setStyleSheet(self._global_style())

        self._build_ui()

    def _build_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setAlignment(Qt.AlignCenter)

        # Card central
        card = QFrame()
        card.setObjectName("card")
        card_layout = QVBoxLayout(card)
        card_layout.setContentsMargins(40, 40, 40, 40)
        card_layout.setSpacing(18)

        # Título
        title = QLabel("Acesso ao Sistema")
        title.setAlignment(Qt.AlignCenter)
        title.setObjectName("title")

        # Inputs
        self.user_input = QLineEdit()
        self.user_input.setPlaceholderText("Usuário")

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Senha")
        self.password_input.setEchoMode(QLineEdit.Password)

        # Botão
        self.login_button = QPushButton("Entrar")
        self.login_button.setObjectName("login_button") # style do botão de login
        self.register_button = QPushButton("Cadastrar")
        self.register_button.setObjectName("register_button") # style do botão de registrar

        # Montagem
        card_layout.addWidget(title)
        card_layout.addWidget(self.user_input)
        card_layout.addWidget(self.password_input)
        card_layout.addWidget(self.login_button)
        card_layout.addWidget(self.register_button)

        main_layout.addWidget(card)

    def _global_style(self):
        return """
        QWidget {
            background-color: #f4f6f8;
            font-family: Segoe UI;
        }

        #card {
            background-color: #ffffff;
            border-radius: 12px;
            min-width: 320px;
            max-width: 420px;
        }

        #title {
            font-size: 22px;
            font-weight: bold;
            color: #222;
            background-color: transparent;
        }
        
        #register_button {
            background-color: green;
        }

        QLineEdit {
            height: 38px;
            border-radius: 8px;
            padding-left: 10px;
            border: 1px solid #ccc;
            font-size: 14px;
        }

        QLineEdit:focus {
            border: 1px solid #2d89ef;
        }

        QPushButton {
            height: 40px;
            border-radius: 8px;
            background-color: #2d89ef;
            color: white;
            font-size: 15px;
            font-weight: bold;
            border: none;
        }

        QPushButton:hover {
            background-color: #1b6fd8;
        }

        QPushButton:pressed {
            background-color: #1558aa;
        }
        """


if __name__ == "__main__":
    app = QApplication(sys.argv)

    resizer = WindowResizer(QGuiApplication.instance())
    window = LoginWindow(resizer)
    window.show()

    sys.exit(app.exec())
