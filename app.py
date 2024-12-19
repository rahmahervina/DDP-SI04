import streamlit as st

#st.title("Hello sist")
#st.markdown("Selamat datang di rumah coding")
#st.image("images.jpg", caption="Ini gambar")

dashboard = st.Page("./fitur/dashboard.py", title="Dashboard")
nabung = st.Page("./fitur/nabung.py", title="Menabung")

pg = st.navigation(
    {
        "Menu Utama" : [dashboard],
        "Transaksi" : [nabung],

    }
)

if "total_semua" not in st.session_state:
    st.session_state["total_semua"] = []

pg.run()