import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="selpy", # Replace with your own username
    version="0.0.1",
    author="Naresh Sekar",
    author_email="nareshnavinash@gmail.com",
    description="Package to hold driver and locator methods for selenium",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nareshnavinash/SePy-Module",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
