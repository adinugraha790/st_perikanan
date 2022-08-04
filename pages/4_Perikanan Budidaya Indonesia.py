import streamlit as st
import streamlit.components.v1 as components
import numpy as np
import pandas as pd

st.set_page_config(page_title= "", page_icon='icon.jpg',layout="wide")

st.sidebar.subheader('Analisis Produksi Perikanan Indonesia dan Potensi IoTnya')
st.sidebar.markdown(f"""
                   Analisis dilakukan berdasarkan data pada **[Statistik Kementerian Kelautan dan Perikanan (KKP)](https://statistik.kkp.go.id/)** dan **[Badan Pusat Statistik (BPS)](https://www.bps.go.id/)**.
                   """)

st.title("Perikanan Budidaya Indonesia")

html_temp = """<div class='tableauPlaceholder' id='viz1659569856749' style='position: relative'><noscript><a href='#'><img alt='VolProdKomd ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;4_&#47;4_2VolumeProduksiberdasarkanKomoditasJenisUsaha&#47;VolProdKomd&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='4_2VolumeProduksiberdasarkanKomoditasJenisUsaha&#47;VolProdKomd' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;4_&#47;4_2VolumeProduksiberdasarkanKomoditasJenisUsaha&#47;VolProdKomd&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1659569856749');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.height='727px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
components.html(html_temp, width=1200, height=900)

st.caption('Grafik ini menunjukkan pertumbuhan total produksi budidaya perikanan (dalam persen) pada 5 pulau dan 2 kepulauan besar di Indonesia menurut Tim Penyusunan Buana Raya (2012).')
st.caption('Mohon dilihat untuk yang Budidayanya saja')

html_temp = """<div class='tableauPlaceholder' id='viz1659571158951' style='position: relative'><noscript><a href='#'><img alt='AnnualGwthD ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;4_&#47;4_1AnnualGrowthBudidayaPerikananMs2Pulau&#47;AnnualGwthD&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='4_1AnnualGrowthBudidayaPerikananMs2Pulau&#47;AnnualGwthD' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;4_&#47;4_1AnnualGrowthBudidayaPerikananMs2Pulau&#47;AnnualGwthD&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1659571158951');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1000px';vizElement.style.height='1277px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1000px';vizElement.style.height='1277px';} else { vizElement.style.width='100%';vizElement.style.height='727px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
components.html(html_temp, width=1200, height=900)

st.subheader("Volume Produksi Perikanan Budidaya Tahunan berdasarkan Komoditas")
with st.expander("Lihat wawasan penting", expanded=True):
    st.markdown("""**Wawasan penting**""")
    lst = ['Pulau/kepulauan dengan pertumbuhan total produksi perikanan budidaya tertinggi adalah Kepulauan Maluku dengan pertumbuhan tertinggi sebesar 2.509%.', 
        'Kepulauan Nusa Tenggara dan Pulau Papua adalah yang tertinggi pertumbuhan total produksi perikanan budidayanya setelah Kepulauan Maluku', 
        'Pulau lainnya di Indonesia cenderung berfluktuasi pertumbuhannya, namun tidak terlalu besar']

    s = ''

    for i in lst:
        s += "- " + i + "\n"

    st.markdown(s)

with st.container():
    st.markdown("""Pulau dengan pertumbuhan total produksi budidaya perikanan adalah Kepulauan Maluku (Provinsi Maluku dan Maluku Utara) pada tahun 2004 dan 2002 dengan pertumbuhan 2.509% dan 1.582%, dan Kepulauan Nusa Tenggara pada tahun 2004 yaitu 885%.""")
    st.markdown('Kepulauan Maluku memiliki pertumbuhan yang sangat besar pada tahun 2002 dan 2004 seperti yang sudah disebutkan di atas. Meskipun sempat menurun tajam, Kepulauan Maluku juga mengalami kenaikan yang tinggi sebesar 331% pada tahun 2007, 484% pada tahun 2010, dan 108% pada tahun 2011. Walaupun begitu, fluktuasi meningkat dan menurun terjadi pada tahun setelahnya dan pada tahun 2020 mengalami penurunan sebesar 60%.')
    st.markdown('Kepulauan Nusa Tenggara juga mengalami kenaikan total produksi perikanan budidaya yang pesat pada tahun 2004 (885%), 2005 (75%), dan 2006 (50%). Setelah tahun tersebut umumnya terjadi fluktuasi, dengan pengecualian pada tahun 2013 (147%). Pulau Papua umumnya mengalami fluktuasi total produksi perikanan budidaya pada rentang 2001-2020, dengan kenaikan cukup hebat terjadi pada tahun 2002 (96%), 2005 (118%), dan 2008 (186%).')
    st.markdown('Pertumbuhan di pulau-pulau lainnya tidak menyimpang dari 100%, Seperti di Pulau Jawa misalnya, pertumbuhan total produksi perikanan budidaya ada pada tahun 2002 (54%) dan 2010 (40%). Selain tahun tersebut, fluktuasi pertumbuhan total produksi perikanan budidaya berada di kisaran -24% hingga 33%. Pada pertumbuhan total produksi perikanan budidaya di Pulau Kalimantan, umumnya hanya terjadi kenaikan total produksi perikanan budidaya, kenaikan tertinggi ada pada tahun 2007 (85%). Sementara itu, penurunan total produksi perikanan budidaya (atau persentase negatif) terjadi pada tahun 2006 (-30%), dan 2019 (-13%).')
    st.markdown('Selain pulau dan kepulauan yang telah disebutkan, ada Pulau Sulawesi dan Sumatera. Pertumbuhan total produksi perikanan budidaya di Pulau Sulawesi cenderung positif atau terjadi kenaikan atau stagnasi total produksi perikanan budidaya pada rentang tahun 2001-2017. Pertumbuhan tertinggi ada pada tahun 2004 (70%) dan 2005 (79%). Sementara itu, pertumbuhan total produksi perikanan budidaya di Pulau Sumatera cenderung positif, dengan penurunan terjadi pada tahun 2004 (-24%) dan 2020 (-12%). Pertumbuhan maksimal total produksi perikanan budidaya ada pada tahun 2002 (89%).')


html_temp = """<div class='tableauPlaceholder' id='viz1659570351241' style='position: relative'><noscript><a href='#'><img alt='N&amp;PBD ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;5_&#47;5_2JumlahNelayandanPembudidayabdsProvinsi&#47;NPBD&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='5_2JumlahNelayandanPembudidayabdsProvinsi&#47;NPBD' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;5_&#47;5_2JumlahNelayandanPembudidayabdsProvinsi&#47;NPBD&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1659570351241');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.height='827px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
components.html(html_temp, width=1200, height=900)

st.caption('Mohon dilihat untuk Pembudidayanya saja (Nelayan di-exclude)')

st.subheader("Jumlah Pembudidaya berdasarkan Provinsi")
with st.expander("Lihat wawasan penting", expanded=True):
    st.markdown("""**Wawasan penting**""")
    lst = ['Pembudidaya populasinya cenderung meningkat namun dapat berfluktuasi tajam', 
        'Jumlah nelayan cenderung lebih stabil populasinya', 
        ]

    s = ''

    for i in lst:
        s += "- " + i + "\n"

    st.markdown(s)

with st.container():
    st.markdown("""Pada kebanyakan provinsi, pembudidaya cenderung lebih banyak daripada nelayan laut dan nelayan PUD. Namun, jumlah pembudidaya di setiap provinsi dapat fluktuasi dengan cukup tajam. Berbeda dengan jumlah nelayan laut dan PUD yang pada kebanyakan provinsi cenderung tidak mengalami fluktuasi yang tajam. Ini terdapat kemungkinan bahwa terjadinya usaha pembudidaya baru untuk melakukan kegiatan budidaya, namun karena terjadinya kerugian ataupun modal yang tidak cukup sehingga usaha dihentikan. Pola terjadinya fluktuasi tersebut berbeda-beda tiap provinsi. Berbeda dengan profesi nelayan yang kemungkinan besar akan mendapatkan hasil perikanan dari laut.""")
    st.markdown('Kenaikan yang tajam ini terjadi contohnya pada provinsi Jawa Barat dan Jawa Tengah, pada tahun 2012, pembudidaya pada Provinsi Jawa Barat sangat tinggi, namun ketika tahun 2015 menjadi sangat kecil. Kenaikan yang tajam ini juga terjadi pada tahun 2018, dengan penurunan kembali pada tahun selanjutnya. Menariknya bersamaan dengan kenaikan tersebut, pembudidaya di provinsi lain cenderung turun.')


html_temp = """<div class='tableauPlaceholder' id='viz1659570798356' style='position: relative'><noscript><a href='#'><img alt='LUB&amp;ProdBD ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;5_&#47;5_4LuasUsahadanProduksiBudidayabdsJenisnya&#47;LUBProdBD&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='5_4LuasUsahadanProduksiBudidayabdsJenisnya&#47;LUBProdBD' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;5_&#47;5_4LuasUsahadanProduksiBudidayabdsJenisnya&#47;LUBProdBD&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1659570798356');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.height='727px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
components.html(html_temp, width=1200, height=900)

st.caption('Mohon dilihat untuk Pembudidayanya saja (Nelayan di-exclude)')

st.subheader("Luas Usaha dan Produksi Budidaya berdasarkan Jenisnya")
with st.expander("Lihat wawasan penting", expanded=True):
    st.markdown("""**Wawasan penting**""")
    lst = ['-	Luas usaha kolam dan sawah cenderung berfluktuasi dan trennya tidak begitu meningkat, namun produksinya yang meningkat', 
        '-	Luas usaha keramba, tambak, dan budidaya laut cenderung mengalami tren meningkat, dan produksinya pun cenderung meningkat', 
        '-	Luas usaha budidaya jaring apung dan jaring tancap bertambah,namun terdapat penurunan pada produksi budidaya jaring apung (2016) dan produksi budidaya jaring tancap (2015).']

    s = ''

    for i in lst:
        s += "- " + i + "\n"

    st.markdown(s)

with st.container():
    st.markdown("""Luas usaha kolam dan sawah cenderung berfluktuasi dan trennya tidak begitu meningkat, namun produksinya yang meningkat. Ini dapat terjadi karena penggunaan sistem budidaya yang lebih baik, seperti biofloc dibanding budidaya konvensional, atau intensifikasi terjadi misalnya dengan penggunaan metode recirculating aquaculture system (RAS) atau dengan penggunaan nanobubble.""")
    st.markdown('Luas usaha keramba, tambak, dan budidaya laut cenderung mengalami tren meningkat, dan produksinya pun cenderung meningkat. Ini terjadi karena perluasan usaha budidaya laut cenderung sebanding dengan peningkatan produksinya. ')
    st.markdown('Luas usaha budidaya jaring apung dan jaring tancap memiliki anomali, karena ketika luas usaha bertambah, terdapat penurunan pada produksi budidaya jaring apung (2016) dan produksi budidaya jaring tancap (2015). Ini dapat terjadi karena kualitas air yang buruk karena mengandalkan perairan terbuka untuk usaha budidayanya, atau terdapat penyakit dan atau mikroorganisme yang menyebabkan kematian massal dan menurunnya produksi komoditas di kedua jenis usaha tersebut.')


# Akhir page
with st.expander("Referensi", expanded=False):
    st.markdown("**Literatur:**")
    lst = ['Junaidi, et al., 2022. Floating cage aquaculture production in Indonesia: Assessment of opportunities and challenges in Lake Maninjau. AIMS Environmental Science, Volume 9, Issue 1: 1-15.', 
        'Penerapan Nanobubble Budidaya Vanameii | Dinas Kelautan dan Perikanan Provinsi Banten',
        'Atlas Global Buana Raya | Perpustakaan Daerah Kabupaten Banyuwangi (banyuwangikab.go.id)']

    s = ''

    for i in lst:
        s += "- " + i + "\n"

    st.markdown(s)

with st.expander("Metode dan/atau Kode", expanded=False):
    st.markdown("**Metode:**")
    lst = ['Modifikasi data dilakukan dengan Microsoft Excel', 
        'Visualisasi data dilakukan dengan Tableau']

    s = ''

    for i in lst:
        s += "- " + i + "\n"

    st.markdown(s)