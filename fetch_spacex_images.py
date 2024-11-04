import os
import argparse
import requests
from load_image import load_image

def fetch_spacex_last_launch(launch_id=None, place_to_save=None):
    if place_to_save is None:
        current_dir = os.path.dirname(__file__)
        place_to_save = f"{current_dir}/images/spaceX/"
        
    spaceX_url = f"https://api.spacexdata.com/v5/launches/{launch_id}" if launch_id else "https://api.spacexdata.com/v5/launches/latest"
    spaceX_response = requests.get(spaceX_url)
    spaceX_response.raise_for_status()
    
    images = spaceX_response.json()
    flickr_images = images['links']['flickr']['original']

    for index, url in enumerate(flickr_images, start=1):
        img_name = f"spacex_{index}"
        load_image(url, place_to_save, name_of_img=img_name)

def main():
    parser = argparse.ArgumentParser(description="Download SpaceX launch images.")
    parser.add_argument("--launch_id", default=None, help="ID of the SpaceX launch to fetch images for.")
    args = parser.parse_args()
    
    CURRENT_DIR = os.path.dirname(__file__)
    IMAGES_PATH = f"{CURRENT_DIR}/images/spaceX/"
    
    fetch_spacex_last_launch(args.launch_id, place_to_save=IMAGES_PATH)

if __name__ == "__main__":
    main()
