import pygame

import Settings


class GasStation:
    def __init__(self):
        self.pos = (20,(Settings.screen.get_height()/2) -100)
        self.size = (500,500)
        self.rec = pygame.Rect(self.pos, self.size)



    def draw(self):
        pygame.draw.rect(Settings.screen, (255,0,0), self.rec, 2)

    #Prüfe ob getakt wird
    def checkRefuels(self, vehicle):
        if self.rec.contains(vehicle.rotated_image_rect):
            vehicle.refuel()
