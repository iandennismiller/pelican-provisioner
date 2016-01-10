#!/bin/bash

WHEELHOUSE_PATH=$VIRTUAL_ENV/share/wheelhouse

echo "Scaffold blog into $1"
mrbob -w -O "$1" $VIRTUAL_ENV/share/skel

echo "Create a new virtual environment called $(basename $1)"
source $(which virtualenvwrapper.sh) && mkvirtualenv --no-site-packages $(basename $1)

echo "Install dependencies"
pushd "$1"
echo "wheelhouse: $WHEELHOUSE_PATH"
source $(which virtualenvwrapper.sh) && \
    workon $(basename $1) && \
    pip install --use-wheel --find-links=$WHEELHOUSE_PATH --no-index -r requirements.txt
