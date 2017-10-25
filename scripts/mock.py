#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 17:42:04 2017

@author: tania
"""

import os
from pathlib import Path
import shutil
import os, sys, glob

try:
    from urllib.parse import quote  # Py 3
except ImportError:
    from urllib2 import quote  # Py 2



# Finding the directories that contain notebooks
    
location = os.path.dirname(os.path.abspath(__file__))
basePath = Path(os.getcwd())
PathList = list(basePath.glob('**/*.ipynb'))
notebooks = [os.path.abspath(i) for i in PathList]

print("Notebooks found")