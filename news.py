from dotenv import load_dotenv
import os
import feedparser
import requests

# Carga las variables de entorno del archivo .env
load_dotenv()

# Asegúrate de que cada feed RSS tenga un emoji correspondiente, puedes agregar diferentes fuentes RSS, solo tienes que seguir el mismo formato.

rss_feeds = [
    ('BBC', 'http://feeds.bbci.co.uk/news/world/rss.xml', "🌍"),
    ('Wired', 'https://es.wired.com/feed/rss', "📰"),
    ('El Periódico', 'https://www.elperiodico.com/es/rss/rss_portada.xml', "🔔"),
    ('Gebna', 'https://gebna.gg/rss.xml', "💻"),
]

# Información del bot y chat para Telegram desde el archivo .env
bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
chat_id = os.getenv('TELEGRAM_CHAT_ID')
weather_api_key = os.getenv('WEATHER_API_KEY')

# Función para procesar y formatear las noticias de cada feed
def process_feed(feed_title, feed_url, emoji):
    try:
        feed = feedparser.parse(feed_url)
        news_items = [f"📌 <b>{feed_title}</b>\n"]
        for i, entry in enumerate(feed.entries[:5]):
            news_items.append(f"{i+1}. {emoji} <a href='{entry.link}'>{entry.title}</a>\n")
        return "\n".join(news_items)
    except Exception as e:
        print(f"Error procesando el feed {feed_title}: {e}")
        return ""

# Función para obtener el informe del tiempo actualizado de la ciudad que quieras
def obtener_informe_del_tiempo(api_key, location="Barcelona"):
    try:
        url = f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={location}&days=1&aqi=yes&alerts=no"
        response = requests.get(url)
        response.raise_for_status()  # Lanza un error si la solicitud no es exitosa
        data = response.json()

        # Extraer información relevante
        condiciones_actuales = data["current"]["condition"]["text"]
        temperatura_actual = data["current"]["temp_c"]
        max_temp = data["forecast"]["forecastday"][0]["day"]["maxtemp_c"]
        min_temp = data["forecast"]["forecastday"][0]["day"]["mintemp_c"]
        posibilidad_lluvia = data["forecast"]["forecastday"][0]["day"]["daily_chance_of_rain"]

        mensaje_tiempo = f"⛅ <b>Tiempo hoy en {location}:</b>\n" \
                         f"- Condiciones actuales: {condiciones_actuales}, {temperatura_actual}°C\n" \
                         f"- Máxima/Mínima Hoy: {max_temp}°C / {min_temp}°C\n" \
                         f"- Posibilidad de lluvia: {posibilidad_lluvia}%\n"

        return mensaje_tiempo
    except Exception as e:
        print(f"Error obteniendo el informe del tiempo: {e}")
        return ""

# Primero, obtenemos el informe del tiempo
mensaje_final = obtener_informe_del_tiempo(weather_api_key)

# Luego, compilamos todas las noticias en una variable y la agregamos al mensaje final
for title, url, emoji in rss_feeds:
    mensaje_final += "\n" + process_feed(title, url, emoji) + "\n"

# Función para enviar mensaje a Telegram
def send_telegram_message(bot_token, chat_id, message):
    try:
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        payload = {
            "chat_id": chat_id,
            "text": message[:4096],
            "parse_mode": "HTML",
            "disable_web_page_preview": True
        }
        response = requests.post(url, json=payload)
        response.raise_for_status()  # Lanza un error si la solicitud no es exitosa
        print(response.json())
    except Exception as e:
        print(f"Error enviando mensaje a Telegram: {e}")

# Enviar el informe del tiempo seguido por el resumen de noticias
send_telegram_message(bot_token, chat_id, mensaje_final)
