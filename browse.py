import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *



class MainWindow(QMainWindow):

    def navigate_home(self):
            self.browser.setUrl(QUrl("http://google.com"))       #home Button function

    def naviagte_to_url(self):                                   #while press enter go to particular url
            url=self.url_bar.text()
            self.browser.setUrl(QUrl(url))        

    def update_url(self, q):                                      #url changes in search bar while url changes
        self.url_bar.setText(q.toString())        

    def __init__(self):
        super(MainWindow,self).__init__()
        self.browser=QWebEngineView()
        self.browser.setUrl(QUrl("http://google.com"))
        self.setCentralWidget(self.browser)

        #create navbar
        navbar=QToolBar()
        self.addToolBar(navbar)


        back_btn=QAction('Back',self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)


        forw_btn=QAction('Forward',self)
        forw_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forw_btn)

        reload_btn=QAction('Reload',self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        home_btn=QAction('Home',self) 
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        self.url_bar=QLineEdit()
        self.url_bar.returnPressed.connect(self.naviagte_to_url)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

    
        self.showMaximized()

app=QApplication(sys.argv)
QApplication.setApplicationName('    MY COOL BROWSER     ')    
window=MainWindow()    
app.exec()