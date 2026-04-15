import streamlit as st 
import random
from PIL import Image
import io

# ============================================
# CONFIGURACIÓN DE LA PÁGINA
# ============================================

st.set_page_config(
    page_title="Duck Detector",
    page_icon="🦆",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ============================================
# TÍTULO Y DESCRIPCIÓN
# ============================================

st.title("🦆 Duck Detector")
st.markdown("### Identifica especies de patos con inteligencia artificial")
st.markdown("---")

# Especies simuladas (después será el modelo real)
DUCK_SPECIES = [
    "Ánade Real (Mallard)",
    "Porrón Europeo (Tufted Duck)",
    "Cerceta Común (Common Teal)",
    "Pato Joyuyo (Whistling Duck)",
    "Pato Colorado (Red Shoveler)"
]

# ============================================
# SIDEBAR CON INFORMACIÓN
# ============================================

with st.sidebar:
    st.markdown("## 📋 Información")
    st.markdown("**Duck Detector v1.0**")
    st.markdown("Proyecto Programación III")
    st.markdown("---")
    st.markdown("### Especies detectables:")
    for species in DUCK_SPECIES:
        st.markdown(f"- {species}")
    st.markdown("---")
    st.markdown("### 📌 Nota")
    st.markdown("> Actualmente en modo simulación. El modelo real de IA se integrará próximamente.")

# ============================================
# SUBIR IMAGEN
# ============================================

st.markdown("## 📸 Sube una foto de un pato")

# Widget para subir imagen
uploaded_file = st.file_uploader(
    "Selecciona una imagen",
    type=["jpg", "jpeg", "png", "webp"],
    help="Formatos permitidos: JPG, PNG, WEBP. Máximo 16MB"
)

# ============================================
# PROCESAR IMAGEN Y PREDECIR
# ============================================

if uploaded_file is not None:
    # Leer la imagen
    image = Image.open(uploaded_file)
    
    # Mostrar la imagen
    st.markdown("### Vista previa")
    st.image(image, caption="Tu imagen", use_column_width=True)
    
    # Botón para analizar
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        analyze_button = st.button("🔍 Analizar pato", use_container_width=True)
    
    if analyze_button:
        # Mostrar spinner mientras "analiza"
        with st.spinner("Analizando imagen..."):
            # Simular tiempo de procesamiento
            import time
            time.sleep(1)
            
            # ============================================
            # SIMULACIÓN DE PREDICCIÓN
            # ============================================
            # Aquí después irá el modelo real de TensorFlow
            
            especie = random.choice(DUCK_SPECIES)
            confianza = random.uniform(0.65, 0.98)
            confianza_baja = confianza < 0.70
            
            # ============================================
            
            # Mostrar resultados
            st.markdown("---")
            st.markdown("## 🎯 Resultado")
            
            # Columnas para resultados
            col_result1, col_result2 = st.columns(2)
            
            with col_result1:
                if confianza_baja:
                    st.metric("🦆 Especie", especie, delta="⚠️ Confianza baja")
                else:
                    st.metric("🦆 Especie", especie)
            
            with col_result2:
                st.metric("📊 Confianza", f"{int(confianza * 100)}%")
            
            # Barra de progreso de confianza
            st.markdown("### Nivel de confianza")
            st.progress(confianza)
            
            # Mensaje adicional
            if confianza_baja:
                st.warning("⚠️ La confianza es baja. Intenta con otra imagen más clara.")
                st.markdown("**Sugerencias:**")
                st.markdown("- Usa una imagen con mejor iluminación")
                st.markdown("- Asegúrate que el pato se vea claramente")
                st.markdown("- Prueba con otra foto")
            else:
                st.success(f"✅ ¡Es un {especie}!")
                
                # Mostrar un dato curioso
                curiosidades = {
                    "Ánade Real": "Es una de las especies de patos más comunes en el mundo.",
                    "Porrón Europeo": "Tiene una característica cresta en la cabeza.",
                    "Cerceta Común": "Es uno de los patos más pequeños de Europa.",
                    "Pato Joyuyo": "Emite un silbido característico.",
                    "Pato Colorado": "El macho tiene un pico de color rojo intenso."
                }
                
                for key, value in curiosidades.items():
                    if key in especie:
                        st.info(f"📖 Dato curioso: {value}")
                        break

else:
    # Mostrar instrucciones cuando no hay imagen
    st.info("👆 Haz clic en 'Browse files' para seleccionar una imagen de un pato")
    
    # Mostrar ejemplo
    with st.expander("ℹ️ ¿Cómo funciona?"):
        st.markdown("""
        1. Haz clic en **Browse files** y selecciona una foto de un pato
        2. La imagen se mostrará en vista previa
        3. Presiona **Analizar pato**
        4. El sistema te dirá qué especie es y con qué confianza
        
        **Formatos soportados:** JPG, PNG, WEBP
        
        **Tamaño máximo:** 16MB
        """)

# ============================================
# FOOTER
# ============================================

st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray;'>Duck Detector v1.0 | Proyecto Programación III</div>",
    unsafe_allow_html=True
)