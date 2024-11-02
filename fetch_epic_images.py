import os
import requests
from dotenv import load_dotenv
from load_image import load_image


current_dir = os.path.dirname(__file__)
images_path = f"{current_dir}/images/spaceX/"


def fetch_nasa_epic(api_key, place_to_save=images_path):
    url = "https://api.nasa.gov/EPIC/api/natural/images"
    params = {"api_key": api_key}
    response = requests.get(url, params=params)
    response.raise_for_status()

    base_url = "https://epic.gsfc.nasa.gov/archive/natural/"
    for img_data in response.json()[:10]:
        time_data = img_data['date'][:10].replace('-', '/')
        img_name = img_data["image"]
        img_url = f"{base_url}/{time_data}/png/{img_name}.png"
        load_image(img_url, place_to_save, name_of_img=img_name)


if __name__ == "__main__":
    load_dotenv(".env")
    API_KEY_NASA = os.getenv("API_KEY_NASA")
    fetch_nasa_epic(API_KEY_NASA)
