import streamlit as st
import requests
import json

@st.cache
class getJSON:

    def __init__(self, url):

        req = requests.get(url)

        self.status_code = req.status_code
        self.reason = req.reason

        if req.status_code == 200:
            json_data = json.loads(req.text)
        else:
            json_data = {}

        self.json = json_data