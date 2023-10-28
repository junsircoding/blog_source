# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = '小骏的博客'
copyright = '2023, 小骏'
author = '小骏'
# release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.duration',
    "sphinxcontrib.video",
    'sphinx_charts.charts',
    "sphinx_comments",
    "sphinx_sitemap"
]

templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CN'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
# html_theme = 'sphinx_rtd_theme'
# html_theme = 'sphinxdoc'
html_theme = 'sphinx_book_theme'
# html_theme = 'furo'
html_logo = '_static/avatar_circle.png'
html_baseurl = 'https://junsircoding.github.io/'
html_show_sphinx = False
html_static_path = ['_static']
html_favicon = '_static/favicon.ico'
comments_config = {
   "utterances": {
      "repo": "junsircoding/blog_comments",
      "optional": "config",
   }
}

html_theme_options = {
"navigation_with_keys":True    
}

