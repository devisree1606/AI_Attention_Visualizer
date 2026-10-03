from PIL import Image, ImageOps, ImageFilter


def preprocess_image(image: Image.Image) -> Image.Image:

    image = ImageOps.grayscale(image)

    image = ImageOps.autocontrast(image)

    image = image.filter(ImageFilter.SHARPEN)

    return image