import streamlit as st

from pathlib import Path

@st.cache
def get_markdown(mdfile, directory='src/md'):
    file_dir = Path.cwd().joinpath(Path(directory)).joinpath(mdfile)
    return Path(file_dir).read_text()