import databroker
from PyQt5.QtWidgets import QApplication
import sys
from xview import xview

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.ion()

db = databroker.Broker.named('iss')


app = QApplication(sys.argv)
xview_gui = xview.XviewGui(db=db)

def xview():
    xview_gui.show()

xview()
