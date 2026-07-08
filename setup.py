from setuptools import setup, find_packages

with open("README.md", encoding="utf-8") as readme:
    README = readme.read()


# This call to setup() does all the work
setup(
    name="cnc_centroid_skinning",
    version="1.5.42",
    description="wrapper for the CncSkinning API (C#) 64 bits",
    long_description=README,
    url="https://github.com/fca1/cnc_centroid_skinning/",
    project_urls={
        "Documentation": "https://htmlpreview.github.io/?https://github.com/fca1/cnc_centroid_skinning/blob/master/cnc_centroid_skinning/doc/cnc_centroid_skinning/index.html",
        "Source Code": "https://github.com/fca1/cnc_centroid_skinning/tree/master/cnc_centroid_skinning/cnc_centroid_skinning/",
    },
    long_description_content_type="text/markdown",
    author="Frantz Capiez",
    author_email="frantz.capiez@epi-rf.fr",
    license="MIT",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python :: 3.12",
        "Operating System :: Microsoft :: Windows :: Windows 11",
        "Topic :: Software Development :: Libraries",
    ],
    packages=find_packages(exclude=("tests", "examples")),
    python_requires=">=3.10",
    include_package_data=True,
    install_requires=["pythonnet", "pycparser"],
    entry_points={
        "console_scripts": [
            "detect-cnc=cnc_centroid_skinning.main.main:main",
        ]
    },
)
