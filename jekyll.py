# This is used to generate Jekyll blog posts from Jupyter notebooks for R codes.
# Following the instruction at http://christop.club/2014/02/21/blogging-with-ipython-and-jekyll/

try:
    from urllib.parse import quote  # Py 3
except ImportError:
    from urllib2 import quote  # Py 2
import os, sys, glob

# ------------------------------
# converting one notebook at a time
# Usage example: jupyter nbconvert  --config jekyll.py <notebok.ipynb>
f = None
for arg in sys.argv:
    if arg.endswith('.ipynb'):
        f = arg.split('.ipynb')[0]
        break
#------------------------------------

#------------------------------------
# converting all the notebooks in a specified directory
# Usage: jupyter nbconvert --config jekyll.py
# to convert just one uncomment this block and line 40
# finding all the notebooks in the specified dir
def locate(nb_dir):
    abs_path = os.path.join('.', nb_dir, '*.ipynb')
    notebooks = glob.glob(abs_path)
    return(notebooks)


notebooks = locate('notebooks')
#------------------------------------

c = get_config()
c.NbConvertApp.export_format = 'markdown'
c.MarkdownExporter.template_path = ['.'] # point this to the location of the jekyll template file
c.MarkdownExporter.template_file = 'jekyll'

# convert all notebooks found
c.NbConvertApp.notebooks = notebooks

#c.Application.verbose_crash=True

# modify this function to point the  images to a custom path
# by default this saves all images to a directory 'images' in the root of the blog directory
def path2support(path):
    """Turn a file path into a URL"""
    parts = path.split(os.path.sep)
    return '{{ site.url}}{{ site.baseurl }}/notebooks/' + '/'.join(quote(part) for part in parts)
#return '../assets/img/notebook_images/' + os.path.basename(path)

c.MarkdownExporter.filters = {'path2support': path2support}

if f:
    c.NbConvertApp.output_base = f.lower().replace(' ', '-')
    #c.FilesWriter.build_directory = '../_drafts/' # point this to your build directory
    c.FilesWriter.build_directory = os.path.join(os.getcwd(), 'notebooks/')
