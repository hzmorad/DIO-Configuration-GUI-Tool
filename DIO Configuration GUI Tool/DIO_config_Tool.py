# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DIO_config_Tool.ui'
#
# Created: Wed Feb 27 20:55:02 2019
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1009, 660)
        self.Pin_0_group = QtGui.QGroupBox(Form)
        self.Pin_0_group.setGeometry(QtCore.QRect(80, 50, 841, 471))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(50)
        font.setBold(False)
        self.Pin_0_group.setFont(font)
        self.Pin_0_group.setObjectName("Pin_0_group")
        self.Mode_group = QtGui.QGroupBox(self.Pin_0_group)
        self.Mode_group.setGeometry(QtCore.QRect(40, 20, 221, 231))
        self.Mode_group.setObjectName("Mode_group")
        self.Output_button = QtGui.QRadioButton(self.Mode_group)
        self.Output_button.setGeometry(QtCore.QRect(40, 40, 131, 20))
        self.Output_button.setObjectName("Output_button")
        self.Input_button = QtGui.QRadioButton(self.Mode_group)
        self.Input_button.setGeometry(QtCore.QRect(40, 100, 131, 20))
        self.Input_button.setObjectName("Input_button")
        self.Output_config_group = QtGui.QGroupBox(self.Pin_0_group)
        self.Output_config_group.setGeometry(QtCore.QRect(370, 30, 361, 141))
        self.Output_config_group.setObjectName("Output_config_group")
        self.High_button = QtGui.QRadioButton(self.Output_config_group)
        self.High_button.setGeometry(QtCore.QRect(30, 40, 131, 20))
        self.High_button.setObjectName("High_button")
        self.Low_button = QtGui.QRadioButton(self.Output_config_group)
        self.Low_button.setGeometry(QtCore.QRect(200, 40, 131, 20))
        self.Low_button.setObjectName("Low_button")
        self.Input_config_group = QtGui.QGroupBox(self.Pin_0_group)
        self.Input_config_group.setGeometry(QtCore.QRect(370, 180, 361, 141))
        self.Input_config_group.setObjectName("Input_config_group")
        self.Pull_Up_button = QtGui.QRadioButton(self.Input_config_group)
        self.Pull_Up_button.setGeometry(QtCore.QRect(200, 30, 131, 20))
        self.Pull_Up_button.setObjectName("Pull_Up_button")
        self.Pull_Imp_button = QtGui.QRadioButton(self.Input_config_group)
        self.Pull_Imp_button.setGeometry(QtCore.QRect(30, 30, 131, 20))
        self.Pull_Imp_button.setObjectName("Pull_Imp_button")
        self.PinName_LineEdit = QtGui.QLineEdit(self.Pin_0_group)
        self.PinName_LineEdit.setGeometry(QtCore.QRect(42, 340, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.PinName_LineEdit.setFont(font)
        self.PinName_LineEdit.setObjectName("PinName_LineEdit")
        self.Default_Name_CheckBox = QtGui.QCheckBox(self.Pin_0_group)
        self.Default_Name_CheckBox.setGeometry(QtCore.QRect(390, 340, 181, 20))
        self.Default_Name_CheckBox.setObjectName("Default_Name_CheckBox")
        self.Output_Folder_Path_LineEdit = QtGui.QLineEdit(Form)
        self.Output_Folder_Path_LineEdit.setGeometry(QtCore.QRect(80, 570, 591, 31))
        self.Output_Folder_Path_LineEdit.setObjectName("Output_Folder_Path_LineEdit")
        self.Generate_Button = QtGui.QPushButton(Form)
        self.Generate_Button.setGeometry(QtCore.QRect(690, 570, 93, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Generate_Button.setFont(font)
        self.Generate_Button.setObjectName("Generate_Button")
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(80, 540, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(50)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.Output_button, QtCore.SIGNAL("clicked(bool)"), self.Output_config_group.setEnabled)
        QtCore.QObject.connect(self.Output_button, QtCore.SIGNAL("clicked(bool)"), self.Input_config_group.setDisabled)
        QtCore.QObject.connect(self.Input_button, QtCore.SIGNAL("clicked(bool)"), self.Input_config_group.setEnabled)
        QtCore.QObject.connect(self.Input_button, QtCore.SIGNAL("clicked(bool)"), self.Output_config_group.setDisabled)
        QtCore.QObject.connect(self.Default_Name_CheckBox, QtCore.SIGNAL("clicked(bool)"), self.PinName_LineEdit.setDisabled)
        QtCore.QObject.connect(self.Default_Name_CheckBox, QtCore.SIGNAL("clicked()"), self.PinName_LineEdit.clear)
        QtCore.QObject.connect(self.Generate_Button, QtCore.SIGNAL("clicked()"), self.GenerateFun) #self.PinName_LineEdit.clear
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "DIO_Configurator", None, QtGui.QApplication.UnicodeUTF8))
        self.Pin_0_group.setTitle(QtGui.QApplication.translate("Form", "Pin 0", None, QtGui.QApplication.UnicodeUTF8))
        self.Mode_group.setTitle(QtGui.QApplication.translate("Form", "Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.Output_button.setText(QtGui.QApplication.translate("Form", "Output", None, QtGui.QApplication.UnicodeUTF8))
        self.Input_button.setText(QtGui.QApplication.translate("Form", "Input", None, QtGui.QApplication.UnicodeUTF8))
        self.Output_config_group.setTitle(QtGui.QApplication.translate("Form", "Output Config", None, QtGui.QApplication.UnicodeUTF8))
        self.High_button.setText(QtGui.QApplication.translate("Form", "High", None, QtGui.QApplication.UnicodeUTF8))
        self.Low_button.setText(QtGui.QApplication.translate("Form", "Low", None, QtGui.QApplication.UnicodeUTF8))
        self.Input_config_group.setTitle(QtGui.QApplication.translate("Form", "Input Config", None, QtGui.QApplication.UnicodeUTF8))
        self.Pull_Up_button.setText(QtGui.QApplication.translate("Form", "Pull Imp", None, QtGui.QApplication.UnicodeUTF8))
        self.Pull_Imp_button.setText(QtGui.QApplication.translate("Form", "Pull Up", None, QtGui.QApplication.UnicodeUTF8))
        self.PinName_LineEdit.setText(QtGui.QApplication.translate("Form", "Enter the pin name", None, QtGui.QApplication.UnicodeUTF8))
        self.Default_Name_CheckBox.setText(QtGui.QApplication.translate("Form", "Set Default Name", None, QtGui.QApplication.UnicodeUTF8))
        self.Generate_Button.setText(QtGui.QApplication.translate("Form", "Generate", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Output Folder Path:", None, QtGui.QApplication.UnicodeUTF8))
        
    def GenerateFun(self):
      outputFolder         = self.Output_Folder_Path_LineEdit.text()
      DIO_Config_File      = outputFolder+'DIO_config.h'
      MFIC_File            = outputFolder+'MFIC.h'
      DIO_File_handler     = open(DIO_Config_File,'w')
      MFIC_File_handler    = open(MFIC_File,'w')
      
      PIN0_Name = ''
      PIN0_Mode = ''
      
      if self.Default_Name_CheckBox.isChecked():
        PIN0_Name = 'DIO_u8_PIN_0'
      else:
        PIN0_Name = self.PinName_LineEdit.text()
      
      if self.Output_button.isChecked():
        if self.High_button.isChecked():
          PIN0_Mode = 'DIO_u8_OUTPUT_HIGH'
        else:
          PIN0_Mode = 'DIO_u8_OUTPUT_LOW'
      else:
        if self.Pull_Up_button.isChecked():
          PIN0_Mode = 'DIO_u8_INPUT_PULL_UP'
        else:
          PIN0_Mode = 'DIO_u8_INPUT_HIGH_IMP'
          
      DIO_File_handler.write(r'#define  DIO_u8_PIN_0_INIT_MODE      '+PIN0_Mode)
      MFIC_File_handler.write(r'#define    '+PIN0_Name+'    0')
      
      DIO_File_handler.close()
      MFIC_File_handler.close()


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

