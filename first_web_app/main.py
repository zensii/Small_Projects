import streamlit as st
import pandas


st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.image('images/photo.png')

with col2:
    st.title('Svetlin Ivanov')
    content = '''
    Hi, I am Svetlin! A Python programmer student and aspiring data scientist.
    '''
    st.write(content)

st.write('some text bellow the picture. Writing more text to see if it will exend past the width of a column. And it actually extended past the width')

col3, empty_col,  col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv('data.csv', sep=';')

with col3:
    for index, col in df[:10].iterrows():
        st.header(col['title'])
        st.write(col['description'])
        st.image('images/' + col['image'])
        st.write(f"[Source code]({col['url']})")

with col4:
    for index, col in df[10:].iterrows():
        st.header(col['title'])
        st.write(col['description'])
        st.image('images/' + col['image'])
        st.write(f"[Source code]({col['url']})")