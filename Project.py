# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ProjectGui.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import nltk
#nltk.download('stopwords')
#nltk.download('punkt')
import math
import re
import heapq
import numpy as np
import pandas as pd
import sys
import PyPDF2
import doctext

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog


class Ui_Form(object):
    def setupUi(self, Form):

        Form.setObjectName("Form")
        Form.resize(1050, 696)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")

        self.lblReport = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Comfortaa SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lblReport.setFont(font)
        self.lblReport.setObjectName("lblReport")
        self.verticalLayout.addWidget(self.lblReport)
        
        self.scrollAreaUpload = QtWidgets.QScrollArea(Form)
        self.scrollAreaUpload.setAutoFillBackground(False)
        self.scrollAreaUpload.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.scrollAreaUpload.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollAreaUpload.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollAreaUpload.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.scrollAreaUpload.setWidgetResizable(True)
        self.scrollAreaUpload.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scrollAreaUpload.setObjectName("scrollAreaUpload")

        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 1009, 216))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        self.lblUpload = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblUpload.setFont(font)
        self.lblUpload.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lblUpload.setText("")
        self.lblUpload.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lblUpload.setWordWrap(True)
        self.lblUpload.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.lblUpload.setObjectName("lblUpload")
        self.verticalLayout_4.addWidget(self.lblUpload)

        self.scrollAreaUpload.setWidget(self.scrollAreaWidgetContents_3)
        self.verticalLayout.addWidget(self.scrollAreaUpload)

        self.lblSummary = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Comfortaa SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lblSummary.setFont(font)
        self.lblSummary.setObjectName("lblSummary")
        self.verticalLayout.addWidget(self.lblSummary)

        self.scrollAreaSubmit = QtWidgets.QScrollArea(Form)
        self.scrollAreaSubmit.setAutoFillBackground(False)
        self.scrollAreaSubmit.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.scrollAreaSubmit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollAreaSubmit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollAreaSubmit.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.scrollAreaSubmit.setWidgetResizable(True)
        self.scrollAreaSubmit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scrollAreaSubmit.setObjectName("scrollAreaSubmit")
        
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 1009, 216))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.lblSubmit = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblSubmit.sizePolicy().hasHeightForWidth())
        self.lblSubmit.setSizePolicy(sizePolicy)
        self.lblSubmit.setSizeIncrement(QtCore.QSize(1, 1))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblSubmit.setFont(font)
        self.lblSubmit.setText("")
        self.lblSubmit.setScaledContents(True)
        self.lblSubmit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lblSubmit.setWordWrap(True)
        self.lblSubmit.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.lblSubmit.setObjectName("lblSubmit")
        self.verticalLayout_3.addWidget(self.lblSubmit)

        self.scrollAreaSubmit.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout.addWidget(self.scrollAreaSubmit)

        self.btnUpload = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHeightForWidth(self.btnUpload.sizePolicy().hasHeightForWidth())
        self.btnUpload.setSizePolicy(sizePolicy)
        self.btnUpload.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Comfortaa SemiBold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.btnUpload.setFont(font)
        self.btnUpload.setAutoDefault(False)
        self.btnUpload.setDefault(False)
        self.btnUpload.setFlat(False)
        self.btnUpload.setObjectName("btnUpload")
        self.verticalLayout.addWidget(self.btnUpload, 0, QtCore.Qt.AlignHCenter)

        self.btnSubmit = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHeightForWidth(self.btnSubmit.sizePolicy().hasHeightForWidth())
        self.btnSubmit.setSizePolicy(sizePolicy)
        self.btnSubmit.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Comfortaa SemiBold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.btnSubmit.setFont(font)
        self.btnSubmit.setCheckable(False)
        self.btnSubmit.setAutoRepeatDelay(300)
        self.btnSubmit.setObjectName("btnSubmit")
        self.verticalLayout.addWidget(self.btnSubmit, 0, QtCore.Qt.AlignHCenter)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        #self.scrollAreaUpload.setWidget(self.lblUpload)
        #self.scrollAreaSubmit.setWidget(self.lblSubmit)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Report Summarization"))
        self.lblReport.setText(_translate("Form", "Report "))
        self.lblSummary.setText(_translate("Form", "Summary"))
        self.btnSubmit.setText(_translate("Form", "SUBMIT"))
        self.btnUpload.setText(_translate("Form", "UPLOAD"))

        self.btnUpload.clicked.connect(self.push_button_Upload)
        self.btnSubmit.clicked.connect(self.push_button_Submit)

    def push_button_Upload(self):
        self.file_name = QFileDialog.getOpenFileName()
        self.path = self.file_name[0]
        file = self.read_content(self.path)
        self.lblUpload.setText(file)
        

    def read_content(self, path):
        try:
            if path.endswith('.docx'):
                doc_text = doctext.DocFile(doc=path)
                text = doc_text.get_text()
                return text
            elif path.endswith('.pdf'):
                text=self.pdf_content_reader(path)
                print("in pdf")
                return text

            elif path.endswith('.txt'):

                with open(path,'r',encoding="mbcs") as f:
                    return f.read()
            else:
                return "FILE CANNOT OPEN!!!\nINVALID FORMAT FILE... \nPLEASE OPEN A WORD, PDF OR A TXT FILE."
        except:
            pass
    
    def pdf_content_reader(self,path):
        # creating a pdf file object 
        pdfFileObj = open(path, 'rb') 
            
        # creating a pdf reader object 
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
        # creating a page object 
        text=""
        for i in range(pdfReader.numPages):
            pageObj = pdfReader.getPage(i) 
            text=text+" " +pageObj.extractText()
        # extracting text from page 
        #print(pageObj.extractText()) 
            
        # closing the pdf file object 
        pdfFileObj.close()
        return text

    def push_button_Submit(self):
        sent_word_length = '30' 
        
        path = self.file_name[0]
        file = self.read_content(path)
        

        text = file
        text = re.sub(r'\[[0-9]*\]',' ',text)
        text = re.sub(r'\s+',' ',text)

        clean_text = text.lower()

        regex_patterns = [r'\W',r'\d',r'\s+']
        for regex in regex_patterns:
            clean_text = re.sub(regex,' ',clean_text)

        sentences = nltk.sent_tokenize(text)
        top_n= math.sqrt(len(sentences))
        stop_words = nltk.corpus.stopwords.words('english')

        word_count = {}
        for word in nltk.word_tokenize(clean_text):
            if word not in stop_words:
                if word not in word_count.keys():
                    word_count[word] = 1
                else:
                    word_count[word] += 1

        sentence_score = {}
        for sentence in sentences:
            for word in nltk.word_tokenize(sentence.lower()):
                if word in word_count.keys():
                    if len(sentence.split(' ')) < int(sent_word_length):
                        if sentence not in sentence_score.keys():
                            sentence_score[sentence] = word_count[word]
                        else:
                            sentence_score[sentence] += word_count[word]
        
        

        best_sentences = heapq.nlargest(int(top_n), sentence_score, key=sentence_score.get)
        
        summarized_text = []

        sentences = nltk.sent_tokenize(text)

        for sentence in sentences:
            if sentence in best_sentences:
                summarized_text.append(sentence)

        summarized_text = "\n".join(summarized_text)

        self.lblSubmit.setText(summarized_text)
        
        savepath=self.path.split('/')
        savepath=savepath[:-1]
        savepath='/'.join(savepath)+'/'+'summary.txt'
        text_file = open(savepath, "w")
        text_file.write(summarized_text)
        text_file.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
