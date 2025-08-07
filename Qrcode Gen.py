import qrcode
import streamlit as st
from PIL import Image
import io

st.title("QR Code Generator")

# Input dari user
data = st.text_input("Masukkan teks atau URL:")

if st.button("Generate QR Code"):
    # Buat QR Code
    qr = qrcode.make(data)
    
    # Simpan ke BytesIO
    buf = io.BytesIO()
    qr.save(buf, format='PNG')
    buf.seek(0)

    # Tampilkan di streamlit
    st.image(buf, caption="QR Code Anda", use_container_width=True)

    # Tambahkan tombol download
    st.download_button(
        label="Download QR Code",
        data=buf,
        file_name="qrcode.png",
        mime="image/png"
    )
