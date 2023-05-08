import pygame
import gameOverView
import mainMenue

FPS = 60
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pygame.init()
    pygame.joystick.init()
    if pygame.joystick.get_count() != 0:
        joystick = pygame.joystick.Joystick(0)
        joystick.init()
    pygame.display.set_caption("Transporterspiel")
    mainMenue.mainMenue()
