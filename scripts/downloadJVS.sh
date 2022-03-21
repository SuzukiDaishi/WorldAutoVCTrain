#!/bin/bash

gdown 19oAw8wWn3Y7z6CKChRdAyGOB9yupL_Xt
unzip jvs_ver1.zip
rm jvs_ver1.zip
python scripts/jvs2vctk.py
rm -rf jvs_ver1