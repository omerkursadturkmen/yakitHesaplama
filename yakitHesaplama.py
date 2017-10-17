from PyQt4.QtGui import *
from PyQt4.QtCore import *

class yakitHesaplama(QDialog):
    def __init__(self,ebeveyn=None):
        super(yakitHesaplama,self).__init__(ebeveyn)
        grid=QGridLayout()
        grid.addWidget(QLabel('Gidilecek Yol:'),0,0)
        self.yol=QLineEdit()
        grid.addWidget(self.yol,0,1)
        grid.addWidget(QLabel('fiyat:'),1,0)
        self.fiyat=QLineEdit()
        grid.addWidget(self.fiyat,1,1)
        grid.addWidget(QLabel('Yakıt Tüketimi:'),2,0)
        self.yakitTuketimi=QLineEdit()
        grid.addWidget(self.yakitTuketimi,2,1)
        grid.addWidget(QLabel('Tutar:'),3,0)
        self.tutar=QLabel('')
        grid.addWidget(self.tutar,3,1)
        hesapla=QPushButton('HESAPLA') 
        grid.addWidget(hesapla,4,0,1,2)
        self.setLayout(grid)
        self.setWindowTitle('Yakıt Hesaplama Programi')
        self.connect(hesapla,SIGNAL('pressed()'),self.yakitHesapla)
    def yakitHesapla(self):
        fiyat=0
        try:fiyat=float(self.fiyat.text())
        except:pass
        yol=0
        try:yol=int(self.yol.text())
        except:pass
        yakitTuketimi=0
        try:yakitTuketimi=float(self.yakitTuketimi.text())
        except:pass
        if not yol:
            self.tutar.setText('<font color="blue" <i>Yol Giriniz</i></font>')
            self.yol.setFocus()
        elif not fiyat:
            self.tutar.setText('<font color="blue" <i>Fiyat Giriniz</i></font>')
            self.yol.setFocus()
        elif not yakitTuketimi:
            self.tutar.setText('<font color="blue" <i>Tüketim Giriniz</i></font>')
            self.yol.setFocus()
        else:
            tutar=fiyat*(yol*yakitTuketimi)/100
            self.tutar.setText('<font color="blue" <b>%0.2f</>TL</font>'%tutar)              

uyg=QApplication([])
pencere=yakitHesaplama()
pencere.show()
uyg.exec_
