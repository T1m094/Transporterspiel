import sys

import pygame

from pygame.locals import *
pygame.init()
pygame.display.set_caption('game base')
screen = pygame.display.set_mode((500, 500), 0, 32)
clock = pygame.time.Clock()

pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
for joystick in joysticks:
    print(joystick.get_name())

my_square = pygame.Rect(50, 50, 50, 50)
my_square_color = 0
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
motion = [0, 0]

#threshold = 0.1

while True:

    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, colors[my_square_color], my_square)
    if abs(motion[0]) < 0.1:
        motion[0] = 0
    if abs(motion[1]) < 0.1:
        motion[1] = 0
    my_square.x += motion[0] * 10
    my_square.y += motion[1] * 10

    for event in pygame.event.get() :
        print(event)
        if event.type == pygame.JOYAXISMOTION:
            if event.axis == 4:  # Achsenindex für R2-Taste
                # Berechne den Schwellenwert basierend auf dem aktuellen Wert
                threshold = int((event.value + 1) * 50)
                # Gib den aktuellen Schwellenwert aus
                print(threshold)




    pygame.display.update()
    clock.tick(60)