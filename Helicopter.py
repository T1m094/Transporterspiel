import math

import pygame

import Settings
from Control import Control
from Truck import Truck
from Vehicle import Vehicle

# Eigenschaften Hubschrauber
maxSpeedForwardHeli = Settings.maxSpeedForwardHeli      # Maximalgeschwindigkeit Vorwärts
maxSpeedBackwardHeli = Settings.maxSpeedBackwardHeli    # Maximalgeschwindigkeit Rückwärts
speedUpHeli = Settings.speedUpHeli                      # Beschleunigung
maxAngleSpeedHeli = Settings.maxAngleSpeedHeli          # Wendekreis
maxLoadedQuantityHeli = Settings.maxLoadedQuantityHeli  # Maximale Ladekappazität Hubschrauber
fuelConsumptionHeli = Settings.fuelConsumptionHeli

class Helicopter(Vehicle):

    def __init__(self, base):
        self.name = "__Helicopter__"
        self.basePosition = base.rec.center
        #self.currentPosition = [((Settings.screen.get_height()/2) + 850), 350]
        self.currentPosition = [200, 800]

        self.maxSpeedForward = maxSpeedForwardHeli
        self.maxSpeedBackward = maxSpeedBackwardHeli
        self.speedUp = speedUpHeli
        self.currentSpeed = 0 #<-

        self.angle = 0 # Min 0 Max 360  Oben=0 Links=90 unten=180 rechts=270 #<-
        self.angleSpeed = maxAngleSpeedHeli

        self.maxFuelLevel = 100 #<-
        self.currentFuelLevel = 100 #<-

        self.maxLoadedQuantity = maxLoadedQuantityHeli
        self.currentLoadedQuantity = 0#<-

        self.control = Control(Settings.controllerHeli) #Steuerung auf Folgen 4


        #Bild
        # Bild laden
        image_path = "scr/img/heliRumpf.png"
        imageRotor_path = "scr/img/heliRotor.png"

        image = pygame.image.load(image_path)
        imageRotor = pygame.image.load(imageRotor_path)
        self.imageRotor = pygame.transform.scale(imageRotor, (300, 300))

        # Bild auf die Größe 200x200 skalieren
        image = pygame.transform.rotate(image, -90)
        self.image = pygame.transform.scale(image, (300, 120))

        #Bild Mitte
        self.imageCenterPoint =[(self.image.get_width()/2) + 60,(self.image.get_height()/2)]
        self.rotated_image_rect = pygame.Rect(self.currentPosition, (self.image.get_width(), self.image.get_height()))

        self.imageRotorCenterPoint =[(self.imageRotor.get_width()/2),(self.imageRotor.get_height()/2)]
        self.rotatedRotor_image_rect = pygame.Rect(self.currentPosition, (self.imageRotor.get_width(), self.imageRotor.get_height()))

        self.rotorAngle = 0


    def rotorSpins(self):


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
        blitRotate(Settings.screen, self.imageRotor, self.currentPosition, self.imageRotorCenterPoint, self.rotorAngle)

        self.rotorAngle += 6




    def flyToBase(self) -> None:

        basePosition = self.basePosition

        if self.currentPosition != basePosition:
            self.currentSpeed += self.speedUp
            if self.currentSpeed >= self.maxSpeedForward:
             self.currentSpeed = self.maxSpeedForward
             self.fuelConsumption()
        else:
            self.currentSpeed = 0

        # Winkel berechnen
        delta_x = basePosition[0] - self.currentPosition[0]
        delta_y = basePosition[1] - self.currentPosition[1]
        if Settings.debug:
            pygame.draw.aaline(Settings.screen, (255, 0, 255), self.currentPosition, basePosition)

        self.angle = - math.degrees(math.atan2(delta_y, delta_x))

        # Bewegungsvektor des Helis berechnen
        car_dx = self.currentSpeed * math.cos(math.radians(self.angle))
        car_dy = self.currentSpeed * math.sin(math.radians(self.angle))

        # Position des Helis aktualisieren
        self.currentPosition[0] += car_dx
        self.currentPosition[1] -= car_dy
        self.steerVehicle()

        self.rotorSpins()

    def followTruck(self,truck: Truck):
        self.control.drive(self, truck)
        self.rotorSpins()

    def checkAndStealOre(self, truck):
        if self.rotated_image_rect.collidepoint(truck.rotated_image_rect.center):
            if truck.currentLoadedQuantity > 0:
                if self.currentLoadedQuantity < self.maxLoadedQuantity:
                    self.loadOre()
                    truck.unloadOre()

