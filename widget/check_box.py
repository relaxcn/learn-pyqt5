import sys
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox
from PyQt5.QtCore import Qt

class Example(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		checkbox = QCheckBox("show the title", self)
		checkbox.move(20, 20)
		# 使开始时为选中状态
		checkbox.toggle()
		# if state is changed
		checkbox.stateChanged.connect(self.changeTitle)

		self.setGeometry(300, 300, 350, 250)
		self.setWindowTitle('QCheckBox')
		self.show()
	def changeTitle(self, state):
		print(state)
		print(Qt.Checked)

		if state == Qt.Checked:
			self.setWindowTitle("QCheckBox")
		else:
			self.setWindowTitle("")
def main():
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())
if __name__ == '__main__':
	main()