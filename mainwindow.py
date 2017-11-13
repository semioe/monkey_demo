from PyQt4 import uic
import RPi.GPIO as GPIO
GPIO_PIN = 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PIN, GPIO.OUT)
( Ui_MainWindow, QMainWindow ) = uic.loadUiType( 'mainwindow.ui' )

class MainWindow ( QMainWindow ):
    """MainWindow inherits QMainWindow"""
    def pushButton_click(self):
        GPIO.output(GPIO_PIN,GPIO.HIGH)
    def pushButton_2_click(self):
        GPIO.output(GPIO_PIN,GPIO.LOW)
    def __init__ ( self, parent = None ):
        QMainWindow.__init__( self, parent )
        self.ui = Ui_MainWindow()
        self.ui.setupUi( self )
        self.ui.pushButton.clicked.connect(self.pushButton_click)
        self.ui.pushButton_2.clicked.connect(self.pushButton_2_click)

    def __del__ ( self ):
        self.ui = None
