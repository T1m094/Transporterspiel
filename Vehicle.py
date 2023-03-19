import math

import pygame

import Settings

# Eigenschaften LKW
maxAngleSpeed = 5
maxSpeedForward = 10
maxSpeedBackward = 5
speedUp = 0.25
maxloadedQuantity = 10
maxFuelLevel = 10

'''
# Eigenschaften Hubschrauber
maxAngleSpeed = 0
maxSpeedForward  = 0
maxSpeedBackward = 0
maxloadedQuantity = 0
maxFuelLevel = 0
'''

class Truck:

    def __init__(self):
        self.basePosition = 0
        self.currentPosition = [0,0]
        self.angle = 0 # Min 0 Max 360  Oben=0 Links=90 unten=180 rechts=270
        self.maxSpeedForward = maxSpeedForward
        self.maxSpeedBackward = maxSpeedBackward
        self.speedUp = speedUp
        self.currentSpeed = 0
        self.angleSpeed = 0
        self.fuelLevel = 0
        self.loadedQuantity = 0

        #Bild
        # Bild laden
        image_path = "./scr/img/LKW.png"
        image = pygame.image.load(image_path)
        # Bild auf die Größe 200x200 skalieren
        image = pygame.transform.rotate(image, -90)
        self.image = pygame.transform.scale(image, (200, 200))
        #Bild Mitte
        self.imageCenterPoint =[(self.image.get_width()/2),(self.image.get_height()/2)]

    # Fahren/ Sprit verbrauchen
    def drive(self, keys):
        #######################################
        #       Steuerung LKW  Tastatur       #
        ######################################

        # Lenken
        if keys[pygame.K_LEFT]:
            if (Settings.debug):
                print("Left")
            self.angleSpeed = maxAngleSpeed
        elif keys[pygame.K_RIGHT]:
            if (Settings.debug):
                print("Right")
            self.angleSpeed = -maxAngleSpeed
        else:
            self.angleSpeed = 0

        # Vorwärts Rückwerts fahren
        if keys[pygame.K_UP]:
            if (Settings.debug):
                print("Hoch")
            self.currentSpeed += self.speedUp
            if( self.currentSpeed >= self.maxSpeedForward):
                self.currentSpeed = self.maxSpeedForward


        elif keys[pygame.K_DOWN]:
            if (Settings.debug):
                print("Runter")
            self.currentSpeed = -self.maxSpeedBackward
        else:
            self.currentSpeed = 0

        # Winkel des Autos aktualisieren
        self.angle += self.angleSpeed
        # Bewegungsvektor des Autos berechnen
        car_dx = self.currentSpeed  * math.cos(math.radians(self.angle))
        car_dy = self.currentSpeed  * math.sin(math.radians(self.angle))

        # Position des Autos aktualisieren
        self.currentPosition[0] += car_dx
        self.currentPosition[1] -= car_dy

        self.steerVehicle()
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
        rotated_image_rect = rotated_image.get_rect(center=rotated_image_center)

        # Zeichen
        Settings.screen.blit(rotated_image, rotated_image_rect)

        # V FOR DEBUG v
        # Hilfslienen
        if (Settings.debug):
            pygame.draw.rect(Settings.screen, (255, 0, 0), (*rotated_image_rect.topleft, *rotated_image.get_size()), 2)
            pygame.draw.line(Settings.screen, (0, 255, 0), (self.currentPosition[0] - 20, self.currentPosition[1]), (self.currentPosition[0] + 20, self.currentPosition[1]), 3)
            pygame.draw.line(Settings.screen, (0, 255, 0), (self.currentPosition[0], self.currentPosition[1] - 20), (self.currentPosition[0], self.currentPosition[1] + 20), 3)
            pygame.draw.circle(Settings.screen, (0, 255, 0), self.currentPosition, 7, 0)
        # ^ FOR DEBUG ^

    # Erz laden
    def loadOre(self):
        pass
    # Erz entladen
    def uploadOre(self):
        pass

    # Erz laden
    def loadOre(self):
        pass

    # Tanken
    def refuel(self):
        pass


    # Zeichen
    def show(self, screen):
        screen.blit(self.scaled_image, (0, 0))
        pass
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