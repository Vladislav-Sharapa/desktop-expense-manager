from typing import Optional
from PySide6.QtCore import (QCoreApplication,
    QMetaObject,QRect, Qt)
from PySide6.QtWidgets import (QDialog, QLabel, QLineEdit,
    QPushButton, QWidget,QComboBox)

class EditCategoryDialog(QDialog):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.ui =  Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.confirm.clicked.connect(self.accept)
        

class DeleteDialog(QDialog):
    def __init__(self, categories, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.ui = DeleteUiDialog()
        self.ui.setupUi(self)

        self.ui.comboBox.addItem('-')
        for _, cat in categories.items():
            self.ui.comboBox.addItem(cat.title, cat.id)

        self.ui.confirm.clicked.connect(self.accept)


class DeleteUiDialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(242, 265)
        self.confirm = QPushButton(Dialog)
        self.confirm.setObjectName(u"confirm")
        self.confirm.setGeometry(QRect(70, 200, 111, 51))
        self.comboBox = QComboBox(Dialog)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(20, 80, 201, 41))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.confirm.setText(QCoreApplication.translate("Dialog", u"Delete", None))
    
    def get_data(self):
        return{
            'id': self.comboBox.currentData()
        }


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(242, 265)
        self.confirm = QPushButton(Dialog)
        self.confirm.setObjectName(u"confirm")
        self.confirm.setGeometry(QRect(60, 200, 111, 51))
        self.confirm.clicked.connect(QDialog.accept)
        self.title = QLineEdit(Dialog)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(90, 80, 141, 41))
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 90, 49, 16))
        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Add category", None))
        self.confirm.setText(QCoreApplication.translate("Dialog", u"Confirm", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Title", None))
    # retranslateUi
        
    def get_data(self):
        return{
            'title': self.title.text()
        }

