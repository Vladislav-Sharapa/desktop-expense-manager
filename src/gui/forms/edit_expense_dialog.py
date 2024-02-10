
from PySide6.QtCore import (QCoreApplication,
    QMetaObject,QRect)
from PySide6.QtWidgets import (QComboBox, QDialog, QLabel,
    QLineEdit, QPushButton)

class UpdateDialog(QDialog):
    def __init__(self, categories, init_data,  *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.comboBox.addItem(init_data.cat, init_data.category_id)
        self.ui.title.setText(str(init_data.title))
        self.ui.amount.setText(str(init_data.amount))

        self.ui.addButton.clicked.connect(self.accept)


class EditDialog(QDialog):
    def __init__(self, categories:dict, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.categories = categories
        self.load_category_combobox()
        self.ui.addButton.clicked.connect(self.accept)


    def load_category_combobox(self):
        self.ui.comboBox.addItem('-')
        for id, cat in self.categories.items():
            self.ui.comboBox.addItem(cat.title, cat.id)
        

class Ui_Dialog(object):
    def get_data(self):
        return {
            'category_id': self.comboBox.currentData(),
            'title': self.title.text(),
            'amount': self.amount.text()
        }

    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(262, 282)
        self.comboBox = QComboBox(Dialog)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(10, 60, 241, 31))
        self.title = QLineEdit(Dialog)
        self.title.setObjectName(u"lineEdit")
        self.title.setGeometry(QRect(100, 100, 151, 31))
        self.addButton = QPushButton(Dialog)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setGeometry(QRect(10, 200, 241, 71))

        self.amount = QLineEdit(Dialog)
        self.amount.setObjectName(u"lineEdit_2")
        self.amount.setGeometry(QRect(100, 140, 151, 31))
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 110, 31, 16))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 150, 49, 16))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Expense", None))
        self.addButton.setText(QCoreApplication.translate("Dialog", u"Confirm", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Title", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Amount", None))
    # retranslateUi
        
        
    

