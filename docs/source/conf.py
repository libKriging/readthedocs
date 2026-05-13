# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'libKriging'
copyright = 'Apache License'
author = 'libKriging team'

release = '1.0'
version = '1.0.0'

# -- General configuration

extensions = [
    'myst_parser',
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinxcontrib.bibtex',
    'sphinxcontrib.katex',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

bibtex_bibfiles = ['libKriging.bib']

# -- Options for EPUB output
epub_show_urls = 'footnote'

myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist"
]

# -- added by Yves
 
import sphinxcontrib.katex as katex

latex_macros = r"""
    \def \m            #1{\mathbf{#1}}
    \def \bs           #1{\boldsymbol{#1}}
    \def \LInv         #1{#1^\star}
    \def \LInvT        #1{#1^{\star\top}}
    \def \LInvHat      #1{\widehat{#1}^{\star}}
    \def \LInvHatT     #1{\widehat{#1}^{\star\top}}
    \def \RInv         #1{#1^\circ}
    \def \RInvT        #1{#1^{\circ\top}}
    \def \RInvHat      #1{\widehat{#1}^{\circ}}
    \def \RInvHatT     #1{\widehat{#1}^{\circ\top}}
    \def \LRInv        #1{#1^{\star\circ}}
    \def \LRInvT       #1{#1^{\star\circ\top}}
    \def \tr           #1{#1^{\top}}
    \def \corr         #1{\mathring{#1}}
    \def \corrinv      #1{\mathring{#1}^{-1}}
    \def \Esp          #1{\mathbb{E}}
    \def \Cov          #1{\textrm{Cov}}
    \def \Corr         #1{\textrm{Corr}}
    \def \Var          #1{\textrm{Var}}
    \def \New          #1{#1_{\texttt{n}}}
    \def \Old          #1{#1_{\texttt{o}}}
    \def \Upd          #1{#1_{\texttt{u}}}
    \def \tnew         #1{\texttt{n}}
    \def \told         #1{\texttt{o}}
    \def \tsim         #1{\texttt{sim}}
    \def \tupd         #1{\texttt{u}}
    \def \NewOld       #1{#1_{\texttt{n},\texttt{o}}}
    \def \NewNew       #1{#1_{\texttt{n},\texttt{n}}}
    \def \OldOld       #1{#1_{\texttt{o},\texttt{o}}}
    \def \OldNew       #1{#1_{\texttt{o},\texttt{n}}}
    \def \OldSim       #1{#1_{\texttt{o},\texttt{s}}}
    \def \SimOld       #1{#1_{\texttt{s},\texttt{o}}}
    \def \NewSim       #1{#1_{\texttt{n},\texttt{s}}}
    \def \SimNew       #1{#1_{\texttt{s},\texttt{n}}}
    \def \SimSim       #1{#1_{\texttt{s},\texttt{s}}}
    \def \OldUpd       #1{#1_{\texttt{o},\texttt{u}}}
    \def \UpdOld       #1{#1_{\texttt{u},\texttt{o}}}
    \def \UpdSim       #1{#1_{\texttt{u},\texttt{s}}}
    \def \SimUpd       #1{#1_{\texttt{s},\texttt{u}}}
    \def \UpdUpd       #1{#1_{\texttt{u},\texttt{u}}}
    \def \UpdNew       #1{#1_{\texttt{u},\texttt{n}}}
    \def \NewUpd       #1{#1_{\texttt{n},\texttt{u}}}
"""

# Translate LaTeX macros to KaTeX and add to options for HTML builder
katex_macros = katex.latex_defs_to_katex_macros(latex_macros)
katex_options = 'macros: {' + katex_macros + '}'

# Add LaTeX macros for LATEX builder
latex_elements = {'preamble': latex_macros}
