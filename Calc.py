from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Calculator(object):
    def setupUi(self, Calculator):
        Calculator.setObjectName("Calculator")
        Calculator.resize(300, 500)
        Calculator.setMinimumSize(QtCore.QSize(300, 500))
        Calculator.setMaximumSize(QtCore.QSize(300, 500))
        Calculator.setStyleSheet("background-color: #2b2b2b;")
        
        self.centralwidget = QtWidgets.QWidget(Calculator)
        self.centralwidget.setObjectName("centralwidget")
        
        
        # Output display
        self.OutputLabel = QtWidgets.QLabel(self.centralwidget)
        self.OutputLabel.setGeometry(QtCore.QRect(10, 10, 280, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.OutputLabel.setFont(font)
        self.OutputLabel.setStyleSheet("""
            background-color: #252525;
            color: #ffffff;
            border: 2px solid #3d3d3d;
            border-radius: 5px;
            padding: 5px;
        """)
        self.OutputLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.OutputLabel.setObjectName("OutputLabel")
        
        # Button styling
        button_style = """
            QPushButton {
                background-color: #4d4d4d;
                color: white;
                border: none;
                border-radius: 5px;
                font-size: 20px;
            }
            QPushButton:hover {
                background-color: #6d6d5d;
            }
            QPushButton:pressed {
                background-color: #3d3d3d;
            }
        """
        
        operator_style = """
            QPushButton {
                background-color: #ff8c00;
                color: black;
                border: none;
                border-radius: 5px;
                font-size: 20px;
                font-weight:bold;
            }
            QPushButton:hover {
                background-color: #ff9e32;
            }
            QPushButton:pressed {
                background-color: #e67e00;
            }
        """
        
        special_style = """
            QPushButton {
                background-color: #3a3a3a;
                color: white;
                border: 1px solid #4a4a4a;
                border-radius: 5px;
                font-size: 20px;
            }
            QPushButton:hover {
                background-color: #4a4a4a;
            }
            QPushButton:pressed {
                background-color: #2a2a2a;
            }
        """
        
        # First row
        self.percentButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("%"))
        self.percentButton.setGeometry(QtCore.QRect(10, 120, 65, 65))
        self.percentButton.setStyleSheet(special_style)
        self.percentButton.setObjectName("percentButton")
        
        self.cButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("C"))
        self.cButton.setGeometry(QtCore.QRect(80, 120, 65, 65))
        self.cButton.setStyleSheet(special_style)
        self.cButton.setObjectName("cButton")
        
        self.arrowButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.remove_it())
        self.arrowButton.setGeometry(QtCore.QRect(150, 120, 65, 65))
        self.arrowButton.setStyleSheet(special_style)
        self.arrowButton.setObjectName("arrowButton")
        
        self.divideButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("/"))
        self.divideButton.setGeometry(QtCore.QRect(220, 120, 65, 65))
        self.divideButton.setStyleSheet(operator_style)
        self.divideButton.setObjectName("divideButton")
        
        # Second row
        self.sevenButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("7"))
        self.sevenButton.setGeometry(QtCore.QRect(10, 190, 65, 65))
        self.sevenButton.setStyleSheet(button_style)
        self.sevenButton.setObjectName("sevenButton")
        
        self.eightButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("8"))
        self.eightButton.setGeometry(QtCore.QRect(80, 190, 65, 65))
        self.eightButton.setStyleSheet(button_style)
        self.eightButton.setObjectName("eightButton")
        
        self.nineButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("9"))
        self.nineButton.setGeometry(QtCore.QRect(150, 190, 65, 65))
        self.nineButton.setStyleSheet(button_style)
        self.nineButton.setObjectName("nineButton")
        
        self.multiplyButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("*"))
        self.multiplyButton.setGeometry(QtCore.QRect(220, 190, 65, 65))
        self.multiplyButton.setStyleSheet(operator_style)
        self.multiplyButton.setObjectName("multiplyButton")
        
        # Third row
        self.fourButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("4"))
        self.fourButton.setGeometry(QtCore.QRect(10, 260, 65, 65))
        self.fourButton.setStyleSheet(button_style)
        self.fourButton.setObjectName("fourButton")
        
        self.fiveButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("5"))
        self.fiveButton.setGeometry(QtCore.QRect(80, 260, 65, 65))
        self.fiveButton.setStyleSheet(button_style)
        self.fiveButton.setObjectName("fiveButton")
        
        self.sixButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("6"))
        self.sixButton.setGeometry(QtCore.QRect(150, 260, 65, 65))
        self.sixButton.setStyleSheet(button_style)
        self.sixButton.setObjectName("sixButton")
        
        self.subtractionButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("-"))
        self.subtractionButton.setGeometry(QtCore.QRect(220, 260, 65, 65))
        self.subtractionButton.setStyleSheet(operator_style)
        self.subtractionButton.setObjectName("subtractionButton")
        
        # Fourth row
        self.oneButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("1"))
        self.oneButton.setGeometry(QtCore.QRect(10, 330, 65, 65))
        self.oneButton.setStyleSheet(button_style)
        self.oneButton.setObjectName("oneButton")
        
        self.twoButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("2"))
        self.twoButton.setGeometry(QtCore.QRect(80, 330, 65, 65))
        self.twoButton.setStyleSheet(button_style)
        self.twoButton.setObjectName("twoButton")
        
        self.threeButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("3"))
        self.threeButton.setGeometry(QtCore.QRect(150, 330, 65, 65))
        self.threeButton.setStyleSheet(button_style)
        self.threeButton.setObjectName("threeButton")
        
        self.addButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("+"))
        self.addButton.setGeometry(QtCore.QRect(220, 330, 65, 65))
        self.addButton.setStyleSheet(operator_style)
        self.addButton.setObjectName("addButton")
        
        # Fifth row
        self.plusminusButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.plus_minus())
        self.plusminusButton.setGeometry(QtCore.QRect(10, 400, 65, 65))
        self.plusminusButton.setStyleSheet(button_style)
        self.plusminusButton.setObjectName("plusminusButton")
        
        self.zeroButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("0"))
        self.zeroButton.setGeometry(QtCore.QRect(80, 400, 65, 65))
        self.zeroButton.setStyleSheet(button_style)
        self.zeroButton.setObjectName("zeroButton")
        
        self.decimalButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.dot_it())
        self.decimalButton.setGeometry(QtCore.QRect(150, 400, 65, 65))
        self.decimalButton.setStyleSheet(button_style)
        self.decimalButton.setObjectName("decimalButton")
        
        self.equalButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.math_it())
        self.equalButton.setGeometry(QtCore.QRect(220, 400, 65, 65))
        self.equalButton.setStyleSheet(operator_style)
        self.equalButton.setObjectName("equalButton")
        
        Calculator.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Calculator)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 22))
        self.menubar.setObjectName("menubar")
        Calculator.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Calculator)
        self.statusbar.setObjectName("statusbar")
        Calculator.setStatusBar(self.statusbar)

        self.retranslateUi(Calculator)
        QtCore.QMetaObject.connectSlotsByName(Calculator)
    
    def remove_it(self):
        screen = self.OutputLabel.text()
        if len(screen) > 0:
            screen = screen[:-1]
            if not screen:
                screen = "0"
            self.OutputLabel.setText(screen)
    
    def math_it(self):
        screen = self.OutputLabel.text()
        try:
            ans = eval(screen)
            # Format to remove trailing .0 for integers
            if isinstance(ans, float) and ans.is_integer():
                ans = int(ans)
            self.OutputLabel.setText(str(ans))
        except:
            self.OutputLabel.setText("Error")
            QtCore.QTimer.singleShot(1000, lambda: self.OutputLabel.setText("0"))

    def plus_minus(self):
        screen = self.OutputLabel.text()
        if screen == "0":
            return
        if screen.startswith("-"):
            self.OutputLabel.setText(screen[1:])
        else:
            self.OutputLabel.setText(f"-{screen}")

    def dot_it(self):
        screen = self.OutputLabel.text()
        if "." in screen:
            # Check if there's already a decimal in the current number
            parts = screen.replace('+', ' ').replace('-', ' ').replace('*', ' ').replace('/', ' ').split()
            if "." not in parts[-1]:
                self.OutputLabel.setText(f"{screen}.")
        else:
            self.OutputLabel.setText(f"{screen}.")

    def press_it(self, pressed):
        if pressed == "C":
            self.OutputLabel.setText("0")
        else:
            if self.OutputLabel.text() == "0" and pressed not in ["+", "-", "*", "/", "%"]:
                self.OutputLabel.setText("")
            self.OutputLabel.setText(f"{self.OutputLabel.text()}{pressed}")

    def retranslateUi(self, Calculator):
        _translate = QtCore.QCoreApplication.translate
        Calculator.setWindowTitle(_translate("Calculator", "Calculator"))
        self.OutputLabel.setText(_translate("Calculator", "0"))
        self.percentButton.setText(_translate("Calculator", "%"))
        self.cButton.setText(_translate("Calculator", "C"))
        self.arrowButton.setText(_translate("Calculator", "⌫"))
        self.divideButton.setText(_translate("Calculator", "÷"))
        self.nineButton.setText(_translate("Calculator", "9"))
        self.eightButton.setText(_translate("Calculator", "8"))
        self.sevenButton.setText(_translate("Calculator", "7"))
        self.multiplyButton.setText(_translate("Calculator", "×"))
        self.sixButton.setText(_translate("Calculator", "6"))
        self.fiveButton.setText(_translate("Calculator", "5"))
        self.fourButton.setText(_translate("Calculator", "4"))
        self.subtractionButton.setText(_translate("Calculator", "-"))
        self.threeButton.setText(_translate("Calculator", "3"))
        self.twoButton.setText(_translate("Calculator", "2"))
        self.oneButton.setText(_translate("Calculator", "1"))
        self.addButton.setText(_translate("Calculator", "+"))
        self.decimalButton.setText(_translate("Calculator", "."))
        self.zeroButton.setText(_translate("Calculator", "0"))
        self.plusminusButton.setText(_translate("Calculator", "±"))
        self.equalButton.setText(_translate("Calculator", "="))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Calculator = QtWidgets.QMainWindow()
    ui = Ui_Calculator()
    ui.setupUi(Calculator)
    Calculator.show()
    sys.exit(app.exec_())