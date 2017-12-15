import os
import nbconvert
import nbformat

from traitlets.config import Config

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

def get_html_from_filepath(filepath):
    """Convert notebook to custom HTML"""
    config = Config()
    exporter = HTMLExporter(config = config,
                            template_file = 'basic',
                            preprocessors = [ExtractOutputPreprocessor],
                            filters = {'jekyllpath': jekyllpath})
    content, info = exporter.from_filename(filepath)
    content = parse_html(content)
    return content, info

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
