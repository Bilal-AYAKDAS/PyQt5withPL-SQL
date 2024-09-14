import cx_Oracle
from datetime import datetime

#ORACLE DATABASE CONNECTİON
dsn = cx_Oracle.makedsn("localhost", 1521, service_name="TEST.bilalayakdas.com")
conn = cx_Oracle.connect(user="PYTHONORA", password="root", dsn=dsn,encoding="UTF-8")
# Establish the database connection