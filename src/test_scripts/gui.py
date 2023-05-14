import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QSize

# Define the function to send the selected menu item as a trigger to the other code
def send_trigger(menu_item):
    # Call the other code and pass in the selected menu item as an argument
    # print("Selected menu item:", menu_item)
    if(menu_item=="menu_item1.png"):
        print("Let's make a hot dog!")
    elif(menu_item=="menu_item2.png"):
        print("Let's make a sandwich!")

# Define the GUI window
class MenuWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Define the menu items as images
        menu_items = ["menu_item1.png", "menu_item2.png", "menu_item3.png"]

        # Define the buttons with the menu item images and callbacks
        self.button1 = QPushButton(self)
        self.button1.setIcon(QIcon(menu_items[0]))
        self.button1.setIconSize(QSize(64, 64))
        self.button1.clicked.connect(lambda: send_trigger(menu_items[0]))

        self.button2 = QPushButton(self)
        self.button2.setIcon(QIcon(menu_items[1]))
        self.button2.setIconSize(QSize(64, 64))
        self.button2.clicked.connect(lambda: send_trigger(menu_items[1]))

        self.button3 = QPushButton(self)
        self.button3.setIcon(QIcon(menu_items[2]))
        self.button3.setIconSize(QSize(64, 64))
        self.button3.clicked.connect(lambda: send_trigger(menu_items[2]))

        # Define the layout and add the buttons
        layout = QHBoxLayout()
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)

        # Set the layout to the central widget
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

# Create and show the GUI window
app = QApplication(sys.argv)
window = MenuWindow()
window.show()
sys.exit(app.exec_())
