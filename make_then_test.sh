#!/bin/bash

C_FILES_DIR=/home/jon/Desktop/scripts/Python/Python_C_functions/C_Files/
PYTHON_FILES_DR=/home/jon/Desktop/scripts/Python/Python_C_functions/Python_Files

cd $C_FILES_DIR && make

cd $PYTHON_FILES_DR && python3 usingCFunctions.py