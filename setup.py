# Installation script for python
import os
import re

from setuptools import find_packages, setup
from setuptools.command.install import install

PACKAGE = "qibojit"


# Returns the version
def get_version():
    """Gets the version from the package's __init__ file
    if there is some problem, let it happily fail"""
    VERSIONFILE = os.path.join("src", PACKAGE, "__init__.py")
    initfile_lines = open(VERSIONFILE).readlines()
    VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
    for line in initfile_lines:
        mo = re.search(VSRE, line, re.M)
        if mo:
            return mo.group(1)


# load long description from README
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name=PACKAGE,
    version=get_version(),
    description="Simulation tools based on numba and cupy.",
    author="The Qibo team",
    author_email="",
    url="https://github.com/qiboteam/qibojit",
    packages=find_packages("src"),
    package_dir={"": "src"},
    package_data={"": ["*.cc"]},
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Physics",
    ],
    install_requires=["numba>=0.51.0", "scipy", "psutil", "qibo>=0.1.13"],
    extras_require={
        "tests": ["pytest"],
    },
    python_requires=">=3.8.0",
    long_description=long_description,
    long_description_content_type="text/markdown",
)
