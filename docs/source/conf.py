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

html_js_files = [
    'js/custom.js',
]

html_extra_path = ['html', 'images']



html_theme_options = {
    "footer_icons": [
        {
            "name": "GitHub",
            "url": "https://github.com/league-curriculum/Python-Introduction",
            "html": """
                <svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 16 16">
                    <path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"></path>
                </svg>
            """,
            "class": "",
        },
    ],
}
def source_read_handler(app, docname, source):
    """Convert Python code blocks to Trinket iframes"""
    # Only preprocess Markdown files
    try:

        # Your preprocessing logic here
        content = source[0]

        def f(content, height, width):

            return generate_trinket_iframe(content, width=width, height=height, embed_type='python')
    
        source[0], code  =  replace_python(content, 'python', f)
       
    except Exception as e:
        logger.error(f"Error processing {docname}: {e}")
    
def setup(app):
    app.connect('source-read', source_read_handler)
    
    
if __name__ == '__main__':
    """Test the source_read_handler"""
    # Read module0/010_meet-tina.md into a string, using pathlib
    from pathlib import Path
    d = Path(__file__).parent
    content = (d/'module0/010_meet-tina.md').read_text()
    
    c = [content]
    r = source_read_handler(None, 'module0/010_meet-tina.md', c)
    print(c[0])
    