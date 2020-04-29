#!/usr/bin/env python3
import sys, os, platform
import setuptools
from distutils.core import setup, Extension
from setuptools.command.develop import develop
from subprocess import check_call

###########################################################
# Utils for submodule
##########################################################
class update_submodules(develop):
    def run(self):
        if os.path.exists('.git'):
            check_call(['git', 'submodule', 'update', '--init', '--recursive'])
        develop.run(self)


###########################################################
# Variables 
##########################################################

OS_NAME = 'linux'

if sys.platform == "darwin":
    OS_NAME = 'osx'
    #os.environ['MACOSX_DEPLOYMENT_TARGET'] = '10.14'
    os.environ["ARCHFLAGS"] = "-arch x86_64"
elif sys.platform == "win32":
    if sys.maxsize > 2**32:
        OS_NAME = 'win64'
    else:
        OS_NAME = 'win32'
elif sys.platform == "linux2":
    OS_NAME = 'linux'

###########################################################
# INCLUDE_DIRS
###########################################################
INCLUDE_DIRS = []
if OS_NAME == 'win32' or OS_NAME == 'win64':
    INCLUDE_DIRS = [
        '..\\3rd_party\\boost_static\\include',
        '..\\libgeoda',
        '..\\src\\weights',
        '..\\src\\sa',
        '..\\src\\shape',
        '..\\src',
        '..\\postgeoda\\src',
        '..\\..\\eigen3',
    ]

else:
    INCLUDE_DIRS = [
        '../3rd_party/boost_static/include',
        '../libgeoda',
        '../src/weights',
        '../src/sa',
        '../src',
        '../postgeoda/src',
        '../../eigen3',
    ]


print(OS_NAME)
print(INCLUDE_DIRS)
###########################################################
# LIBRARIES and INCLUDE_DIRS
###########################################################
LIBRARY_DIRS = []
LIBRARIES = [] # -lxxx

if OS_NAME == 'win32' or OS_NAME == 'win64':
    LIBRARIES = ['comctl32','rpcrt4']

if OS_NAME == 'linux':
    LIBRARY_DIRS += ['/usr/lib', '/usr/lib/x86_64-linux-gnu']
    LIBRARIES = []
elif OS_NAME == 'osx':
    LIBRARY_DIRS += ['/usr/lib']
    LIBRARIES = ['curl', 'iconv']

###########################################################
# SWIG_OPTS and Compiler args
###########################################################
SWIG_OPTS = ['-c++']
EXTRA_COMPILE_ARGS = []

if OS_NAME == 'win32' or OS_NAME == 'win64':
    EXTRA_COMPILE_ARGS += [
        '/EHsc', #MSVC is not throwing exceptions and you need to enable it in your vcproj.
    ]
else:
    EXTRA_COMPILE_ARGS = [
        '-std=c++11',
    ]


###########################################################
#  Link args
###########################################################
EXTRA_LINK_ARGS = []

if OS_NAME == 'win32' or OS_NAME == 'win64':
    EXTRA_LINK_ARGS += ['/ignore:4229']

elif OS_NAME == 'osx':
    EXTRA_LINK_ARGS = []

###########################################################
#  Link objects 
###########################################################
EXTRA_OBJECTS = []

if OS_NAME == 'win32' or OS_NAME == 'win64':
    EXTRA_OBJECTS = [
        '..\\3rd_party\\boost_static\\lib\\' + OS_NAME + '\\libboost_thread-vc100-mt-1_57.lib',
        '..\\3rd_party\\boost_static\\lib\\' + OS_NAME + '\\libboost_system-vc100-mt-1_57.lib',
        '..\\3rd_party\\boost_static\\lib\\' + OS_NAME + '\\libboost_date_time-vc100-mt-1_57.lib',
        '..\\3rd_party\\boost_static\\lib\\' + OS_NAME + '\\libboost_chrono-vc100-mt-1_57.lib', 
    ]
else:
    EXTRA_OBJECTS = [
        '../3rd_party/boost_static/lib/' + OS_NAME + '/libboost_thread.a',
        '../3rd_party/boost_static/lib/' + OS_NAME + '/libboost_system.a',
        '../3rd_party/boost_static/lib/' + OS_NAME + '/libboost_date_time.a',
    ]

###########################################################
#  Source files
###########################################################
SOURCE_FILES  = [
    'pygeoda/libgeoda.cpp',
    '../src/SpatialIndAlgs.cpp',
    '../src/gda_sa.cpp',
    '../src/gda_data.cpp',
    '../src/gda_clustering.cpp',
    '../src/gda_algorithms.cpp',
    '../src/gda_weights.cpp',
    '../src/GenGeomAlgs.cpp',
    '../src/GenUtils.cpp',
    '../src/clustering/cluster.cpp',
    '../src/clustering/maxp.cpp',
    '../src/clustering/maxp_wrapper.cpp',
    '../src/clustering/mds.cpp',
    '../src/clustering/pca.cpp',
    '../src/clustering/redcap.cpp',
    '../src/clustering/redcap_wrapper.cpp',
    '../src/sa/LISA.cpp',
    '../src/sa/MultiGeary.cpp',
    '../src/sa/MultiJoinCount.cpp',
    '../src/sa/UniG.cpp',
    '../src/sa/UniGeary.cpp',
    '../src/sa/UniGstar.cpp',
    '../src/sa/UniJoinCount.cpp',
    '../src/sa/UniLocalMoran.cpp',
    '../src/weights/VoronoiUtils.cpp',
    '../src/weights/PolysToContigWeights.cpp',
    '../src/weights/GalWeight.cpp',
    '../src/weights/GeodaWeight.cpp',
    '../src/weights/GwtWeight.cpp',
    '../src/pg/geoms.c',
    '../src/pg/utils.c',
    '../src/libgeoda.cpp',
]


###########################################################
# Extensions 
###########################################################
extensions = []
package_data = {}
include_package_data = False

extensions = [Extension('pygeoda._libgeoda',
                        sources=SOURCE_FILES,
                        include_dirs=INCLUDE_DIRS,
                        swig_opts=SWIG_OPTS,
                        extra_compile_args=EXTRA_COMPILE_ARGS,
                        extra_link_args=EXTRA_LINK_ARGS,
                        library_dirs=LIBRARY_DIRS,
                        runtime_library_dirs=LIBRARY_DIRS,
                        libraries=LIBRARIES,
                        extra_objects=EXTRA_OBJECTS),]

setup (name = 'pygeoda',
       version = '0.0.4',
       author = "Xun Li",
       author_email = "lixun910@gmail.com",
       url = "https://github.com/lixun910/libgeoda",
       description = """pygeoda is a python library for spatial data analysis based on GeoDa and libgeoda.""",
       ext_modules = extensions,
       package_data = package_data,
       cmdclass = {"develop": update_submodules},
       include_package_data = include_package_data,
       packages=['pygeoda','pygeoda.weights','pygeoda.sa','pygeoda.clustering', 'pygeoda.classify']
      )

