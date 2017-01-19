import os
import sys


currentlocation = os.getcwd()

#return when the first occurence
for subdirectory in os.walk(currentlocation):
    
    first, second, third = subdirectory
    
    for file in third:
        if '.log' in file:
            
            realpath = '{}\{}'.format(first, file)
            
            with open(realpath) as infile:
                buffers = infile.read()
                for line in buffers.split('\n'):
                    line = line.split()
                    if 'DEVICE' in line and 'NAME:' in line:
                        if len(line) > 3:
                            print(line)
                            
                            
                