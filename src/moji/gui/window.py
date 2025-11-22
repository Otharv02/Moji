
from PyQt5.QtCore import QSize, Qt, QTimer
from PyQt5.QtWidgets import QMainWindow, QLabel, QToolBar, QAction, QStatusBar, QLineEdit, QVBoxLayout, QWidget

from core.responses import*
from core.assistant import*

# Window Size
height = 295
width  = 295

# Font Size
moji_font_size = 30



"""
For setting window
"""
class SecondaryWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Secondary title
        self.setWindowTitle("Menu")

        # window fixed size
        self.setFixedSize(QSize(height,width))




"""
Displays the title and Fixed Window & Moji 1.0 and button
"""
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Title
        self.setWindowTitle("Moji")

        # container widget
        container = QWidget()
        self.setCentralWidget(container)

        # Layout
        layout = QVBoxLayout()
        container.setLayout(layout)

        # Moji 1.0
        self.widget = QLabel(get_face())
        # text font 
        font   = self.widget.font()
        font.setPointSize(moji_font_size)
        # font alignment
        self.widget.setFont(font)
        self.widget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)


        # Result Display 
        self.result_label = QLabel("")
        self.result_label.setAlignment(Qt.AlignHCenter)

        # Text Input 
        self.textbox = QLineEdit()
        self.textbox.returnPressed.connect(self.on_enter_pressed)

        # Add Widget to Layout
        layout.addWidget(self.widget)
        layout.addWidget(self.result_label)
        layout.addWidget(self.textbox)

        # Timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_widget)
        self.timer.start(1500)

        # Toolbar
        toolbar = QToolBar("Tool Bar")
        self.addToolBar(toolbar)
        action = QAction("Setting", self)
        action.triggered.connect(self.toolbar_button_clicked)
        toolbar.addAction(action)

        self.setStatusBar(QStatusBar(self))

        self.setFixedSize(QSize(height, width))



    """
    Setting Button Click Function
    """
    def toolbar_button_clicked(self,s):
        self.secondary = SecondaryWindow()
        self.secondary.show()

    """
    Taking user input from the textbox
    """
    def on_enter_pressed(self):
        text = self.textbox.text().strip()
        #print(text)

        if text.startswith("/"):
            result = handle_commad(text)
        
        else:
            result = handle_chat(text)

        self.result_label.setText(result)
        self.textbox.clear()


    """
    Function for randomly selecting widgets
    """
    def update_widget(self):
        pick_random_mood()       # change mood each tick
        self.widget.setText(get_face())  # update face