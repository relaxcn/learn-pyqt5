import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QTextEdit, QLineEdit, QGridLayout

class Example(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		title = QLabel('Title')
		author = QLabel('Author')
		review = QLabel('Review')

		titleEdit = QLineEdit()
		authorEdit = QLineEdit()
		reviewEdit = QTextEdit()

		grid = QGridLayout()
		# 设置组件的上下间距
		grid.setSpacing(10)
		self.setLayout(grid)

		grid.addWidget(title, 0, 0)
		grid.addWidget(titleEdit, 0, 1)

		grid.addWidget(author, 1, 0)
		grid.addWidget(authorEdit, 1, 1)

		grid.addWidget(review, 2, 0)
		grid.addWidget(reviewEdit, 2, 1, 4, 1)

		self.setGeometry(300, 300, 400, 400)
		self.setWindowTitle('review')
		self.show()

def main():
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())


if __name__ == '__main__':
	main()