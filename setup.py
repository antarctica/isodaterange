import os
from setuptools import setup

setup(
    name             = "isodaterange",
    version          = "1.0.0",
    author           = "Tim Barnes",
    author_email     = "tdba@bas.ac.uk",
    url              = "https://gitlab.data.bas.ac.uk/uk-pdc/utils/isodaterange",
    packages         = ["isodaterange"],
    install_requires = [
        "isodate"
    ]
)
