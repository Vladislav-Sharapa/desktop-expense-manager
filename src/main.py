import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from gui.forms.main_form import MainWindow


if __name__ == "__main__":
    app = QApplication([])
    main_window = QMainWindow()
    ui = MainWindow(main_window)
    main_window.show()
    sys.exit(app.exec())
