import os
import time
import random
import argparse
from dotenv import load_dotenv
from telegram import Bot

DEFAULT_INTERVAL = 60 * 60 * 4  # 4 часа по умолчанию


def get_images_list(directory):
    """Получает список путей к файлам изображений в указанной директории."""
    return [os.path.join(directory, file) for file in os.listdir(directory) if file.lower().endswith(('jpeg', 'jpg', 'png', 'gif'))]


def start_publishing(bot, chat_id, directory, interval):
    """Публикует изображения из директории в чат с заданным интервалом."""
    while True:
        images = get_images_list(directory)
        if not images:
            return "В директории нет изображений для публикации."

        random.shuffle(images)

        for image in images:
            with open(image, "rb") as img:
                bot.send_photo(chat_id=chat_id, photo=img)
            time.sleep(interval)


def main():
    """Основная функция для запуска публикации изображений."""
    load_dotenv(".env")
    TG_TOKEN = os.getenv("TG_TOKEN")
    CHAT_ID = os.getenv("CHAT_ID")
    parser = argparse.ArgumentParser(
        description="Автоматическая публикация изображений в Telegram канал.")
    current_dir = os.path.dirname(__file__)
    img__path = f"{current_dir}/images"
    parser.add_argument("directory", default=img__path,
                        help="Путь к директории с изображениями.")
    parser.add_argument("--interval", type=int, default=DEFAULT_INTERVAL,
                        help="Интервал публикации в секундах (по умолчанию: 4 часа).")

    args = parser.parse_args()

    bot = Bot(token=TG_TOKEN)
    start_publishing(bot, args.chat_id, args.directory, args.interval)


if __name__ == "__main__":
    main()
