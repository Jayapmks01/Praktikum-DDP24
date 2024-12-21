import streamlit as st 
from app import total



#Halaman Dashboard
st.title("Aplikasi Masjid Nurul Jami") # Menampilkan Judul
st.markdown("Selamat Datang di Aplikasi Masjid Nurul Jami") # Menampilkan Deskripsi
st.image("Image.png", caption="Masjid Nurul Jami") # Menampilkan Gambar dengan caption
    
    
st.title("Dashboard Kas Masjid") # Menampilkan Judul
transaksi = st.session_state['transaksi'] # Mengambil data transaksi dari st.session_state
total_pemasukan, total_pengeluaran, saldo = total(transaksi) # Memanggil fungsi total dari tiga nilai tersebut.

st.metric("Total Pemasukan", f"Rp {total_pemasukan:,}") # Menampilkan metrik berupa total pemasukan dalam format rupiah
st.metric("Total Pengeluaran", f"Rp {total_pengeluaran:,}") # Menampilkan metrik berupa total pengeluaran dalam format rupiah
st.metric("Saldo Kas", f"Rp {saldo:,}") # Menampilkan metrik saldo kas (total pemasukan dikurangi total pengeluaran)