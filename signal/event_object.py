from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout
from PyQt5.QtCore import Qt
import sys

class Example(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):

		grid = QGridLayout()
		self.setLayout(grid)
		x = 0
		y = 0
		self.text = f"x={x}, y={y}"

		self.label = QLabel(self.text ,self)

		self.setMouseTracking(True)

		self.setGeometry(300, 300, 400, 400)
		self.setWindowTitle("Event Object")
		self.show()
		
	def mouseMoveEvent(self, e):
		x = e.x()
		y = e.y()
		text = f"x={x}, y={y}"
		# print(text)
		self.label.setText(text)

	def keyPressEvent(self, e):
		if e.key() == Qt.Key_Escape:
			print("got it!")
			self.close()

def main():
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())

if __name__=='__main__':
	main()