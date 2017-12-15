import os
import fnmatch
import glob
from pathlib import Path
import io


from traitlets.config import Config
from nbconvert.preprocessors import ExtractOutputPreprocessor
from nbconvert import HTMLExporter

from bs4 import BeautifulSoup


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
    notebook_namefull = resources['metadata']['name'] + resources.get('output_extension')
    outdir_nb = resources['metadata']['path']
    notebook_name = resources['metadata']['name']
    outfile = os.path.join(outdir_nb, notebook_name)
    imgs_outdir = os.path.join(os.path.split(outdir)[0], '/images/notebook_images/', notebook_name)

    # write file
    with open(outfile, 'w') as fout:
        body = content.prettify(formatter='html')
        fout.write(body)

    items = resources.get('outputs', {}).items()
    for filename, data in items:
        dest = os.path.join(imgs_outdir,filename)
        path = os.path.dirname(dest)
        print(dest)


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