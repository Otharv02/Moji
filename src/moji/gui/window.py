
from PyQt5.QtCore import QSize, Qt, QTimer
from PyQt5.QtWidgets import QMainWindow, QLabel, QToolBar, QAction, QStatusBar, QLineEdit

from core.responses import*

# Window Size
height = 295
width  = 295

# Font Size
moji_font_size = 30



"""
For setting tab
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

        # Moji 1.0
        self.widget = QLabel(get_face())
        
        # text font 
        font   = self.widget.font()
        font.setPointSize(moji_font_size)
        
        # font alignment
        self.widget.setFont(font)
        self.widget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.setCentralWidget(self.widget)

        # timer for rotating widgets
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_widget)
        self.timer.start(1500)   # 1.5s

        # ToolBar 
        toolbar = QToolBar("Tool Bar")
        self.addToolBar(toolbar)

        # Secondary window button
        toolbar_button_action = QAction("Talk To Me!",self)
        #toolbar_button_action.setStatusTip("Yes")
        toolbar_button_action.triggered.connect(self.toolbar_button_clicked)
        toolbar_button_action.setCheckable(True)
        toolbar.addAction(toolbar_button_action)

        self.setStatusBar(QStatusBar(self))


        # Text Box
        self.textbox = QLineEdit(self)

        # user text input   
        self.textbox.returnPressed.connect(self.on_enter_pressed)

        # textbox location
        self.textbox.move(0,258)
        self.textbox.resize(280,40)
        
        

        # window fixed size
        self.setFixedSize(QSize(height,width))


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
        text = self.textbox.text()
        print(text)
        self.textbox.clear()


    """
    used for randomly selecting widgets
    """
    def update_widget(self):
        pick_random_mood()       # change mood each tick
        self.widget.setText(get_face())  # update face