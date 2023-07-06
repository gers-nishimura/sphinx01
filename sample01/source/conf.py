# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# Below is to reduce font size in code block
# \tiny         5pt
# \scriptsize   7pt
# \footnotesize 8pt
# \small        9pt
#


from sphinx.highlighting import PygmentsBridge
from pygments.formatters.latex import LatexFormatter

class CustomLatexFormatter(LatexFormatter):
    def __init__(self, **options):
        super(CustomLatexFormatter, self).__init__(**options)
        self.verboptions = r"formatcom=\scriptsize"

PygmentsBridge.latex_formatter = CustomLatexFormatter

# for jupyter-notebook

from recommonmark.parser import CommonMarkParser

source_parsers = {
    '.md': CommonMarkParser,
}

from recommonmark.transform import AutoStructify

github_doc_root = 'https://github.com/rtfd/recommonmark/tree/master/doc/'
def setup(app):
    app.add_config_value('recommonmark_config', {
            'url_resolver': lambda url: github_doc_root + url,
            'auto_toc_tree_section': 'Contents',
            }, True)
    app.add_transform(AutoStructify)


# -- Project information -----------------------------------------------------

project = 'Sphinx勉強会'
copyright = '2023, ERS西村'
author = 'ERS西村'

# The full version, including alpha/beta/rc tags
release = '1.0.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.mathjax',
    'sphinxcontrib.blockdiag',
    'sphinxcontrib.actdiag',
    'sphinx.ext.graphviz',
    'nbsphinx',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'ja'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

source_suffix = ['.rst', '.md']

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'alabaster'

import sphinx_rtd_theme
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
'papersize': 'a4paper',

# The font size ('10pt', '11pt' or '12pt').
'pointsize': '12pt',


# geometry
'geometry': '\\usepackage[vmargin=2cm, hmargin=2cm]{geometry}',
#babel
'babel': '\\usepackage[japanese]{babel}',

# Additional stuff for the LaTeX preamble.
#\\usepackage[top=20truemm,bottom=20truemm,left=20truemm,right=20truemm]{geometry}

'preamble': r'''

\setlength\parindent{1zw}
\renewcommand{\baselinestretch}{0.8}

\usepackage[version=4]{mhchem}
\usepackage{siunitx}
\usepackage{chemfig}

\makeatletter
\renewcommand{\maketitle}{
\begin{center}
    {\Large \@title} \par
\end{center}
\begin{flushright}
    \@date \hspace{3zw} \@author \par
\end{flushright}
}

\@addtoreset{equation}{section} \def\theequation{\thesection.\arabic{equation}}

\makeatother

\pagestyle{plain}
\thispagestyle{plain}

'''
}

latex_elements['tableofcontents'] = r'''
\pagenumbering{arabic} % page numbering as arabic
\pagestyle{normal} % page set to normal
'''

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
# latex_documents = [
#     (master_doc, 'output.tex', u'NewTitle',
#     u'Fujisawa', 'howto'),
# ]

# Numbering tables and figures
numfig=True
numfig_secnum_depth=2