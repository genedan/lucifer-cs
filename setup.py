import setuptools

from lucifer.constants import BUILD_VERSION

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lucifer-cs",
    version=BUILD_VERSION,
    author="Gene Dan",
    author_email="genedan@gmail.com",
    description="Lucifer Claim Simulator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/genedan/lucifer-cs",
    project_urls={
        "Documentation": "https://genedan.com/lucifer-cs/docs"
    },
    install_requires=['chainladder'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires='>=3.11.0',
)