class ImageDownloadException(Exception):
    def __init__(self, image_url: str) -> None:
        self.message = f"Trying to download image from url {image_url}"
        super().__init__(self.message)
