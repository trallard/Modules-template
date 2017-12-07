# -*- coding: utf-8 -*-
"""
Custom Markdown template for Jekyll purposes
Adapted from the HTML / markdown Exporters
Distributed under the terms of the Modified BSD License.

"""

import os

from traitlets import default, Unicode
from traitlets.config import Config

from nbconvert.filters.highlight import Highlight2HTML
from nbconvert.filters.markdown_mistune import IPythonRenderer, MarkdownWithMath

from .templateexporter import TemplateExporter


class JekyllExporter(TemplateExporter):
    """
    Exports a basic HTML document.  This exporter assists with the export of
    HTML.  Inherit from it if you are writing your own HTML template and need
    custom preprocessors/filters.  If you don't need custom preprocessors/
    filters, just change the 'template_file' config option.
    """

    anchor_link_text = Unicode(u'¶',
                               help="The text used as the text for anchor links.").tag(config=True)

    @default('file_extension')
    def _file_extension_default(self):
        #return '.html'
        return '.md'

    @default('default_template_path')
    def _default_template_path_default(self):
        """ This will help to find the other templates
        could be useful if you're extending a given template"""
        return os.path.join("..", "templates", "html")

    @default('template_file')
    def _template_file_default(self):
        #return 'full.tpl'
        return  'markdown.tpl'

    output_mimetype = 'text/html'
    output_mimetype = 'text/markdown'

    @property
    def default_config(self):
        c = Config({
            'NbConvertBase': {
                'display_data_priority': ['application/vnd.jupyter.widget-state+json',
                                          'application/vnd.jupyter.widget-view+json',
                                          'application/javascript',
                                          'text/html',
                                          'text/markdown',
                                          'image/svg+xml',
                                          'text/latex',
                                          'image/png',
                                          'image/jpeg',
                                          'text/plain'
                                          ]
            },
            'CSSHTMLHeaderPreprocessor': {
                'enabled': True
            },
            'HighlightMagicsPreprocessor': {
                'enabled': True
            }
        })
        c.merge(super(HTMLExporter, self).default_config)
        return c

    def markdown2html(self, source):
        """Markdown to HTML filter respecting the anchor_link_text setting"""
        renderer = IPythonRenderer(escape=False,
                                   anchor_link_text=self.anchor_link_text)
        return MarkdownWithMath(renderer=renderer).render(source)

    def default_filters(self):
        for pair in super(HTMLExporter, self).default_filters():
            yield pair
        yield ('markdown2html', self.markdown2html)

    def from_notebook_node(self, nb, resources=None, **kw):
        langinfo = nb.metadata.get('language_info', {})
        lexer = langinfo.get('pygments_lexer', langinfo.get('name', None))
        self.register_filter('highlight_code',
                             Highlight2HTML(pygments_lexer=lexer, parent=self))
        return super(HTMLExporter, self).from_notebook_node(nb, resources, **kw)