project = 'junsircoding\'s blog'
copyright = '2023, junsircoding'
author = '小骏'
# release = '0.1'

extensions = [
   'sphinx.ext.duration',
   "sphinxcontrib.video",
   'sphinx_charts.charts',
   "sphinx_comments",
   "sphinx_sitemap",
   'sphinxemoji.sphinxemoji',
   'notfound.extension',
]

templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CN'

sitemap_url_scheme = "{link}"

# html_theme = 'alabaster'
# html_theme = 'sphinxdoc'
# html_theme = 'sphinx_book_theme'
# html_theme = 'furo'
html_theme = 'sphinx_rtd_theme'
html_logo = '_static/logo.png'
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
github_url='https://github.com/junsircoding'

html_theme_options = {
   "navigation_with_keys":True,
   'analytics_id': 'G-KTSZ2L0J1T',
   'display_version': False,
   'style_external_links': False,
   'vcs_pageview_mode': '',
   'logo_only': True,
   'titles_only': False
}

sphinxemoji_style = 'twemoji'

# 不显示'显示页面源码'链接
html_show_sourcelink = False

notfound_context = {
   'title': '不存在这篇文章',
   'body': "<h1>不存在这篇文章。</h1>\n\n看看别的文章吧。"
}

notfound_urls_prefix = "/"
