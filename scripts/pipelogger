#!/usr/bin/env python
#

import argparse
import atexit
import os
import sys
import syslog

parser = argparse.ArgumentParser(
	description='Syslog messages as read from a pipe')

parser.add_argument('-i', '--ident',
	help='Use the given identifier for syslogging',
	required=True)
parser.add_argument('-p', '--pid',
	help='File to write the process ID to')
parser.add_argument('pipe', help='Pipe file to read log records from. ' +
	'Must be an absolute path.')
args = parser.parse_args()

def delstuff():
	"""Delete the pipe and PID file."""
	if os.path.exists(args.pipe):
		os.remove(args.pipe)
	if os.path.exists(args.pid):
		os.remove(args.pid)

syslog.openlog(args.ident, 0)

# We should become a daemon. For that, we have to perform a few steps:
#
# 1. Relinquish the present working directory.
try:
	os.chdir("/")
except Exception, e:
	syslog.syslog("chdir to /: " + str(e))
	sys.exit(1)

# 2. Fork into a process of our own.
try:
	pid = os.fork()
	if pid > 0:
		# Exit the first parent.
		sys.exit(0)
except OSError, e:
	syslog.syslog("fork failed: " + str(e))

# 3. Create a new session.
try:
	os.setsid()
except OSError, e:
	syslog.syslog("setsid: " + str(e))

# 4. Redirect stdin/stdout/stderr file descriptors.
try:
	sys.stdout.flush()
	sys.stderr.flush()
except Exception, e:
	syslog.syslog("flush: " + str(e))
	sys.exit(1)

dnw = None
dnr = None

try:
	dnw = open(os.devnull, 'a+')
	dnr = open(os.devnull, 'r')
except Exception, e:
	syslog.syslog(os.devnull + ": " + str(e))
	sys.exit(1)

try:
	os.dup2(dnr.fileno(), sys.stdin.fileno())
	os.dup2(dnw.fileno(), sys.stdout.fileno())
	os.dup2(dnw.fileno(), sys.stderr.fileno())
except Exception, e:
	syslog.syslog("dup2: " + str(e))
	sys.exit(1)

# 5. Fork again in the new session.
try:
	pid = os.fork()
	if pid > 0:
		# Exit the first parent.
		sys.exit(0)
except OSError, e:
	syslog.syslog("fork failed: " + str(e))

# 6. Ensure we delete the affected files at exit.
atexit.register(delstuff)

# 7. Write the PID to a file if requested.
if args.pid:
	pid = str(os.getpid())
	try:
		file(args.pid,'w+').write("%s\n" % pid)
	except Exception, e:
		syslog.syslog(args.pid + ": " + str(e))
		sys.exit(1)

# If the FIFO doesn't exist yet, we need to create it.
if not os.path.exists(args.pipe):
	try:
		os.mkfifo(args.pipe)
	except Exception, e:
		syslog.syslog(args.pipe + ": " + str(e))
		sys.exit(1)

while os.path.exists(args.pipe):
	f = open(args.pipe, 'r')

	for l in f:
		syslog.syslog(l)

	f.close()

syslog.closelog()
