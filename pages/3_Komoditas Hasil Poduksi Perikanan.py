import streamlit as st
import streamlit.components.v1 as components
import numpy as np
import pandas as pd

st.set_page_config(page_title= "", page_icon='icon.jpg',layout="wide")

st.sidebar.subheader('Analisis Produksi Perikanan Indonesia dan Potensi IoTnya')
st.sidebar.markdown(f"""
                   Analisis dilakukan berdasarkan data pada **[Statistik Kementerian Kelautan dan Perikanan (KKP)](https://statistik.kkp.go.id/)** dan **[Badan Pusat Statistik (BPS)](https://www.bps.go.id/)**.
                   """)

st.title("Komoditas Hasil Produksi Perikanan")
st.subheader("Volume Produksi berdasarkan Komoditas Perikanan dan Provinsi")

html_temp = """<div class='tableauPlaceholder' id='viz1659567799420' style='position: relative'><noscript><a href='#'><img alt='Dashboard 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;2_&#47;2_2VolumeProduksibdsKomoditasProvinsi&#47;Dashboard1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='2_2VolumeProduksibdsKomoditasProvinsi&#47;Dashboard1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;2_&#47;2_2VolumeProduksibdsKomoditasProvinsi&#47;Dashboard1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1659567799420');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.height='727px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
components.html(html_temp, width=1200, height=900)

st.caption('')

html_temp = """<div class='tableauPlaceholder' id='viz1659568823662' style='position: relative'><noscript><a href='#'><img alt='VolProdKom2020 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;3_&#47;3_1VolumeProduksiKomditasberdasarkanProvinsi&#47;VolProdKom2020_1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='3_1VolumeProduksiKomditasberdasarkanProvinsi&#47;VolProdKom2020_1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;3_&#47;3_1VolumeProduksiKomditasberdasarkanProvinsi&#47;VolProdKom2020_1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1659568823662');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.height='727px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
components.html(html_temp, width=1200, height=900)

with st.expander("Lihat wawasan penting", expanded=True):
    st.markdown("""**Wawasan penting**""")
    lst = ['Komoditas yang diproduksi terbanyak dengan usaha budidaya adalah ikan bandeng dan bawal.  Keduanya memiliki jumlah volume produksi total tertinggi.', 
        'Komoditas yang diproduksi terbanyak dengan usaha tangkap laut adalah ikan bawal, ikan baronang, dan ikan belanak', 
        'Komoditas yang diproduksi terbanyak dengan usaha tangkap PUD adalah ikan betok dan ikan baung',
        'Nilai produksi cenderung sebanding dengan total produksinya untuk kebanyakan spesies']

    s = ''

    for i in lst:
        s += "- " + i + "\n"

    st.markdown(s)

with st.container():
    st.markdown("""Ikan bandeng (Chanos chanos)adalah komoditas yang memiliki volume produksi total terbanyak pada tahun 2020 di Indonesia. Provinsi yang  terbanyak menghasilkan ikan dari famili Chanidae ini pada tahun 2020 adalah Provinsi Sumatera Selatan (193.765 ton), Jawa Timur (167.605), Jawa Tengah (92.583 ton), dan Jawa Barat (83.410 ton). Di Pulau Jawa, ikan bandeng ini menjadi komoditas unggulan dan olahan dari ikan ini menjadi makanan khas provinsi.""")
    st.markdown('Ikan bawal adalah komoditas yang memiliki jumlah volume produksi total kedua terbanyak di Indonesia pada tahun 2020. Provinsi Papua (19.275 ton) dan Jawa Barat (37.180 ton) menjadi dua provinsi dengan kontribusi terbanyak untuk ikan yang menghuni famili Bramidae ini. Di Indonesia, dua ikan bawal yang memiliki peluang besar adalah ikan bawal emas dan bawal bintang. Pada tahun 2021, dikembangkan ikan bawal hibrid yang merupakan hasil perkawinan silang antara kedua ikan bawal tersebut.  Setelah ikan bawal, ikan baronang, ikan belanak, dan ikan ayam-ayam menjadi komoditas terbanyak yang diproduksi di Indonesia pada tahun 2020.')
    st.markdown('Komoditas yang diproduksi terbanyak dengan usaha budidaya adalah ikan bandeng dan bawal. Komoditas yang diproduksi terbanyak dengan usaha tangkap laut adalah ikan bawal, ikan baronang, dan ikan belanak. Sedangkan komoditas yang diproduksi terbanyak dengan usaha tangkap PUD adalah ikan betok dan ikan baung.')

st.subheader("Nilai Produksi berdasarkan Komoditas Perikanan dan Provinsi")

html_temp="""<div class='tableauPlaceholder' id='viz1659569034661' style='position: relative'><noscript><a href='#'><img alt='Dashboard 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;2_&#47;2_3NilaiProduksibdsKomoditasProvinsi&#47;Dashboard1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='2_3NilaiProduksibdsKomoditasProvinsi&#47;Dashboard1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;2_&#47;2_3NilaiProduksibdsKomoditasProvinsi&#47;Dashboard1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1659569034661');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.height='727px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
components.html(html_temp, width=1200, height=900)

st.markdown('Untuk nilai produksi komoditas perikanan pada tahun 2020 kurang lebih sama kesimpulannya dengan volume komoditas yang telah dijelaskan, karena kebanyakan volumenya sebanding dengan nilainya pada grafik. Namun yang perlu diperhatikan adalah ketika nilainya lebih tinggi dengan volume produksi yang rendah, artinya terdapat nilai (harga) lebih untuk setiap satuan volume komoditas tersebut dibanding dengan komoditas yang lain.')

st.subheader("Volume Produksi berdasarkan Komoditas Perikanan dan Jenis Usaha")

html_temp="""<div class='tableauPlaceholder' id='viz1659569260314' style='position: relative'><noscript><a href='#'><img alt='VolProdKomd ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;4_&#47;4_2VolumeProduksiberdasarkanKomoditasJenisUsaha&#47;VolProdKomd&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='4_2VolumeProduksiberdasarkanKomoditasJenisUsaha&#47;VolProdKomd' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;4_&#47;4_2VolumeProduksiberdasarkanKomoditasJenisUsaha&#47;VolProdKomd&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1659569260314');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.height='727px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
components.html(html_temp, width=1200, height=900)
with st.expander("Lihat wawasan penting", expanded=True):
    st.markdown("""**Wawasan penting**""")
    lst = ['Rumput laut adalah komoditas budidaya dengan produksi terbesar dibandingkan dengan komoditas lain dan jenis usaha lainnya, bahkan Menyusun hingga lebih dari 50% total volume produksi', 
        'Komoditas dengan volume produksi total terbanyak jenis usaha budidaya setelah rumput laut adalah ikan nila, lele, udang, bandeng, mas, dan patin', 
        'Komoditas dengan volume produksi total terbanyak jenis usaha tangkap laut adalah ikan tongkol, layang, cakalang, tuna, dan kakap',
        'Komoditas dengan volume produksi total terbanyak jenis usaha tangkap darat adalah ikan nila, patin, dan gabus']

    s = ''

    for i in lst:
        s += "- " + i + "\n"

    st.markdown(s)

st.markdown('Komoditas dengan volume produksi terbesar total di semua jenis usaha adalah rumput laut, yang produksinya hingga mencapai 11.05 juta ton pada tahun 2016. Volumenya sangat besar bahkan dapat mencapai lebih dari 50% total volume produksi. Selain rumput laut, yang memiliki volume produksi terbesar pada jenis usaha budidaya adalah ikan nila (1.172.616 ton), ikan lele (993.749 ton), udang (881.581 ton), dan ikan bandeng (811.870 ton), ikan mas (560.651 ton), dan ikan patin (327.129 ton).')
st.markdown('Komoditas yang memiliki volume produksi total terbanyak pada jenis usaha tangkap laut adalah ikan tongkol (581.057 ton), ikan layang (548.645 ton), ikan cakalang (468.258 ton), ikan tuna (300.791 ton) dan ikan kakap (292.531 ton).')
st.markdown('Komoditas yang memiliki volume produksi total terbanyak pada jenis usaha tangkap perairan umum daratan (PUD) adalah ikan nila (57.849 ton), ikan patin (53.088 ton), dan ikan gabus (59.510 ton).')


st.subheader("Volume dan Nilai Ekspor-Impor berdasarkan Tahun dan Komoditas")

html_temp="""<div class='tableauPlaceholder' id='viz1659569539841' style='position: relative'><noscript><a href='#'><img alt='N&amp;VEksim ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;5_&#47;5_1VolumedanNilaiEksImpbdsTahunKomoditas&#47;NVEksim&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='5_1VolumedanNilaiEksImpbdsTahunKomoditas&#47;NVEksim' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;5_&#47;5_1VolumedanNilaiEksImpbdsTahunKomoditas&#47;NVEksim&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1659569539841');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.height='827px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
components.html(html_temp, width=1200, height=900)
with st.expander("Lihat wawasan penting", expanded=True):
    st.markdown("""**Wawasan penting**""")
    lst = ['Selama periode 2012-2012, seluruh komoditas kecuali udang cenderung mengalami penurunan volume ekspor', 
        'Seluruh komoditas mengalami fluktuasi volume impor kecuali ikan sarden-sardinella yang volume impornya menurun', 
        'Rajungan dan udang memiliki nilai ekspor yang tinggi']

    s = ''

    for i in lst:
        s += "- " + i + "\n"

    st.markdown(s)

st.markdown('Berdasarkan grafik, terlihat bahwa yang memiliki volume ekspor terbesar adalah komoditas lainnya. Setelah komoditas lainnya, ikan tuna-tongkol-cakalang dan rumput laut merupakan yang kedua dan ketiga paling besar dalam volume ekspor. Komoditas lainnya mengalami penurunan volume ekspor, namun udang cenderung mengalami kenaikan di sepanjang periode 2012-2021.')
st.markdown('Komoditas yang mendominasi volume impor adalah tepung ikan-pellet, ikan sarden-sardinella, makarel, dan komoditas lainnya. Di sepanjang periode 2012-2021, volume impor ikan sarden-sardinella cenderung menurun, sedangkan lainnya berfluktuasi.')
st.markdown('Jika dibandingkan dengan volume ekspor-impor, grafik nilai ekspor-impor ini memiliki perbedaan. Rajungan dan udang memiliki nilai ekspor yang tinggi dan tidak sebanding dengan volumenya, sebaliknya rumput laut dan komoditas lainnya memiliki nilai ekspor yang rendah dibandingkan dengan volumenya. Ini berarti bahwa rajungan dan udang memiliki nilai per volume yang tinggi dibandingkan komoditas lainnya untuk pasar mancanegara.')


# Akhir page
with st.expander("Referensi", expanded=False):
    st.markdown("**Literatur:**")
    lst = ['Profil Komoditas Ikan Bandeng | Warta Pasar Ikan (kkp.go.id)', 
        ]

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

    st.markdown("**Kode:**")
    st.code("""
    ### tabel_3 adalah sumber utama dataset dari csv
    ### tabel_kom_4 adalah tabel kosong template yang ingin diisi

    for i in range(0, len(tabel_3.index)):
            # untuk iterasi indeks baris tabel_3
    for n in range(0, len(tabel_komp_4.columns)):
            # untuk iterasi indeks kolom tabel_kom_4
        for x in range(0, len(tabel_komp_4.index)):
            # untuk iterasi indeks baris tabel_komp_4
            # jika jenis ikan pada baris ke i tabel_3 sama dengan kolom ke-n dari list tabel_komp_4
            if tabel_3['Jenis Ikan'][i] == list(tabel_komp_4.columns)[n] and 
            tabel_3['Jenis Usaha'][i] == tabel_komp_4['Jenis Usaha'][x] and
            tabel_3['Tahun'][i] == tabel_komp_4['Tahun'][x]:
                           tabel_komp_4.iloc[x,n] = int(tabel_komp_4.iloc[x,n]) + int(tabel_3['Nilai Produksi'][i])
            # dan jenis usahanya sama dengan baris ke x
            # dan tahunnya sama dengan baris ke x
            # maka ditambahkan jumlah komoditasnya

        # Prosedur ini dilakukan untuk Nilai Produksi dan Volume Produksi

tabel_komp_4""")