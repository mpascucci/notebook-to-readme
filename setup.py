import setuptools
import os

with open(os.path.join(os.path.split(__file__)[0], "README.md"), "r") as fh:
    long_description = fh.read()

python_dir = os.path.dirname(__file__)

CLASSIFIERS = [
    "Programming Language :: Python",
    "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    "Operating System :: OS Independent"
]

ENTRYPOINTS = dict(
    console_scripts = ['nb2md=nb2md.notebook2markdown:main','notebook_preview=nb2md.notebook2markdown:preview']
)

setuptools.setup(
    name="notebook to readme",
    version='0.1',
    description="easily convert jupyter notebooks into markdown README",
    author="Marco Pascucci",
    author_email="marpas.paris@gmail.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mpascucci/notebook-to-readme",
    packages=setuptools.find_packages(),
    install_requires=['nbconvert', 'nbformat'],
    classifiers=CLASSIFIERS,
    extras_require={},
    entry_points=ENTRYPOINTS,
)
