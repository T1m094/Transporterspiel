import base64
from io import BytesIO
import pygame

bg_byte_data = base64.b64decode(bg_str)
bg_image_data = BytesIO(bg_byte_data)
bgImage = pygame.image.load(bg_image_data)