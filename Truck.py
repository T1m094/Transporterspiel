import math

import pygame

import Settings
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
        self.currentPosition = [200,200]

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

    #######################################
    #       Steuerung LKW  Mouse          #
    #######################################
    def driveWithMouse(self):
        # Mouse Informationen
        mousePos = pygame.mouse.get_pos()
        mouseLeftClick = pygame.mouse.get_pressed()[0]
        mouseRightClick =  pygame.mouse.get_pressed()[2]

        # Vorwärts Rückwerts fahren
        if mouseLeftClick:
            self.currentSpeed += self.speedUp
            if self.currentSpeed >= self.maxSpeedForward:
                self.currentSpeed = self.maxSpeedForward
        elif mouseRightClick:
            self.currentSpeed = -self.maxSpeedBackward
        else:
            self.currentSpeed = 0

        #Winkel berechnen
        delta_x = mousePos[0]- self.currentPosition[0]
        delta_y = mousePos[1] -self.currentPosition[1]
        if Settings.debug:
         pygame.draw.aaline(Settings.screen, (0, 255, 0), self.currentPosition, mousePos)


        self.angle =  - math.degrees(math.atan2(delta_y, delta_x))

        # Bewegungsvektor des Autos berechnen
        car_dx = self.currentSpeed  * math.cos(math.radians(self.angle))
        car_dy = self.currentSpeed  * math.sin(math.radians(self.angle))

        # Position des Autos aktualisieren
        self.currentPosition[0] += car_dx
        self.currentPosition[1] -= car_dy
        self.steerVehicle()

    # Fahren/ Sprit verbrauchen
    #######################################
    #       Steuerung LKW  Tastatur       #
    #######################################
    def drive(self):
        # Überprüfe den Status aller Tasten
        keys = pygame.key.get_pressed()
        # Lenken
        if keys[pygame.K_LEFT]:
            self.angleSpeed = maxAngleSpeed
        elif keys[pygame.K_RIGHT]:
            self.angleSpeed = -maxAngleSpeed
        else:
            self.angleSpeed = 0

        # Vorwärts Rückwerts fahren
        if keys[pygame.K_UP]:
            self.fuelConsumption()
            self.currentSpeed += self.speedUp
            if( self.currentSpeed >= self.maxSpeedForward):
                self.currentSpeed = self.maxSpeedForward

        elif keys[pygame.K_DOWN]:
            self.fuelConsumption()
            self.currentSpeed = -self.maxSpeedBackward
        else:
            self.currentSpeed = 0

        # Winkel des Autos aktualisieren
        self.angle += self.angleSpeed
        if self.angle > 360:
            self.angle = 0
        elif self.angle < 0:
            self.angle = 360
        # Bewegungsvektor des Autos berechnen
        car_dx = self.currentSpeed  * math.cos(math.radians(self.angle))
        car_dy = self.currentSpeed  * math.sin(math.radians(self.angle))

        # Position des Autos aktualisieren
        self.currentPosition[0] += car_dx
        self.currentPosition[1] -= car_dy

        self.steerVehicle()

        if self.currentFuelLevel > 0:
            return True
        else:
            return False



