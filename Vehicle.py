import math

import pygame

import Settings

# Eigenschaften LKW
maxSpeedForward = Settings.maxSpeedForwardTruck
maxSpeedBackward = Settings.maxSpeedBackwardTruck
speedUp = Settings.speedUpTruck
maxAngleSpeed = Settings.maxAngleSpeedTruck
maxLoadedQuantity = Settings.maxLoadedQuantityTruck
fuelConsumption = Settings.fuelConsumptionTruck


maxFuelLevel = 100

class Vehicle:
    # Fahrzeug lenken
    def steerVehicle(self):
        # offset from pivot to center
        image_rect = self.image.get_rect(topleft=(self.currentPosition[0] - self.imageCenterPoint[0], self.currentPosition[1] - self.imageCenterPoint[1]))
        offset_center_to_pivot = pygame.math.Vector2(self.currentPosition) - image_rect.center

        # Drehpunkt Mitte
        rotated_offset = offset_center_to_pivot.rotate(-self.angle)

        # roatetd image center
        rotated_image_center = (self.currentPosition[0] - rotated_offset.x, self.currentPosition[1] - rotated_offset.y)

        # gedrehtes Bild erhalten
        rotated_image = pygame.transform.rotate(self.image, self.angle)
        self.rotated_image_rect = rotated_image.get_rect(center=rotated_image_center)

        # Zeichen und updaten
        Settings.screen.blit(rotated_image, self.rotated_image_rect)

        # V FOR DEBUG v
        # Hilfslienen
        if (Settings.debug):
            pygame.draw.rect(Settings.screen, (255, 0, 0), (*self.rotated_image_rect.topleft, *rotated_image.get_size()), 2)
            pygame.draw.line(Settings.screen, (0, 255, 0), (self.currentPosition[0] - 20, self.currentPosition[1]), (self.currentPosition[0] + 20, self.currentPosition[1]), 3)
            pygame.draw.line(Settings.screen, (0, 255, 0), (self.currentPosition[0], self.currentPosition[1] - 20), (self.currentPosition[0], self.currentPosition[1] + 20), 3)
            pygame.draw.circle(Settings.screen, (0, 255, 0), self.currentPosition, 7, 0)
        # ^ FOR DEBUG ^
    # Spritt verbrauchen
    def fuelConsumption(self):
        self.currentFuelLevel -= fuelConsumption
    # Erz entladen
    def unloadOre(self):
        if self.currentLoadedQuantity > 0:
            self.currentLoadedQuantity -= 1


    # Erz aufladen
    def loadOre(self):
        if self.currentLoadedQuantity < self.maxLoadedQuantity:
            self.currentLoadedQuantity += 1

    # Tanken
    def refuel(self):
        if self.currentFuelLevel < self.maxFuelLevel:
            self.currentFuelLevel += 1

    # Debug info LKW
    def debugPrinterArry(self):
        info = []

        text = self.name
        text_surface = Settings.font.render(str(text) , False, Settings.debugInfoColor)
        info.append(text_surface)

        text = 'currentpos: ' + str(self.currentPosition)
        text_surface = Settings.font.render(str(text) , False, Settings.debugInfoColor)
        info.append(text_surface)

        text = 'currentSpeed: ' + str(self.currentSpeed)
        text_surface = Settings.font.render(str(text) , False, Settings.debugInfoColor)
        info.append(text_surface)

        text = 'angle: ' + str(self.angle)
        text_surface = Settings.font.render(str(text), False, Settings.debugInfoColor)
        info.append(text_surface)

        text = 'currentFuelLevel: ' + str(self.currentFuelLevel)
        text_surface = Settings.font.render(str(text), False, Settings.debugInfoColor)
        info.append(text_surface)

        text = 'currentLoadedQuantity: ' + str(self.currentLoadedQuantity)
        text_surface = Settings.font.render(str(text), False, Settings.debugInfoColor)
        info.append(text_surface)

        return info



'''
class Lkw(Vehicle):
    # Bild laden
    image_path = "./scr/img/LKW.png"
    image = pygame.image.load(image_path)
    # Bild auf die Größe 200x200 skalieren
    scaled_image = pygame.transform.scale(image, (200, 200))
    #scaled_image = pygame.transform.rotate(scaled_image, degree)

    def __init__(self):
        super().__init__()

    def showSpeed(self):
        print(self.speed)

    def steerCarRight(self):
        self.rotateImgRight()

    def steerCarLeft(self):
        self.rotateImgLeft()

'''