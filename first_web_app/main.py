import streamlit as st

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
