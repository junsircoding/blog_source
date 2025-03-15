import os
import datetime as dt
import jieba

# 设置 jieba 临时目录
conf_dir = os.path.dirname(os.path.abspath(__file__))
os.environ["TMPDIR"] = os.path.join(conf_dir, 'jieba_tmp')

project = '小骏不抬杠'
copyright = f'2023-{dt.datetime.now():%Y}, 小骏不抬杠'
author = '小骏'
# release = '0.1'

extensions = [
   'sphinx.ext.duration',
   'sphinxemoji.sphinxemoji',
   'notfound.extension',
   'sphinxnotes.strike',
   'sphinx_copybutton',
]

templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CN'

sitemap_url_scheme = "{link}"

# html_theme = 'alabaster'
# html_theme = 'sphinxdoc'
# html_theme = 'sphinx_book_theme'
# html_theme = 'furo'
# html_theme = 'sphinx_rtd_theme'
html_theme = 'python_docs_theme'
html_logo = '_static/logo.png'
html_baseurl = 'https://junsircoding.github.io/'
html_show_sphinx = False
html_static_path = ['_static']
html_favicon = '_static/favicon.ico'
github_url='https://github.com/junsircoding'

html_theme_options = {
   "navigation_with_keys":True,

   # python_docs_theme confs
   "root_url" : "https://junsircoding.github.io",
   "root_icon" : 'favicon.ico',
   "root_name":"首页",
   "root_icon_alt_text":"首页",
   "root_include_title":False,

   # sphinx_rtd_theme confs
   # 'analytics_id': 'G-KTSZ2L0J1T',
   # 'display_version': False,
   # 'style_external_links': False,
   # 'vcs_pageview_mode': '',
   # 'logo_only': True,
   # 'titles_only': False
}

# 不显示'显示页面源码'链接
html_show_sourcelink = False

notfound_context = {
   'title': '不存在这篇文章',
   'body': "<h1>不存在这篇文章。</h1>\n\n看看别的文章吧。"
}

notfound_urls_prefix = "/"

html_css_files = ["css/custom.css"]

html_js_files = [
    'js/custom.js',
    'js/back_to_top.js',
]

