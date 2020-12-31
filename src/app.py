import streamlit as st
import pandas as pd
import sqlalchemy
import json_module

from pathlib import Path
from PIL import Image
from config import db_connection_string, api_key

@st.cache
def get_stock_list():
    db_engine = sqlalchemy.create_engine(db_connection_string)
    db_query = "SELECT (symbol+' - '+name+' ('+exchange+')') AS stock, symbol, name, exchange FROM Symbols ORDER BY symbol"
    return pd.read_sql(db_query, con=db_engine)

@st.cache
def get_markdown(mdfile, directory=''):
    file_dir = Path.cwd().joinpath(Path(directory)).joinpath(mdfile)
    return Path(file_dir).read_text()


pages = st.sidebar.radio(('Navigation'), ('Home', 'Charts', 'MorningStar Dashboard', 'About'))
if pages == 'Charts':
    st.write('This is Charts Page!')
    stock_df = get_stock_list()
    stock_select = st.selectbox('Pick a stock', stock_df.stock)
    sel_stock_df = stock_df[stock_df.stock==stock_select]
    sel_symbol = sel_stock_df.iloc[0]['symbol']
    sel_name = sel_stock_df.iloc[0]['name']
    sel_exchange = sel_stock_df.iloc[0]['exchange']
    st.write('Symbol : '+sel_symbol)
    st.write('Company Name : '+sel_name)
    st.write('Exchange : '+sel_exchange)

    j = json_module.getJSON(f'https://financialmodelingprep.com/api/v3/quote-short/{sel_symbol}?apikey={api_key}')
    if j.status_code==200:
        st.write(j.json)
        st.header(j.json[0]['price'])
    else:
        st.write('Error!')

elif pages=='MorningStar Dashboard':
    st.write('This is MorningStar Dashboard Page!')

elif pages=='About':
    st.write('About Page')
else:
    home_markdown = get_markdown('home.md','src')
    st.markdown(home_markdown, unsafe_allow_html=True)
