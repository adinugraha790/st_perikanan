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

st.header("Potensi IoT untuk Perikanan Tangkap dan Budidaya di Indonesia")
with st.expander("Lihat wawasan penting", expanded=True):
    st.markdown("""**Wawasan penting**""")
    lst = ['Potensi IoT untuk menambah produksi perikanan budidaya dan tangkap serta mengoptimalkannya itu tinggi', 
        'Potensi pasar IoT untuk perikanan tangkap dan budidaya Indonesia sangat besar', 
        'Biaya merupakan kendala utama pada penerapan IoT pada nelayan dan pembudidaya kecil']

    s = ''

    for i in lst:
        s += "- " + i + "\n"

    st.markdown(s)

with st.container():
    st.markdown("""IoT adalah suatu atau kelompok objek fisik dengan sensor, kemampuan pemrosesan, perangkat lunak, dan teknologi lainnya yang dapat menghubungkan dan bertukar data dengan perangkat dan sistem lainnya melalui internet atau jaringan komunikasi lainnya . Pada beberapa tahun terakhir, IoT telah diterapkan di banyak sektor.  Untuk sektor perikanan tangkap dan budidaya, beberapa potensi IoT adalah :""")

    lst = ['untuk mencegah over-fishing dan meningkatkan praktik penangkapan ikan yang berkelanjutan', 
        'precision fishing dimana AI dan perangkat IoT digunakan untuk menentukan lokasi dimana kemungkinan ikan berada sehingga biaya operasionalnya yang menurun', 
        'monitoring parameter kualitas air, perilaku ikan, maupun mendeteksi keberadaan mikroorganisme penyebab penyakit tertentu secara real-time dapat digunakan dengan IoT sehingga mempercepat penanganan ketika terjadi perubahan kualitas air yang signifikan dan menurunkan mortalitas ikan , ini sangat krusial untuk kegiatan pembenihan dimana mortalitas yang tinggi biasanya terjadi',
        'optimisasi pakan dapat dilakukan dengan IoT sehingga didapatkan feed conversion ratio (FCR) yang tinggi, yield produksi yang lebih tinggi, kualitas air yang lebih terjaga dari peningkatan kadar nitrogen, dan mengontrol pertumbuhan alga',
        'optimisasi panen juga dapat dilakukan dengan modeling dengan seluruh data-data yang berkaitan dengan ikan dan lingkungan budidaya sehingga panen dapat terencana lebih matang, dan dapat diprediksi kuantitasnya']

    s = ''

    for i in lst:
        s += "- " + i + "\n"

    st.markdown(s)

st.markdown("Salah satu cara untuk mengetahui potensi pasar IoT di Indonesia adalah dengan melihat luas usaha budidaya untuk sektor budidaya dan jumlah kapal untuk sektor usaha penangkapan ikan. Sebagai referensi, luas kolam pembesaran tahap III untuk membesarkan benih ikan nila mempunyai luas 500-2000 m2. Sebagai hitungan kasar dimana kolam tahap ini merupakan kolam yang mayoritas digunakan untuk produksi budidaya, ini berarti bahwa terdapat kemungkinan 750 ribu – 3 juta perangkat IoT dapat diinstalasi untuk satu jenis perangkat IoT untuk kolam saja pada tahun 2016. Ini tidak memperhitungkan bahwa terdapat kolam pembenihan, maupun kolam pembesaran tahap I dan II yang luasnya lebih kecil, sehingga jumlahnya kemungkinan lebih dari itu. Inovasi-inovasi sehingga perangkat IoT dapat digunakan untuk optimasi produksi di tambak dan sawah juga diperlukan mengingat luasnya yang tinggi.")
st.markdown('Berdasarkan pengalaman pribadi penulis berinteraksi dengan beberapa pembudidaya di Jatinangor, Sumedang, pembudidaya sangat ingin untuk menerapkan IoT dan teknologi modern seperti nanobubble, ataupun sistem RAS yang optimal untuk usaha budidayanya. Namun mereka terkendala masalah biaya. Ini dapat diberikan solusi dengan cara peminjaman produk dan dibayar nanti ketika panen, penyewaan, maupun cicilan untuk produk IoT tersebut. Atau mungkin dapat dilakukan Trial sehingga pengguna mendapatkan diskon untuk beberapa periode dan merasakan manfaat dari perangkat IoT tersebut sebelum akhirnya yakin untuk menggunakan perangkat tersebut ke depannya.')
st.markdown('Untuk pasar IoT Indonesia sektor perikanan tangkap, potensinya penulis perkirakan sangat besar untuk sektor perikanan tangkap laut. Kesimpulan tersebut didapat karena selain jumlah perahu yang sangat tinggi dibandingkan dengan jumlah perahu tangkap PUD, produksinya juga tinggi sehingga jika nilai dari produksi tersebut minimal setara atau tinggi, maka penghasilan yang didapat nelayan laut lebih tinggi. Ini berarti kemampuan nelayan laut dalam membeli produk lebih besar dibanding nelayan PUD. Penghitungan biaya operasional memerlukan AI predictive maintenance, McKinsey mengatakan bahwa jika perusahaan perikanan skala besar di dunia menggunakan model tersebut, biaya operasi tahunan dapat berkurang hingga 11 milyar dolar AS.')

Di bawah ini adalah rekomendasi yang dapat penulis berikan untuk pasar IoT di Indonesia, dengan berbagai parameter dan target pasar serta provinsi yang dapat dijadikan prioritas utama dalam pemasaran.
rekomen = pd.read_excel('Rekomendasi.xlsx')
rekomen

# Akhir page
with st.expander("Referensi", expanded=False):
    st.markdown("**Literatur:**")
    lst = [' Internet of Things Global Standards Initiative (itu.int)', 
        '5 Ways IoT and AI Are Changing Fisheries and Aquaculture (iotforall.com)', 
        'Development of IoT Based Fish Monitoring System for Aquaculture (techscience.com)']

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
