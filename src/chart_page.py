
import streamlit as st
import sqlalchemy
import pandas as pd
import plotly.graph_objects as go

from config import db_connection_string, api_key
from json_module import getJSON
from chart_config import chartTemplate

@st.cache
def get_stock_list():
    db_engine = sqlalchemy.create_engine(db_connection_string)
    db_query = "SELECT (symbol+' - '+name+' ('+exchange+')') AS stock, symbol, name, exchange FROM Symbols ORDER BY symbol"
    return pd.read_sql(db_query, con=db_engine)

def get_chart():
    stock_df = get_stock_list()
    list_default = 'Choose from the dropdown list or start typing'
    list_default_df = pd.DataFrame({'stock':list_default, 'symbol':'', 'name':'', 'exchange':''}, index=[0])
    stock_df = pd.concat([list_default_df, stock_df]).reset_index(drop = True)
    stock_select = st.selectbox('Pick a stock', stock_df.stock)
    if stock_select != list_default_df.stock[0]:
        sel_stock_df = stock_df[stock_df.stock==stock_select]
        sel_symbol = sel_stock_df.iloc[0]['symbol']
        sel_name = sel_stock_df.iloc[0]['name']
        # sel_exchange = sel_stock_df.iloc[0]['exchange']
        st.title(f'{sel_name} ({sel_symbol})')
        # st.title(sel_symbol)

        profile_expand = st.beta_expander('Profile')
        with profile_expand:
            j = getJSON(f'https://financialmodelingprep.com/api/v3/profile/{sel_symbol}?apikey={api_key}')
            if j.status_code==200:
                profile_df = pd.DataFrame(j.json).set_index('symbol')
                # st.table(profile_df.T)
                for i in profile_df.T.itertuples():
                    col0, col1 = st.beta_columns((1,3))
                    col0.markdown(f'**{i[0]}**')
                    col1.write(f'{i[1]}')
            else:
                st.write('Error!')
                st.write(j.reason)
        
        chart_expand = st.beta_expander('Chart')
        with chart_expand:
            chart_json = getJSON(f'https://financialmodelingprep.com/api/v3/historical-price-full/{sel_symbol}?apikey={api_key}')
            if chart_json.status_code==200:
                if len(chart_json.json)>0:
                    chart_df = pd.DataFrame(chart_json.json['historical'])
                    price_chart_df = pd.DataFrame(chart_df, columns=['date', 'close'])

                    fig = go.Figure(go.Scatter(x=price_chart_df['date'], y=price_chart_df['close'], line=dict(color='#045FB4', width=2)))
                    fig.update_layout(chartTemplate('Historical Share Price').layout)
                    st.plotly_chart(fig, use_container_width=True)
                else:
                    st.write('No historical price found!')
            else:
                st.write('Error!')
                st.write(chart_json.reason)
