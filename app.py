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
st.markdown("<h1 style='text-align: center;'>📚 Plan de Clases 🎨</h1>", unsafe_allow_html=True)

# ---- IMAGEN DESDE GITHUB ----
st.image("https://raw.githubusercontent.com/jesusalvarado2023/nayeli2025/refs/heads/main/img/imagen001.png", caption="¡Bienvenida! 🧙‍♂️", use_column_width=True)


# ---- TABLA DE DATOS ----
data = {
    "Día": ["2025-05-06", "2025-05-07", "2025-05-08"],
    "Asignatura": ["Algebra 🧮", "Aritmética 🧬", "Geometría 🎨"],
    "Tema": ["Planteo de ecuaciones", "Numeración", "Ángulos y segmentos"]
}
df = pd.DataFrame(data)

st.markdown("### 📅 Horario de esta semana")
st.dataframe(df, use_container_width=True)

# ---- PIE DECORATIVO ----
st.markdown("💡 Alegría + Motivación = Gran sonrisa 😄")

