# notebooks/conf.py
project = "LAMTA Examples"
author = "OceanCruises"

extensions = [
    "myst_nb",            # handles .ipynb + MyST
    "sphinx_book_theme",
    "sphinx_external_toc",
    "sphinx_design",
]

master_doc = "index"

# Important: use a LIST (or remove entirely), do NOT map ".md" in a dict
source_suffix = [".md", ".rst", ".ipynb"]

html_theme = "sphinx_book_theme"
external_toc_path = "_toc.yml"
