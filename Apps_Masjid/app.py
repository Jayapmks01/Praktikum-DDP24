import streamlit as st

# Custom CSS untuk tampilan
st.markdown(
    """
    <style>
    /* Warna latar belakang aplikasi */
    .stApp {
        background-color: #fffff;
    }

    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: #31511E;
        color: white;
        padding: 5px;
    }

    /* Teks pada sidebar */
    [data-testid="stSidebar"] * {
        color: white !important;
        font-size: 16px;
        margin-bottom: 5px;
        margin-top: 5px;
    }

    [data-testid="stSidebar"] *:hover {
        color: #ecf0f1 !important;
    }

    /* Header bar styling */
    header[data-testid="stHeader"] {
        background-color: #859F3D;
        color: white;
        padding: 5px;
        
    }

    header[data-testid="stHeader"] h1 {
        color: white;
        font-size: 10px;
    }

    .stButton > button:hover {
        background-color: #2980b9;
        color: #ecf0f1;
    }

    /* Custom title style for Kas Masjid */
    .sidebar-title {
        font-size: 20px;
        font-weight: bold;
        color: #ffffff;
        margin-bottom: 20px;
        text-align: center;
    }
    
    </style>
    """,
    unsafe_allow_html=True
)


#Data in-memory storage (simulasi database)
if 'transaksi' not in st.session_state: # jika tidak ada data, maka buat data dummy
    st.session_state['transaksi'] = [] # inisiasi data transaksi
if 'logistik' not in st.session_state: # jika tidak ada data, maka buat data dummy
    st.session_state['logistik'] = [] # inisiasi data logistik

#Fungsi untuk menghitung total pemasukan, pengeluaran, dan saldo
def total(transaksi): # fungsi untuk menghitung total pemasukan, pengeluaran, dan saldo
    total_pemasukan = sum(t['jumlah'] for t in transaksi if t['type'] == 'Pemasukan') # total pemasukan
    total_pengeluaran = sum(t['jumlah'] for t in transaksi if t['type'] == 'Pengeluaran') # total pengeluaran
    saldo = total_pemasukan - total_pengeluaran # saldo
    return total_pemasukan, total_pengeluaran, saldo # return total pemasukan, pengeluaran, dan saldo




# Setiap halaman di aplikasi didefinisikan menggunakan (st.Page(path, title))
dashboard = st.Page("./fitur/dashboard.py", title="Dashboard", icon=":material/dashboard:")
pemasukan = st.Page("./fitur/pemasukan.py", title="Pemasukan")
pengeluaran = st.Page("./fitur/pengeluaran.py", title="Pengeluaran")
logistik = st.Page("./fitur/logistik.py", title="Logistik")
riwayat = st.Page("./fitur/riwayat.py", title="Riwayat", icon=":material/history:")

# Membuat navigasi halaman dalam aplikasi.
pg = st.navigation(
    {
    "Rekap": [dashboard, riwayat],
    "Utama": [pemasukan,pengeluaran, logistik],
    }
)

# Menjalankan navigasi dan memuat halaman sesuai pilihan pengguna.
pg.run()

