# Product Review Sentiment Analysis App

Bienvenido al repositorio de la aplicación **Product Review Sentiment Analysis**. Esta aplicación fue desarrollada para analizar el sentimiento de las opiniones de productos utilizando el poder de la API de OpenAI.

Las reviews se obtuvieron del sition [Mercado Libre Argentina](https://www.mercadolibre.com.ar/) utilizando las diferentes [APIs](https://developers.mercadolibre.com.ar/es_ar) que tienen disponibles en su web para developers.

## Características

- **Análisis de sentimiento:** Proporciona una evaluación del sentimiento de las opiniones de los productos, clasificándolas en Positivas o Negativas.
- **Interfaz fácil de usar:** Creada con Streamlit.
- **API de OpenAI:** Utiliza el modelo GPT para analizar el sentimiento de las opiniones.

## Tecnologías Utilizadas

- **OpenAI API:** Para procesar y clasificar las opiniones en términos de sentimiento.
- **Streamlit:** Para desarrollar la interfaz de usuario y desplegar la aplicación.

### Ejecución de una aplicación en local

1. **Clonar el repositorio:**
   ```bash
   git clone git@github.com:pablojrosa/SentimentAnalysis.git
   ```

2. **Crear una carpeta en la raiz del proyecto llamada `.streamlit`:** Será utilizada por streamlit para obtener las credenciales necesarias.

3. **Dentro de la carpeta `.streamlit`, crear un archivo llamado `secrets.toml` y agregar el API key de OpenAI:**
   ```
   OPENAI_API_KEY = "sk-proj-lasd1232131"
   ```

4. **Instalar las dependencias necesarias:**
   ```
   pip install -r requirements.txt
   ```
   O
   ```
   pip3 install -r requirements.txt
   ```

5. **Ejecutar la aplicación usando Streamlit:**
   ```
   python -m streamlit run app.py
   ```
   O si estás utilizando Python 3:
   ```
   python3 -m streamlit run app.py
   ```