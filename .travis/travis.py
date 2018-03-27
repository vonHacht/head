'''
    For travis sanity check, keep as simple as possible
'''
import os

print ("== Hi travis ! ==")
print ("== Directory copied to: {0} ==".format(os.environ['TRAVIS_BUILD_DIR']))
