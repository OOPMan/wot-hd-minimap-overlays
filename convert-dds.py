#!/usr/bin/python

from __future__ import print_function
from sys import argv
import os
import subprocess


argv = argv[1:]
if not len(argv):
  print('Usage: python convert-dds.py <PATH> [PATH]...')
  exit(1)

for path in argv:
  for directory, subdirectories, files in os.walk(path):
    for file in files:
      if file == 'mmap.dds':
	print('Converting %s/%s', % (directory, file))
	subprocess.Popen(['convert', file, 'mmap.png'], cwd=directory)
      

