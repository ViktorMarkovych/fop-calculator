from tkinter import font
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys




class Exit_Window(QMainWindow):
   def __init__(self):
      super(Exit_Window, self).__init__()

      self.setWindowTitle("Калькулятор ФОП")
      self.setGeometry(300, 100, 500, 350)
      self.setStyleSheet('background-color:#9aa8a1; border: 0px;')
    
      self.exit_text = QtWidgets.QLabel(self)
      self.exit_text.setText("Калькулятор ФОП")
      self.exit_text.move(200, 100)
      self.exit_text.adjustSize()


      self.button_registration = QtWidgets.QPushButton(self)
      self.button_registration.move(175, 150)
      self.button_registration.setText("Реєстрація")
      self.button_registration.setFixedWidth(150)
      self.button_registration.setStyleSheet("background-color : cyan")
      

      self.button_exit = QtWidgets.QPushButton(self)
      self.button_exit.move(175, 200)
      self.button_exit.setText("Вхід")
      self.button_exit.setFixedWidth(150)
      self.button_exit.setStyleSheet("background-color : #50C878")



class Registration_Window(QMainWindow):
   def __init__(self):
      super(Registration_Window, self).__init__()

      self.setWindowTitle("Калькулятор ФОП")
      self.setGeometry(300, 100, 500, 350)
      self.setStyleSheet('background-color:#9aa8a1; border: 0px;')
    
      
      self.exit_text = QtWidgets.QLabel(self)
      self.exit_text.setText("Реєстрація")
      self.exit_text.move(200, 30)
      self.exit_text.adjustSize()

      
      self.email_adress = QtWidgets.QLineEdit(self)
      self.email_adress.setPlaceholderText("Електронна адреса")
      self.email_adress.move(200, 80)
      self.email_adress.setStyleSheet('background-color:#6ba5a1; border: 0px;')

      
      self.password = QtWidgets.QLineEdit(self)
      self.password.setPlaceholderText("Пароль")
      self.password.move(200, 130)
      self.password.setStyleSheet('background-color:#6ba5a1; border: 0px;')


      self.password_verification = QtWidgets.QLineEdit(self)
      self.password_verification.setPlaceholderText("Підтвердження пароля")
      self.password_verification.move(200, 180)
      self.password_verification.setStyleSheet('background-color:#6ba5a1; border: 0px;')


      self.button_registration = QtWidgets.QPushButton(self)
      self.button_registration.move(175, 270)
      self.button_registration.setText("Реєстрація")
      self.button_registration.setFixedWidth(150)
      self.button_registration.setStyleSheet("background-color : cyan")



class Enter_Window(QMainWindow):
   def __init__(self):
      super(Enter_Window, self).__init__()


      self.setWindowTitle("Калькулятор ФОП")
      self.setGeometry(300, 100, 500, 350)
      self.setStyleSheet('background-color:#9aa8a1; border: 0px;')
    
      
      self.enter_text = QtWidgets.QLabel(self)
      self.enter_text.setText("Вхід")
      self.enter_text.move(250, 50)
      self.enter_text.adjustSize()


      self.enter_email_adress = QtWidgets.QLineEdit(self)
      self.enter_email_adress.setPlaceholderText("Електронна адреса")
      self.enter_email_adress.move(200, 100)
      self.enter_email_adress.setStyleSheet('background-color:#6ba5a1; border: 0px;')


      self.enter_password = QtWidgets.QLineEdit(self)
      self.enter_password.setPlaceholderText("Пароль")
      self.enter_password.move(200, 180)
      self.enter_password.setStyleSheet('background-color:#6ba5a1; border: 0px;')


      self.enter_button = QtWidgets.QPushButton(self)
      self.enter_button.move(175, 270)
      self.enter_button.setText("Вхід")
      self.enter_button.setFixedWidth(150)
      self.enter_button.setStyleSheet("background-color : cyan")



class Officer_Window(QMainWindow):
   def __init__(self):
      super(Officer_Window, self).__init__()


      self.setWindowTitle("Калькулятор ФОП")
      self.setGeometry(300, 100, 500, 350)
      self.setStyleSheet('background-color:#9aa8a1; border: 0px;')
    
      
      self.enter_text = QtWidgets.QLabel(self)
      self.enter_text.setText("Кабінет")
      self.enter_text.move(250, 50)
      self.enter_text.adjustSize()



      








def Calc():
    app = QApplication(sys.argv)
    exit_window = Officer_Window()



    exit_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    Calc()

