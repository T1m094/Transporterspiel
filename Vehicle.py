import math

import pygame

import Settings

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
        self.rotated_image = pygame.transform.rotate(self.image, self.angle)
        self.rotated_image_rect = self.rotated_image.get_rect(center=rotated_image_center)

        # Falls der Rand erreicht wird, soll das Fahrzeug nicht weiter fahren
        # Links
        if (self.currentPosition[0] < 0):
            self.currentSpeed = 0
            self.currentPosition[0] = self.currentPosition[0] + 10

        # Rechts
        elif (self.currentPosition[0] > Settings.screen.get_width()):
            self.currentSpeed = 0
            self.currentPosition[0] = self.currentPosition[0] - 10

        # Oben
        elif (self.currentPosition[1] < 0):
            self.currentSpeed = 0
            self.currentPosition[1] = self.currentPosition[1] + 10

        # Unten
        elif (self.currentPosition[1] > Settings.screen.get_height()):
            self.currentSpeed = 0
            self.currentPosition[1] = self.currentPosition[1] - 10

        # Zeichen und updaten
        Settings.screen.blit(self.rotated_image, self.rotated_image_rect)

        # V FOR DEBUG v
        # Hilfslienen
        if (Settings.debug):
            pygame.draw.rect(Settings.screen, (255, 0, 0), (*self.rotated_image_rect.topleft, *self.rotated_image.get_size()), 2)
            pygame.draw.line(Settings.screen, (0, 255, 0), (self.currentPosition[0] - 20, self.currentPosition[1]), (self.currentPosition[0] + 20, self.currentPosition[1]), 3)
            pygame.draw.line(Settings.screen, (0, 255, 0), (self.currentPosition[0], self.currentPosition[1] - 20), (self.currentPosition[0], self.currentPosition[1] + 20), 3)
            pygame.draw.circle(Settings.screen, (0, 255, 0), self.currentPosition, 7, 0)
        # ^ FOR DEBUG ^

    # Erz entladen
    def unloadOre(self):
        if Settings.controllerTruck == 3:
            pygame.joystick.Joystick(0).rumble(0.5, 0.5, 100)
        if self.currentLoadedQuantity > 0:
            self.currentLoadedQuantity -= 1

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

        text = f"currentpos: {self.currentPosition}"
        text_surface = Settings.font.render(str(text) , False, Settings.debugInfoColor)
        info.append(text_surface)

        text = f"currentSpeed: {self.currentSpeed}"
        text_surface = Settings.font.render(str(text) , False, Settings.debugInfoColor)
        info.append(text_surface)

        text = f"MaxSpeed: {Settings.maxSpeedForwardTruck[Settings.difficulty]}"
        text_surface = Settings.font.render(str(text) , False, Settings.debugInfoColor)
        info.append(text_surface)

        text = f"angle: {self.angle}"
        text_surface = Settings.font.render(str(text), False, Settings.debugInfoColor)
        info.append(text_surface)

        text = f"currentFuelLevel: {self.currentFuelLevel}"
        text_surface = Settings.font.render(str(text), False, Settings.debugInfoColor)
        info.append(text_surface)

        text = f"currentLoadedQuantity: {self.currentLoadedQuantity}"
        text_surface = Settings.font.render(str(text), False, Settings.debugInfoColor)
        info.append(text_surface)

        return info



