import streamlit as st
import qrcode
from io import BytesIO

# Configuración básica de la página
st.set_page_config(page_title="Generador de QR para Drive", page_icon="🔗")

st.title("Generador de Código QR")
st.write("Pega tu enlace de Google Drive y obtén tu código QR para compartir.")

# Campo de entrada para el enlace
enlace = st.text_input("Enlace de Google Drive:", placeholder="https://drive.google.com/...")

if st.button("Generar QR"):
    if enlace.strip() == "":
        st.error("Por favor, ingresa un enlace válido.")
    else:
        # Instanciar y configurar el objeto QRCode
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(enlace)
        qr.make(fit=True)

        # Generar la imagen del QR
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Guardar la imagen en un buffer en memoria (BytesIO) para evitar escribir en disco
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        
        # Mostrar el QR en la interfaz de Streamlit
        st.image(buffer.getvalue(), caption="Tu Código QR", width=300)
        
        # Botón para descargar la imagen directamente
        st.download_button(
            label="Descargar Código QR",
            data=buffer.getvalue(),
            file_name="qr_drive.png",
            mime="image/png"
        )