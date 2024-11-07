import os
import time
import random
import argparse
from dotenv import load_dotenv
from telegram import Bot



def get_images(directory):
    """Получает список путей к файлам изображений в указанной директории."""
    paths_to_images=[]
    for file in os.listdir(directory):
        if file.lower().endswith(('jpeg', 'jpg', 'png', 'gif')):
            paths_to_images.append(os.path.join(directory, file))
        
    return paths_to_images

def start_publishing(bot, chat_id, directory, interval):
    """Публикует изображения из директории в чат с заданным интервалом."""
    while True:
        images = get_images(directory)
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
    tg_token = os.getenv("TG_TOKEN")
    chat_id = os.getenv("CHAT_ID")
    default_interval = 60 * 60 * 4  # 4 часа по умолчанию
    
    parser = argparse.ArgumentParser(
        description="Автоматическая публикация изображений в Telegram канал.")
    current_dir = os.path.dirname(__file__)
    img__path = f"{current_dir}/images"
    parser.add_argument("directory", default=img__path,
                        help="Путь к директории с изображениями.")
    parser.add_argument("--interval", type=int, default=default_interval,
                        help="Интервал публикации в секундах (по умолчанию: 4 часа).")

    args = parser.parse_args()
    
    bot = Bot(token=tg_token)
    start_publishing(bot, chat_id, args.directory, args.interval)


if __name__ == "__main__":
    main()
