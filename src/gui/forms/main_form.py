from typing import Any, Callable, Optional, Union
from PySide6.QtCore import (QCoreApplication, QModelIndex, 
    QMetaObject, QModelIndex, QObject, QPersistentModelIndex, QRect, Qt, QAbstractTableModel)
from PySide6.QtWidgets import ( QHBoxLayout, QLabel,
    QLayout, QPushButton,QMainWindow, QDialog,
    QSplitter, QTableView, QWidget)

from app.services import ExpenseService, ExpenseCategoryService
from .edit_expense_dialog import EditDialog, UpdateDialog
from .category_dialog import EditCategoryDialog, DeleteDialog

class ExpenseModel(QAbstractTableModel):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.items = []

    def setItems(self, items):
        self.beginResetModel()
        self.items = items
        self.endResetModel()

    def rowCount(self, *args, **kwargs) -> int:
        return len(self.items)
    
    def columnCount(self,  *args, **kwargs) -> int:
        return 4
    
    def data(self, index: QModelIndex, role: Qt.ItemDataRole) -> Any:
        if not index.isValid():
            return
        
        if role == Qt.ItemDataRole.DisplayRole:
            data = self.items[index.row()]
            col = index.column()
            if col == 0:
                return f'{data.title}'
            elif col == 1:
                return f'{data.created_at}'
            elif col == 2:
                return f'{data.amount}'
            elif col == 3:
                return f'{data.cat}'
        elif role == Qt.ItemDataRole.UserRole:
            return self.items[index.row()]
         
    def headerData(self, section: int, orientation: Qt.Orientation, role: Qt.ItemDataRole) -> Any:
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                return {
                    0: 'Title',
                    1: 'Created',
                    2: 'Amount',
                    3: 'Category',
                }.get(section)


class MainWindow(object):
    def __init__(self, window: QMainWindow) -> None:
        self.setupUi(window)
        self.expense_service = ExpenseService()
        self.expense_category_service = ExpenseCategoryService()
        
        self.model = ExpenseModel()
        self.tableView.setModel(self.model)
        self.load_data()
        self.load_category()

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(664, 449)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(10, 170, 641, 271))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 121, 41))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(120, 20, 41, 41))
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 120, 641, 41))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.layoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.clicked.connect(self.on_btnAddExpense_clicked)

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.clicked.connect(self.on_btnUpdateExpense_clicked)

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.clicked.connect(self.on_btnDeleteExpense_clicked)

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(460, 30, 181, 53))
        self.splitter.setOrientation(Qt.Vertical)
        self.add_category_button = QPushButton(self.splitter)
        self.add_category_button.setObjectName(u"add_category_button")
        self.add_category_button.clicked.connect(self.on_btnAddExpenseCategory_clicked)
        self.splitter.addWidget(self.add_category_button)
        self.delete_category_button = QPushButton(self.splitter)
        self.delete_category_button.setObjectName(u"add_category_button_2")
        self.delete_category_button.clicked.connect(self.on_btnDeleteExpenseCategory_clicked)
        self.splitter.addWidget(self.delete_category_button)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi
        
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Expanse manager", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Current expanses", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"000", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"New expanse", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Edit expanse", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Delete Expanse", None))
        self.add_category_button.setText(QCoreApplication.translate("MainWindow", u"Add category", None))
        self.delete_category_button.setText(QCoreApplication.translate("MainWindow", u"Delete category", None))
        
    def load_data(self):
        self.table_data = self.expense_service.get_all()
        print(self.table_data)
        self.model.setItems(self.table_data)
        self.label_2.setText(str(self.expense_service.get_total())) 

    def load_category(self):
        self.categories = {}
        rows = self.expense_category_service.get_all()
        for row in rows:
            self.categories[row.id] = row


    def run_dialog(self, dialog: QDialog, func: Callable):
        r = dialog.exec()
        if r == 1:
            data = dialog.ui.get_data()
            func(data)
            self.load_data()
        else:
            return

    def on_btnAddExpense_clicked(self):
        dialog = EditDialog(self.categories)
        self.run_dialog(dialog, lambda data: self.expense_service.add(data))
    
    def on_btnUpdateExpense_clicked(self):
        item = self.tableView.currentIndex()
        init_data = item.data(Qt.ItemDataRole.UserRole)
        dialog = UpdateDialog(self.categories, init_data)
        self.run_dialog(dialog, lambda data: self.expense_service.update(int(init_data.id), data))
    
    def on_btnDeleteExpense_clicked(self):
        item = self.tableView.currentIndex()
        data = item.data(Qt.ItemDataRole.UserRole)
        self.expense_service.delete(data.id)
        self.load_data()
    
    def on_btnAddExpenseCategory_clicked(self):
        dialog = EditCategoryDialog()
        self.run_dialog(dialog, lambda data: self.expense_category_service.add(data=data))
        self.load_category()

    def on_btnDeleteExpenseCategory_clicked(self):
        dialog = DeleteDialog(self.categories)
        self.run_dialog(dialog, lambda data: self.expense_category_service.delete(**data))
        self.load_category()