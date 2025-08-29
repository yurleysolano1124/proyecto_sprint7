import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------
# Encabezado de la aplicación con estilo
# -----------------------------
st.markdown(
    "<h1 style='text-align: center; color: #FF4B4B;'>🚗 Exploración de datos de vehículos en EE. UU. 🚙</h1>",
    unsafe_allow_html=True
)

st.write(
    "Esta aplicación permite analizar un conjunto de datos de anuncios de venta de vehículos "
    "en Estados Unidos mediante **histogramas** y **gráficos de dispersión interactivos**."
)

# -----------------------------
# Leer el archivo CSV
# -----------------------------
car_data = pd.read_csv('vehicles_us.csv')

# -----------------------------
# Botón para construir histograma
# -----------------------------
hist_button = st.button('Construir histograma 📊')

if hist_button:
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de coches')
    fig_hist = px.histogram(
        car_data,
        x="odometer",
        nbins=50,
        title="Distribución del Odómetro",
        color_discrete_sequence=["#FF4B4B"]  # Color llamativo
    )
    fig_hist.update_layout(title_font=dict(size=22, color='#FF4B4B'))
    st.plotly_chart(fig_hist, use_container_width=True)

# -----------------------------
# Botón para construir gráfico de dispersión
# -----------------------------
scatter_button = st.button('Construir gráfico de dispersión 🔎')

if scatter_button:
    st.write('Creación de un gráfico de dispersión entre **precio** y **odómetro**')
    fig_scatter = px.scatter(
        car_data,
        x="odometer",
        y="price",
        color="price",  # Colorear los puntos por precio
        title="Precio vs. Odómetro",
        color_continuous_scale="Turbo"  # Escala de colores vibrante
    )
    fig_scatter.update_layout(title_font=dict(size=22, color='#0099FF'))
    st.plotly_chart(fig_scatter, use_container_width=True)

# -----------------------------
# Casilla de verificación adicional
# -----------------------------
show_data = st.checkbox("📋 Mostrar las primeras filas del dataset")
if show_data:
    st.write(car_data.head())
