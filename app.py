import streamlit as st
from src import home_page, chart_page

from src.markdown_module import get_markdown


#--- Available Contents
page_home = 'HOME'
page_chart = 'Charts'
page_morningstar = 'MorningStar Dashboard'
page_about = 'About'
pages = (page_home, page_chart, page_morningstar, page_about)

def main():
#--- Add Logo to Sidebar
    st.sidebar.markdown(get_markdown('logo.md'), unsafe_allow_html=True)

    #--- Add Menu to Sidebar
    page_selected = st.sidebar.radio('Navigation', pages)
    if page_selected == page_chart:
        chart_page.get_chart()

    elif page_selected==page_morningstar:
        st.write('This is MorningStar Dashboard Page!')

    elif page_selected==page_about:
        st.write('This is About Page!')

    else: #--- HOME Page
        home_page.home()

if __name__ == "__main__":
    main()