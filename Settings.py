import pygame


#   Display
screen = pygame.display.set_mode()
pygame.font.init()
font = pygame.font.SysFont('Times', 15)

debug = True

debugPrints = True


def printDebugInfo(*args):

    if debugPrints:
        i = 0
        for array in args:
            for text_surface in array:
                screen.blit(text_surface, (20, i))
                i += 20
            i += 10


