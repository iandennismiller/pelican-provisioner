#!/usr/bin/env python

import sys, os, glob, re, datetime, time

# create a new article; fab new:'some title'

template = """category: uncategorized
date: {datestamp}
title: {title}
status: draft

This is just a template.
"""

if len(sys.argv) < 2:
    sys.stderr.write("Usage: %s \"[post_title]\"\n\n" % sys.argv[0])
    sys.exit(1)

title = sys.argv[1]

now = datetime.datetime.now()
datestamp = "%d-%0.2d-%0.2d" % (now.year, now.month, now.day)
filename = "content/post/%s %s.md" % (datestamp, title)
with open(filename, "w") as f:
    f.write(template.format(datestamp=datestamp, title=title))
