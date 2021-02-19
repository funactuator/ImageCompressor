import sys
import PyQt5
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QFrame,QLabel
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
        #---------------------------main_widow-----------------------------------
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # -----------------------first frame in main window on app starrt-----------------------
        # ------------------------to resize a single image at once------------------------------
        self.file_bubble=QFrame(self)
        self.file_bubble.setObjectName('bubble')
        self.file_bubble.move(50,50)
        self.file_bubble.mousePressEvent = self.file_bubble_clicked

        self.file_bubble_heading = QLabel(self.file_bubble)
        self.file_bubble_heading.setObjectName("bubble_heading")
        self.file_bubble_heading.move(49, 8)
        self.file_bubble_heading.setText("Compress Single Image")

        self.file_bubble_para = QLabel(self.file_bubble)
        self.file_bubble_para.setObjectName("bubble_para")
        self.file_bubble_para.move(55, 35)
        self.file_bubble_para.setText("Click Here to Compress One Image!")
        self.file_bubble_para.setWordWrap(True)


        # -----------------------second  frame in main window on app starrt  ------------------
        # -----------------------To compress whole folder at once------------------------------
        self.dir_bubble = QFrame(self)
        self.dir_bubble.setObjectName('bubble')
        self.dir_bubble.move(50, 250)
        self.dir_bubble.mousePressEvent = self.dir_bubble_clicked

        self.dir_bubble_heading = QLabel(self.dir_bubble)
        self.dir_bubble_heading.setObjectName("bubble_heading")
        self.dir_bubble_heading.move(38, 8)
        self.dir_bubble_heading.setText("Compress Multiple Images")

        self.dir_bubble_para = QLabel(self.dir_bubble)
        self.dir_bubble_para.setObjectName("bubble_para")
        self.dir_bubble_para.move(43, 35)
        self.dir_bubble_para.setText("Click Here to Compress all images of a folder!")
        self.dir_bubble_para.setWordWrap(True)









        #---------------------file_bubble_expanded--> on clicking on first frame--------------------
        self.file_bubble_expanded = QFrame(self)
        self.file_bubble_expanded.setObjectName('bubble_expanded')
        self.file_bubble_expanded.move(50, 100)
        # -----------initially they are said to false so that dont get visibel on app start-----------
        self.file_bubble_expanded.setVisible(False)
        #---------------------file_bubble_expanded--------------------

        #---------------------dir_bubble_expanded ---> on cicking on second frame--------------------
        self.dir_bubble_expanded = QFrame(self)
        self.dir_bubble_expanded.setObjectName('bubble_expanded')
        self.dir_bubble_expanded.move(50, 100)
        self.dir_bubble_expanded.setVisible(False)
        #---------------------dir_bubble_expanded--------------------


        #----------------------------end main_window---------------------
        
        self.show()
        # ---------------------------Functionalities-----------------
    def file_bubble_clicked(self, event):
        self.file_bubble.setVisible(False)
        self.dir_bubble.setVisible(False)
        # print('Single Bubble Clicked')
        self.file_bubble_expanded.setVisible(True)

    def dir_bubble_clicked(self, event):
        self.file_bubble.setVisible(False)
        self.dir_bubble.setVisible(False)
        # print('Directory Bubble Clicked')
        self.dir_bubble_expanded.setVisible(True)

    
if __name__ == '__main__':
    # I dont know what these 3 lines do
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
