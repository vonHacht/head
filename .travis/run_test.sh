#!/bin/bash

set -e
#set -x

type time

if [ $TRAVIS == true ] ; then
    echo "Running in Travis context"
    python setup.py test
else
    echo "Not running in Travis context";
    virtualenv ../ENV
    source ../ENV/bin/activate
    ( cd ../ ; python setup.py test )
    deactivate
fi
