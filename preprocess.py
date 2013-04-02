''' preprocess
crop, greyscale and resample input test data
usage:
    $ python preprocess.py in/ out/
'''
import os
import sys

import envoy

if len(sys.argv) < 2:
    print 'error: need an input path'
elif len(sys.argv) < 3:
    print 'error: need an output path'

input_directory = sys.argv[1]
output_directory = sys.argv[2]

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

for filename in os.listdir(input_directory):
    print filename
    input_path = os.path.join(input_directory, filename)
    output_path = os.path.join(output_directory, filename)
    envoy.run('convert'
            ' -crop 206x57+55+121'
            ' -density 200'
            ' -units PixelsPerInch'
            ' -type Grayscale'
            ' +compress'
            ' %s %s' % (input_path, output_path))
