

## Deployment

1. update libgeoda/
2. ./swig.sh
3. add test cases in pygeoda
4. add modules in pygeoda
5. local dev and test
6. pr

**deprecated**
Pygeoda for windows is built using Appveyor (see: appveyor.yml)

NOTE:

python 3.5.0 msc 1900 visual c++ 2015  msvc14.0 (vs2015)
(NOTE: python3.5 will not be supported on PyPi after 0.0.8-1)

python 3.6.1 msc 1900 visual c++ 2015  (!!as conda-forge, msvc14.1 for py36) (vs2017)
python 3.7.0 msc 1914 visual c++ 2017  msvc14.1 (vs2017)
python 3.8.1 msc 1916 visual c++ 2017  msvc14.1 (vs2017)
python 3.9.1 msc 1928 visual c++ 2019  msvc14.2  (vs2019)

Pygeoda for Linux and Mac OSX is built using Travis (see .travis.yml)

## Sphinx Doc

1. use venv
2. pip install -U sphinx
3. pip install matplotlib
4. goto docsrc/
5. make github

## conda-forge

For conda-forge, the pygeoda PyPI package is used as the source. So, when 
updating pygeoda PyPI package, the conda-forge package should be 
automatically updated.

1. Fork conda-forge/staged-recipes
2. Create a new branch from the master branch
3. Add meta.yaml in the recipes/pygeoda/ directory
4. Submit a pull request (This will trigger testing on all operating systems)
5. Once merged, the package will be built and uploaded to conda-forge