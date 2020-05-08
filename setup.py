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

if sys.platform == "win32":
    OS_NAME = 'win64' if sys.maxsize > 2**32 else 'win32'

elif sys.platform == "darwin":
    OS_NAME = 'osx'
    os.environ["ARCHFLAGS"] = "-arch x86_64"
    mac_ver = platform.mac_ver()[0]
    os.environ['MACOSX_DEPLOYMENT_TARGET'] = mac_ver

elif sys.platform == "linux2":
    OS_NAME = 'linux'

LIBGEODA_SRC = 'libgeoda_src'

###########################################################
# INCLUDE_DIRS
###########################################################
INCLUDE_DIRS = []
if OS_NAME == 'win32' or OS_NAME == 'win64':
    INCLUDE_DIRS = [
        '.\\pygeoda_boost\\include',
        '.\\eigen3',
        '.\\' + LIBGEODA_SRC,
    ]

else:
    INCLUDE_DIRS = [
        './pygeoda_boost/include',
        './eigen3',
        './' + LIBGEODA_SRC,
    ]


###########################################################
# LIBRARIES and INCLUDE_DIRS
###########################################################
LIBRARY_DIRS = []
LIBRARIES = [] # -lxxx

if OS_NAME == 'win32' or OS_NAME == 'win64':
    LIBRARIES = [
        #'comctl32','rpcrt4'
        ]

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
        '/EHsc', #MSVC is not throwing exceptions, boost::throw_exception error
        '/MD', # only for python 27  amd64
    ]
else:
    EXTRA_COMPILE_ARGS = [
        '-stdlib=libc++',
        '-fvisibility=hidden'
    ]


###########################################################
#  Link args
###########################################################
EXTRA_LINK_ARGS = []

if OS_NAME == 'win32' or OS_NAME == 'win64':
    EXTRA_LINK_ARGS += [
        '/ignore:4229',
        #'/NODEFAULTLIB:msvcrt.lib'
        ]

elif OS_NAME == 'osx':
    EXTRA_LINK_ARGS = []

###########################################################
#  Link objects 
###########################################################
EXTRA_OBJECTS = []

if OS_NAME == 'win32' or OS_NAME == 'win64':
    BOOST_ARC = 'x32' if OS_NAME == 'win32' else 'x64'
    pyversion = sys.version[:3]
    MSVC_VER = ''
    BOOST_VER = '1_69'
    if pyversion in ['2.6', '2.7', '3.0', '3.1', '3.2']:
        MSVC_VER = 'vc90'
    elif pyversion in ['3.3', '3.4']:
        MSVC_VER = 'vc100'
    elif pyversion in ['3.5', '3.6', '3.7', '3.8']:
        MSVC_VER = 'vc141'


    EXTRA_OBJECTS = [
        '.\\pygeoda_boost\\lib\\' + OS_NAME + '\\libboost_thread-' + MSVC_VER+ '-mt-' + BOOST_ARC + '-' + BOOST_VER + '.lib',
        '.\\pygeoda_boost\\lib\\' + OS_NAME + '\\libboost_system-' + MSVC_VER+ '-mt-' + BOOST_ARC + '-' + BOOST_VER + '.lib',
        '.\\pygeoda_boost\\lib\\' + OS_NAME + '\\libboost_date_time-' + MSVC_VER+ '-mt-' + BOOST_ARC + '-' + BOOST_VER + '.lib',
        '.\\pygeoda_boost\\lib\\' + OS_NAME + '\\libboost_chrono-' + MSVC_VER+ '-mt-' + BOOST_ARC + '-' + BOOST_VER + '.lib', 
    ]
else:
    EXTRA_OBJECTS = [
        './pygeoda_boost/lib/' + OS_NAME + '/libboost_thread.a',
        './pygeoda_boost/lib/' + OS_NAME + '/libboost_system.a',
        './pygeoda_boost/lib/' + OS_NAME + '/libboost_date_time.a',
    ]

###########################################################
#  Source files
###########################################################
SOURCE_FILES  = [
    'pygeoda/libgeoda.cpp',
    './' + LIBGEODA_SRC + '/SpatialIndAlgs.cpp',
    './' + LIBGEODA_SRC + '/gda_sa.cpp',
    './' + LIBGEODA_SRC + '/gda_data.cpp',
    './' + LIBGEODA_SRC + '/gda_clustering.cpp',
    './' + LIBGEODA_SRC + '/gda_algorithms.cpp',
    './' + LIBGEODA_SRC + '/gda_weights.cpp',
    './' + LIBGEODA_SRC + '/GenGeomAlgs.cpp',
    './' + LIBGEODA_SRC + '/GenUtils.cpp',
    './' + LIBGEODA_SRC + '/clustering/cluster.cpp',
    './' + LIBGEODA_SRC + '/clustering/maxp.cpp',
    './' + LIBGEODA_SRC + '/clustering/maxp_wrapper.cpp',
    './' + LIBGEODA_SRC + '/clustering/mds.cpp',
    './' + LIBGEODA_SRC + '/clustering/pca.cpp',
    './' + LIBGEODA_SRC + '/clustering/redcap.cpp',
    './' + LIBGEODA_SRC + '/clustering/redcap_wrapper.cpp',
    './' + LIBGEODA_SRC + '/sa/LISA.cpp',
    './' + LIBGEODA_SRC + '/sa/MultiGeary.cpp',
    './' + LIBGEODA_SRC + '/sa/MultiJoinCount.cpp',
    './' + LIBGEODA_SRC + '/sa/UniG.cpp',
    './' + LIBGEODA_SRC + '/sa/UniGeary.cpp',
    './' + LIBGEODA_SRC + '/sa/UniGstar.cpp',
    './' + LIBGEODA_SRC + '/sa/UniJoinCount.cpp',
    './' + LIBGEODA_SRC + '/sa/UniLocalMoran.cpp',
    './' + LIBGEODA_SRC + '/weights/VoronoiUtils.cpp',
    './' + LIBGEODA_SRC + '/weights/PolysToContigWeights.cpp',
    './' + LIBGEODA_SRC + '/weights/GalWeight.cpp',
    './' + LIBGEODA_SRC + '/weights/GeodaWeight.cpp',
    './' + LIBGEODA_SRC + '/weights/GwtWeight.cpp',
    './' + LIBGEODA_SRC + '/pg/geoms.c',
    './' + LIBGEODA_SRC + '/pg/utils.c',
    './' + LIBGEODA_SRC + '/shapelib/shpopen.c',
    './' + LIBGEODA_SRC + '/shapelib/dbfopen.c',
    './' + LIBGEODA_SRC + '/shapelib/safileio.c',
    './' + LIBGEODA_SRC + '/libgeoda.cpp',
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

