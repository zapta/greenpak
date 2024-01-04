#!/bin/bash

cp ../src/greenpak/__init__.py /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages/__init__.py

cp ../src/greenpak/drivers.py /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages/drivers.py

#SPHINXOPTS    ?=
#SOURCEDIR 
#make html SOURCEDIR="../src"

#./make.bat html
#make html SPHINXOPTS="-vvv"
make html



