# notebooks/conf.py
project = "LAMTA Examples"
author = "OceanCruises"

extensions = [
    "myst_nb",
    "sphinx_book_theme",
    "sphinx_external_toc",
    "sphinx_design",
]

master_doc = "index"

# Increase execution timeout (apply for both config keys)
nb_execution_timeout = 300
mystnb_execution_timeout = 300

source_suffix = [".md", ".rst", ".ipynb"]

html_theme = "sphinx_book_theme"
external_toc_path = "_toc.yml"
