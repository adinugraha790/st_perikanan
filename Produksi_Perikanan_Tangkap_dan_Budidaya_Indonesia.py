import streamlit as st
import streamlit.components.v1 as components
import numpy as np
import pandas as pd

st.set_page_config(page_title= "Produksi Perikanan Tangkap dan Budidaya Indonesia", page_icon='icon.jpg',layout="wide")

st.sidebar.subheader('Analisis Produksi Perikanan Indonesia dan Potensi IoTnya')
st.sidebar.markdown(f"""
                   Analisis dilakukan berdasarkan data pada **[Statistik Kementerian Kelautan dan Perikanan (KKP)](https://statistik.kkp.go.id/)** dan **[Badan Pusat Statistik (BPS)](https://www.bps.go.id/)**.
                   \n(klik tanda v untuk melihat lebih banyak)""")
st.sidebar.markdown('**[Adi Nugraha, 2022](https://id.linkedin.com/in/adinugraha790)**')

st.title("Produksi Perikanan Tangkap dan Budidaya Indonesia")
st.subheader("Produksi Perikanan Tangkap dan Budidaya Indonesia 2000-2020")
html_temp = """
<div class='tableauPlaceholder' id='viz1659563949195' style='position: relative'><noscript><a href='#'><img alt='Dashboard 2 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;1_&#47;1_1ProduksiTotalPerikanan&#47;Dashboard2&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='1_1ProduksiTotalPerikanan&#47;Dashboard2' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;1_&#47;1_1ProduksiTotalPerikanan&#47;Dashboard2&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1659563949195');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.height='727px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
components.html(html_temp, width=1200, height=900)

st.caption('')

with st.expander("Lihat wawasan penting", expanded=True):
    st.markdown("""**Wawasan penting**""")
    lst = ['Kontribusi perikanan budidaya terhadap produksi total meningkat dari 16% ke 68% pada rentang tahun 2000-2020', 
        'Produksi perikanan tangkap cenderung stabil mengalami kenaikan 2-8%, namun pada tahun 2020 menurun 9.5%', 
        'Produksi perikanan budidaya laut meningkat pesat menyusun 0.6% (2000) ke 60% (2013-sekarang) produksi total perikanan laut',
        'Pandemi COVID-19 diperkirakan merupakan penyebab turunnya perikanan tangkap pada tahun 2020']

    s = ''

    for i in lst:
        s += "- " + i + "\n"

    st.markdown(s)

with st.container():
    st.markdown("""Total produksi perikanan tangkap dan budidaya (termasuk rumput laut) meningkat dari 4,9 juta ton ke 21.8 juta ton selama rentang tahun 2000-2020. Pertumbuhan tahunan total produksi berfluktuasi di sekitar angka 7-25% pada tahun 2002-2015, kemudian menurun pertumbuhannya hingga 2,7% pada tahun 2017. Setelah itu, total produksi stagnan cenderung menurun di bawah 1% pada tahun 2018-2019, dan menurun kembali sebanyak 5.2% pada tahun 2020. Nilai total produksi perikanan tangkap dan budidaya pada tahun 2020 adalah sekitar 363 triliun, dimana 176.5 triliun berasal dari produksi perikanan budidaya.""")
    st.markdown("""Keadaan stagnan cenderung menurun pada tahun 2018-2019 ini terjadi karena adanya penurunan produksi budidaya laut sebanyak 536.000 ton dan 663.000 ton pada 2018 dan 2019, serta penurunan produksi perikanan tangkap darat menurun sekitar 102.000 ton pada tahun 2019.  Pada tahun 2020, seluruh produksi perikanan menurun dibanding tahun sebelumnya.""")
    st.markdown("""Sementara itu, produksi budidaya dari tahun 2000 hingga 2013 cenderung meningkat pesat, dengan pertumbuhan rata-rata 25,3%. Pertumbuhan paling tinggi ada pada tahun 2002 yaitu 51,4%. Pada tahun 2014-2016, pertumbuhannya melambat di bawah 8%. Setelah cenderung stagnan pada tahun 2017, pada tahun 2017-2020 terjadi penurunan sekitar 2-3%.""")
    st.markdown("""Produksi perikanan tangkap dari tahun 2000-2019 cenderung mengalami kenaikan dengan kenaikan. Pertumbuhan per tahun produksi perikanan tangka pada di sekitar 2-8% pada periode tersebut. Penurunan drastis sebesar 9.5% terjadi pada tahun 2020.""")
st.markdown("""Bagian total produksi perikanan yang bersumber dari budidaya itu meningkat pesat dari 765.000 ton dibanding 3,8 juta ton pada tahun 2000 hingga 14.8 juta ton dibanding 21,8 ton pada tahun 2020. Ini berarti peningkatan pesat dari 16% bagian produksi budidaya pada tahun 2000 hingga 71% dan 68% bagian produksi budidaya pada tahun 2017 dan 2020.""")

st.subheader("Persentase Perikanan Darat dan Laut Indonesia")

html_temp = """<div class='tableauPlaceholder' id='viz1659564484272' style='position: relative'><noscript><a href='#'><img alt='Dashboard 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;1_&#47;1_2PersenPerikananDaratLaut&#47;Dashboard1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='1_2PersenPerikananDaratLaut&#47;Dashboard1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;1_&#47;1_2PersenPerikananDaratLaut&#47;Dashboard1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1659564484272');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.height='727px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
components.html(html_temp, width=1200, height=900)

st.caption('')

with st.container():
    st.markdown("""Dari total produksi tahun 2020, 72% (15,7 juta ton) diantaranya kontribusi dari perikanan laut (58,5% dari perikanan budidaya, dan 41,5% dari perikanan tangkap) dan 28% dari perikanan darat (92% dari perikanan budidaya, dan 8% dari perikanan tangkap). Pertumbuhan produksi perikanan budidaya pada dua dekade terakhir telah menambah pertumbuhan produksi  perikanan laut dan darat.""")
    st.markdown("""Sementara itu, produksi budidaya perikanan laut meningkat dari 0.6% pada tahun 2000, hingga ke sekitar 60% pada tahun 2013 hingga sekarang.""")  

st.subheader("Persentase Perikanan Budidaya dan Tangkap Darat")

html_temp = """<div class='tableauPlaceholder' id='viz1659565365012' style='position: relative'><noscript><a href='#'><img alt='Dashboard 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;1_&#47;1_3PersenBudidayaTangkapDarat&#47;Dashboard1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='1_3PersenBudidayaTangkapDarat&#47;Dashboard1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;1_&#47;1_3PersenBudidayaTangkapDarat&#47;Dashboard1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1659565365012');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.height='727px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
components.html(html_temp, width=1200, height=900)

st.markdown("""Produksi budidaya perikanan darat pada tahun 2000 hanya 70% dibanding total produksi, namun semenjak tahun 2013 hingga tahun 2020 berada di sekitar 90% ke atas.""")

st.subheader("Persentase Perikanan Budidaya dan Tangkap Laut")

html_temp = """<div class='tableauPlaceholder' id='viz1659565420973' style='position: relative'><noscript><a href='#'><img alt='Dashboard 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;1_&#47;1_4PersenBudidayaTangkapLaut&#47;Dashboard1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='1_4PersenBudidayaTangkapLaut&#47;Dashboard1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;1_&#47;1_4PersenBudidayaTangkapLaut&#47;Dashboard1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1659565420973');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.height='727px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
components.html(html_temp, width=1200, height=900)

st.markdown("""Produksi perikanan tangkap laut cenderung selalu mengalami kenaikan per tahunnya dari tahun 2000-2019. Pada tahun 2020, terjadi penurunan sekitar 671.000 ton.""")
st.markdown("""Pandemi COVID-19 diperkirakan merupakan penyebab utama dari menurunnya total produksi perikanan Indonesia, khususnya perikanan tangkap. Karena sepertinya terjadi anomali produksi perikanan tangkap, pada tahun-tahun sebelumnya tidak pernah ada penurunan sebanyak tahun 2020. Selain itu, dari analisis Wilayah Pengelolaan Perikanan atau WPP (yang akan dibahas nanti), kebanyakan WPP ini mengalami penurunan jumlah komoditas yang statusnya over-exploited, sehingga  potensi terjadinya penurunan produksi perikanan tangkap karena over-fishing itu kemungkinannya kecil. Menurut FAO (2022), perubahan permintaan konsumsi, disrupsi pasar, dan kesulitan logistik karena pembatasan sosial menghambat aktivitas penangkapan dan budidaya ikan, khususnya lockdown, physical distancing, dan pembatasan akses pelabuhan. Selain itu, penurunan atau pemberhentian aktivitas baik budidaya maupun tangkap dapat terjadi karena adanya penurunan permintaan dan harga produk perikanan dan budidaya. Pada perikanan tangkap, kuota perikanan dapat tidak terpenuhi karena permintaan yang sedikit, penutupan pasar, maupun kekurangannya kapasitas cold storage. Tren ini juga mirip dengan produksi perikanan tangkap dunia yang katanya relatif stabil, namun pada tahun 2020 mengalami penurunan karena pandemi COVID-19.""")

st.subheader("Volume Produksi Total dengan dan tanpa Rumput Laut")

html_temp = """<div class='tableauPlaceholder' id='viz1659567436635' style='position: relative'><noscript><a href='#'><img alt='RumputLautD ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;4_&#47;4_3VolumeProduksiTotaldengantanpaRumputLaut&#47;RumputLautD&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='4_3VolumeProduksiTotaldengantanpaRumputLaut&#47;RumputLautD' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;4_&#47;4_3VolumeProduksiTotaldengantanpaRumputLaut&#47;RumputLautD&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1659567436635');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.height='727px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
components.html(html_temp, width=1200, height=900)

st.markdown("""Rumput laut adalah komoditas yang mempunyai potensi yang luas dan belum dimanfaatkan. Potensi rumput laut beberapa diantaranya adalah sebagai pakan dan makanan, biostimulan, nutrasetika, kosmetik, dan lebih dikenal beberapa waktu ini sebagai solusi perubahan iklim.  Potensi pasar untuk komoditas ini pun tinggi.  Tujuh taksa yang menyusun produksi rumput laut global adalah Euchema spp, Kappaphycus alvarezii, Gracilaria spp., Saccharina japonica, Undaria pinnatifida, Pyropia spp., dan Sargassum fusiforme (Buschmann, et al., 2017) .""")
st.markdown("""Volume produksi total dengan dan tanpa rumput laut ini menegaskan kontribusi rumput laut dalam total produksi perikanan Indonesia. Volume produksi total budidaya merupakan yang paling terpengaruhi oleh volume produksi rumput laut. Pada tahun 2010, jika dihitung dengan rumput laut maka akan terdapat volume 5.8 juta ton dibandingkan dengan tanpa rumput laut yaitu 1.9 juta ton. Sedangkan pada tahun 2020, volume dengan rumput laut adalah 14.8 juta ton, dibandingkan dengan tanpa rumput laut adalah 5.2 juta ton. Perbedaan pada tahun 2010 dan 2020 adalah 3.9 juta ton dan 9.6 juta ton. Menariknya, jika produksi perikanan budidaya ditambah produksi rumput laut, produksi total dari budidaya mengalami kenaikan hingga 2016 dan setelah itu mengalami penurunan. Namun jika produksi budidaya rumput laut tidak dihitung, maka produksi perikanan budidaya terus mengalami kenaikan hingga tahun 2020 meskipun dengan jumlah kenaikan yang kecil. Ini mungkin dapat terjadi karena produksi perikanan budidaya Indonesia yang belum memenuhi permintaan pasar domestik dan mancanegara meskipun permintaan pasar tersebut menurun, sehingga pertumbuhan tetap terjadi. Ini juga berarti bahwa potensi perikanan budidaya Indonesia yang masih tinggi untuk dioptimalkan, diintensifikasi produksinya, sehingga dapat memenuhi permintaan pasar.""")
st.markdown('Volume produksi perikanan tangkap laut hanya terpengaruhi sedikit oleh volume produksi rumput laut. Pada tahun 2010, volume produksi dengan dan tanpa rumput laut adalah 2.500.297 ton dan 2.497.600 ton. Sedangkan pada tahun 2020 volume produksi dengan dan tanpa rumput laut adalah 6.429.221 ton dan 6.493.249 ton. Perbedaan pada tahun 2010 dan 2020 untuk volume produksi perikanan tangkap laut adalah 2.697 ton dan 64.028 ton. Ini menandakan bahwa pada perikanan tangkap laut, volume rumput laut yang tertangkap hanya sedikit meskipun terdapat pertumbuhan sebesar 23 kali lipat selama dekade tersebut.')

# Akhir page
with st.expander("Referensi", expanded=False):
    st.markdown("**Literatur:**")
    lst = ['FAO. 2022. The State of World Fisheries and Aquaculture 2022. Towards Blue Transformation. Rome, FAO. https://doi.org/10.4060/cc0461en', 
        'Fresh thoughts on the seaweed farming sector | The Fish Site',
        'Buschmann, AH., et al. 2017. Seaweed production: overview of the global state of exploitation, farming and emerging research activity. European Journal of Phycology, volume 52, issue 4']

    s = ''

    for i in lst:
        s += "- " + i + "\n"

    st.markdown(s)

with st.expander("Metode dan/atau Kode", expanded=False):
    st.markdown("**Metode:**")
    lst = ['Modifikasi data dilakukan dengan Microsoft Excel', 
        'Visualisasi data dilakukan dengan Tableau', 
        ]

    s = ''

    for i in lst:
        s += "- " + i + "\n"

    st.markdown(s)