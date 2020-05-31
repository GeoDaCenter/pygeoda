.. _install_ref:

.. currentmodule:: pygeoda

2 Installation
==============

Like GeoDa desktop software, pygeoda are avaiable to
different platforms including: Mac, Linux and Windows.


2.1 Mac
-------

If you are running Mac OSX, you should be able to install pygeoda using pip:
::

    pip install pygeoda

Otherwise, you can install pygeoda from source:
::

    pip install git+https://github.com/lixun910/pygeoda

For Mac users, the “Xcode Command Line Tools” needs to be
installed for installing pygeoda from source.
It is a free software provided by Apple, which can be installed
by using the following command in a terminal:
::

    xcode-select --install



2.2 Windows
-----------

Please download installers from the release page
https://github.com/lixun910/pygeoda/releases/tag/v0.0.3
for Python 2.7 (32bit and 64bit) and Python 3.7 (32bit and 64bit).

Or, you can install pygeoda from source using pip:
::

    pip install git+https://github.com/lixun910/pygeoda


.. note::
    Install pygeoda on windows from source code requires either visual studio or mingw.

2.3 Linux
---------

If you are running Ubuntu systems (18.04 Bionic), you should
be able to install pygeoda using pip:
::

    pip install pygeoda

Otherwise, please install pygeoda from source:
::

    pip install git+https://github.com/lixun910/pygeoda

For Linux users, the “Build Essential Tools” needs to be installed first:
::

    sudo apt-get update
    sudo apt-get install build-essential

2.4 Import pygeoda 
------------------

If everything installed without error, you should be able to load pygeoda:
::

    import pygeoda
