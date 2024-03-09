#!/bin/bash

jupyter notebook \
    --no-browser \
    --allow-root \
    --ip=0.0.0.0 \
    --port=8888 \
    --NotebookApp.notebook_dir='/sources' \
    --NotebookApp.token='' \
    --NotebookApp.password=''