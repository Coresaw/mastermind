
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import random as rnd
import mm_algos

class Separator(QWidget):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        self.configFont = QtGui.QFont()
        self.configFont.setPixelSize(16)
        self.configFont.setBold(True)
        self.setGeometry(10, 10, 500, 40)
        self.setFixedHeight(40)
        self.victoryText = ("────── " + window.agent + " solved in " 
                                + str(window.totalSteps) + " steps! ──────")
        window.theBox.widgetList.append(self)
        self.show()    
    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setFont(self.configFont)
        painter.setPen(QPen(Qt.black, 2, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.gray, Qt.SolidPattern))
        painter.drawRect(20,5, 490, 30)
        painter.drawText(30, 23, self.victoryText)

class GuessRow(QWidget):
    def __init__(self, *args, **kwargs): 
        QWidget.__init__(self, *args, **kwargs)
        self.configFont = QtGui.QFont()
        self.configFont.setPixelSize(16)
        self.configFont.setBold(True)
        
        self.colours = window.guess
        self.setGeometry(10, 10, 500, 88)
        self.setFixedHeight(88)
        self.textToDrawTop = (str("Exact: " + str(window.Cluenumbers[0])))
        self.textToDrawBottom = (" Color: " + str(window.Cluenumbers[1]))
        window.theBox.widgetList.append(self)
        if window.Cluenumbers[0] == 4:
            window.solved = True
            window.submit.setEnabled(False)
            window.joe.setEnabled(False)
            window.leyla.setEnabled(False)
            window.daryl.setEnabled(False)
            window.cheat.setEnabled(False)
            window.play.setEnabled(True)
            
        self.show()

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.black, 2, Qt.SolidLine))
        
        for i in range(4):
            if self.colours[i] == 0:
                painter.setBrush(QBrush(Qt.red, Qt.SolidPattern))
            elif self.colours[i] == 1:
                painter.setBrush(QBrush(Qt.green, Qt.SolidPattern))
            elif self.colours[i] == 2:
                painter.setBrush(QBrush(Qt.blue, Qt.SolidPattern))
            elif self.colours[i] == 3:
                painter.setBrush(QBrush(Qt.yellow, Qt.SolidPattern))
            elif self.colours[i] == 4:
                painter.setBrush(QBrush(Qt.gray, Qt.SolidPattern))
            elif self.colours[i] == 5:
                painter.setBrush(QBrush(Qt.black, Qt.SolidPattern))
            painter.drawEllipse(25+100*(i), 10, 80, 65)
        
        painter.setFont(self.configFont)
        painter.drawText(425, 30, self.textToDrawTop)
        painter.drawText(420, 55, self.textToDrawBottom)

class Scrolling(QScrollArea): 

    # constructor 
    def __init__(self, *args, **kwargs): 
        QScrollArea.__init__(self, *args, **kwargs) 
        global contents 
        self.setWidgetResizable(True) 
		# making qwidget object 
        contents = QWidget(self) 
        self.setWidget(contents) 
		# vertical box layout 
        self.lay = QVBoxLayout(contents)
        self.widgetList = [] 

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.completeCopy = mm_algos.CompleteList()
        self.solved = False
        self.diff = 6   #difficulty = number of colors. not modifiable at the moment
        self.Cluenumbers = []
        self.mastersolution = []
        self.colourList = ["Red", "Green", "Blue", "Yellow", "Grey", "Black"]
        self.title = "MasterMind in PyQt5"
        self.top = 100
        self.left = 100
        self.width = 710
        self.minimumWidth = 710 
        self.height = 675
        self.minimumHeight = 300
        self.UiComponents()
        self.InitWindow()
        self.agent = "player"
        self.totalSteps = 0
        self.font = QtGui.QFont()
        self.font.setPointSize(12)
        self.font.setBold(True)
        self.font.setWeight(75)
    def UiComponents(self):

        self.theBox = Scrolling(self)
        self.theBox.setGeometry(10, 75, 550, 565)
        ghostWid = QLabel(contents)
        ghostWid.setGeometry(10, 10, 500, 88)
        ghostWid.setMaximumHeight(450)
        ghostWid.setAlignment(Qt.AlignLeft | Qt.AlignBottom)
        self.theBox.lay.insertWidget(0, ghostWid)
        
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)

        self.comboBox1 = QtWidgets.QComboBox(self)
        self.comboBox1.setGeometry(QtCore.QRect(10, 10,  85, 50))
        self.comboBox1.setFont(font)
        self.comboBox1.addItems(self.colourList)

        self.comboBox2 = QtWidgets.QComboBox(self)
        self.comboBox2.setGeometry(QtCore.QRect(105, 10, 85, 50))
        self.comboBox2.setFont(font)
        self.comboBox2.addItems(self.colourList)

        self.comboBox3 = QtWidgets.QComboBox(self)
        self.comboBox3.setGeometry(QtCore.QRect(200, 10, 85, 50))
        self.comboBox3.setFont(font)
        self.comboBox3.addItems(self.colourList)

        self.comboBox4 = QtWidgets.QComboBox(self)
        self.comboBox4.setGeometry(QtCore.QRect(295, 10, 85, 50))
        self.comboBox4.setFont(font)
        self.comboBox4.addItems(self.colourList)


        self.submit = QPushButton("submit", self)
        self.submit.setGeometry(QRect(390,10,150,50))
        self.submit.setEnabled(False)
        self.submit.clicked.connect(self.SubmitClicked)
        
        self.play = QPushButton("play", self)
        self.play.setGeometry(QRect(550,10,150,50))
        self.play.clicked.connect(self.PlayClicked)
        
        self.joe = QPushButton("Joe", self)
        self.joe.setGeometry(QRect(580,80,120,50))
        self.joe.setEnabled(False)
        self.joe.clicked.connect(self.JoeClicked)

        self.leyla = QPushButton("Leyla", self)
        self.leyla.setGeometry(QRect(580,150,120,50))
        self.leyla.setEnabled(False)
        self.leyla.clicked.connect(self.LeylaClicked)

        self.daryl = QPushButton("Daryl", self)
        self.daryl.setGeometry(QRect(580,220,120,50))
        self.daryl.setEnabled(False)
        self.daryl.clicked.connect(self.DarylClicked)

        self.cheat = QPushButton("Cheat", self)
        self.cheat.setGeometry(QRect(580, 480, 120, 50))
        self.cheat.clicked.connect(self.CheatClicked)

        self.clear = QPushButton("Clear", self)
        self.clear.setGeometry(QRect(580, 550, 120, 50))
        self.clear.clicked.connect(self.clearClicked)

    def CompareInput(self, guess, solution):
        cntExact = 0
        cntColOnly = 0
        for i in range(4):
            if guess[i] == solution[i] and solution[i] != -1:
                solution[i] = -1
                guess[i] = -1 
                cntExact += 1
        while -1 in solution:
            solution.remove(-1)
        while -1 in guess:
            guess.remove(-1)
        for i in range(len(guess)):
            if guess[i] in solution:
                solution.remove(guess[i])
                guess[i] = -1
                cntColOnly += 1
        return(cntExact, cntColOnly)

    def PlayClicked(self):
        self.solved = False
        self.submit.setEnabled(True)
        self.joe.setEnabled(True)
        self.leyla.setEnabled(True)
        self.daryl.setEnabled(True)
        self.cheat.setEnabled(True)
        self.play.setEnabled(False)
        self.mastersolution = []
        self.totalSteps = 0
        for i in range(4):
            self.mastersolution.append(rnd.randrange(self.diff))
        
    def AddRow(self):
        self.totalSteps += 1
        nextRow = GuessRow(contents)
        self.theBox.lay.insertWidget(0,nextRow)
        if window.solved == True:
            nextSepar = Separator(contents)
            window.theBox.lay.insertWidget(0,nextSepar)

    def SubmitClicked(self):
        self.agent = "player"
        self.joe.setEnabled(False)
        self.leyla.setEnabled(False)
        self.daryl.setEnabled(False)
        self.guess = (self.comboBox1.currentIndex(), self.comboBox2.currentIndex(),
                        self.comboBox3.currentIndex(), self.comboBox4.currentIndex())
        self.Cluenumbers = self.CompareInput(list(self.guess), list(self.mastersolution))
        self.AddRow()
        contents.update()

    def JoeClicked(self):
        self.agent = "Joe"
        Joe = mm_algos.JoeSolve(self, self.mastersolution)
        Joe.solve()

    def LeylaClicked(self):
        self.agent = "Leyla"
        Leyla = mm_algos.LeylaSolve(self, self.mastersolution)
        Leyla.solve()

    def DarylClicked(self):
        self.agent = "Daryl"
        Daryl = mm_algos.DarylSolve(self, self.mastersolution)
        Daryl.solve()

    def CheatClicked(self):
        self.agent = "Cheat (Daryl)"
        Daryl = mm_algos.DarylSolve(self, self.mastersolution)
        Daryl.solve()

    def clearClicked(self):
        for i in range(self.theBox.lay.count()):
            self.theBox.lay.itemAt(i).widget().close()
        ghostWid = QLabel(contents)
        ghostWid.setGeometry(10, 10, 500, 88)
        ghostWid.setMaximumHeight(450)
        ghostWid.setAlignment(Qt.AlignLeft | Qt.AlignBottom)
        self.theBox.lay.insertWidget(0, ghostWid)

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())