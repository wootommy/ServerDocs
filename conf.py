"""
FilePath: /conf.py
LastEditTime: 2020-11-14 20:50
Author: tommy
Description: Config file for sphinx project.
"""
# global ref:
# https://github.com/readthedocs/recommonmark/blob/master/docs/conf.py

# -------------------------------- Path setup -------------------------------- #

import sphinx_rtd_theme
import recommonmark
from recommonmark.transform import AutoStructify

# ---------------------------- Project information --------------------------- #

project = "NaMI Server Docs"
copyright = "2020, nami-442"
author = "nami-442@tommy"

# --------------------------- General configuration -------------------------- #

extensions = [
    "sphinx_rtd_theme",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.mathjax",
    "recommonmark",
]
master_doc = "index"
exclude_patterns = ["_build"]

# -------------------------- Options for HTML output ------------------------- #
# ref: https://sphinx-rtd-theme.readthedocs.io/en/latest/configuring.html#

html_theme = "sphinx_rtd_theme"
html_theme_options = {
    # toc options
    "navigation_depth": 3,
    "includehidden": True,
    "titles_only": False,
    # display options
    "display_version": False,
    "style_external_links": True,
}
html_logo = None
html_favicon = None
html_last_updated_fmt = "%b %d, %Y"
html_show_sphinx = False
html_baseurl = "./files"

# ------------------------- Options for AutoStructify ------------------------ #

# At the bottom of conf.py
# github_doc_root = 'https://github.com/rtfd/recommonmark/tree/master/doc/'
def setup(app):
    app.add_config_value(
        "recommonmark_config",
        {
            "enable_auto_toc_tree": True,
            "auto_toc_tree_section": "Contents",
            # "enable_auto_doc_ref": True,
            "enable_math": True,
            "enable_inline_math": True,
            "enable_eval_rst": True,
            # "url_resolver": lambda url: github_doc_root + url,
        },
        True,
    )
    app.add_transform(AutoStructify)
