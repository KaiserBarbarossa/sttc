#!/usr/bin/python3

import argparse
import os
import sys
from sys import exit

version = '1.0'

parser = argparse.ArgumentParser()
parser = argparse.ArgumentParser()
parser.add_argument('-v', '--version', help='display version', action='store_true')
parser.add_argument('-i', '--init', help='init site here', action='store_true')
parser.add_argument('-c', '--compile', help='compile site', action='store_true')
args = parser.parse_args()
print('Using Sttc Version '+version+'\n')
if args.version:
	print(version)
	exit()
elif args.init:
	os.system('python3 init.py')
elif args.compile:
	os.system('python3 compile.py')
else:
	print('You have to provide an argument. For help see:\n  sttc -h')
