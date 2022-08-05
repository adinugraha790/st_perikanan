import streamlit as st
import streamlit.components.v1 as components
import numpy as np
import pandas as pd

st.set_page_config(page_title= "", page_icon='icon.jpg',layout="wide")

st.sidebar.subheader('Analisis Produksi Perikanan Indonesia dan Potensi IoTnya')
st.sidebar.markdown(f"""
                   Analisis dilakukan berdasarkan data pada **[Statistik Kementerian Kelautan dan Perikanan (KKP)](https://statistik.kkp.go.id/)** dan **[Badan Pusat Statistik (BPS)](https://www.bps.go.id/)**.
                   """)

st.title("Perikanan Tangkap Indonesia")

html_temp = """<div class='tableauPlaceholder' id='viz1659572010036' style='position: relative'><noscript><a href='#'><img alt='VolProdKomd ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;4_&#47;4_2VolumeProduksiberdasarkanKomoditasJenisUsaha&#47;VolProdKomd&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='4_2VolumeProduksiberdasarkanKomoditasJenisUsaha&#47;VolProdKomd' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;4_&#47;4_2VolumeProduksiberdasarkanKomoditasJenisUsaha&#47;VolProdKomd&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1659572010036');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.height='727px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
components.html(html_temp, width=1200, height=900)

st.caption('Mohon dilihat Jenis Usaha Tangkap Laut dan PUD saja (Budidaya di exclude)')

st.subheader("Volume Produksi Perikanan Tangkap Tahunan berdasarkan Komoditas")
with st.expander("Lihat wawasan penting", expanded=True):
    st.markdown("""**Wawasan penting**""")
    lst = ['Komoditas dengan volume produksi total terbanyak jenis usaha tangkap laut adalah ikan tongkol, layang, cakalang, tuna, dan kakap', 
        'Komoditas dengan volume produksi total terbanyak jenis usaha tangkap darat adalah ikan nila, patin, dan gabus.']

    s = ''

    for i in lst:
        s += "- " + i + "\n"

    st.markdown(s)

with st.container():
    st.markdown("""Komoditas yang memiliki volume produksi total terbanyak pada jenis usaha tangkap laut adalah ikan tongkol (581.057 ton), ikan layang (548.645 ton), ikan cakalang (468.258 ton), ikan tuna (300.791 ton) dan ikan kakap (292.531 ton).""")
    st.markdown('Komoditas yang memiliki volume produksi total terbanyak pada jenis usaha tangkap perairan umum daratan (PUD) adalah ikan nila (57.849 ton), ikan patin (53.088 ton), dan ikan gabus (59.510 ton).')

st.image('wpp.png')
st.caption('Wilayah Pengelolaan Perikanan di Indonesia')

html_temp = """<div class='tableauPlaceholder' id='viz1659572533346' style='position: relative'><noscript><a href='#'><img alt='TPKomoditas ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;4_&#47;4_4TingkatPemanfaatanKomoditasdiWPP&#47;TPKomoditas_1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='4_4TingkatPemanfaatanKomoditasdiWPP&#47;TPKomoditas_1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;4_&#47;4_4TingkatPemanfaatanKomoditasdiWPP&#47;TPKomoditas_1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1659572533346');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1000px';vizElement.style.height='1527px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1000px';vizElement.style.height='1527px';} else { vizElement.style.width='100%';vizElement.style.height='727px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
components.html(html_temp, width=1200, height=1500)

st.subheader("Tingkat Pemanfaatan Ikan berdasarkan Wilayah Pengelolaan Perikanan berdasarkan Kepmen No. 50/2017 & No.19/2022")
with st.expander("Lihat wawasan penting", expanded=True):
    st.markdown("""**Wawasan penting**""")
    lst = ['WPP 571, 572, dan 714 mengalami penambahan komoditas yang statusnya over-exploited', 
        'WPP 573, 711, 712, 713, 715, 716, dan 717 mengalami penurunan komoditas yang statusnya over-exploited',
        'Ikan karang dan lobster pada WPP 573 mempunyai status pemanfaatan yang sangat over-exploited']

    s = ''

    for i in lst:
        s += "- " + i + "\n"

    st.markdown(s)

with st.container():
    st.markdown("""Wilayah Pengelolaan Perikanan Negara Republik Indonesia adalah wilayah pengelolaan perikanan untuk penangkapan ikan, pembudidayaan ikan, konservasi, penelitian, dan pengembangan perikanan yang meliputi perairan pedalaman, perairan kepulauan, laut territorial, zona tambahan, dan zona ekonomi eksklusif, dikutip dari Peraturan Menteri Kelautan dan Perikanan RI No. 18/2014. Pada grafik adalah Tingkat Pemanfaatan Komoditas Ikan berdasarkan Keputusan Menteri Kelautan dan Perikanan No. 50/2017 dan No. 19/2022.""")
    st.markdown('Tingkat pemanfaatan adalah suatu indikator yang menunjukkan tingkat termanfaatkannya suatu komoditas di Wilayah Pengelolaan Perikanan (WPP) di Indonesia. Ketika tingkat pemanfaatannya kurang dari 0.5, maka penangkapannya boleh ditambah. Mengutip keputusan Menteri di atas, ketika tingkat pemanfaatannya antara 0.5 dan 1, maka komoditas tersebut sudah fully exploited dan penangkapannya perlu dimonitor ketat. Sedangkan ketika tingkat pemanfaatannya lebih dari 1, berarti komoditas tersebut over-exploited dan upaya penangkapan harus dikurangi .')
    st.markdown('Pada WPP 571, WPP572, dan WPP714 terdapat masing-masing 5, 5, 3 komoditas yang statusnya over-exploited berdasarkan Kepmen KP No.19/2022, bertambah dari masing-masing 2, 1, 2 komoditas pada Kepmen KP No.50/2017. Berbeda dengan WPP yang baru saja disebutkan, WPP573, 711, 712, 713, 715, 716, dan 717 mengalami penurunan jumlah komoditas yang mempunyai status over-exploited dari Kepmen KP No.50/2017 ke Kepmen KP No.19/2022. Namun perlu diingat bahwa WPP 573 dan WPP 711 mempunyai komoditas dengan tingkat pemanfaatan mendekati dan melebihi 2. Untuk WPP 573 adalah ikan karang (2), dan lobster (2.5), sedangkan untuk WPP 711 adalah kepiting (1.9).')


html_temp = """<div class='tableauPlaceholder' id='viz1659572624360' style='position: relative'><noscript><a href='#'><img alt='N&amp;PBD ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;5_&#47;5_2JumlahNelayandanPembudidayabdsProvinsi&#47;NPBD&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='5_2JumlahNelayandanPembudidayabdsProvinsi&#47;NPBD' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;5_&#47;5_2JumlahNelayandanPembudidayabdsProvinsi&#47;NPBD&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1659572624360');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.height='827px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
components.html(html_temp, width=1200, height=900)
st.caption('Mohon untuk dilihat nelayan laut dan PUDnya saja.')

st.subheader("Jumlah Nelayan berdasarkan Provinsi")
with st.expander("Lihat wawasan penting", expanded=True):
    st.markdown("""**Wawasan penting**""")
    lst = ['Jumlah nelayan cenderung lebih stabil populasinya']

    s = ''

    for i in lst:
        s += "- " + i + "\n"

    st.markdown(s)

with st.container():
    st.markdown("""Pada kebanyakan provinsi, pembudidaya cenderung lebih banyak daripada nelayan laut dan nelayan PUD. Namun, jumlah pembudidaya di setiap provinsi dapat fluktuasi dengan cukup tajam. Berbeda dengan jumlah nelayan laut dan PUD yang pada kebanyakan provinsi cenderung tidak mengalami fluktuasi yang tajam. Ini terdapat kemungkinan bahwa terjadinya usaha pembudidaya baru untuk melakukan kegiatan budidaya, namun karena terjadinya kerugian ataupun modal yang tidak cukup sehingga usaha dihentikan. Pola terjadinya fluktuasi tersebut berbeda-beda tiap provinsi. Berbeda dengan profesi nelayan yang kemungkinan besar akan mendapatkan hasil perikanan dari laut.""")
    st.markdown('Kenaikan yang tajam ini terjadi contohnya pada provinsi Jawa Barat dan Jawa Tengah, pada tahun 2012, pembudidaya pada Provinsi Jawa Barat sangat tinggi, namun ketika tahun 2015 menjadi sangat kecil. Kenaikan yang tajam ini juga terjadi pada tahun 2018, dengan penurunan kembali pada tahun selanjutnya. Menariknya bersamaan dengan kenaikan tersebut, pembudidaya di provinsi lain cenderung turun.')

html_temp = """<div class='tableauPlaceholder' id='viz1659572877482' style='position: relative'><noscript><a href='#'><img alt='KPLPRODT ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;5_&#47;5_6JumlahKapalTangkapIkandanProduksinya&#47;KPLPRODT&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='5_6JumlahKapalTangkapIkandanProduksinya&#47;KPLPRODT' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;5_&#47;5_6JumlahKapalTangkapIkandanProduksinya&#47;KPLPRODT&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1659572877482');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.height='727px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
components.html(html_temp, width=1200, height=900)
st.caption('Mohon untuk dilihat nelayan laut dan PUDnya saja.')

st.subheader("Jumlah Kapal Tangkap Ikan dan Produksinya")
with st.expander("Lihat wawasan penting", expanded=True):
    st.markdown("""**Wawasan penting**""")
    lst = ['Jumlah perahu perikanan tangkap laut cenderung menurun, namun produksi perikanan tangkapnya naik',
    'Jumlah perahu untuk perikanan tangkap darat juga berfluktuasi cenderung stabil, namun untuk produksi perikanan tangkap daratnya cenderung naik']

    s = ''

    for i in lst:
        s += "- " + i + "\n"

    st.markdown(s)

with st.container():
    st.markdown("""Jumlah perahu untuk perikanan tangkap laut berfluktuasi cenderung menurun, namun produksi perikanan tangkapnya naik. Jumlah perahu untuk perikanan tangkap darat juga berfluktuasi cenderung stabil, namun untuk produksi perikanan tangkap daratnya cenderung naik. Kedua tren ini dapat terjadi karena manajemen dan monitor WPP yang baik, atau karena total produksinya belum memenuhi Maximum Sustainable Yield, ataupun meningkatnya kualitas manajemen penangkapan ikan. """)


# Akhir page
with st.expander("Referensi", expanded=False):
    st.markdown("**Literatur:**")
    lst = ["""Malin L. Pinsky, Rebecca L. Selden,
Chapter 2 - Climate Variability, Climate Change, and Conservation in a Dynamic Ocean,
Editor(s): Phillip S. Levin, Melissa R. Poe,
Conservation for the Anthropocene Ocean,
Academic Press,
2017,
Pages 23-38"""]

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
