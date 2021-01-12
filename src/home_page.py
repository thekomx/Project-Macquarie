import streamlit as st
import pandas as pd
import plotly.graph_objects as go

from src.config import api_key
from src.markdown_module import get_markdown
from src.json_module import getJSON
from src.chart_config import chartTemplate

def get_chart():
    j = getJSON(f'https://financialmodelingprep.com/api/v3/historical-price-full/MQG.AX?from=2020-01-01&to=2020-12-31&apikey={api_key}')
    if (j.status_code==200)and(len(j.json)>0):
        price_df = pd.DataFrame(j.json['historical'])
        fig = go.Figure(data=[go.Candlestick(x=price_df['date'],
                                            open=price_df['open'], close=price_df['close'],
                                            high=price_df['high'], low=price_df['low'],
                                            increasing_line_color= '#04B404', decreasing_line_color= '#B40404')])
        fig.update_layout(chartTemplate('Year 2020 Historical Share Price').layout, height=550)
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.write('Server error!')
        st.write('Refresh page to try again.')
        pass


def home():
    st.markdown(get_markdown('home.md'), unsafe_allow_html=True)

    # st.title('About')
    st.title('')
    st.write('Macquarie is a global financial services group operating in 31 markets in asset management, retail and business banking, wealth management, leasing and asset financing, market access, commodity trading, renewables development, investment banking and principal investment.')
    st.write('The diversity of our operations, combined with a strong capital position and robust risk management framework, has contributed to our 51-year record of unbroken profitability.')
    st.markdown('[Leran more ...](https://www.macquarie.com/au/en/about.html)')

    st.title('Share Price :')
    get_chart()