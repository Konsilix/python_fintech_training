#!/usr/bin/env python

import pyodbc

dsn = 'mssqlsrv1.c2xwsbezn8re.us-east-1.rds.amazonaws.com'
user = 'totem'
password = 'T0t3m2016!'
database = 'system'

con_string = 'DSN=%s;UID=%s;PWD=%s;DATABASE=%s;' % (dsn, user, password, database)
cnxn = pyodbc.connect(con_string)

