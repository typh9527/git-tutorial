from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
import sys
import sendfile
import configparser
class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.myButton = QtWidgets.QPushButton(self)
        self.myButton.setObjectName("myButton")
        self.myButton.setText("上传")
        self.myButton.move(260,100)
        self.setGeometry(300, 380, 360, 170)
        self.myButton.clicked.connect(self.msg)

    def msg(self):
        config = configparser.ConfigParser()
        config.read('log.ini')
        host = config.get("Settings","host")
        user_email = config.get("Settings","email")
        print(user_email)
        fileName1, filetype = QFileDialog.getOpenFileName(self,
                                    "选取文件",
                                    "/",
                                    "Rar Files(*.zip)")   #设置文件扩展名过滤,注意用双分号间隔
        
        if fileName1 == '':
            flag = False
        else:
            flag = sendfile.send(host ,user_email , fileName1)
#        directory1 = QFileDialog.getExistingDirectory(self,
#                                    "选取文件夹",
#                                    "C:/")                                 #起始路径
#        print(directory1)
        if flag:
            msg = 'success'
        else:
            msg = "failed"
        reply = QMessageBox.information(self,                         #使用infomation信息框
                                    "标题",
                                    msg,
                                    QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            sys.exit()
#        fileName1, filetype = QFileDialog.getOpenFileName(self,
#                                    "选取文件",
#                                    "C:/",
#                                    "All Files (*);;Text Files (*.txt)")   #设置文件扩展名过滤,注意用双分号间隔
#        print(fileName1,filetype)
#
#        files, ok1 = QFileDialog.getOpenFileNames(self,
#                                    "多文件选择",
#                                    "C:/",
#                                    "All Files (*);;Text Files (*.txt)")
#        print(files,ok1)
#
#        fileName2, ok2 = QFileDialog.getSaveFileName(self,
#                                    "文件保存",
#                                    "C:/",
#                                    "All Files (*);;Text Files (*.txt)")

if __name__=="__main__":  
    app=QtWidgets.QApplication(sys.argv)	
    myshow=MyWindow()
    label = QtWidgets.QLabel(myshow)
    label_text = "<br>使用说明：</br><br>1、使用前请打开log.ini文件，配置登陆信息</br><br>2、点击上传按钮选择zip文件</br>"
    label2_text = "<br>注意：</br><br>zip文件要求：<br/><br>1、压缩包(即项目名)名字不要重复</br><br>2、zip文件内必须有和zip文件名相同的子目录<br/><br>3、子目录中的要执行的.m文件必须以main命名</br><br>具体请参考附带的test\
                   .zip文件</br>"
    label.setText(label_text+label2_text)
    myshow.show()
    sys.exit(app.exec_())  
