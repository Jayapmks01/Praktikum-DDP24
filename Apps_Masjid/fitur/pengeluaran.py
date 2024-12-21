import streamlit as st
from datetime import datetime
import pandas as pd

#Halaman Tambah Pengeluaran
st.title("Tambah Pengeluaran") # Judul Halaman
with st.form("pengeluaran_form"): # Membuat Form
    petugas = st.text_input("Petugas") # Input Petugas
    keterangan = st.text_input("Keterangan") # Input Keterangan
    jumlah = st.number_input("Jumlah (Rp)", min_value=0, step=1000) # Input Jumlah
    tanggal = st.date_input("Tanggal", value=datetime.today().date()) # Input Tanggal
    waktu = st.time_input("Waktu", value=datetime.now().time()) # Input Waktu
    submitted = st.form_submit_button("Tambahkan") # Tombol Tambahkan
    if submitted and keterangan and jumlah > 0: # Jika tombol Tambahkan diklik dan input keterangan dan jumlah tidak kosong
        tanggal_waktu = datetime.combine(tanggal, waktu) # Menggabungkan Tanggal dan Waktu
        st.session_state['transaksi'].append({ # Menambahkan Data Transaksi
                "type": "Pengeluaran",
                "petugas": petugas,
                "keterangan": keterangan,
                "jumlah": jumlah,
                "tanggal": tanggal_waktu
            })
        st.success("Pengeluaran berhasil ditambahkan!") # Pesan Sukses
    else:
        st.error("Jumlah harus lebih besar dari 0 dan data tidak boleh kosong.") # Pesan Error