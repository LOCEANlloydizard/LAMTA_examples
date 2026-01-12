# notebooks/conf.py
project = "LAMTA Examples"
author = "OceanCruises"

extensions = [
    "myst_nb",
    "sphinx_book_theme",
    "sphinx_external_toc",
    "sphinx_design",
    "sphinxcontrib.datatemplates",
]

templates_path = ["_templates"]

myst_enable_extensions = ["colon_fence"]

nb_execution_mode = "off"
nb_execution_timeout = -1

source_suffix = [".md", ".rst", ".ipynb"]

html_theme = "sphinx_book_theme"
external_toc_path = "_toc.yml"
