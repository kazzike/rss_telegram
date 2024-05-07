# Proyecto de Noticias RSS y Clima para Telegram

Este proyecto es un script de Python que recopila noticias de varios feeds RSS y un informe del tiempo, y luego envía esta información a un chat de Telegram.

## Estructura del Proyecto

El proyecto consta de los siguientes archivos:

- `script.py`: El script principal que ejecuta todas las tareas.
- `.env`: Un archivo que contiene las variables de entorno necesarias para el script.

## Pre-requisitos

Antes de ejecutar el script, asegúrate de tener instalado Python en tu sistema. Además, necesitarás instalar las siguientes librerías:

- `feedparser`: Para procesar los feeds RSS.
- `requests`: Para realizar solicitudes HTTP.
- `python-dotenv`: Para cargar las variables de entorno desde un archivo `.env`.

Puedes instalar estas librerías utilizando `pip`:

``` pip install feedparser requests python-dotenv ```

## Configuración

* Clonar el Repositorio: * Clona este repositorio en tu máquina local usando git clone.
  
* Archivo .env: * Crea un archivo .env en el directorio raíz del proyecto con el siguiente contenido:
  
** WEATHER_API_KEY=tu_clave_api_del_servicio_de_clima **

** TELEGRAM_BOT_TOKEN=tu_token_de_bot_de_telegram **

** TELEGRAM_CHAT_ID=tu_id_de_chat_de_telegram **

Reemplaza los valores de ejemplo con tus claves API y tokens reales.

* Ejecución: * Ejecuta el script con el siguiente comando:
  
``` python script.py ```

## Uso
El script se ejecutará automáticamente y realizará las siguientes acciones:

- Obtener el informe del tiempo actualizado para la ubicación especificada.
- Recopilar las últimas noticias de los feeds RSS proporcionados.
- Enviar un mensaje a Telegram con el informe del tiempo y las noticias.

## Contribuciones
Las contribuciones son bienvenidas. Si tienes alguna sugerencia para mejorar el script, no dudes en crear un ‘pull request’ o abrir un ‘issue’.

## Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.
