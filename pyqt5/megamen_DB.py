import sys, os
import shutil
import torch
from PyQt5 import QtCore
from ultralytics import YOLO
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QLineEdit, QFrame
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from zipfile import ZipFile
from classifier import *


class DragDropImage(QWidget):
    def __init__(self):
        super().__init__()
        self.tmp = 'wertyui'
        self.arr = []
        self.setStyleSheet("background-color: white;")
        self.model = YOLO('./yolo8nano_best_model.pt')
        # настройки окна
        self.setWindowTitle('Drag and Drop Image')
        self.setGeometry(200, 200, 1200, 800)
        self.setAcceptDrops(True)
        # элементы GUI
        self.image_label = QLabel(self)
        self.image_label.setGeometry(90, 145, 450, 450)
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
        self.text_input.setGeometry(125, 670, 300, 40)
        self.text_input.editingFinished.connect(self.set_path)
        
        # кнопки
        self.clear_button = QPushButton('Clear', self)
        self.clear_button.setGeometry(290, 720, 100, 30)
        self.clear_button.clicked.connect(self.clear_image)
        
        self.accept_button_2 = QPushButton('Accept', self)
        self.accept_button_2.setGeometry(160, 720, 100, 30)
        self.accept_button_2.clicked.connect(self.accept_image)

        # Лейблы
        self.app_label = QLabel(self)
        self.app_label.setGeometry(90, 20, 450, 45)
        self.app_label.setText('MegaMen / Цифровой прорыв')
        self.app_label.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.app_label.setStyleSheet('''
            border-color: rgb(30, 30, 30);
            border-style: outset;
            border-width: 1px;
        ''')
        
        self.app_label = QLabel(self)
        self.app_label.setGeometry(90, 80, 450, 45)
        self.app_label.setText('Поместите вашу картинку ниже')
        self.app_label.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.app_label.setStyleSheet('''
            border-color: rgb(30, 30, 30);
            border-style: outset;
            border-width: 1px;
        ''')

        self.app_label_2 = QLabel(self)
        self.app_label_2.setGeometry(30, 620, 550, 30)
        self.app_label_2.setText('Путь до вашего датасета вставьте ниже')
        self.app_label_2.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

        self.app_label3 = QLabel(self)
        self.app_label3.setGeometry(50, 670, 40, 40)
        self.app_label3.setText('')
        self.app_label3.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.app_label3.setStyleSheet('''
                    border-color: rgb(30, 30, 30);
                    border-style: outset;
                    border-width: 1px;
                ''') 

        self.app_label4 = QLabel(self)
        self.app_label4.setGeometry(630, 20, 500, 40)
        self.app_label4.setText('Статистика')
        self.app_label4.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.app_label4.setStyleSheet('''
                    border-color: rgb(30, 30, 30);
                    border-style: outset;
                    border-width: 1px;
                ''') 

        self.app_label5 = QLabel(self)
        self.app_label5.setGeometry(630, 70, 500, 600)
        self.app_label5.setText('')
        self.app_label5.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.app_label5.setStyleSheet('''
                    border-color: rgb(30, 30, 30);
                    border-style: outset;
                    border-width: 1px;
                ''') 
        # для вывода имени фотографии (вводить через \n)
        self.app_label6 = QLabel(self)
        self.app_label6.setGeometry(630, 70, 350, 600)
        self.app_label6.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.app_label6.setStyleSheet('''
                    border-color: rgb(30, 30, 30);
                    border-style: outset;
                    border-width: 1px;
                ''') 

        # для значений по фотографиям
        self.app_label7 = QLabel(self)
        self.app_label7.setGeometry(980, 70, 150, 600)
        self.app_label7.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.app_label7.setStyleSheet('''
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
            if event.mimeData().urls()[-1].toLocalFile().split('.')[-1] == 'zip':
                self.tmp = event.mimeData().urls()[-1].toLocalFile()
                self.image_label.setText('ZIP-файл успешно загружен.')
                self.app_label3.setText('1')
            else:
                self.tmp = event.mimeData().urls()[-1].toLocalFile()
                image = QPixmap(self.tmp)
                self.display_image(image.scaled(450, 450))
                self.app_label3.setText('2')
        else:
            event.ignore()
            shutil.rmtree('./runs/detect/predict')
            self.setText('\n\n Загрузите zip-файл. \n\n')

    def set_path(self):
        model = self.text_input.text()
        model = model.replace('\\', '/')
        print(f'{model}')

    def clear_image(self):
        # очищаем содержимое метки
        self.image_label.clear()
        self.text_input.clear()
        self.arr.clear()
        self.app_label3.setText('0')
        self.app_label6.clear()
        self.app_label7.clear()
        
    def accept_image(self):
        print(self.tmp)
        self.app_label6.clear()
        self.app_label7.clear()
        model = Classifier()
        model = model.get_model_from_file('classifier_efficient_net_95-8acc.pt')
        #model.eval()
        if self.tmp.split('.')[-1] == 'zip':
            with ZipFile(self.tmp) as zip_file:
                arr = list(map(lambda x: str(x).split("'")[1], zip_file.infolist()))
                print(arr)
                for img_name in arr:
                    try:
                        zip_file.extract(img_name, path='.')
                        result = self.model.predict(source=img_name, save_crop=True)
                        print(result)
                        #model.predict(result)
                        os.remove(img_name, dir_fd=None)
                    except:
                        continue
        else:
            print(self.tmp)
            result = self.model.predict(source=self.tmp, save_crop=True)
            elephant = list(
                map(lambda x: f'runs/detect/predict/crops/Swan/{x}', os.listdir('runs/detect/predict/crops/Swan')))
            print(elephant)

            if len(elephant) > 1:
                print(model.VoitingEnsemble(elephant))

            else:
                print(model.solo_object_prediction(elephant[0]))
                self.app_label6.setText(self.tmp.split('/')[-1])
                if model.solo_object_prediction(elephant[0]) == 3:
                    self.app_label7.setText('Шипун')
                elif model.solo_object_prediction(elephant[0]) == 2:
                    self.app_label7.setText('Кликун')
                elif model.solo_object_prediction(elephant[0]) == 1:
                    self.app_label7.setText('Малый')
                # else:
                #    self.app_label7.setText('')
        # for i in os.listdir('runs/detect/predict/crops/Swan'):
        #    print(model.predict(f'runs/detect/predict/crops/Swan/{i}'))
        shutil.rmtree('./runs')
        self.image_label.setText('Подтверждено, проверка.')


def modeling(filepath):
    PATH = 'classifier_efficient_net_95-8acc.pt'
    model = torchvision.models.e


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DragDropImage()
    window.show()
    sys.exit(app.exec_())