import os
from dotenv import load_dotenv
import requests
from load_image import load_image

def fetch_nasa_apod(api_key, place_to_save, amount_of_images=5):
    params = {
        "api_key": api_key,
        "count": amount_of_images
    }
    nasa_url = f"https://api.nasa.gov/planetary/apod"
    response = requests.get(nasa_url, params=params)
    response.raise_for_status()

    images = response.json()
    for number, image in enumerate(images, start=1):
        url = image.get("url")
        if url:
            file_name = f"nasa_apod_{number}"
            load_image(url, place_to_save, name_of_img=file_name)

if __name__ == "__main__":
    load_dotenv(".env")
    CURRENT_DIR = os.path.dirname(__file__)
    IMAGES_PATH = f"{current_dir}/images/spaceX/"
    API_KEY_NASA = os.getenv("API_KEY_NASA")

    if API_KEY_NASA:
        fetch_nasa_apod(API_KEY_NASA, images_path)
    else:
        print("API_KEY_NASA is missing in environment variables.")
