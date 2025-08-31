# 🚗 Exploración de Datos de Vehículos en EE. UU.  

Esta aplicación web interactiva, desarrollada con **Streamlit**, **Pandas** y **Plotly Express**, permite explorar de manera visual y dinámica un conjunto de datos de anuncios de venta de coches en Estados Unidos. La app combina **interactividad**, **visualizaciones atractivas** y **control del usuario** para un análisis rápido y comprensible de la información. Incluye un encabezado con estilo, un **histograma del odómetro**, un **gráfico de dispersión entre precio y odómetro** con colores llamativos y opción de mostrar las primeras filas del dataset.  

### 🌟 Funcionalidades principales
- **Encabezado llamativo:** Título centrado con emojis y colores personalizados, con breve descripción de la app.  
- **Histograma del odómetro:** Botón "Construir histograma 📊" que genera un histograma de `odometer` (kilometraje) con 50 bins y color rojo vibrante para ver la distribución de los vehículos.  
- **Gráfico de dispersión Precio vs. Odómetro:** Botón "Construir gráfico de dispersión 🔎" que muestra la relación entre `price` y `odometer`, con puntos coloreados según precio usando una escala de colores continua y vibrante, útil para detectar patrones y outliers.  
- **Visualización del dataset:** Casilla "📋 Mostrar las primeras filas del dataset" que permite inspeccionar directamente los registros del CSV.  

### ⚙️ Instalación
1. Clonar el repositorio:
```bash
git clone https://github.com/TU-USUARIO/vehicles-streamlit-app.git
cd vehicles-streamlit-app
Crear y activar un entorno virtual:

Con Conda:

bash
Copiar código
conda create -n vehicles_env python=3.10 -y
conda activate vehicles_env
Con venv (alternativa):

bash
Copiar código
python3 -m venv venv
source venv/bin/activate   # macOS / Linux
venv\Scripts\activate      # Windows
Instalar dependencias:

bash
Copiar código
pip install -r requirements.txt
# o manualmente:
pip install streamlit pandas plotly
▶️ Ejecución
bash
Copiar código
streamlit run app.py
Se abrirá en http://localhost:8501.

Para cambiar el puerto:

bash
Copiar código
streamlit run app.py --server.port 8502
📊 Especificaciones técnicas
Lenguajes y librerías: Python 3.10, Streamlit, Pandas, Plotly Express.

Dataset: vehicles_us.csv, contiene información de vehículos como precio, kilometraje, modelo y año.

Interactividad: Botones y casillas de verificación permiten generar gráficos y visualizar datos bajo demanda.

Visualización: Histograma rojo llamativo y gráfico de dispersión con escala de color continua y títulos estilizados.

📂 Estructura del proyecto
bash
Copiar código
vehicles-streamlit-app/
├─ app.py             # Código principal
├─ vehicles_us.csv    # Dataset de vehículos
├─ requirements.txt   # Dependencias
└─ README.md          # Documentación
🚀 Despliegue en la nube
Publicación gratuita con Streamlit Cloud: conectar GitHub, seleccionar repo y archivo app.py, presionar Deploy y obtener enlace público.

## 🌐 Acceso a la aplicación
Puedes acceder a la aplicación desplegada aquí: [Mi App en Render
(https://proyecto-sprint7-86gv.onrender.com)
