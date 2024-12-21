import streamlit as st 
from datetime import datetime


#Halaman Tambah Pemasukan
st.title("Tambah Pemasukan") # Menampilkan judul besar di halaman web
with st.form("pemasukan_form"): # Membuat sebuah form dengan konteks with
    petugas = st.text_input("Petugas") # Input teks dan disimpan pada variabel
    keterangan = st.text_input("Keterangan") # Input teks dan disimpan pada variabel
    jumlah = st.number_input("Jumlah (Rp)", min_value=0, step=1000) # Input angka dan disimpan pada variabel
    tanggal = st.date_input("Tanggal", value=datetime.today().date()) # Input tanggal dan disimpan pada variabel
    waktu = st.time_input("Waktu", value=datetime.now().time()) # Input waktu dan disimpan pada variabel
    submitted = st.form_submit_button("Tambahkan") # Tombol submit form
    if submitted and keterangan and jumlah > 0: # Jika tombol submit ditekan dan keterangan dan jumlah tidak kosong
        tanggal_waktu = datetime.combine(tanggal, waktu) # Menggabungkan tanggal dan waktu menjadi satu variabel
        st.session_state['transaksi'].append({ # Menambahkan transaksi baru ke dalam session state
                "type": "Pemasukan",
                "petugas": petugas,
                "keterangan": keterangan,
                "jumlah": jumlah,
                "tanggal": tanggal_waktu
            })
        st.success("Pemasukan berhasil ditambahkan!") # Menampilkan pesan sukses
    else:
        st.error("Jumlah harus lebih besar dari 0 dan data tidak boleh kosong.") # Menampilkan pesan kesalahan

