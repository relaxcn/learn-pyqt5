import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLCDNumber, QSlider, QVBoxLayout
from PyQt5.QtCore import Qt

class Example(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):

		lcd = QLCDNumber(self)

		#  slider 水平放置
		sli = QSlider(Qt.Horizontal, self)

		# 创建一个垂直布局对象
		vbox = QVBoxLayout()
		vbox.addWidget(lcd)
		vbox.addWidget(sli)

		self.setLayout(vbox)

		# 连接信号与信号槽
		sli.valueChanged.connect(lcd.display)

		self.setGeometry(300, 300, 400, 400)
		self.setWindowTitle("Signal and Sltos")
		self.show()

def main():
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()
	