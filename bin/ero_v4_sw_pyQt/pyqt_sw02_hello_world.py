import sys
#Hello World mit den Aenderungen fuer Qt5

#from PyQt4 import QtGui
from PyQt5 import QtWidgets

def window():
   #app = QtGui.QApplication(sys.argv)
   app = QtWidgets.QApplication(sys.argv)

   #w = QtGui.QWidget()
   #b = QtGui.QLabel(w)
   w = QtWidgets.QWidget()   
   b = QtWidgets.QLabel(w)

   b.setText("Hello World!")
   w.setGeometry(100,100,200,50)
   b.move(50,20)
   w.setWindowTitle("PyQt - Version Qt5")
   w.show()
   sys.exit(app.exec_())
   
if __name__ == '__main__':
   window()
