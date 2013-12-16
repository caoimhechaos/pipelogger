# coding=utf-8
#!/usr/bin/env python

from setuptools import setup, find_packages

VERSION = "1.0"

def params():
	name = "pipelogger"
	version = VERSION
	description = "Python program to read from a pipe and write to syslog"
	long_description = open("README.md").read()
	classifiers = [
		"Development Status :: 6 - Mature",
		"Environment :: No Input/Output (Daemon)",
		"Intended Audience :: Developers",
		"Intended Audience :: Information Technology",
		"Intended Audience :: System Administrators",
		"License :: OSI Approved :: BSD License",
		"Natural Language :: English",
		"Operating System :: POSIX",
		"Programming Language :: Python :: 2.7",
		"Programming Language :: Python :: 3",
		"Topic :: System :: Logging",
		"Topic :: Utilities",
	]
	author = "Tonnerre LOMBARD"
	author_email = "tonnerre@ancient-solutions.com"
	license = "BSD"

	scripts = ["scripts/pipelogger"]

	return locals()

setup(**params())
