#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: trallard

This code is used to generate Jekyll blogpost from Jupyter notebooks
within a main Jekyll repository. This uses the library 'nbconvert-jekyll'.

Since the templates are given in this package there is no need to specify a custom template.
"""

# Import libraries
import fnmatch
import glob
import os
from pathlib import Path


try:
    from urllib.parse import quote  # Py 3
except ImportError:
    from urllib2 import quote  # Py 2


# ---------------------------------------

def find_notebooks():
    """ Find all the notebooks in the repo, but excludes those
    in the _site folder"""

    basePath = Path(os.getcwd())
    notebooksAll = [nb for nb in glob.glob('**/*.ipynb')]
    exception = str(basePath) + '/_site/*/*'
    notebooks = [nb for nb in notebooksAll if not fnmatch.fnmatch(nb, exception)]
    return notebooks


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


# ---------------------------------------
notebooks = find_notebooks()
# check if the list is empty
if not notebooks:
    print("No notebook found in this repository \n")
else:
    for nb in notebooks:
        print(" ***** Notebook found: {} \n)".format(nb))

"""Converting  notebooks now: this uses nbconvert with
a custom generated template"""

c = get_config()
c.NbConvertApp.export_format = 'md_jk'
c.Exporter.preprocessors = ['nbconvert.preprocessors.ExtractOutputPreprocessor']


scriptsPath = os.path.join(os.getcwd(), 'scripts')

# Uncomment if you want to pass a custom template
#c.MarkdownExporter.template_path = [scriptsPath]  # point this to the location of the jekyll template file
#c.MarkdownExporter.template_file = 'jekyll_html'

# convert all notebooks found
c.NbConvertApp.notebooks = notebooks

# customise the images output directory
c.NbConvertApp.output_files_dir = '../images/notebook_images/{notebook_name}'

# c.Application.verbose_crash = True

c.JekyllExporter.filters = {'jekyllpath': jekyllpath}
