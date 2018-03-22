#!/bin/bash

set -e
set -x

echo "location: $(pwd)"
echo "content:"
echo "$(ls)"

if [ $TRAVIS == true ] ; then
    echo "Running in Travis context"
    python travis.py
    python setup.py test
else
    echo "Not running in Travis context";
    virtualenv ../ENV
    source ../ENV/bin/activate
    ( cd ../ ; python setup.py test )
    deactivate
fi
