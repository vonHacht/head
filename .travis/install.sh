#!/bin/bash

set -e
#set -x

if [ $TRAVIS == true ]; then
    echo "Installing in Travis context"
    python travis.py
    python setup.py install
else
    virtualenv ../ENV
    source ../ENV/bin/activate
    ( cd ../ ; python setup.py install )
    deactivate
fi



