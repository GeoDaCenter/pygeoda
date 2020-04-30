if [[ "$OSTYPE" == "linux-gnu" ]]; then
  python setup.py build_ext --inplace --force
elif [[ "$OSTYPE" == "darwin"* ]]; then
  python3 setup.py build_ext --inplace --force
  #python3 setup.py build_ext --inplace --force
  mv pygeoda/_libgeoda.*.so pygeoda/_libgeoda.so
elif [[ "$OSTYPE" == "cygwin" ]]; then
  echo "POSIX compatibility layer and Linux environment emulation for Windows"
elif [[ "$OSTYPE" == "msys" ]]; then
  echo "Lightweight shell and GNU utilities compiled for Windows (part of MinGW)"
elif [[ "$OSTYPE" == "win32" ]]; then
  echo "I'm not sure this can happen."
elif [[ "$OSTYPE" == "freebsd"* ]]; then
  echo "freebsd"
else
  echo "Unknown."
fi

