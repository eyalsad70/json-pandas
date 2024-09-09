from create_my_engine import create_db_engine
from sqlalchemy import text
from sqlalchemy import MetaData, Table, Column, Integer, String

import pandas as pd
import ast

def create_players_table(engine):
    # Define table schema
    metadata = MetaData()
    my_table = Table(
        'players', metadata,
        Column('id', Integer, primary_key=True),
        Column('Name', String(255)),  # Correct type
        Column('YOB', Integer),
        Column('Team', String(255)),
        Column('Goals', Integer) )
    
    # Create the table
    metadata.create_all(engine)
    


create_table_text = text('CREATE TABLE players (Name string, YOB int, Team string, Goals int)') 
insert_prefix = 'INSERT INTO players (Name, YOB, Team, Goals) VALUES '
# Define the SQL for checking if the record exists
check_exists_sql = 'SELECT 1 FROM players WHERE Name = '

table = [
    "('Pele', 1980, 'Brazil', 103)",
    "('Paul Pogba', 1993, 'France', 11)",
    "('Cristiano Ronaldo', 1985, 'Portugal', 123)",
]

insert_row_sql = """
INSERT INTO my_table (id, Name, YOB, Team, Goals)
VALUES (:id, :name, :description);
"""

def insert_players(engine, rows):
    with engine.connect() as connection:
        # connection.execute(create_table_text)
        for row in rows:
            tuple_value = ast.literal_eval(row)
            player_name = f"'{tuple_value[0]}'"
            # print("checking row for player", player_name)
            result = connection.execute(text(check_exists_sql + player_name)).fetchone()
            if result:
                print(f"player {player_name} already exists")
            else:
                connection.execute(text(insert_prefix + row))
        connection.commit() 
        
        # print(connection.execute(text('SELECT * from players')).fetchall())
        

if __name__ == '__main__':
    engine = create_db_engine()
    create_players_table(engine)
    insert_players(engine, table)
    
    df = pd.read_sql_table('players', engine)
    print(df)

