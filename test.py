import math

import pygame


def blitRotate(surf, image, pos, originPos, angle):
    # offset from pivot to center
    image_rect = image.get_rect(topleft=(pos[0] - originPos[0], pos[1] - originPos[1]))
    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center

    # roatated offset from pivot to center
    rotated_offset = offset_center_to_pivot.rotate(-angle)

    # roatetd image center
    rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)

    # get a rotated image
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_image_rect = rotated_image.get_rect(center=rotated_image_center)

    # rotate and blit the image
    surf.blit(rotated_image, rotated_image_rect)

    # draw rectangle around the image
    #pygame.draw.rect(surf, (255, 0, 0), (*rotated_image_rect.topleft, *rotated_image.get_size()), 2)
    #pygame.draw.line(screen, (0, 255, 0), (pos[0]-20, pos[1]), (pos[0]+20, pos[1]), 3)
    #pygame.draw.line(screen, (0, 255, 0), (pos[0], pos[1]-20), (pos[0], pos[1]+20), 3)
    #pygame.draw.circle(screen, (0, 255, 0), pos, 7, 0)


pygame.init()
screen = pygame.display.set_mode((1000, 1000))
clock = pygame.time.Clock()


#IMAGE
image_path = "./scr/img/LKW.png"
image = pygame.image.load(image_path)
# Bild auf die Größe 200x200 skalieren
image = pygame.transform.scale(image, (200, 200))
image = pygame.transform.rotate(image, -90)


# Auto-Position und Winkel
car_x = (screen.get_width()/2)
car_y = (screen.get_height()/2)
car_angle = 0

# Auto-Geschwindigkeit und Winkelgeschwindigkeit
car_speed = 0
car_angle_speed = 0

w, h = image.get_size()

done = False
while not done:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            # Pfeiltasten abfragen
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                car_speed = 10
            elif event.key == pygame.K_DOWN:
                car_speed = -5
            elif event.key == pygame.K_LEFT:
                car_angle_speed = 5
            elif event.key == pygame.K_RIGHT:
                car_angle_speed = -5

            # Pfeiltasten loslassen
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                car_speed = 0
            elif event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                car_angle_speed = 0
    # Winkel des Autos aktualisieren
    car_angle += car_angle_speed

    # Bewegungsvektor des Autos berechnen
    car_dx = car_speed * math.cos(math.radians(car_angle))
    car_dy = car_speed * math.sin(math.radians(car_angle))




    # Position des Autos aktualisieren
    car_x += car_dx
    car_y -= car_dy

    # Auto-Bild rotieren
    rotated_car_image = blitRotate(screen, image, (car_x, car_y), (image.get_width()/2, image.get_height()/2), car_angle)

    # Auto-Bild zeichnen
    print(car_x, car_y)
   # screen.blit(rotated_car_image, (car_x, car_y))

    pygame.display.flip()
    screen.fill(0)

pygame.quit()
exit()