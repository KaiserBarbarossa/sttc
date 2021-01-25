#!/usr/bin/python

import os
import markdown

if not os.path.exists('.cfg'):
	print('''
	Config directory does not exist. Nothing to compile. \n
	Try:\n
	sttc -i
	''')

files = os.listdir()

for f in files:
	f_name, f_ext = os.path.splitext(f)
	if f_ext != '.md':
		pass
	else:
		new_name = f_name + '.html'
		markdown.markdownFromFile(
			input=f,
			output=new_name,
			encoding='utf8',
			)
