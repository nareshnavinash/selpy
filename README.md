# Se-Py Package

python3 -m pip install --user --upgrade setuptools wheel

python3 setup.py sdist bdist_wheel

python3 -m twine upload -u <username> -p <password> --repository-url https://upload.pypi.org/legacy/ dist/* --verbose
