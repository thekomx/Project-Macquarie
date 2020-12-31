import pandas as pd
import sqlalchemy

from config import api_key, db_connection_string

const_insert_row_max = 999

json_df = pd.read_json(f'https://financialmodelingprep.com/api/v3/stock/list?apikey={api_key}')
json_df.drop(columns='price', inplace=True)
json_df.dropna()

db_engine = sqlalchemy.create_engine(db_connection_string)

# json_df.to_sql('Symbols', con=db_engine, if_exists='replace', index=False)

insert_value = ''
row_num = 0
for i, row in json_df.iterrows():
    symbol = str(row['symbol']).replace("'", "''")
    namex = str(row['name']).replace("'", "''")
    exchange = str(row['exchange']).replace("'", "''")
    insert_value += f"('{symbol}', '{namex}', '{exchange}'), "
    row_num += 1
    print(row_num)
    if (row_num >= const_insert_row_max)or(i == json_df.index[-1]):
        query = f'INSERT INTO Symbols (symbol, name, exchange) VALUES {insert_value[:len(insert_value)-2]}'
        db_engine.execute(query)
        insert_value = ''
        row_num = 0