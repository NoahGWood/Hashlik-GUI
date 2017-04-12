from PyQt4 import QtGui,QtCore
from PyQt4.QtGui import * #for some reason I can't just import all of PyQt4 or all of these two modules. Figures.
from PyQt4.QtCore import *
import sys
import time
import subprocess
import gui

class EmittingStream(QtCore.QObject):
    textWritten = QtCore.pyqtSignal(str)
    def write(self, text):
        self.textWritten.emit(str(text))


class ExampleApp(QtGui.QMainWindow, gui.Ui_HashlikGUI):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.browse_folder)
        self.pushButton_2.clicked.connect(self.installAPK)
        sys.stdout = EmittingStream(textWritten=self.normalOutputWritten)
        print("Instructions:")
        print("""Press "Select APK" to browse and find the APK you wish to install, then press "Install" """)
        print("");print("");print("");print("");print("");print("");print("");print("")
        print("Made By Noah Wood using PyQt4 https://github.com/NoahGWood")        

    
    def browse_folder(self):
        self.textEdit.clear()
        global fname
        fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file',   'c:\\',"APK Files (*apk)")
        print(fname)

    def __del__(self):
        # Restore sys.stdout
        sys.stdout = sys.__stdout__

    def normalOutputWritten(self, text):
        cursor = self.textEdit.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.textEdit.setTextCursor(cursor)
        self.textEdit.ensureCursorVisible()
        

    def installAPK(self):
        global fname
        a = fname
        fname = None
        if a != None:
            #test if logfile exists:
            log = subprocess.call(['ls -l install_log'], shell=True)
            if log >0:
                install = subprocess.call([
                    '/opt/shashlik/bin/shashlik-install {0} | cat > install_log'.format(str(a))],
                                          stderr=subprocess.STDOUT, shell=True)
            elif log ==0:
                install = subprocess.call([
                    '/opt/shashlik/bin/shashlik-install {0} | cat >> install_log'.format(str(a))],
                                          stderr=subprocess.STDOUT, shell=True)
                
        else:
            self.textEdit.clear()
            print("Instructions:")
            print("""Press "Select APK" to browse and find the APK you wish to install, then press "Install" """)
            print("");print("");print("");print("");print("");print("");print("");print("")
            print("Made By Noah Wood using PyQt4 https://github.com/NoahGWood")         

def main():
    app = QtGui.QApplication(sys.argv)
    form = ExampleApp()
    splash_pix = QPixmap('/opt/shashlik/data/shashlik.png')
    splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    splash.setMask(splash_pix.mask())
    splash.show()
    app.processEvents()
    time.sleep(2)
    form.show()
    splash.close()
    app.exec_()
    
    
if __name__ == '__main__':
    main()
