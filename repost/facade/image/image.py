import logging
from io import BytesIO

from PIL import Image
from requests import get, RequestException

from repost.exception.image_download_exception import ImageDownloadException
from repost.exception.image_save_exception import ImageSaveException

IMAGE_FORMAT = "PNG"


def save_url_image(image_url: str, image_name: str) -> str:
    logging.info(f"Trying to download image from url {image_url}...")

    try:
        resp = get(image_url, stream=True)  # TODO Download imgur images
        resp.raise_for_status()
    except RequestException:
        logging.error(f"Failed to download image from url {image_url}", exc_info=True)
        raise ImageDownloadException(image_url)

    try:
        image = Image.open(BytesIO(resp.raw.read()))
        image.save(image_name, IMAGE_FORMAT)
    except IOError:
        logging.error(f"Failed to save image {image_name}", exc_info=True)
        raise ImageSaveException(image_name)

    logging.info(f"Image saved with name: {image_name}")
    return image_name
