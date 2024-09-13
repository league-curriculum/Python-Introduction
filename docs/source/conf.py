# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import sys
import os 

import logging

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

logger.setLevel(logging.INFO)

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from preprocess import replace_python, generate_trinket_iframe

project = 'Python-Introduction'
copyright = '2024, The League'
author = 'Eric Busboom'

html_title = 'Introduction to Python '
html_logo = 'https://images.jointheleague.org/logos/logo4.png'
# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


extensions = [
    'sphinx.ext.githubpages',
    'myst_parser',
    'sphinx_togglebutton',
    'sphinx_design'
]

myst_enable_extensions = [
    "amsmath",
    "attrs_inline",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]

source_suffix = ['.rst', '.md']

templates_path = ['_templates']
exclude_patterns = []

html_last_updated_fmt = '%b %d, %Y %H:%M'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo' # 'alabaster'
html_static_path = ['_static']

html_css_files = [
    'css/custom.css',
]

html_extra_path = ['html', 'images']


def source_read_handler(app, docname, source):
    # Only preprocess Markdown files
    try:

        # Your preprocessing logic here
        content = source[0]

        def f(content, height):

            return generate_trinket_iframe(content, width=700, height=height, embed_type='python')
    
        source[0], code  =  replace_python(content, 'python', f)
       
    except Exception as e:
        logger.error(f"Error processing {docname}: {e}")
    
def setup(app):
    app.connect('source-read', source_read_handler)