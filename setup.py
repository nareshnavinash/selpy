import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

install_requires = [
    "selenium==3.141.0",
    "allure-pytest==2.8.6",
    "webdriver-manager==2.3.0"
]

setuptools.setup(
    name="selpy",
    version="0.1.0",
    author="Naresh Sekar",
    author_email="nareshnavinash@gmail.com",
    description="Package to hold driver and locator methods for selenium",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nareshnavinash/selpy",
    packages=setuptools.find_packages(),
    keywords = ['POM', 'Selenium_POM', 'Selenium_pytest_POM', 'Page_Object_Model'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Operating System :: OS Independent",
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Software Development :: Testing',
    ],
    python_requires='>=3.6',
    install_requires=install_requires
)
