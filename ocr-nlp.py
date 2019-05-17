import io
import six

from google.cloud import language
from google.cloud.language import enums
from google.cloud import vision

# Extract text from image

client = vision.ImageAnnotatorClient()

# path_to_image = 'img/test.png'
# path_to_image = 'img/english.jpg'
# path_to_image = 'img/angry.jpg'
path_to_image = 'img/spanish.jpg'

with io.open(path_to_image, 'rb') as image_file:
    content = image_file.read()

image = vision.types.Image(content=content)

response = client.text_detection(image=image)
texts = response.text_annotations

text_contet = texts[0].description
print(text_contet)

# Amalize sentiment and entities from text

client = language.LanguageServiceClient()

if isinstance(text_contet, six.binary_type):
    text_contet = text_contet.decode('utf-8')

type_ = enums.Document.Type.PLAIN_TEXT
document = {'type': type_, 'content': text_contet}

response = client.analyze_sentiment(document)
sentiment = response.document_sentiment
entities = client.analyze_entities(document).entities

sentiment_type = "neutral"

if sentiment.score >= 0.25:
    sentiment_type = "Positive"
elif sentiment.score > -0.25 and sentiment.score < 0.25:
    sentiment_type = "Neutral"
elif sentiment.score >= -1.0 and sentiment.score <= -0.25:
    sentiment_type = "Negative"

print('Calificación: {}\n'.format(sentiment.score))
print('Sentimiento: {}\n'.format(sentiment_type))
print('Magnitud: {}\n'.format(sentiment.magnitude))


for entity in entities:
    entity_type = enums.Entity.Type(entity.type)
    print('=' * 20)
    print(u'{:<16}: {}'.format('name', entity.name))
    print(u'{:<16}: {}'.format('type', entity_type.name))
    print(u'{:<16}: {}'.format('salience', entity.salience))
