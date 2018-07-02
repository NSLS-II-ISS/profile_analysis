import databroker
from PyQt5.QtWidgets import QApplication
import sys
from isstools import Xview

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

db = databroker.Broker.named('iss')

iss_mono_pulses_per_deg= 360000
app = QApplication(sys.argv)
xview_gui = Xview.XviewGui(iss_mono_pulses_per_deg, db=db)

def xview():
    xview_gui.show()

xview()
