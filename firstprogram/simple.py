import sys
from PyQt5.QtWidgets import QApplication, QWidget

def main():

    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(500, 150)
    w.move(300, 300)
    w.setWindowTitle("xiu货！")
    w.show()
    
    
    sys.exit(app.exec_())

if __name__=='__main__':
    main()