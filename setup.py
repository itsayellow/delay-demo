# setup for datadiary

import sys
from setuptools import setup, find_packages

# here = os.path.abspath(os.path.dirname(__file__))

setup(
    name="delay-demo",
    version="0.1.0",
    description="entry point makes a delay until the user Ctrl-C's it.",
    author="Matthew A. Clapp",
    author_email="itsayellow+dev@gmail.com",
    url="https://github.com/itsayellow/delay-demo",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
    entry_points={"console_scripts": ["delay-demo=delay_demo.main:cli"]},
    python_requires=">=3.6",
)
