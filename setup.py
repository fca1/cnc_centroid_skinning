import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="cnc_centroid_skinning",
    version="1.0.1",
    description="wrapper for the CncSkinning API (C#) 64 bits",
    long_description=open('README.md').read(),
    url="https://github.com/fca1/cnc_centroid_skinning/",
    project_urls={
        "Documentation": "https://htmlpreview.github.io/?https://github.com/fca1/cnc_centroid_skinning/blob/master/cnc_centroid_skinning/doc/cnc_centroid_skinning/index.html",
        "Source Code": "https://github.com/fca1/cnc_centroid_skinning/tree/master/cnc_centroid_skinning/cnc_centroid_skinning/",
    },
    long_description_content_type="text/markdown",
    author="Frantz Capiez",
    author_email="cnc@epi-rf.fr",
    license="Mit",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.12",
        "Operating System :: Microsoft :: Windows :: Windows 11",
        "Topic :: Software Development :: Libraries",
    ],
    packages=find_packages(exclude=("tests","examples")),
    include_package_data=True,
    install_requires=["pythonnet", "pycparser"],
    entry_points={
        "console_scripts": [
            "realpython=cnc_centroid_skinning.detect_cnc",
        ]
    },
)
