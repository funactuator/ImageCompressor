import sys
import PyQt5
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QFrame
from PyQt5.QtGui import QIcon
# import design
class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Image Compressor'
        # Start position wrt to monitor screen, of top left corner of window
        self.left = 600
        self.top = 200
        # Window Height and width
        self.width = 400
        self.height = 600
        self.setFixedSize(self.width, self.height)
        # self.setStyleSheet("background-color:black")
        self.setObjectName('main_window')
        stylesheet = ""
        with open("design.qss", "r") as f:
            stylesheet = f.read()
        
        self.setStyleSheet(stylesheet)
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)


        #---------------------------main_widow-----------------------------------
        self.single_bubble=QFrame(self)
        self.single_bubble.setObjectName('bubble')
        self.single_bubble.move(50,125)
        self.single_bubble.mousePressEvent = self.single_bubble_clicked


        self.dir_bubble = QFrame(self)
        self.dir_bubble.setObjectName('bubble')
        self.dir_bubble.move(50, 275)
        self.dir_bubble.mousePressEvent = self.dir_bubble_clicked

        #---------------------single_bubble_expanded--------------------
        self.single_bubble_expanded = QFrame(self)
        self.single_bubble_expanded.setObjectName('bubble_expanded')
        self.single_bubble_expanded.move(50, 100)
        self.single_bubble_expanded.setVisible(False)
        #---------------------single_bubble_expanded--------------------

        #---------------------dir_bubble_expanded--------------------
        self.dir_bubble_expanded = QFrame(self)
        self.dir_bubble_expanded.setObjectName('bubble_expanded')
        self.dir_bubble_expanded.move(50, 100)
        self.dir_bubble_expanded.setVisible(False)
        #---------------------dir_bubble_expanded--------------------


        #----------------------------end main_window---------------------
        
        self.show()
        # ---------------------------Functionalities-----------------
    def single_bubble_clicked(self, event):
        self.single_bubble.setVisible(False)
        self.dir_bubble.setVisible(False)
        # print('Single Bubble Clicked')
        self.single_bubble_expanded.setVisible(True)

    def dir_bubble_clicked(self, event):
        self.single_bubble.setVisible(False)
        self.dir_bubble.setVisible(False)
        # print('Directory Bubble Clicked')
        self.dir_bubble_expanded.setVisible(True)

    
if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
