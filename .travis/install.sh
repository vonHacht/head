#!/bin/bash

set -e
#set -x

if [ $TRAVIS == true ]; then
    echo "Installing in Travis context"
    echo "$(pwd)"
    echo "$(ls)"
    python "$TRAVIS_BUILD_DIR/.travis/travis.py"
    python setup.py install
else
    virtualenv ../ENV
    source ../ENV/bin/activate
    ( cd ../ ; python setup.py install )
    deactivate
fi



