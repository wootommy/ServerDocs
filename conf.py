# -- Path setup --------------------------------------------------------------

import sphinx_rtd_theme


# -- Project information -----------------------------------------------------

project = "Ubuntu Server Notes"
copyright = "2020, nami-442"
author = "nami-442"


# -- General configuration ---------------------------------------------------

extensions = ["sphinx_rtd_theme", "recommonmark"]
templates_path = ["_templates"]
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]

