import streamlit as st
import qrcode
from io import BytesIO

st.set_page_config(page_title="QR Code Generator", layout="centered")
st.title("🔲 QR Code Generator")

st.markdown("Masukkan teks, link, atau data lainnya untuk dibuat menjadi QR Code.")

input_data = st.text_area("Masukkan teks/link yang ingin dikodekan", placeholder="Contoh: https://google.com")
box_size = st.slider("Ukuran QR Code", min_value=5, max_value=20, value=10)

if st.button("🔄 Generate QR Code") and input_data:
    qr = qrcode.QRCode(version=1, box_size=box_size, border=4)
    qr.add_data(input_data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)

    st.image(img, caption="QR Code Anda", use_container_width=True)
    st.download_button("⬇️ Download QR Code", data=buffer, file_name="qrcode.png", mime="image/png")

