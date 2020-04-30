#!/usr/bin/env python3
import sys, os, platform
import setuptools
from distutils.core import setup, Extension
from setuptools.command.develop import develop
from subprocess import check_call


###########################################################
# Variables 
##########################################################
OS_NAME = 'linux'
BOOST_DIR = '../pygeoda_boost'
EIGEN_DIR = '../eigen3'

if sys.platform == "win32":
    BOOST_DIR = '..\\boost_static'
    LIBGEODA_DIR = '..\\libgeoda_src'
    EIGEN_DIR = '..\\eigen3'

    OS_NAME = 'win64' if sys.maxsize > 2**32 else 'win32'

elif sys.platform == "darwin":
    OS_NAME = 'osx'
    #os.environ['MACOSX_DEPLOYMENT_TARGET'] = '10.14'
    os.environ["ARCHFLAGS"] = "-arch x86_64"

elif sys.platform == "linux2":
    OS_NAME = 'linux'

pyversion = sys.version[:3]
# 14.X 3.5, 3.6, 3.7, 3.8
# 10.0 3.3, 3.4
# 9.0 2.6, 2.7, 3.0, 3.1, 3.2
MSVC_VER = ''
BOOST_VER = '1_64'

if pyversion in ['2.6', '2.7', '3.0', '3.1', '3.2']:
    MSVC_VER = 'vc90'
elif pyversion in ['3.3', '3.4']:
    MSVC_VER = 'vc100'
elif pyversion in ['3.5', '3.6', '3.7', '3.8']:
    MSVC_VER = 'vc140'

###########################################################
# INCLUDE_DIRS
###########################################################
INCLUDE_DIRS = []
if OS_NAME == 'win32' or OS_NAME == 'win64':
    INCLUDE_DIRS = [
        BOOST_DIR + '\\include',
        EIGEN_DIR,
        '.\\libgeoda_src\\weights',
        '.\\libgeoda_src\\sa',
        '.\\libgeoda_src\\shape',
        '.\\libgeoda_src\\pg',
        '.\\libgeoda_src',
    ]

else:
    INCLUDE_DIRS = [
        BOOST_DIR + '/include',
        EIGEN_DIR,
        './libgeoda_src',
        './libgeoda_src/weights',
        './libgeoda_src/sa',
        './libgeoda_src/pg',
    ]


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
    LIBRARIES = []

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
        #'-std=c++11',
        '-fvisibility=hidden'
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
        BOOST_DIR + '\\lib\\' + OS_NAME + '\\libboost_thread-' + MSVC_VER+ '-mt-' + BOOST_VER + '.lib',
        BOOST_DIR + '\\lib\\' + OS_NAME + '\\libboost_system-' + MSVC_VER+ '-mt-' + BOOST_VER + '.lib',
        BOOST_DIR + '\\lib\\' + OS_NAME + '\\libboost_date_time-' + MSVC_VER+ '-mt-' + BOOST_VER + '.lib',
        BOOST_DIR + '\\lib\\' + OS_NAME + '\\libboost_chrono-' + MSVC_VER+ '-mt-' + BOOST_VER + '.lib', 
    ]
else:
    EXTRA_OBJECTS = [
        BOOST_DIR + '/lib/' + OS_NAME + '/libboost_thread.a',
        BOOST_DIR + '/lib/' + OS_NAME + '/libboost_system.a',
        BOOST_DIR + '/lib/' + OS_NAME + '/libboost_date_time.a',
    ]

###########################################################
#  Source files
###########################################################
SOURCE_FILES  = [
    'pygeoda/libgeoda.cpp',
    './libgeoda_src/SpatialIndAlgs.cpp',
    './libgeoda_src/gda_sa.cpp',
    './libgeoda_src/gda_data.cpp',
    './libgeoda_src/gda_clustering.cpp',
    './libgeoda_src/gda_algorithms.cpp',
    './libgeoda_src/gda_weights.cpp',
    './libgeoda_src/GenGeomAlgs.cpp',
    './libgeoda_src/GenUtils.cpp',
    './libgeoda_src/clustering/cluster.cpp',
    './libgeoda_src/clustering/maxp.cpp',
    './libgeoda_src/clustering/maxp_wrapper.cpp',
    './libgeoda_src/clustering/mds.cpp',
    './libgeoda_src/clustering/pca.cpp',
    './libgeoda_src/clustering/redcap.cpp',
    './libgeoda_src/clustering/redcap_wrapper.cpp',
    './libgeoda_src/sa/LISA.cpp',
    './libgeoda_src/sa/MultiGeary.cpp',
    './libgeoda_src/sa/MultiJoinCount.cpp',
    './libgeoda_src/sa/UniG.cpp',
    './libgeoda_src/sa/UniGeary.cpp',
    './libgeoda_src/sa/UniGstar.cpp',
    './libgeoda_src/sa/UniJoinCount.cpp',
    './libgeoda_src/sa/UniLocalMoran.cpp',
    './libgeoda_src/weights/VoronoiUtils.cpp',
    './libgeoda_src/weights/PolysToContigWeights.cpp',
    './libgeoda_src/weights/GalWeight.cpp',
    './libgeoda_src/weights/GeodaWeight.cpp',
    './libgeoda_src/weights/GwtWeight.cpp',
    './libgeoda_src/pg/geoms.c',
    './libgeoda_src/pg/utils.c',
    './libgeoda_src/libgeoda.cpp',
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
       #cmdclass = {"develop": update_submodules},
       include_package_data = include_package_data,
       packages=['pygeoda','pygeoda.weights','pygeoda.sa','pygeoda.clustering', 'pygeoda.classify', 'pygeoda.data']
      )

