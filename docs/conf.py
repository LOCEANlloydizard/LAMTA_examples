# docs/conf.py
project = "LAMTA Examples"
author = "OceanCruises"

extensions = [
    "myst_parser",
    "nbsphinx",
]


# Allow Markdown files
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

master_doc = "index"

html_theme = "sphinx_rtd_theme"
