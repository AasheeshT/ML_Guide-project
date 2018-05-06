from PyQt5.QtWidgets import (QMainWindow, QTextEdit, 
    QAction, QFileDialog, QApplication)
from PyQt5.QtGui import QIcon
import sys
from sklearn.base import TransformerMixin
import pandas as pd
from test2 import Ui_MainWindow

class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):      

        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openFile = QAction(QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.openWindow)

        saveFile = QAction(QIcon('open.png'), 'Save', self)
        saveFile.setShortcut('Ctrl+S')
        saveFile.setStatusTip('Save File')
        saveFile.triggered.connect(self.getCSV)

        saveAsFile = QAction(QIcon('open.png'), 'Save as', self)
        saveAsFile.setStatusTip('Save File')
        saveAsFile.triggered.connect(self.getCSV)

        Exit = QAction(QIcon('open.png'), 'Exit', self)
        Exit.setStatusTip('Save File')
        Exit.triggered.connect(self.getCSV)

        Impute = QAction(QIcon('open.png'), 'Missing data', self)
        Impute.setStatusTip('Save File')
        Impute.triggered.connect(self.imputer)

        Normalize = QAction(QIcon('open.png'), 'Normalize', self)
        Normalize.setStatusTip('Save File')
        Normalize.triggered.connect(self.getCSV)

        Bar = QAction(QIcon('open.png'), 'Bar plot', self)
        Bar.setStatusTip('Save File')
        Bar.triggered.connect(self.getCSV)

        Scatter = QAction(QIcon('open.png'), 'Scatter plot', self)
        Scatter.setStatusTip('Save File')
        Scatter.triggered.connect(self.getCSV)

        Box = QAction(QIcon('open.png'), 'Box plot', self)
        Box.setStatusTip('Gives Box plot representation of data')
        Box.triggered.connect(self.getCSV)

        loReg = QAction(QIcon('open.png'), 'Logistic Regression', self)
        loReg.setStatusTip('Gives Box plot representation of data')
        loReg.triggered.connect(self.getCSV)

        SVM = QAction(QIcon('open.png'), 'SVM', self)
        SVM.setStatusTip('Gives Box plot representation of data')
        SVM.triggered.connect(self.getCSV)

        Rf= QAction(QIcon('open.png'), 'Random Forest', self)
        Rf.setStatusTip('Gives Box plot representation of data')
        Rf.triggered.connect(self.getCSV)

        Dt= QAction(QIcon('open.png'), 'Decision Tree', self)
        Dt.setStatusTip('Gives Box plot representation of data')
        Dt.triggered.connect(self.getCSV)

        Knn= QAction(QIcon('open.png'), 'KNN', self)
        Knn.setStatusTip('Gives Box plot representation of data')
        Knn.triggered.connect(self.getCSV)

        

        ts= QAction(QIcon('open.png'), 'Test split', self)
        ts.setStatusTip('Gives Box plot representation of data')
        ts.triggered.connect(self.getCSV)

        oh= QAction(QIcon('open.png'), 'One hot encoding', self)
        oh.setStatusTip('Encodes categorical data')
        oh.triggered.connect(self.getCSV)
        
        lh= QAction(QIcon('open.png'), 'Label Encoding', self)
        lh.setStatusTip('Encodes categorical data')
        lh.triggered.connect(self.labelEncoder)





        

        







        




        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        fileMenu = menubar.addMenu('&File')
        preprocess = menubar.addMenu('&Preprocessing')
        EDA = menubar.addMenu('&EDA')
        Tsp = menubar.addMenu('&Test split')
        Model = menubar.addMenu('Model')

        fileMenu.addAction(openFile)
        fileMenu.addAction(saveFile)
        fileMenu.addAction(saveAsFile)
        fileMenu.addAction(Exit)
 #       preprocess.addAction(Encode)
        preprocess.addAction(oh)
        preprocess.addAction(lh)
        preprocess.addAction(Impute)
        preprocess.addAction(Normalize)
        EDA.addAction(Bar)
        EDA.addAction(Scatter)
        EDA.addAction(Box)
        EDA.addAction(Bar)
        Model.addAction(loReg)
        Model.addAction(SVM)
        Model.addAction(Rf)
        Model.addAction(Dt)
        Model.addAction(Knn)
        Model.addAction(ts)




        


        

        
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('File dialog')
        self.show()
        
        
    def getCSV(self):
        filePath, _ = QFileDialog.getOpenFileName(self, 'Open file', '/home')
        if filePath != "":
            print ("Dirección",filePath) #Opcional imprimir la dirección del archivo
            self.df = pd.read_csv(str(filePath))
            print(self.df.describe())

    def labelEncoder(self):
      
        
      self.obj_df = self.df.select_dtypes(include=['object']).copy()
      for col in self.obj_df:
          
        self.obj_df[str(col)] = self.obj_df[str(col)].astype('category')
        self.obj_df[str(col)] = self.obj_df[str(col)].cat.codes
      for element in self.df:
          for c in self.obj_df:
              if(element == c):
                  self.df[str(element)] = self.obj_df[str(c)]
      print(self.df.head())
            
    def openWindow(self):
           self.w = QMainWindow()
           self.w = Ui_MainWindow
           self.w.setupUi(self)
           self.w.show()
           self.w.exec_()
           
    
    def imputer():
        
        imputer = preprocessing.Imputer(missing_values='NaN', strategy='most_frequent', axis=0)
        self.df = imputer.fit_transform(df)
        print(self.df.head())
        joblib.dump(imputer, 'imputer.pkl')
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
