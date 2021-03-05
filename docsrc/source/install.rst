.. _install_ref:

.. currentmodule:: pygeoda

2 Installation
==============

Like GeoDa desktop software, pygeoda are avaiable to
different platforms including Mac, Linux, and Windows. 
You can install pygeoda using pip:
::

    pip install pygeoda


To install pygeoda from source:

2.1 Windows
-----------

For Windows users, Microsoft Visual C++ needs to be installed first. 
Please see https://wiki.python.org/moin/WindowsCompilers to find which Visual 
C++ compiler to use with a specific python version.

Install pygeoda from source using pip:
::

    pip install git+https://github.com/GeoDaCenter/pygeoda

2.2 Linux
---------

For Linux users, the “Build Essential Tools” needs to be installed first:
::

    sudo apt-get update
    sudo apt-get install build-essential

Install pygeoda from source using pip:
::

    pip install git+https://github.com/GeoDaCenter/pygeoda

2.3 Mac
-------

For Mac users, the “Xcode Command Line Tools” needs to be
installed for installing pygeoda from source.
It is a free software provided by Apple, which can be installed
by using the following command in a terminal:
::

    xcode-select --install

Install pygeoda from source using pip:
::

    pip install git+https://github.com/GeoDaCenter/pygeoda

2.4 Import pygeoda 
------------------

If everything installed without error, you should be able to import pygeoda in Python:
::

    import pygeoda
