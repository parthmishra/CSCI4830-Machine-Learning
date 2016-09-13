#!/bin/bash

rm iris.model
vw -f iris.model --passes=10 --cache_file=iris.cache --kill_cache --oaa 3 --loss_function=hinge --learning_rate=0.05 < iris.vw
