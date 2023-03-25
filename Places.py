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


class oreMine:
    def __init__(self):
        self.pos = (Settings.screen.get_height()/2, 20)
        self.size = (500,500)
        self.rec = pygame.Rect(self.pos, self.size)
        self.percentOre = 100

    def draw(self):
        pygame.draw.rect(Settings.screen, (0,0,255), self.rec, 2)

    # Prüfen ob LKW an der Miene ist
    # Wenn ja, dann aufladen
    def checkLoad(self, vehicle):
        # TODO Miene percentOre veringern um Lademaenge
        if self.rec.contains(vehicle.rotated_image_rect):
            vehicle.loadOre()

class truckDestination:
    def __init__(self):
        self.pos = (Settings.screen.get_height()/2, 950)
        self.size = (500,500)
        self.rec = pygame.Rect(self.pos, self.size)
        self.percentOre = 0
    def draw(self):
        pygame.draw.rect(Settings.screen, (0,0,255), self.rec, 2)

    # Prüfen ob LKW im Ziel ist
    # Wenn ja, dann abladen
    def checkUnLoad(self, vehicle):
        if self.rec.contains(vehicle.rotated_image_rect):
            self.percentOre = vehicle.currentLoadedQuantity
            vehicle.uploadOre()