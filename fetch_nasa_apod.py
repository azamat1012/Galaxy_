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
    current_dir = os.path.dirname(__file__)
    place_to_save = f"{current_dir}/images/spaceX/"
    api_key_nasa = os.getenv("API_KEY_NASA")

    if api_key_nasa:
        fetch_nasa_apod(api_key_nasa, place_to_save)
    else:
        print("API_KEY_NASA is missing in environment variables.")
