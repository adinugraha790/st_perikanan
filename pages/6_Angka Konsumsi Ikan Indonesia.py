import streamlit as st
import streamlit.components.v1 as components
import numpy as np
import pandas as pd

st.set_page_config(page_title= "", page_icon='icon.jpg',layout="wide")

st.sidebar.subheader('Analisis Produksi Perikanan Indonesia dan Potensi IoTnya')
st.sidebar.markdown(f"""
                   Analisis dilakukan berdasarkan data pada **[Statistik Kementerian Kelautan dan Perikanan (KKP)](https://statistik.kkp.go.id/)** dan **[Badan Pusat Statistik (BPS)](https://www.bps.go.id/)**.
                   """)

st.title("")

html_temp = """"""
components.html(html_temp, width=1200, height=900)

st.caption('Ini caption dashboard')

st.header("")
with st.expander("Lihat wawasan penting", expanded=True):
    st.markdown("""**Wawasan penting**""")
    lst = ['a', 
        'b', 
        'c']

    s = ''

    for i in lst:
        s += "- " + i + "\n"

    st.markdown(s)

with st.container():
    st.markdown("""_________________""")


# Akhir page
with st.expander("Referensi", expanded=False):
    st.markdown("**Data:**")
    lst = ['a', 
        'b', 
        'c']

    s = ''

    for i in lst:
        s += "- " + i + "\n"

    st.markdown(s)

    st.markdown("**Lainnya:**")
    lst = ['a', 
            'b', 
            'c']

    s = ''

    for i in lst:
        s += "- " + i + "\n"

    st.markdown(s)

with st.expander("Metode dan/atau Kode", expanded=False):
    st.markdown("**Metode:**")
    lst = ['a', 
        'b', 
        'c']

    s = ''

    for i in lst:
        s += "- " + i + "\n"

    st.markdown(s)