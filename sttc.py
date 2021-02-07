#!/usr/bin/env python3

import argparse
import os
import sys
from sys import exit
import markdown

version = '1.0'

def main():
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
		init()
	elif args.compile:
		compile()
	else:
		print('You have to provide an argument. For help see:\n  sttc -h')

def init():
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

def compile():
	if not os.path.exists('.cfg'):
		print('''
		Config directory does not exist. Nothing to compile. \n
		Try:\n
		sttc -i
		''')

	if not os.path.exists('public'):
		os.makedirs('public')

	os.chdir('content')

	files = os.listdir()

	for f in files:
		f_name, f_ext = os.path.splitext(f)
		if f_ext != '.md':
			pass
		else:
			new_name = '../public/' + f_name + '.html'
			markdown.markdownFromFile(
				input=f,
				output=new_name,
				encoding='utf8',
			)

main()
