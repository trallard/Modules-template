import os
import fnmatch
import glob
from pathlib import Path


from traitlets.config import Config

import nbformat
import nbconvert
from nbconvert.preprocessors import ExtractOutputPreprocessor
from nbconvert import HTMLExporter

from bs4 import BeautifulSoup

notebook = '/Users/tania/Documents/Git_Repos/Modules-template/_Day1/Tutorial.ipynb'
my_notebook = nbformat.read(notebook, as_version=4)

# Instantiate the exporter. We use the `basic` template for now; we'll get into more details
# later about how to customize the exporter further.
html_exporter = HTMLExporter()
html_exporter.template_file = 'basic'

# 3. Process the notebook we loaded earlier
(body, resources) = html_exporter.from_notebook_node(my_notebook)

print(body[:400] + '...')
print(resources.keys())


def find_notebooks():
    """ Find all the notebooks in the repo, but excludes those
    in the _site folder, this will be default if no specific
    notebook was passed for conversion """

    basePath = Path(os.getcwd())
    notebooksAll = [nb for nb in glob.glob('**/*.ipynb')]
    exception = os.path.join(basePath , '/_site/*/*')
    notebooks = [nb for nb in notebooksAll if not fnmatch.fnmatch(nb, exception)]
    return notebooks

def init_nb_resources(notebook_filename):
    """Step 1: Initialize resources
            This initializes the resources dictionary for a single notebook.
            Returns
            -------
            notebook_out: the directory to save the output files in
    """
    resources = {}
    basename = os.path.basename(notebook_filename)
    notebook_name = basename[:basename.rfind('.')]
    resources['unique_key'] = notebook_name
    return resources

def get_html_from_filepath(notebook_filename, resources):
    """Convert notebook to custom HTML"""
    config = Config()
    exporter = HTMLExporter(config = config,
                            template_file = 'basic',
                            preprocessors = [ExtractOutputPreprocessor],
                            filters = {'jekyllpath': jekyllpath})
    content, resources = exporter.from_filename(notebook_filename, resources = resources)
    content = parse_html(content)
    return content, resources

def parse_html(content):
    soup = BeautifulSoup(content, 'html.parser')
    soup.table['class'] = 'table-responsive table-striped'
    return soup


def jekyllpath(path):
    """
	Take the filepath of an image output by the ExportOutputProcessor
	and convert it into a URL we can use with Jekyll
	"""
    base = os.path.split(path)[1]
    return path.replace("..", "{{site.url}}{{site.baseurl}}")


def write_outputs(content, resources):
    """Step 3: Write the notebook to file
            This writes output from the exporter to file using the specified writer.
            It returns the results from the writer.
            Parameters
            ----------
            output :
            resources : dict
                resources for a single notebook including name, config directory
                and directory to save output
            Returns
            -------
            file
                results from the specified writer output of exporter
            """
    notebook_name = resources['metadata']['name'] + resources.get('output_extension')
    outdir = resources['metadata']['path']
    outfile = os.path.join(outdir, notebook_name)

    # write file
    with open(outfile, 'w') as fout:
        body = content.prettify(formatter='html')
        fout.write(body)



def convert_single_nb(notebook_filename):
    """Convert a single notebook.
            Performs the following steps:
                1. Initialize notebook resources
                2. Export the notebook to a particular format
                3. Write the exported notebook to file
            Parameters
            ----------
            notebook_filename : str
            """
    resources = init_nb_resources(notebook_filename)
    content, resources = get_html_from_filepath(notebook_filename, resources)
    write_outputs = write_nb(content, resources)
# -----

content, resources = get_html_from_filepath(notebook)