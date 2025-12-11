import requests
from telegram.ext import ApplicationBuilder, CommandHandler

TELEGRAM_TOKEN = "8544580629:AAE5a6jGHl3exQogq9uZ3IlYr5SgmjhWEOo"

def get_weather():
    try:
        url = "https://wttr.in/Khujand?format=j1"
        data = requests.get(url).json()

        current = data["current_condition"][0]
        temp = current["temp_C"]
        feels = current["FeelsLikeC"]
        desc = current["weatherDesc"][0]["value"]

        return (
            f"Погода в Худжанде:\n"
            f"🌡 Температура: {temp}°C\n"
            f"🤔 Ощущается как: {feels}°C\n"
            f"☁ {desc}"
        )
    except:
        return "❌ Ошибка: не удалось получить погоду."

async def start(update, context):
    weather_info = get_weather()
    await update.message.reply_text(weather_info)

def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    print("Бот запущен!")
    app.run_polling()

if __name__ == "__main__":
    main()
