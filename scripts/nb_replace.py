#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 10:09:43 2017

@author: tania
"""

from os import remove, close
import re, glob, os, fnmatch
from shutil import move
from tempfile import mkstemp
from pathlib import Path



#---------------------------------------
def find_notebooks():
    """ Find all the notebooks in the repo previsouly converted to 
    markdown"""
    
    basePath = Path(os.getcwd())
    notebooksAll = [nb for nb in glob.glob('**/*.ipynb')]
    exception = str(basePath) + '/_site/*/*'
    notebooks = [nb for nb in notebooksAll if not fnmatch.fnmatch(nb, exception)]
    notebooks = [os.path.abspath(nb).replace('ipynb', 'md') for nb in notebooks]
    return notebooks


def replace(file_path):
    """ Replaces the expressions"""
    fh, abs_path = mkstemp()
    with open(abs_path,'w') as new_file:
        with open(file_path) as source_file:
            for line in source_file:
                if any(s in line for s in s_repl):
                    line_new = robj.sub(lambda m: rdict[m.group(0)], line)
                    line_new2 = quoteobj.sub(lambda m: rquote[m.group(0)], line_new)
                    new_file.write(line_new2)
                elif any(s in line for s in scope):
                    line_new = scopeobj.sub(lambda m: rscope[m.group(0)], line)
                    new_file.write(line_new)
                else:
                    new_file.write(line)
    new_file.close()
    #Remove original file
    remove(file_path)
    #Move new file
    move(abs_path, file_path)


# Replacement rules: needed to parse the html properly
rdict = {'class=': 'class="', '<table>':'<table class="table-responsive table-striped>'}
s_repl = {'class=', '<table>'}
robj = re.compile('|'.join(rdict.keys()))

rquote ={'>':'">' }
quoteobj= re.compile('|'.join(rquote.keys()))

rscope = {'scope=row':'scope="row"','scope=col':'scope="col"'}
scope = {'scope=row', 'scope=col'}
scopeobj = re.compile('|'.join(rscope.keys()))


notebooks = find_notebooks()
for nb in notebooks: replace(nb)
