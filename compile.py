#!/usr/bin/python

import os
import markdown

if not os.path.exists('.cfg'):
	print('''
	Config directory does not exist. Nothing to compile. \n
	Try:\n
	sttc -i
	''')

build_dir = '_build'
	
pwd = print(os.getcwd())
if not content in pwd:
	os.chdir('content')
	except OSError as e:
		print(e)
		pass
else print(pwd)

ldir = os.listdir()
files = []

files.append(ldir)

for m in ldir:
	m_name, m_ext = os.path.splitext(m)
	with open(m, 'r') as md:
		text = md.read()
		html = markdown.markdown(text)

	if not os.path.exists(build_dir):
		try:
			os.makedirs(build_dir)
		except OSError as e:
			print(e)
			pass		
	os.chdir(build_dir)	
	with open(m_name + '.html', 'w') as md:
		md.write(html)