#!/usr/bin/env python3
import sys, os, platform
import setuptools
from distutils.core import setup, Extension
from setuptools.command.develop import develop


###########################################################
# Variables 
##########################################################
OS_NAME = 'linux'

if sys.platform == "win32":
    OS_NAME = 'win64' if sys.maxsize > 2**32 else 'win32'

elif sys.platform == "darwin":
    OS_NAME = 'osx'
    os.environ["ARCHFLAGS"] = "-arch x86_64"
    if platform.machine() == 'arm64':
        os.environ["ARCHFLAGS"] = "-arch arm64"
    os.environ['MACOSX_DEPLOYMENT_TARGET'] = platform.mac_ver()[0]

elif sys.platform == "linux2":
    OS_NAME = 'linux'

LIBGEODA_SRC = 'libgeoda'

###########################################################
# INCLUDE_DIRS
###########################################################
INCLUDE_DIRS = []
if OS_NAME == 'win32' or OS_NAME == 'win64':
    INCLUDE_DIRS = [
        '.\\boost\\include',
        '.\\' + LIBGEODA_SRC,
    ]

else:
    INCLUDE_DIRS = [
        './boost/include',
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
        '/DNOMINMAX', # for win Macro define for min/max that impacts std::numeric_limits<int>::max()
    ]
else:
    EXTRA_COMPILE_ARGS = [
        '-w',
        '-std=c++14',
        '-fvisibility=hidden',
        '-D__USE_PTHREAD__' # use pthread!!! on *nix
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

else:
    EXTRA_LINK_ARGS = [
        '-pthread' # in *nix, using pthread instead of boost::thread
    ]

###########################################################
#  Link objects 
###########################################################
EXTRA_OBJECTS = []

if OS_NAME == 'win32' or OS_NAME == 'win64':
    BOOST_ARC = 'x32' if OS_NAME == 'win32' else 'x64'
    pyversion = sys.version[:3]
    MSVC_VER = ''
    BOOST_VER = '1_75'
    if pyversion in ['3.5']:
        MSVC_VER = 'vc140'
    elif pyversion in ['3.6', '3.7', '3.8']:
        MSVC_VER = 'vc141'
    elif pyversion in ['3.9']:
        MSVC_VER = 'vc142'


    EXTRA_OBJECTS = [
        '.\\boost\\lib\\' + OS_NAME + '\\libboost_thread-' + MSVC_VER+ '-mt-' + BOOST_ARC + '-' + BOOST_VER + '.lib',
        '.\\boost\\lib\\' + OS_NAME + '\\libboost_system-' + MSVC_VER+ '-mt-' + BOOST_ARC + '-' + BOOST_VER + '.lib',
        '.\\boost\\lib\\' + OS_NAME + '\\libboost_date_time-' + MSVC_VER+ '-mt-' + BOOST_ARC + '-' + BOOST_VER + '.lib',
        '.\\boost\\lib\\' + OS_NAME + '\\libboost_chrono-' + MSVC_VER+ '-mt-' + BOOST_ARC + '-' + BOOST_VER + '.lib', 
    ]
else:
    EXTRA_OBJECTS = [
    ]

###########################################################
#  Source files
###########################################################
SOURCE_FILES  = [
    'pygeoda/libgeoda.cpp',
    './' + LIBGEODA_SRC + '/libgeoda.cpp',
    './' + LIBGEODA_SRC + '/gda_sa.cpp',
    './' + LIBGEODA_SRC + '/gda_data.cpp',
    './' + LIBGEODA_SRC + '/gda_weights.cpp',
    './' + LIBGEODA_SRC + '/gda_clustering.cpp',
    './' + LIBGEODA_SRC + '/GenGeomAlgs.cpp',
    './' + LIBGEODA_SRC + '/GenUtils.cpp',
    './' + LIBGEODA_SRC + '/SpatialIndAlgs.cpp',
    './' + LIBGEODA_SRC + '/pg/geoms.cpp',
    './' + LIBGEODA_SRC + '/pg/utils.cpp',
    './' + LIBGEODA_SRC + '/shapelib/shpopen.cpp',
    './' + LIBGEODA_SRC + '/shapelib/dbfopen.cpp',
    './' + LIBGEODA_SRC + '/shapelib/safileio.cpp',
    './' + LIBGEODA_SRC + '/weights/PointsToContigWeights.cpp',
    './' + LIBGEODA_SRC + '/weights/PolysToContigWeights.cpp',
    './' + LIBGEODA_SRC + '/weights/GalWeight.cpp',
    './' + LIBGEODA_SRC + '/weights/GwtWeight.cpp',
    './' + LIBGEODA_SRC + '/weights/GeodaWeight.cpp',
    './' + LIBGEODA_SRC + '/weights/VoronoiUtils.cpp',
    './' + LIBGEODA_SRC + '/sa/BatchLISA.cpp',
    './' + LIBGEODA_SRC + '/sa/BatchLocalMoran.cpp',
    './' + LIBGEODA_SRC + '/sa/LISA.cpp',
    './' + LIBGEODA_SRC + '/sa/MultiGeary.cpp',
    './' + LIBGEODA_SRC + '/sa/MultiJoinCount.cpp',
    './' + LIBGEODA_SRC + '/sa/UniG.cpp',
    './' + LIBGEODA_SRC + '/sa/UniGeary.cpp',
    './' + LIBGEODA_SRC + '/sa/UniGstar.cpp',
    './' + LIBGEODA_SRC + '/sa/UniJoinCount.cpp',
    './' + LIBGEODA_SRC + '/sa/UniLocalMoran.cpp',
    './' + LIBGEODA_SRC + '/sa/BiLocalMoran.cpp',
    './' + LIBGEODA_SRC + '/clustering/fastcluster.cpp',
    './' + LIBGEODA_SRC + '/clustering/redcap.cpp',
    './' + LIBGEODA_SRC + '/clustering/redcap_wrapper.cpp',
    './' + LIBGEODA_SRC + '/clustering/azp.cpp',
    './' + LIBGEODA_SRC + '/clustering/maxp_wrapper.cpp',
    './' + LIBGEODA_SRC + '/clustering/azp_wrapper.cpp',
    './' + LIBGEODA_SRC + '/clustering/schc_wrapper.cpp',
    './' + LIBGEODA_SRC + '/clustering/cluster.cpp',
    './' + LIBGEODA_SRC + '/clustering/joincount_ratio.cpp',
    './' + LIBGEODA_SRC + '/clustering/spatial_validation.cpp',
    './' + LIBGEODA_SRC + '/clustering/make_spatial.cpp',
    './' + LIBGEODA_SRC + '/knn/ANN.cpp',
	'./' + LIBGEODA_SRC + '/knn/perf.cpp',
	'./' + LIBGEODA_SRC + '/knn/kd_util.cpp',
	'./' + LIBGEODA_SRC + '/knn/kd_tree.cpp',
	'./' + LIBGEODA_SRC + '/knn/kd_split.cpp',
	'./' + LIBGEODA_SRC + '/knn/kd_search.cpp',
	'./' + LIBGEODA_SRC + '/knn/kd_pr_search.cpp',
	'./' + LIBGEODA_SRC + '/knn/kd_fix_rad_search.cpp',
	'./' + LIBGEODA_SRC + '/knn/kd_dump.cpp',
	'./' + LIBGEODA_SRC + '/knn/brute.cpp',
	'./' + LIBGEODA_SRC + '/knn/bd_tree.cpp',
	'./' + LIBGEODA_SRC + '/knn/bd_search.cpp',
	'./' + LIBGEODA_SRC + '/knn/bd_pr_search.cpp',
	'./' + LIBGEODA_SRC + '/knn/bd_fix_rad_search.cpp',
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
       version = '0.0.8.post1',
       author = "Xun Li",
       author_email = "lixun910@gmail.com",
       url = "https://github.com/geodacenter/pygeoda",
       description = """pygeoda is a python library for spatial data analysis based on GeoDa and libgeoda.""",
       ext_modules = extensions,
       package_data = package_data,
       include_package_data = include_package_data,
       packages=['pygeoda','pygeoda.weights','pygeoda.sa','pygeoda.clustering', 'pygeoda.classify', 'pygeoda.data']
      )

