import pygame

import Settings

# Lade Bild
imageFuelScale = pygame.image.load("scr/img/instrumentsDisplay/tanktachometer.png")
imageFuelScaleNeedle = pygame.image.load("scr/img/instrumentsDisplay/tanknadel.png")
pos = (660, Settings.screen.get_height() - imageFuelScale.get_height() - 20)
posImageFuelScale = (pos[0], pos[1])
posFuelScaleNeedle = (pos[0] + (imageFuelScale.get_width()/2), pos[1] +  imageFuelScale.get_height() + 20)



def drawLevelDisplay(vehicle, angelNeedle):

    Settings.screen.blit(imageFuelScale,posImageFuelScale)
    blitRotate(Settings.screen, imageFuelScaleNeedle, posFuelScaleNeedle, (0,0), angleCalculation(vehicle))

def angleCalculation(vehicle):
    fuleLevel = vehicle.currentFuelLevel
    # Bereich des Winkels von 0 bis -125
    angle_range = -125 - 0
    # Berechnung des Winkels entsprechend des aktuellen Füllstands
    angle = fuleLevel * angle_range / 100
    # Rückgabe des berechneten Winkels
    return angle


def blitRotate(surf, image, pos, originPos, angle):
    image_rect = image.get_rect(bottomright=(pos[0] - originPos[0], pos[1] - originPos[1]))
    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center

    rotated_offset = offset_center_to_pivot.rotate(-angle)

    rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)

    rotated_image = pygame.transform.rotate(image, angle)
    rotated_image_rect = rotated_image.get_rect(center=rotated_image_center)

    # rotate and blit the image
    surf.blit(rotated_image, rotated_image_rect)

    if Settings.debug:
        # draw rectangle around the image
        pygame.draw.rect(surf, (255, 0, 0), (*rotated_image_rect.topleft, *rotated_image.get_size()), 2)
        pygame.draw.line(surf, (0, 255, 0), (pos[0]-20, pos[1]), (pos[0]+20, pos[1]), 3)
        pygame.draw.line(surf, (0, 255, 0), (pos[0], pos[1]-20), (pos[0], pos[1]+20), 3)
        pygame.draw.circle(surf, (0, 255, 0), pos, 7, 0)

