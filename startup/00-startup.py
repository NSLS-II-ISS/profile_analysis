import databroker
from PyQt5.QtWidgets import QApplication
from PyQt5 import uic, QtCore
import sys
from xview import xview
from xview.spectra_db.db_io import get_spectrum_catalog
import os
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.ion()

db = databroker.Broker.named('iss')

db_proc = get_spectrum_catalog()


# os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"

app = QApplication(sys.argv)
app.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
xview_gui = xview.XviewGui(db=db, db_proc=db_proc)

def xview():
    xview_gui.show()

xview()
