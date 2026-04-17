import streamlit as st
from PIL import Image

# ============================================
# CONFIGURACIÓN DE LA PÁGINA
# ============================================

st.set_page_config(
    page_title="Duck Detector",
    page_icon="🦆",
    layout="centered"
)

# ============================================
# TÍTULO
# ============================================

st.title("🦆 Duck Detector")
st.markdown("### Identifica especies de patos con inteligencia artificial")
st.markdown("---")

# ============================================
# DDT-1: SUBIR IMAGEN DESDE PC
# ============================================

st.markdown("## 📸 Sube una foto de un pato")

# Widget para subir imagen
uploaded_file = st.file_uploader(
    "Selecciona una imagen",
    type=["jpg", "jpeg", "png", "webp"],
    help="Formatos permitidos: JPG, PNG, WEBP. Máximo 16MB"
)

# Mostrar la imagen si fue subida
if uploaded_file is not None:
    # Abrir la imagen
    image = Image.open(uploaded_file)
    
    # Mostrar vista previa
    st.markdown("### Vista previa")
    st.image(image, caption="Tu imagen", use_column_width=True)
    
    # Mostrar información de la imagen
    with st.expander("📋 Información de la imagen"):
        st.write(f"**Nombre del archivo:** {uploaded_file.name}")
        st.write(f"**Tamaño:** {uploaded_file.size / 1024:.2f} KB")
        st.write(f"**Tipo:** {uploaded_file.type}")
        st.write(f"**Dimensiones:** {image.width} x {image.height} píxeles")
    
    # Botón (por ahora solo informativo, luego hará la predicción)
    st.info("✅ Imagen cargada correctamente. La funcionalidad de análisis vendrá en DDT-2")
    
else:
    # Mostrar instrucciones cuando no hay imagen
    st.info("👆 Haz clic en 'Browse files' para seleccionar una imagen de un pato")
    
    with st.expander("ℹ️ ¿Cómo funciona?"):
        st.markdown("""
        1. Haz clic en **Browse files** y selecciona una foto de un pato
        2. La imagen se mostrará en vista previa
        3. Podrás ver información de la imagen (nombre, tamaño, dimensiones)
        4. Próximamente: análisis de la especie
        
        **Formatos soportados:** JPG, PNG, WEBP
        **Tamaño máximo:** 16MB
        """)

# ============================================
# FOOTER
# ============================================

st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray;'>Duck Detector v1.0 | DDT-1: Subir imagen ✅ | Proyecto Programación III</div>",
    unsafe_allow_html=True
)