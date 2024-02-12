class ImageSaveException(Exception):
    def __init__(self, image_name: str) -> None:
        self.message = f"Failed to save image {image_name}"
        super().__init__(self.message)
