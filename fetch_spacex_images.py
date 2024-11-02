import os
import argparse
import requests
from load_image import load_image

current_dir = os.path.dirname(__file__)
images_path = f"{current_dir}/images/spaceX/"


def fetch_spacex_last_launch(launch_id=None, place_to_save=images_path):
    spaceX_url = f"https://api.spacexdata.com/v5/launches/{launch_id}" if launch_id else "https://api.spacexdata.com/v5/launches/latest"
    spaceX_response = requests.get(spaceX_url)
    images_data = spaceX_response.json()
    flickr_images = images_data['links']['flickr']['original']

    for index, url in enumerate(flickr_images, start=1):
        img_name = f"spacex_{index}"
        load_image(url, place_to_save, name_of_img=img_name)


def main():
    parser = argparse.ArgumentParser(description="Download SpaceX launch images.")
    parser.add_argument("--launch_id", help="ID of the SpaceX launch to fetch images for.")
    args = parser.parse_args()
    fetch_spacex_last_launch(args.launch_id)


if __name__ == "__main__":
    main()
