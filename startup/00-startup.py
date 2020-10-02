import databroker
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore
import sys,os
from xview import xview

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

db = databroker.Broker.named('iss')

os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"

app = QApplication(sys.argv)
app.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
xview_gui = xview.XviewGui(db=db)

def xview():
    xview_gui.show()

xview()
