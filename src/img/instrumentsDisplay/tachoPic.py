import base64
from io import BytesIO
import pygame
from PIL import Image

str = b'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'
byte_data = base64.b64decode(str)
image_data = BytesIO(byte_data)
tachoImage = Image.open(image_data)

# Konvertieren des Bildes in ein unterstütztes Format
if tachoImage.mode != 'RGB':
    pil_image = tachoImage.convert('RGB')
tachoImage.save('temp.bmp')

# Laden des Bildes in ein Surface-Objekt
tachoImage = pygame.image.load('temp.bmp').convert_alpha()
