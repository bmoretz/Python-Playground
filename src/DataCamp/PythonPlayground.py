
#!/usr/bin/env python
# -*- coding: utf8 -*-
__version__ = '$Id: pyodbc_sources.py 1736 2014-01-28 10:36:41Z mn $'

# shows ODBC data sources with driver info

# author: Michal Niklas

import pyodbc
import json

def show_odbc_sources():
	sources = pyodbc.dataSources()
	dsns = sources.keys()
	sl = []
	for dsn in dsns:
		sl.append('%s [%s]' % (dsn, sources[dsn]))
	print('\n'.join(sl))
	
def get_data_sources():
	src = []
	sources = pyodbc.dataSources()
    dsns = sources.keys()
	
	for dsn in dsns:
        src.append('{0} - {1}'.format(dsn, sources[dsn]))
    
	print(src)

if __name__ == '__main__':
	json.dumps(pyodbc.dataSources())