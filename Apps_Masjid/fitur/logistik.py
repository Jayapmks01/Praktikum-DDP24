import streamlit as st 
import pandas as pd

#Halaman Logistik Masjid
st.title("Logistik Masjid")
with st.form("logistik_form"):
    nama_barang = st.text_input("Nama Barang")
    jumlah = st.number_input("Jumlah", min_value=0, step=1)
    keterangan = st.text_area("Keterangan")
    submitted = st.form_submit_button("Tambahkan")
    if submitted and nama_barang and jumlah > 0:
        st.session_state['logistik'].append({
            "nama_barang": nama_barang,
            "jumlah": jumlah,
            "keterangan": keterangan
        })
        st.success("Logistik berhasil ditambahkan!")

st.subheader("Data Logistik")
logistik = st.session_state['logistik']
if logistik:
    df = pd.DataFrame(logistik)
    st.dataframe(df)
else:
    st.info("Belum ada data logistik.")