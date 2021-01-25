#!/usr/bin/python
#TODO: Change shebang

import os

if not os.path.exists('.cfg'):
	try:
		os.makedirs('.cfg')
	except OSError as e:
		print(e)
		pass

if not os.path.exists('template'):
	try:
		os.makedirs('template')
	except OSError as e:
		print(e)
		pass

if not os.path.exists('content'):
	try:
		os.makedirs('content')
	except OSError as e:
		print(e)
		pass

conf = open('.cfg/sttc.conf', 'w')
conf.write('''
[general]
experimental = false

[compile]
template = $FOO

[html]
generator = false
keywords = false
doctype = $DOCTYPE
''')
