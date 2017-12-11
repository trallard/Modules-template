#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: tania
This code is used to generate Jekyll blogpost from Jupyter notebooks
within a main Jekyll repository
"""

from pathlib import Path
import os, glob, fnmatch

try:
    from urllib.parse import quote  # Py 3
except ImportError:
    from urllib2 import quote  # Py 2



# Finding the directories that contain notebooks
# note that this will return all of the notebooks in the repo
basePath = Path(os.getcwd())
PathList = list(basePath.glob('**/*.ipynb'))
notebooks = [os.path.abspath(i) for i in PathList]

print("Notebooks found")
for i in notebooks:print(i)

# nbconvert
c = get_config()
c.NbConvertApp.export_format = 'markdown'
c.MarkdownExporter.template_path = ['./scripts'] # point this to the location of the jekyll template file
c.MarkdownExporter.template_file = 'jekyll.tpl'

# convert all notebooks found
c.NbConvertApp.notebooks = notebooks

# customise the images output directory

c.NbConvertApp.output_files_dir = '../images/notebook_images/{notebook_name}'

#c.Application.verbose_crash=True

# modify this function to point the  images to a custom path
# the default for nbconvert is to create a directory {notebook_name}_files
# where the notebook is located
def jekyllpath(path):
    """
	Take the filepath of an image output by the ExportOutputProcessor
	and convert it into a URL we can use with Jekyll
	"""
    base = os.path.split(path)[1]
    return path.replace("..", "{{site.url}}{{site.baseurl}}")

c.MarkdownExporter.filters = {'jekyllpath': jekyllpath}
