import pyodbc

host = "SQL"
database = "FLASK"
username = "bmoretz"
password = "l3tm31n"

print ("DB CONNECT ATTEMPT")
try:
	pyodbc.connect(r'Driver={SQL Server Native Client 11.0};Server=DATACENTER;Database=FLASK;UID=bmoretz;PWD=l3tm31n')

    cs = 'DSN=%s;UID=%s;PWD=%s;DATABASE=%s;' % (host, username, password, database)
    cnxn = pyodbc.connect(cs)
    print ("SUCCESS")
except Exception as e:
    print ("Error: " + str(e))