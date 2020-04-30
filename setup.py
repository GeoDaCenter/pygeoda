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
BOOST_DIR = '../boost_static'
LIBGEODA_DIR = '../libgeoda_src'
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
        '..\\libgeoda_src\\weights',
        '..\\libgeoda_src\\sa',
        '..\\libgeoda_src\\shape',
        '..\\libgeoda_src\\pg',
        '..\\libgeoda_src',
    ]

else:
    INCLUDE_DIRS = [
        BOOST_DIR + '/include',
        EIGEN_DIR,
        '../libgeoda_src/weights',
        LIBGEODA_DIR + '/sa',
        LIBGEODA_DIR + '/pg',
        LIBGEODA_DIR,
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
    LIBGEODA_DIR + '/SpatialIndAlgs.cpp',
    LIBGEODA_DIR + '/gda_sa.cpp',
    LIBGEODA_DIR + '/gda_data.cpp',
    LIBGEODA_DIR + '/gda_clustering.cpp',
    LIBGEODA_DIR + '/gda_algorithms.cpp',
    LIBGEODA_DIR + '/gda_weights.cpp',
    LIBGEODA_DIR + '/GenGeomAlgs.cpp',
    LIBGEODA_DIR + '/GenUtils.cpp',
    LIBGEODA_DIR + '/clustering/cluster.cpp',
    LIBGEODA_DIR + '/clustering/maxp.cpp',
    LIBGEODA_DIR + '/clustering/maxp_wrapper.cpp',
    LIBGEODA_DIR + '/clustering/mds.cpp',
    LIBGEODA_DIR + '/clustering/pca.cpp',
    LIBGEODA_DIR + '/clustering/redcap.cpp',
    LIBGEODA_DIR + '/clustering/redcap_wrapper.cpp',
    LIBGEODA_DIR + '/sa/LISA.cpp',
    LIBGEODA_DIR + '/sa/MultiGeary.cpp',
    LIBGEODA_DIR + '/sa/MultiJoinCount.cpp',
    LIBGEODA_DIR + '/sa/UniG.cpp',
    LIBGEODA_DIR + '/sa/UniGeary.cpp',
    LIBGEODA_DIR + '/sa/UniGstar.cpp',
    LIBGEODA_DIR + '/sa/UniJoinCount.cpp',
    LIBGEODA_DIR + '/sa/UniLocalMoran.cpp',
    LIBGEODA_DIR + '/weights/VoronoiUtils.cpp',
    LIBGEODA_DIR + '/weights/PolysToContigWeights.cpp',
    LIBGEODA_DIR + '/weights/GalWeight.cpp',
    LIBGEODA_DIR + '/weights/GeodaWeight.cpp',
    LIBGEODA_DIR + '/weights/GwtWeight.cpp',
    LIBGEODA_DIR + '/pg/geoms.c',
    LIBGEODA_DIR + '/pg/utils.c',
    LIBGEODA_DIR + '/libgeoda.cpp',
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

