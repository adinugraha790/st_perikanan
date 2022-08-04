import streamlit as st
import streamlit.components.v1 as components
import numpy as np
import pandas as pd

st.set_page_config(page_title= "", page_icon='icon.jpg',layout="wide")

st.sidebar.subheader('Analisis Produksi Perikanan Indonesia dan Potensi IoTnya')
st.sidebar.markdown(f"""
                   Analisis dilakukan berdasarkan data pada **[Statistik Kementerian Kelautan dan Perikanan (KKP)](https://statistik.kkp.go.id/)** dan **[Badan Pusat Statistik (BPS)](https://www.bps.go.id/)**.
                   """)

st.title("Angka Konsumsi Ikan Indonesia")

html_temp = """<div class='tableauPlaceholder' id='viz1659574309804' style='position: relative'><noscript><a href='#'><img alt='AKI ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;5_&#47;5_5AngkaKonsumsiIkanbdsProvinsi&#47;AKI&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='5_5AngkaKonsumsiIkanbdsProvinsi&#47;AKI' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;5_&#47;5_5AngkaKonsumsiIkanbdsProvinsi&#47;AKI&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1659574309804');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.height='777px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
components.html(html_temp, width=1200, height=900)


st.header("")
with st.expander("Lihat wawasan penting", expanded=True):
    st.markdown("""**Wawasan penting**""")
    lst = ['Angka Konsumsi Ikan (AKI) untuk kebanyakan provinsi di Indonesia cenderung naik setiap tahunnya, dengan konsumsi tertinggi ada pada Provinsi Kalimantan Timur', 
        'AKI Indonesia jauh dari target konsumsi perikanan nasional']

    s = ''

    for i in lst:
        s += "- " + i + "\n"

    st.markdown(s)

html_temp = """<div class='tableauPlaceholder' id='viz1659574521041' style='position: relative'><noscript><a href='#'><img alt='CumAKID ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;1_&#47;1_5KumulatifAKIdanJumlahPenduduk&#47;CumAKID&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='1_5KumulatifAKIdanJumlahPenduduk&#47;CumAKID' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;1_&#47;1_5KumulatifAKIdanJumlahPenduduk&#47;CumAKID&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1659574521041');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.height='727px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
components.html(html_temp, width=1200, height=900)
st.caption('Mohon diperhatikan bahwa satuan AKI dan Jumlah Penduduk berbeda.')

with st.container():
    st.markdown("""Angka Konsumsi Ikan (AKI) adalah jumlah kilogram ikan yang dikonsumsi masyarakat Indonesia selama satu tahun dalam bantuk konversi setara konsumsi ikan utuh segar . Angka Konsumsi Ikan (AKI) untuk kebanyakan provinsi di Indonesia cenderung naik setiap tahunnya, dengan konsumsi tertinggi ada pada Provinsi Kalimantan Timur. Namun meskipun begitu, konsumsi ikan Kalimantan Timur yang ada di sekitar 45 kg per kapita per tahun masih jauh dari target konsumsi perikanan nasional 2019 (54,5 kg per kapita per tahun) . Sementara itu, pulau atau kepulauan yang mempunyai AKI tinggi adalah Pulau Kalimantan, Pulau Sulawesi, Kepulauan Maluku, dan Pulau Papua.""")




# Akhir page
with st.expander("Referensi", expanded=False):
    st.markdown("**Literatur:**")
    lst = ['FAQ Tentang Penghitungan Angka Konsumsi Ikan Nasional | KKP | Kementerian Kelautan dan Perikanan', 
        'Nurmawati, et al. (2021). GEMARIKAN WARGA KELURAHAN MANGGAR BARU, BALIKPAPAN TIMUR : KONSUMSI IKAN KEKINIAN MELALUI INOVASI PRODUK OLAHAN IKAN. Seminar Nasional Pengabdian Kepada Masyarakat (SEPAKAT), Volume 1, Issue 1.']

    s = ''

    for i in lst:
        s += "- " + i + "\n"

    st.markdown(s)

with st.expander("Metode dan/atau Kode", expanded=False):
    st.markdown("**Metode:**")
    lst = ['Modifikasi data dilakukan dengan Microsoft Excel', 
        'Visualisasi data dilakukan dengan Tableau',
        'Model Regresi Linier dilakukan untuk memprediksi jumlah penduduk yang nullr']

    s = ''

    for i in lst:
        s += "- " + i + "\n"

    st.markdown(s)
    st.code("""import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

pop = pd.read_excel('Populasi Indonesia - ML.xlsx')
pop # pop adalah dataframe berisi kolom Tahun dan jumlah penduduk (JP)

%matplotlib inline
plt.xlabel('Tahun')
plt.ylabel('Jumlah Penduduk')
plt.scatter(pop.Tahun, pop['JP'], color='red', marker='*')
# plot scatter untuk melihat tren dan persebaran data

reg = linear_model.LinearRegression()
reg.fit(pop[['Tahun']], pop.JP) # dilakukan prediksi model regresi linier

pop_new = pop

for i in range(2011,2015):
  pend = int(reg.predict([[i]]))
  prd = {'Tahun': i, 'JP': pend}
  pop_new = pop_new.append(prd, ignore_index=True)

# dilakukan iterasi prediksi untuk tahun 2011-2014

pop_new = pop_new.sort_values('Tahun')
pop_new

""")