import streamlit as st
import streamlit.components.v1 as components
import numpy as np
import pandas as pd

st.set_page_config(page_title= "Produksi Perikanan Tangkap dan Budidaya Indonesia", page_icon='icon.jpg',layout="wide")

st.sidebar.subheader('Analisis Produksi Perikanan Indonesia dan Potensi IoTnya')
st.sidebar.markdown(f"""
                   Analisis dilakukan berdasarkan data pada **[Statistik Kementerian Kelautan dan Perikanan (KKP)](https://statistik.kkp.go.id/)** dan **[Badan Pusat Statistik (BPS)](https://www.bps.go.id/)**.
                   """)

st.title("Produksi Perikanan Tangkap dan Budidaya Indonesia")

html_temp = """
<div class='tableauPlaceholder' id='viz1659499460459' style='position: relative'><noscript><a href='#'><img alt='Dashboard 4 ' 
src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Pe&#47;Perikanan_5&#47;Dashboard4&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'>
<param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> 
<param name='embed_code_version' value='3' /> 
<param name='site_root' value='' />
<param name='name' value='Perikanan_5&#47;Dashboard4' />
<param name='tabs' value='no' /><param name='toolbar' value='yes' />
<param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Pe&#47;Perikanan_5&#47;Dashboard4&#47;1.png' /> 
<param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' />
<param name='display_spinner' value='yes' />
<param name='display_overlay' value='yes' />
<param name='display_count' value='yes' />
<param name='language' value='en-US' /></object></div> 
               <script type='text/javascript'>   
                                var divElement = document.getElementById('viz1659499460459');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.height='777px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
    """
components.html(html_temp, width=1200, height=900)

st.caption('Ini caption dashboard')

st.header("Produksi Perikanan Tangkap dan Budidaya Indonesia 2000-2020")
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