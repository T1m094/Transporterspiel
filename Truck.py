import math

import pygame

import Settings
from Control import Control
from Vehicle import Vehicle

# Eigenschaften LKW
maxSpeedForward = Settings.maxSpeedForward
maxSpeedBackward = Settings.maxSpeedBackward
speedUp = Settings.speedUp
maxAngleSpeed = Settings.maxAngleSpeed
maxLoadedQuantity = Settings.maxLoadedQuantity
fuelConsumption = Settings.fuelConsumption

class Truck(Vehicle):
    def __init__(self):
        self.name = "__Truck__"
        self.basePosition = 0
        self.currentPosition = [200, 200]

        self.maxSpeedForward = maxSpeedForward
        self.maxSpeedBackward = maxSpeedBackward
        self.speedUp = speedUp
        self.currentSpeed = 0 #<-

        self.angle = 0 # Min 0 Max 360  Oben=0 Links=90 unten=180 rechts=270 #<-
        self.angleSpeed = maxAngleSpeed

        self.maxFuelLevel = 100 #<-
        self.currentFuelLevel = 100 #<-

        self.maxLoadedQuantity = maxLoadedQuantity
        self.currentLoadedQuantity = 0 #<-

        self.control = Control(1) #Steuerung <-TODO:

        #Bild
        # Bild laden
        image_path = "scr/img/LKW.png"
        image = pygame.image.load(image_path)
        # Bild auf die Größe 200x200 skalieren
        image = pygame.transform.rotate(image, -90)
        self.image = pygame.transform.scale(image, (200, 200))
        #Bild Mitte
        self.imageCenterPoint =[(self.image.get_width()/2),(self.image.get_height()/2)]
        self.rotated_image_rect = pygame.Rect(self.currentPosition, (self.image.get_width(), self.image.get_height()))
    def steering(self):
        return self.control.drive(self)


