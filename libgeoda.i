%module libgeoda
%begin %{
#define SWIG_PYTHON_2_UNICODE
%}
%include "stl.i"
%include "std_string.i"
%include "std_vector.i"
%include "std_pair.i"


%template(VecVoid) std::vector<void*>;
%template(VecFloat) std::vector<float>;
%template(VecString) std::vector<std::string>;
%template(VecDouble) std::vector<double>;
%template(VecChar) std::vector<char>;
%template(VecVecDouble) std::vector<std::vector<double> >;
%template(VecInt) std::vector<int>;
%template(VecBool) std::vector<bool>;
%template(VecVecBool) std::vector<std::vector<bool> >;
%template(VecLong) std::vector<long>;
%template(VecInt64) std::vector<long long>;
%template(VecVecInt) std::vector<std::vector<int> >;
%template(VecUINT8) std::vector<unsigned char>;
%template(VecVecUINT8) std::vector<std::vector<unsigned char> >;
%template(VecVecChar) std::vector<std::vector<char> >;
%template(Pair) std::pair<double, std::vector<double> >;
%template(VecPair) std::vector<std::pair<double, std::vector<double> > >;


#if defined(SWIGPYTHON)

%typemap(ignore) TYPEMAP(unsigned char* temp) {
    $1 = ($1_ltype) temp;
}

%typemap(in) (unsigned char*) {
  if (!PyByteArray_Check($input)) {
    SWIG_exception_fail(SWIG_TypeError, "in method '" "$symname" "', argument "
                       "$argnum"" of type '" "$type""'");
  }
  $1 = (unsigned char*) PyByteArray_AsString($input);
}

/*
%typemap(in) (const std::vector<std::string>& ) {
    // vector of string from unicode string list
    int iLen = PySequence_Length($input);
    std::cout << iLen << "dafadfa" << std::endl;
    for(unsigned int i = 0; i < iLen; i++) {
        PyObject *o = PySequence_GetItem($input, i);
        $1->push_back(PyUnicode_AS_DATA(o));
    }
}
*/
#endif

%{
#include <string>
#include <stdint.h>
#include <weights/GeodaWeight.h>
#include <sa/LISA.h>
#include <sa/BatchLISA.h>
#include <pg/geoms.h>
#include <gda_interface.h>
#include <libgeoda.h>
#include <gda_sa.h>
#include <gda_data.h>
#include <gda_weights.h>
#include <gda_clustering.h>
%}

// release memory for some function to prevent memory leaking
// the SWIG generated wrappers will have a memory leak--the returned
// data will be copied into a string object and the old contents ignored.
%newobject gda_queen_weights;
%newobject gda_rook_weights;
%newobject gda_knn_weights;
%newobject gda_distance_weights;
%newobject gda_localmoran;
%newobject gda_batchlocalmoran;
%newobject gda_localgeary;
%newobject gda_localmultigeary;
%newobject gda_localjoincount;
%newobject gda_localmultijoincount;
%newobject gda_localg;
%newobject gda_localgstar;
%newobject gda_quantilelisa;
%newobject gda_multiquantilelisa;
%newobject gda_fdr;
%newobject gda_bo;
%newobject CreateGeoDaFromGPD;
%newobject CreateGeoDaFromSHP;

%include <std_string.i>
%include <weights/GeodaWeight.h>
%include <sa/LISA.h>
%include <sa/BatchLISA.h>
%include <gda_interface.h>
%include <libgeoda.h>
%include <gda_sa.h>
%include <gda_data.h>
%include <gda_weights.h>
%include <gda_clustering.h>

%template(VecGeoDaColumn) std::vector<GeoDaColumn*>;


