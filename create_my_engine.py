from sqlalchemy import create_engine
# from sqlalchemy import text
import pyodbc
from sqlalchemy.exc import SQLAlchemyError


server = 'localhost\MSSQLSERVER01'
database = 'Naya'

# for SQLite
# connection_string = "sqlite+pysqlite:///:memory:"

# for MS SQL Server
connection_string = 'mssql+pyodbc://' + server + '/' + database + '?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server'


def create_db_engine():
    # print(pyodbc.drivers())
    print(connection_string + "\n\n")
    
    engine = create_engine(connection_string , echo=False)
    
    # try:
    #     with engine.connect() as connection:
    #         result = connection.execute("SELECT 1")
    #         for row in result:
    #             print(row)
    # except SQLAlchemyError as e:
    #     print(f"Error occurred: {str(e)}")
        
    return engine




