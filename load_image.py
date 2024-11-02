import os
import requests
from urllib.parse import urlparse


def load_image(url, place_to_save, name_of_img="img"):
    extension = os.path.splitext(urlparse(url).path)[1]

    response = requests.get(url)
    response.raise_for_status()

    with open(f"{place_to_save}/{name_of_img}{extension}", "wb") as file:
        file.write(response.content)
