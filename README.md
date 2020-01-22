# Selpy

Selpy module is to have all the common methods that will be used in functional UI automation in Page Object Model. Selpy also powered to have snapshot feature that will save the data from UI to a file if needed. This in turn reduces the test data maintenance efforts.


[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](LICENSE)
[![Made with Python](https://img.shields.io/badge/Made%20with-Python-yellow.svg)](https://www.python.org/)
[![StackOverflow](http://img.shields.io/badge/Stack%20Overflow-Ask-blue.svg)]( https://stackoverflow.com/users/10505289/naresh-sekar )
[![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg)](CONTRIBUTING.md)
[![email me](https://img.shields.io/badge/Contact-Email-green.svg)](mailto:nareshnavinash@gmail.com)


![alt text](selpy/selpy_module.png)

## Installation

Add this line to your application's requirements.txt file:

```
selpy==<version>
```

And then execute:

```
pip3 install -r requirements.txt
```

Or install it yourself as:

```
pip3 install selpy
```

## Usage

This module is built to replace the library methods in [Selpy-Python](https://github.com/nareshnavinash/Selpy-Python/) framework. This allows us to share the methods among different teams and completely ignore the repetitive work. For more details on Page object model for functional UI automation verify [Selpu Python Documentation](https://nareshnavinash.github.io/Selpy-Python/) page.

### Adding new methods

Add all the new methods inside `/selpy/` path and add import the class inside `__init__.py` file in the same path so that the newly added class can be imported by using this module.

### Require and Include

To import this module use,
```
import selpy
```
To import specific class in this module use,
```
from selpy.driver import Driver
```

## Detailing the module

### Driver

Driver file holds all the common actions that are executed by the driver. Initiate the driver by,
```
driver = Driver()
```
The `driver` will hold the selenium webdriver object.

For configuring the driver capabilities, one has to specify the details in the global_data.yml in [Selpy-Python](https://github.com/nareshnavinash/Selpy-Python/).

### Locator

This class is to declare the selenium locators in Page Object Model. You can declare the locators as follows,

```
class AmazonHomePageLocator:
    # Static locators
    amazon_logo = Locator("css selector", "div#nav-logo a[aria-label='Amazon']")
    amazon_search_categories = Locator("css selector", "div.nav-search-scope select.nav-search-dropdown")

    def __init__(self):
        print("Locators for Amazon home page")
    
    # Dynamic locators
    @staticmethod
    def amazon_search_category_list(string):
        return Locator("xpath", "//select[contains(@class,'nav-search-dropdown')]//option[text()='%s']" % string)
```

To use the Locator method we need to pass the type of locator and the actual locator element. Type of locator has to be mentioned in the following way to allow `selpy` to process the locator.

```
CSS - 'css selector'
XPATH - 'xpath'
ID - 'id'
NAME - 'name'
LINK TEXT - 'link text'
PARTIAL LINK TEXT - 'partial link text'
TAG NAME - 'tag name'
CLASS NAME - 'class name'
``` 

### Store

This class is to store the run time configurations for this module. Kind of a memcached or redis for our framework. Centralized run time data which are needed by other modules are being stored here and retrived by other modules.

### Variable

This is where the actual snap feature logic is present. In order to save the UI data in to the dynamic file one has to run the tests with,

```
snap=1 pytest
``` 
But, only this will not ensure the data is getting saved in to dynamic file. One has to script their automation code in such a way that snap feature is supported. For example one can look in to [Selpy-Python](https://github.com/nareshnavinash/Selpy-Python/) framework inside `Tests/amazon.py`

Upon running the tests in normal mode `pytest` the dynamic data will not be overridden rather it will assert the data present in UI with the dynamic data file.

To get this feature running smoothly and to access the variables in smoother way, one has to configure the following params in their framework in `pytest_configure` method (so that these path variables will be set on initiating the pytest).

```
from selpy.store import Store

def pytest_configure(config):
    # Configuring the selpy with data path location
    Store.global_data_path = os.path.dirname(os.path.abspath(__file__)).replace("/Tests", "") + '/Data/GlobalData/global_data.yml'
    Store.static_data_path = os.path.dirname(os.path.abspath(__file__)).replace("/Tests", "") + '/Data/TestData/'
    Store.dynamic_data_path = os.path.dirname(os.path.abspath(__file__)).replace("/Tests", "") + '/Data/DynamicData/'
``` 

## To publish a module in pypi

1. Install the following dependencies
```
python3 -m pip install --user --upgrade setuptools wheel
```
2. In the root directory of your newly created module run,
```
python3 setup.py sdist bdist_wheel
```
3. Then add the username and password and upload to the pypi server,
```
python3 -m twine upload -u <username> -p <password> --repository-url https://upload.pypi.org/legacy/ dist/* --verbose
```
Ensure that you have deleted the old files from your dist directory.


## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/nareshnavinash/selpy/. This project is intended to be a safe, welcoming space for collaboration, and contributors are expected to adhere to the [Contributor Covenant](http://contributor-covenant.org) code of conduct.

## Authors

* **[Naresh Sekar](https://github.com/nareshnavinash)**

## License

The gem is available as open source under the terms of the [GPL-3.0 License](https://opensource.org/licenses/GPL-3.0).

## Code of Conduct

Everyone interacting in the Teber project’s codebases, issue trackers, chat rooms and mailing lists is expected to follow the [code of conduct](https://github.com/nareshnavinash/Teber-Gem/blob/master/CODE_OF_CONDUCT.md).
