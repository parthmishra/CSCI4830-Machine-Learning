#!/bin/bash

rm predictions.txt
vw -i iris.model -t -p ./predictions.txt < iris.vw
python3 accuracy.py
