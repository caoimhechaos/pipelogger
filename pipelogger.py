#!/usr/bin/env python
#

import argparse
import os
import syslog

parser = argparse.ArgumentParser(
	description='Syslog messages as read from a pipe')

parser.add_argument('-i', '--ident',
	help='Use the given identifier for syslogging',
	required=True)
parser.add_argument('pipe', help='Pipe file to read log records from')
args = parser.parse_args()

syslog.openlog(args.ident, 0)

if not os.path.exists(args.pipe):
	os.mkfifo(args.pipe)

while os.path.exists(args.pipe):
	f = open(args.pipe, 'r')

	for l in f:
		syslog.syslog(l)

	f.close()

syslog.closelog()
