

## Setup Development Enviroment 

### Windows

#### Build for Python 3.7 

* Download and install Visual studio 2017

* Start a terminal using Visual Studio 2017 menu: "X64 native tools command prompt"



## Clone pygeoda repository

The repository  is at https://gitee.com/lixun910/pygeoda

You can clone it using command lines:

```
git clone https://gitee.com/lixun910/pygeoda
cd pygeoda
git submodule update --init --recursive
```

Note: The last command will get the submodules "libgeoda_src" and "pygeoda_boost"

## Build pygeoda

* Build pygeoda c++ wrapper  and test it
```
cd pygeoda
python setup.py build_ext --inplace
```

To install
```
python setup.py install
````

* Create binary (windows installer or pip wheels)
```
python setup.py bdist_wheel
```

For windows:
```
python setup.py bdist_wininst
```

#### Build for Python  2.7 (32-bit)

* Download Visual C++ Compiler for Python 2.7 from http://www.microsoft.com/en-us/download/details.aspx?id=44266

* Install it, the full path of vcvarsall.bat is at

```
C:\Users\UserName\AppData\Local\Programs\Common\Microsoft\Visual C++ for Python\9.0\vcvarsall.bat
```

* Modify find_vcvarsall(version) function in Python27\Lib\distutils\msvc9compiler.py

```python
def find_vcvarsall(version):
    productdir= "C:/Users/UserName/AppData/Local/Programs/Common/Microsoft/Visual C++ for Python/9.0"
    vcvarsall = os.path.join(productdir, "vcvarsall.bat")
    if os.path.isfile(vcvarsall):
        return vcvarsall
    else:
        return None
```


