import base64
from io import BytesIO
import pygame

byte_data = base64.b64decode(str)
image_data = BytesIO(byte_data)
bgImage = pygame.image.load(image_data)