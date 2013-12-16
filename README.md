pipelogger
==========

Python program to read data from a pipe and write it to syslog.  It can be
used for writing to syslog from programs which have only support for log
files, which can be useful on machines with no writable storage.

Usage
-----

Read all data from /var/log/nginx/error.log and write it to the local
syslog server as nginx:

    pipelogger -i nginx /var/log/nginx/error.log
