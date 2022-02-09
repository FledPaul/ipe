# Import Libs
import sys
import time
import requests
import json

from urllib.request import urlopen

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


#! Create GUI
class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        #* GUI Styling
        self.setWindowTitle('IPE - Internet Protocol Information Tool')
        self.setFixedHeight(340)
        self.setFixedWidth(700)
        self.setStyleSheet('background-color: #0D0D0D')

        #* IP-Input
        self.ip_input = QLineEdit(self)
        self.ip_input.setPlaceholderText('Enter ...')
        self.ip_input.resize(425, 50)
        self.ip_input.move(25, 25)
        self.ip_input.setStyleSheet('background-color: #222222; border: none; border-radius: 15px; padding-left: 10px; padding-right: 10px; font-size: 15px; color: #FFFFFF; font-weight: 700;')

        #* Scan Button
        self.ip_scan = QPushButton('Scan', self)
        self.ip_scan.resize(200, 50)
        self.ip_scan.move(475, 25)
        self.ip_scan.setStyleSheet('background-color: #2361FF; border: none; color: #FFF; font-size: 15px; font-weight: 800; border-radius: 15px;')

        #* Horizontal Line
        self.line = QLabel(self)
        self.line.resize(650, 2)
        self.line.move(25, 100)
        self.line.setStyleSheet('background-color: #222222; border-radius: 25px;')


        #! Location

        #* Background
        self.location_background = QLabel(self)
        self.location_background.resize(315, 85)
        self.location_background.move(25, 125)
        self.location_background.setStyleSheet('background-color: #222222; border-radius: 25px;')

        #* Title
        self.location_title = QLabel(self)
        self.location_title.setText('Location')
        self.location_title.resize(325, 24)
        self.location_title.move(45, 139)
        self.location_title.setStyleSheet('color: #FFF; background-color: transparent; font-weight: 700; font-size: 20px;')

        #* Description
        self.location_desc = QLabel(self)
        self.location_desc.setText('-')
        self.location_desc.resize(325, 25)
        self.location_desc.move(45, 170)
        self.location_desc.setStyleSheet('color: #FFF; background-color: transparent; font-weight: 400; font-size: 18px;')


        #! Provider

        #* Background
        self.provider_background = QLabel(self)
        self.provider_background.resize(315, 85)
        self.provider_background.move(360, 125)
        self.provider_background.setStyleSheet('background-color: #222222; border-radius: 25px;')

        #* Title
        self.provider_title = QLabel(self)
        self.provider_title.setText('Provider')
        self.provider_title.resize(325, 24)
        self.provider_title.move(380, 139)
        self.provider_title.setStyleSheet('color: #FFF; background-color: transparent; font-weight: 700; font-size: 20px;')

        #* Description
        self.provider_desc = QLabel(self)
        self.provider_desc.setText('-')
        self.provider_desc.resize(325, 25)
        self.provider_desc.move(380, 170)
        self.provider_desc.setStyleSheet('color: #FFF; background-color: transparent; font-weight: 400; font-size: 18px;')


        #! Timezone

        #* Background
        self.timezone_background = QLabel(self)
        self.timezone_background.resize(315, 85)
        self.timezone_background.move(25, 235)
        self.timezone_background.setStyleSheet('background-color: #222222; border-radius: 25px;')

        #*  Title
        self.timezone_title = QLabel(self)
        self.timezone_title.setText('Local Time')
        self.timezone_title.resize(325, 24)
        self.timezone_title.move(45, 244)
        self.timezone_title.setStyleSheet('color: #FFF; background-color: transparent; font-weight: 700; font-size: 20px;')

        #* Description
        self.timezone_desc = QLabel(self)
        self.timezone_desc.setText('-')
        self.timezone_desc.resize(325, 25)
        self.timezone_desc.move(45, 275)
        self.timezone_desc.setStyleSheet('color: #FFF; background-color: transparent; font-weight: 400; font-size: 18px;')


        #! Long- & Latitude

        #* Background
        self.loc_background = QLabel(self)
        self.loc_background.resize(315, 85)
        self.loc_background.move(360, 235)
        self.loc_background.setStyleSheet('background-color: #222222; border-radius: 25px;')

        #* Title
        self.loc_title = QLabel(self)
        self.loc_title.setText('Long- & Latitude')
        self.loc_title.resize(325, 28)
        self.loc_title.move(380, 244)
        self.loc_title.setStyleSheet('color: #FFF; background-color: transparent; font-weight: 700; font-size: 20px;')

        #* Description
        self.loc_desc = QLabel(self)
        self.loc_desc.setText('-')
        self.loc_desc.resize(325, 25)
        self.loc_desc.move(380, 275)
        self.loc_desc.setStyleSheet('color: #FFF; background-color: transparent; font-weight: 400; font-size: 18px;')
        
        #* Set Font
        self.ip_input.setFont(QFont('Segoe UI', 10))
        self.ip_scan.setFont(QFont('Segoe UI', 10))
        self.location_title.setFont(QFont('Segoe UI', 10))
        self.location_desc.setFont(QFont('Segoe UI', 10))
        self.provider_title.setFont(QFont('Segoe UI', 10))
        self.provider_desc.setFont(QFont('Segoe UI', 10))
        self.timezone_title.setFont(QFont('Segoe UI', 10))
        self.timezone_desc.setFont(QFont('Segoe UI', 10))
        self.loc_title.setFont(QFont('Segoe UI', 10))
        self.loc_desc.setFont(QFont('Segoe UI', 10))

        #! Scan Function
        def scan_ip():
            temp_ip = self.ip_input.text()

            #! Replace Spaces
            ip = str(temp_ip).replace(' ', '')

            #! Check IP
            if ip == '':
                print('Error : Input Empty')
                time.sleep(2)
                quit()


            #* Get Geolocation / Provider / Timezone
            url = 'https://ipinfo.io/'+ip
            response = urlopen(url)
            data = json.load(response)

            #* Define
            country = data['country']
            city = data['city']
            timezone = data['timezone']
            temp_provider = data['org']
            temp_loc = data['loc']

            #* Split
            tz_cn = str(timezone).split('/')[0] # Timezone Continent
            tz_ct_temp = str(timezone).split('/')[1] # Timezone City200.203.105.239
            tz_ct = str(tz_ct_temp).replace('_', ' ')
            temp_timezone = tz_cn+' / '+tz_ct # Temp Timezone
            st_provider = str(temp_provider).split(' ')[1] # Provider
            st_loc = str(temp_loc).replace(',', ' ') # Long- & Latitude

            #* Final Variables
            location = country+' / '+city
            provider = st_provider
            loc = st_loc
            tz = temp_timezone

            #* Change Text
            self.location_desc.setText(location)
            self.provider_desc.setText(provider)
            self.timezone_desc.setText(tz)
            self.loc_desc.setText(loc)

        #! Scan Onclick
        self.ip_scan.clicked.connect(scan_ip)

        #! Show Widgets
        self.show()

#! Create Application
App = QApplication(sys.argv)

#! Create Window Instance
window = Window()

#! Start Application
sys.exit(App.exec())