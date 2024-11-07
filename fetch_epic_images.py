import os
import requests
from dotenv import load_dotenv
from load_image import load_image

def fetch_nasa_epic(api_key, place_to_save):
    url = "https://api.nasa.gov/EPIC/api/natural/images"
    params = {"api_key": api_key}
    response = requests.get(url, params=params)
    response.raise_for_status()

    base_url = "https://epic.gsfc.nasa.gov/archive/natural/"
    image_amount = 10
    for image in response.json()[:image_amount]:
        formatted_time = image['date'][:10].replace('-', '/')
        img_name = image["image"]
        img_url = f"{base_url}/{formatted_time}/png/{img_name}.png"
        load_image(img_url, place_to_save, name_of_img=img_name)

if __name__ == "__main__":
    load_dotenv(".env")
    current_dir = os.path.dirname(__file__)
    place_to_save = f"{current_dir}/images/spaceX/"
    api_key_nasa = os.getenv("api_key_nasa")

    if API_KEY_NASA:
        fetch_nasa_epic(API_KEY_NASA, place_to_save)
    else:
        print("api_key_nasa is missing in environment variables.")
