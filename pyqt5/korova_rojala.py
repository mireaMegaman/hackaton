import sys
# import torch
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QLineEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap


class DragDropImage(QWidget):
    def __init__(self):
        super().__init__()
        self.tmp = 'wertyui'
        self.arr = []
        # настройки окна
        self.setWindowTitle('Drag and Drop Image')
        self.setGeometry(200, 200, 550, 680)
        self.setAcceptDrops(True)
        # элементы GUI
        self.image_label = QLabel(self)
        self.image_label.setGeometry(50, 110, 450, 450)
        self.image_label.setAcceptDrops(True)
        self.image_label.setText('Ваша фотография здесь')
        self.image_label.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.image_label.setStyleSheet('''
            color: rgb(97, 97, 97);                           
            border: 4px dashed #aaa;
            text-align: center;
        ''')
        # инпут пути до сета
        self.text_input = QLineEdit(self)
        self.text_input.setGeometry(125, 600, 300, 30)
        self.text_input.editingFinished.connect(self.set_path)
        
        # кнопки
        self.clear_button = QPushButton('Clear', self)
        self.clear_button.setGeometry(290, 640, 100, 30)
        self.clear_button.clicked.connect(self.clear_image)
        
        self.accept_button_2 = QPushButton('Accept', self)
        self.accept_button_2.setGeometry(160, 640, 100, 30)
        self.accept_button_2.clicked.connect(self.accept_image)

        # Лейблы
        self.app_label = QLabel(self)
        self.app_label.setGeometry(50, 30, 450, 30)
        self.app_label.setText('MegaMen / Цифровой прорыв')
        self.app_label.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.app_label.setStyleSheet('''
            border-color: rgb(30, 30, 30);
            border-style: outset;
            border-width: 1px;
        ''')
        
        self.app_label = QLabel(self)
        self.app_label.setGeometry(50, 70, 450, 30)
        self.app_label.setText('Поместите вашу картинку ниже')
        self.app_label.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.app_label.setStyleSheet('''
            border-color: rgb(30, 30, 30);
            border-style: outset;
            border-width: 1px;
        ''')

        self.app_label_2 = QLabel(self)
        self.app_label_2.setGeometry(50, 570, 450, 30)
        self.app_label_2.setText('Вставьте путь до вашего датасета в рамку ниже')
        self.app_label_2.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

        self.app_label3 = QLabel(self)
        self.app_label3.setGeometry(50, 600, 30, 30)
        self.app_label3.setText('')
        self.app_label3.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.app_label3.setStyleSheet('''
                    border-color: rgb(30, 30, 30);
                    border-style: outset;
                    border-width: 1px;
                ''') 

    def dragEnterEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()
            
    def dragMoveEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def display_image(self, image):
        # выводим изображение на метку
        self.image_label.setPixmap(image)

    def dropEvent(self, event):
        if event.mimeData().hasImage:
            event.setDropAction(Qt.CopyAction)
            # event.accept()
            files = list(map(lambda x: x.toLocalFile(), event.mimeData().urls()))
            self.tmp = files[-1]
            self.arr += files
            print(self.arr)
            image = QPixmap(self.tmp)
            self.display_image(image.scaled(450, 450))
            self.app_label3.setText(f'{len(self.arr)}')
        else:
            event.ignore()
            self.setText('\n\n Drop Image Here \n\n')

    def set_path(self):
        model = self.text_input.text()
        model = model.replace('\\', '/')
        print(f'{model}')
        

    def clear_image(self):
        # очищаем содержимое метки
        self.image_label.clear()
        self.text_input.clear()
        self.arr.clear()
        
    def accept_image(self):
        print(self.tmp)
        self.image_label.setText('Подтверждено, проверка.')


def modeling(filepath):
    PATH = ''
    # model = torch.load(PATH) 


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DragDropImage()
    window.show()
    sys.exit(app.exec_())
