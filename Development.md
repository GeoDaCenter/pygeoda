

## Deployment


Pygeoda for windows is built using Appveyor (see: appveyor.yml)

Pygeoda for Linux and Mac OSX is built using Travis (see .travis.yml)

For conda-forge, the pygeoda PyPI package is used as the source. So, when 
updating pygeoda PyPI package, the conda-forge package should be 
automatically updated.

1. Fork conda-forge/staged-recipes
2. Create a new branch from the master branch
3. Add meta.yaml in the recipes/pygeoda/ directory
4. Submit a pull request (This will trigger testing on all operating systems)
5. Once merged, the package will be built and uploaded to conda-forge