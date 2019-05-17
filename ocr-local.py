import io

def detect_text(path):
    """Detects text in the file."""
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    
    print(texts[0].description)

# path_to_image = 'img/test.png'
# path_to_image = 'img/english.jpg'
# path_to_image = 'img/angry.jpg'
path_to_image = 'img/spanish.jpg'

detect_text(path_to_image)
