# used to replace the needed headings within the exported notebooks


from os import remove, close
import re, glob, os
from shutil import move
from tempfile import mkstemp

## replacements needed to be done at various levels to allow for HTMl rendering
rdict = {'class=': 'class="', '<table>':'<table class="table-responsive table-striped>'}
s_repl = {'class=', '<table>'}
robj = re.compile('|'.join(rdict.keys()))

rquote ={'>':'">' }
quoteobj= re.compile('|'.join(rquote.keys()))

rscope = {'scope=row':'scope="row"','scope=col':'scope="col"'}
scope = {'scope=row', 'scope=col'}
scopeobj = re.compile('|'.join(rscope.keys()))

#replace the expressions that are not correcly parsed
def replace(file_path):
    #Create temp file
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


# find all the notebooks in the dir
def locate(nb_dir):
    abs_path = os.path.join('.', nb_dir, '*.md')
    notebooks = glob.glob(abs_path)
    return(notebooks)


notebooks = locate('notebooks')
for nb in notebooks: replace(nb)
