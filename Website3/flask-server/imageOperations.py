from PIL import Image

def crop_image(input_image_path, area):
    # Open the original image
    original_image = Image.open(input_image_path)

    # Crop the image using the specified area (x, y, x+w, y+h)
    cropped_image = original_image.crop((area['x'], area['y'], area['x'] + area['w'], area['y'] + area['h']))

    # Return the cropped image
    return cropped_image
    