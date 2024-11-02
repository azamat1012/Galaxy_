import os
from dotenv import load_dotenv
import requests
from load_image import load_image

load_dotenv(".env")
current_dir = os.path.dirname(__file__)
images_path = f"{current_dir}/images/spaceX/"
API_KEY_NASA = os.getenv("API_KEY_NASA")

def fetch_nasa_apod(api_key, place_to_save=images_path):
    amount_of_images
    params = {
        "api_key": api_key,
        "count": amount_of_images
    }
    nasa_url = f"https://api.nasa.gov/planetary/apod"
    response = requests.get(nasa_url, params=params)
    response.raise_for_status()

    images_data = response.json()
    for index_of_image, image_data in enumerate(images_data, start=1):
        url = image_data.get("url")
        if url:
            file_name = f"nasa_apod_{index_of_image}"
            load_image(url, place_to_save, name_of_img=file_name)


def main():
    fetch_nasa_apod(API_KEY_NASA)


if __name__ == "__main__":
    main()
