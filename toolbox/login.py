import json
import urllib.request
from pathlib import Path
from PyQt5.QtWidgets import (
    QDialog, QVBoxLayout, QLabel, QLineEdit,
    QPushButton, QMessageBox, QHBoxLayout
)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class LoginWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("VOICE-GEN")
        self.setWindowFlags(Qt.Window |
                            Qt.WindowMinimizeButtonHint |
                            Qt.WindowMaximizeButtonHint |
                            Qt.WindowCloseButtonHint)

        # 🔽 Try to download background image if not already downloaded
        image_url = "https://www.sngular.com/images/1/1532/original/VoiceCloning4.webp"
        local_image = Path("bg2.jpg")

        try:
            if not local_image.exists():
                urllib.request.urlretrieve(image_url, local_image)
        except Exception as e:
            print("❌ Failed to download background image:", e)

        # 🔽 Set StyleSheet (background-image applied to QDialog)
        self.setStyleSheet(f"""
            QDialog {{
                background-image: url("{local_image.resolve().as_posix()}");
                background-repeat: no-repeat;
                background-position: center;
                background-size: cover;
                font-family: 'Segoe UI', Arial;
            }}
            QLabel {{
                color: #ffffff;
                font-size: 14pt;
            }}
            QLineEdit {{
                padding: 8px;
                font-size: 12pt;
                border: 1px solid #ccc;
                border-radius: 5px;
                background-color: rgba(255, 255, 255, 0.8);
            }}
            QPushButton {{
                background-color: #0078d4;
                color: white;
                padding: 8px;
                font-size: 12pt;
                border-radius: 5px;
            }}
            QPushButton:hover {{
                background-color: #005a9e;
            }}
        """)

        # 🔽 Load/create user file
        self.users_file = Path(__file__).parent / "users.json"
        if not self.users_file.exists():
            self.users_file.write_text(json.dumps({}))

        # 🔽 Layout
        layout = QVBoxLayout()
        layout.setContentsMargins(40, 40, 40, 40)
        layout.setSpacing(20)
        layout.setAlignment(Qt.AlignCenter)
        self.setLayout(layout)

        # 🔽 Logo
        logo = QLabel()
        logo_path = Path(__file__).parent / ""
        pixmap = QPixmap(str(logo_path))
        if not pixmap.isNull():
            pixmap = pixmap.scaled(64, 64, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            logo.setPixmap(pixmap)
            logo.setAlignment(Qt.AlignCenter)
            layout.addWidget(logo)

        # 🔽 Welcome
        self.info_label = QLabel("Welcome!<br><span style='font-size:18pt;'>Login to continue</span>")
        self.info_label.setAlignment(Qt.AlignCenter)
        self.info_label.setStyleSheet("""
            QLabel {
                color: black;
                font-size: 24pt;
                font-weight: bold;
            }
        """)
        layout.addWidget(self.info_label)


        # 🔽 Username
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Username")
        self.username_input.setMaximumWidth(320)
        layout.addWidget(self.username_input, alignment=Qt.AlignCenter)

        # 🔽 Password
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setMaximumWidth(320)
        layout.addWidget(self.password_input, alignment=Qt.AlignCenter)

        # 🔽 Buttons
        button_layout = QHBoxLayout()
        button_layout.setSpacing(20)

        self.login_button = QPushButton("Login")
        self.login_button.setMaximumWidth(160)
        self.login_button.clicked.connect(self.login)
        button_layout.addWidget(self.login_button)

        self.create_button = QPushButton("Sign Up")
        self.create_button.setMaximumWidth(160)
        self.create_button.clicked.connect(self.create_account)
        button_layout.addWidget(self.create_button)

        layout.addLayout(button_layout)

        self.result = None
        self.showMaximized()

    def load_users(self):
        with self.users_file.open("r") as f:
            return json.load(f)

    def save_users(self, users):
        with self.users_file.open("w") as f:
            json.dump(users, f, indent=2)

    def login(self):
        username = self.username_input.text().strip()
        password = self.password_input.text().strip()
        users = self.load_users()

        if username in users and users[username]["password"] == password:
            self.result = username
            self.accept()
        else:
            QMessageBox.warning(self, "Login Failed", "Incorrect username or password.")

    def create_account(self):
        username = self.username_input.text().strip()
        password = self.password_input.text().strip()
        users = self.load_users()

        if username in users:
            QMessageBox.warning(self, "Account Exists", "Username already exists.")
        elif not username or not password:
            QMessageBox.warning(self, "Invalid", "Username and password cannot be empty.")
        else:
            users[username] = {"password": password}
            self.save_users(users)
            QMessageBox.information(self, "Account Created", "Account successfully created!")
