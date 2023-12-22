import streamlit as st
from PIL import Image

st.set_page_config(layout="wide")

# Titre de l'application
st.title(" Stack Overflow recommendation")

title = st.text_input('Entrer la question', '  ')

st.button("Submit", type="primary")

options = st.multiselect(
    'topic',
    ['Tag1', 'Tag2', 'Tag3', 'Tag4'])
