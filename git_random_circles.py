import sys
from random import randint
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QPainter, QBrush, QColor
from PyQt5.QtCore import Qt, QRect


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(10, 10, 300, 300)
        self.button = QPushButton("Создать окружность", self)
        self.button.setGeometry(QRect(10, 10, 280, 30))
        self.button.clicked.connect(self.create_circle)
        self.circle_x = None
        self.circle_y = None
        self.circle_diameter = None
        self.circle_color = None

    def create_circle(self):
        self.circle_x = randint(0, self.width())
        self.circle_y = randint(0, self.height())
        self.circle_diameter = randint(10, 100)
        self.circle_color = QColor(randint(0, 255), randint(0, 255), randint(0, 255))
        self.update()

    def paintEvent(self, event):
        super().paintEvent(event)
        if (
            self.circle_x is not None
            and self.circle_y is not None
            and self.circle_diameter is not None
        ):
            qp = QPainter(self)
            qp.setBrush(QBrush(self.circle_color))
            qp.setRenderHint(QPainter.Antialiasing)
            qp.drawEllipse(
                self.circle_x, self.circle_y, self.circle_diameter, self.circle_diameter
            )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
