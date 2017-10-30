#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 17:42:04 2017

@author: trallard
"""

# Import libraries 
from pathlib import posixpath, Path
import os, glob, fnmatch

try:
    from urllib.parse import quote  # Py 3
except ImportError:
    from urllib2 import quote  # Py 2



#---------------------------------------
    
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
    
#---------------------------------------    
notebooks = find_notebooks()
# check if the list is empty
if not notebooks:
    print ("No notebook found in this repository \n")
else:
    for nb in notebooks:
        print("Notebook found: {} \n)".format(nb))
    
"""Converting  notebooks now: this uses nbconvert with
a custom generated template"""

c = get_config()
c.NbConvertApp.export_format = 'markdown'

scriptsPath = os.path.join(os.getcwd(), 'scripts')

c.MarkdownExporter.template_path = [scriptsPath] # point this to the location of the jekyll template file
c.MarkdownExporter.template_file = 'jekyll'

# convert all notebooks found
c.NbConvertApp.notebooks = notebooks

# customise the images output directory
c.NbConvertApp.output_files_dir = '../images/notebook_images/{notebook_name}'

#c.Application.verbose_crash=True

c.MarkdownExporter.filters = {'jekyllpath': jekyllpath}

    
    
