import os
from dotenv import load_dotenv
import requests
from load_image import load_image

current_dir = os.path.dirname(__file__)
images_path = f"{current_dir}/images/spaceX/"


def fetch_nasa_apod(api_key, place_to_save=images_path):

    params = {
        "api_key": api_key,
        "count": 30,
    }

    nasa_url = f"https://api.nasa.gov/planetary/apod"

    response = requests.get(nasa_url, params=params)
    response.raise_for_status()

    url_to_pic = response.json()

    for index, item in enumerate(url_to_pic, start=1):
        url = item.get("url")
        if url:
            file_name = f"nasa_apod_{index}"
            load_image(url, place_to_save, name_of_img=file_name)



if __name__ == "__main__":
    load_dotenv(".env")
    API_KEY_NASA = os.getenv("API_KEY_NASA")
    fetch_nasa_apod(API_KEY_NASA)
