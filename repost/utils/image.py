import logging
from os import remove, path


def remove_img(img_name: str) -> None:
    logging.info(f"Trying to remove the image with name: {img_name}...")

    if path.exists(img_name):
        remove(img_name)
        logging.info(f"Deleted image {img_name}")
    else:
        logging.warning(f"Image {img_name} does not exist, it cannot be deleted")
