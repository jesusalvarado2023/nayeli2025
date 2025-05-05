#nayeli2025
import streamlit as st
import pandas as pd

# ---- DISEÑO INFANTIL ----
st.set_page_config(page_title="Plan de Clases 🧁", page_icon="🎈", layout="centered")

# ---- FONDO DECORATIVO ----
st.markdown(
    """
    <style>
        body {
            background-color: #FFF0F5;
        }
        .main {
            background-color: #FFFAFA;
            border-radius: 15px;
            padding: 20px;
            box-shadow: 0 0 10px #FFB6C1;
        }
        h1 {
            color: #FF69B4;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# ---- TÍTULO ----
st.markdown("<h1 style='text-align: center;'>📚 Plan de Clases de Nayeli🎨</h1>", unsafe_allow_html=True)


# ---- TABLA DE DATOS ----
data = {
    "Día": ["Domingo 2025-05-04", "2025-05-11", "2025-05-18"],
    "Asignatura": ["Algebra 🧮", "Aritmética 🧬", "Geometría 🎨"],
    "Tema": ["Planteo de ecuaciones", "Numeración", "Ángulos y segmentos"]
}
df = pd.DataFrame(data)

st.markdown("### 📅 Horario")
st.dataframe(df, use_container_width=True)


# ---- IMAGEN DESDE GITHUB ----
st.image("https://raw.githubusercontent.com/jesusalvarado2023/nayeli2025/refs/heads/main/img/imagen001.png", caption="¡Bienvenida Nayeli! 🧙‍♂️", use_container_width=True)


# ---- PIE DECORATIVO ----
st.markdown("💡 Alegría + Motivación = Gran sonrisa 😄")

