from PIL import Image

class ImageProcessor:
    @staticmethod
    def load(path):
        return Image.open(path).load()

    @staticmethod
    def export(image, path):
        image.save(path)
