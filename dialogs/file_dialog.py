import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QTextEdit, QFileDialog
from PyQt5.QtGui import QIcon
from pathlib import Path

class Example(QMainWindow):
	def __init__(self):
		super().__init__()
		self.initUI()
	def initUI(self):

		self.statusBar()
		menubar = self.menuBar()

		self.textEdit = QTextEdit()	
		self.setCentralWidget(self.textEdit)

		openFile = QAction(QIcon('open.png'), 'Open', self)
		openFile.setStatusTip("open new file")
		openFile.setShortcut('Ctrl+O')
		openFile.triggered.connect(self.showDialog)

		saveFile = QAction(QIcon('save_file.png'), 'Save File', self)
		saveFile.setShortcut('Ctrl+S')
		saveFile.setStatusTip('Save File')
		saveFile.triggered.connect(self.saveFileAction)

		fileMenu = menubar.addMenu('&File')
		fileMenu.addAction(openFile)
		fileMenu.addAction(saveFile)

		self.setGeometry(300, 300, 400, 400)
		self.setWindowTitle("File Dialog")
		self.show()

	def showDialog(self):
		home_dir = str(Path.home())
		self.fname = QFileDialog.getOpenFileName(self, 'Open File', home_dir)
		print(self.fname)
		if self.fname[0]:
			f = open(self.fname[0], 'r')
			with f:
				data = f.read()
				self.textEdit.setText(data)
	def saveFileAction(self):
		try:
			if self.fname[0]:
				f = open(self.fname[0], 'w')
				with f:
					data = self.textEdit.toPlainText()
					print(str(data))
					f.write(str(data))
		except AttributeError:
			print("must open a file.")
			self.showDialog()
		except:
			print("other Failed.")
		else:
			self.statusBar().showMessage("Save Success.")

def main():
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())
if __name__ == '__main__':
	main()