import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class Main_window(QMainWindow):

    def __init__(self):
        super(Main_window,self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        #navigation_bar
        nav_bar = QToolBar()
        self.addToolBar(nav_bar)

        #back_button
        back_button = QAction('<--',self)
        back_button.triggered.connect(self.browser.back)
        nav_bar.addAction(back_button)

        #forward_button
        forw_button = QAction('-->', self)
        forw_button.triggered.connect(self.browser.forward)
        nav_bar.addAction(forw_button)

        #reload_button
        reload_button = QAction('Refresh',self)
        reload_button.triggered.connect(self.browser.reload)
        nav_bar.addAction(reload_button)

        #home_button
        home_button = QAction('home', self)
        home_button.triggered.connect(self.navi_home)
        nav_bar.addAction(home_button)

        #navigation bar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navi_to_url)
        nav_bar.addWidget(self.url_bar)

        #changing urls
        self.browser.urlChanged.connect(self.update_url)

    def navi_home(self):
        self.browser.setUrl(QUrl('https://www.google.com'))

    def navi_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self,url):
        self.url_bar.setText(url.toString())



app = QApplication(sys.argv)
QApplication.setApplicationName('Personalized Browser')
window = Main_window()
app.exec_()