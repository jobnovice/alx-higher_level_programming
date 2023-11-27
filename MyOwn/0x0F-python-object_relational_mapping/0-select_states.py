#!/usr/bin/python3
from MySQLdb import _mysql
from sys import argv
db = _mysql.connect(argv[0],  argv[1])



