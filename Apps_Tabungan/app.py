import streamlit as st 

# CSS to Streamlit

st.markdown(
    """
    <style>
    .stApp{
        background-color: #FFFBE6;
    }
    
    [data-testid="stSidebar"]{
        background-color: #347928;
        color: white;
    }
    
    [data-testid="stSidebar"] * {
        color: white !important;
        font-size: 14px;
    
    }
    
    # .stApp{
    # background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366");
    # background-size: cover;
    # }
    
    </style>
    """,
    unsafe_allow_html = True 
)

dashboard = st.Page("./fitur/dashboard.py", title="Dashboard")
nabung = st.Page("./fitur/nabung.py", title="Menabung")
penarikan = st.Page("./fitur/penarikan.py", title="Penarikan")

pg = st.navigation(
    {
     "Menu Utama" : [dashboard],
     "Transaksi" : [nabung, penarikan],
        
    }
)

if 'total_semua' not in st.session_state:
    st.session_state['total_semua'] = []

pg.run()