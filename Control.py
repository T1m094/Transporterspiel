import math

import pygame

import Settings
import main


class Control:
    MAXSPEEDFORWARD = Settings.maxSpeedForwardTruck
    MAXSPEEDBACKWARD = Settings.maxSpeedBackwardTruck
    SPEEDUP = Settings.speedUpTruck
    MAXANGLESPEED = Settings.maxAngleSpeedTruck

    MAXSPEEDFORWARDHELI = Settings.maxSpeedForwardHeli
    MAXSPEEDBACKWARDHELI = Settings.maxSpeedBackwardHeli
    SPEEDUPHELI = Settings.speedUpHeli
    MAXANGLESPEEDHELI = Settings.maxAngleSpeedHeli

    # Steuerung für
    # 1 - Tastatur
    # 2 - Maus
    # 3 - Joystick
    # 4 - Folgen

    def __init__(self,cotrollType):
        self.cotrollType = cotrollType

    def drive(self, vehicle, truck=None):
        if self.cotrollType == 1:
            self.driveKeyboard(vehicle)
        elif self.cotrollType == 2:
            self.driveToPoint(vehicle)
            pass
        elif self.cotrollType == 3:
            self.dirveJoysick(vehicle)
        elif self.cotrollType == 4:
            self.followTruck(vehicle,truck)

    #######################################
    #       Steuerung      Tastatur       #
    #######################################
    def driveKeyboard(self, vehicle):
        # Überprüfe den Status aller Tasten
        keys = pygame.key.get_pressed()
        # Lenken
        if keys[pygame.K_LEFT]:
            vehicle.angleSpeed = self.MAXANGLESPEED
        elif keys[pygame.K_RIGHT]:
            vehicle.angleSpeed = -self.MAXANGLESPEED
        else:
            vehicle.angleSpeed = 0

        # Vorwärts Rückwerts fahren
        if keys[pygame.K_UP]:
            vehicle.fuelConsumption()
            vehicle.currentSpeed += self.SPEEDUP
            if vehicle.currentSpeed >= self.MAXSPEEDFORWARD:
                vehicle.currentSpeed = self.MAXSPEEDFORWARD

        elif keys[pygame.K_DOWN]:
            vehicle.fuelConsumption()
            vehicle.currentSpeed = -self.MAXSPEEDBACKWARD
        else:
            vehicle.currentSpeed = 0

        # Winkel des Autos aktualisieren
        vehicle.angle += vehicle.angleSpeed
        if vehicle.angle > 360:
            vehicle.angle = 0
        elif vehicle.angle < 0:
            vehicle.angle = 360

        self.update_vehicle_position(vehicle)

        if vehicle.currentFuelLevel > 0:
            return True
        else:
            return False

    #######################################
    #       Steuerung Maus                #
    #######################################

    def driveToPoint(self, vehicle):
        # Mouse Informationen
        mousePos = pygame.mouse.get_pos()
        mouseLeftClick = pygame.mouse.get_pressed()[0]
        mouseRightClick = pygame.mouse.get_pressed()[2]

        # Vorwärts Rückwerts fahren
        if mouseLeftClick:
            vehicle.fuelConsumption()
            vehicle.currentSpeed += self.SPEEDUP
            if vehicle.currentSpeed >= self.MAXSPEEDFORWARD:
                vehicle.currentSpeed = self.MAXSPEEDFORWARD
        elif mouseRightClick:
            vehicle.fuelConsumption()
            vehicle.currentSpeed = -self.MAXSPEEDBACKWARD
        else:
            vehicle.currentSpeed = 0

        #Winkel berechnen
        delta_x = mousePos[0] - vehicle.currentPosition[0]
        delta_y = mousePos[1] - vehicle.currentPosition[1]
        if Settings.debug:
         pygame.draw.aaline(Settings.screen, (0, 255, 0), vehicle.currentPosition, mousePos)

        vehicle.angle =  - math.degrees(math.atan2(delta_y, delta_x))

        self.update_vehicle_position(vehicle)

        if vehicle.currentFuelLevel > 0:
            return True
        else:
            return False
    #######################################
    #       Steuerung Joysick             #
    #######################################
    def dirveJoysick(self, vehicle):
        # Joystick-Events abfragen
        pygame.event.pump()

        # Vorwärts fahren
        accelerate = pygame.joystick.Joystick(0).get_axis(5)


        # Berechne den Schwellenwert basierend auf dem aktuellen Wert
        accelerate = int((accelerate + 1) * 50)
        accelerate = accelerate / 10


        driveBackward = pygame.joystick.Joystick(0).get_axis(4)

        # Berechne den Schwellenwert basierend auf dem aktuellen Wert
        driveBackward = int((driveBackward + 1) * 50)
        driveBackward = driveBackward / 10

        if (accelerate > 0) and (driveBackward == 0):

            vehicle.fuelConsumption()
            # Geschwindigkeit erhöhen basierend auf der Gaspedalstellung und dem Beschleunigungswert
            vehicle.currentSpeed += self.SPEEDUP

            pygame.joystick.Joystick(0).rumble(0.5, 0.5, 1)
            # Maximalwert für die Geschwindigkeit beachten
            if vehicle.currentSpeed > self.MAXSPEEDFORWARD:
                vehicle.currentSpeed = self.MAXSPEEDFORWARD


        elif (accelerate == 0) and (driveBackward > 0):
            vehicle.fuelConsumption()
            pygame.joystick.Joystick(0).rumble(0.5, 0.5, 1)
            vehicle.currentSpeed  = -self.MAXSPEEDBACKWARD


        else:
            pygame.joystick.Joystick(0).rumble(0.009, 0.009, 1)
            vehicle.currentSpeed = 0

        # Lenkung
        steering  = pygame.joystick.Joystick(0).get_axis(2)

        # Lenken
        if steering < 0:
            vehicle.angleSpeed = self.MAXANGLESPEED
        elif  steering > 0:
            vehicle.angleSpeed = -self.MAXANGLESPEED
        else:
            vehicle.angleSpeed = 0

        # Winkel des Autos aktualisieren
        vehicle.angle += vehicle.angleSpeed
        if vehicle.angle > 360:
            vehicle.angle = 0
        elif vehicle.angle < 0:
            vehicle.angle = 360

        self.update_vehicle_position(vehicle)

        if vehicle.currentFuelLevel > 0:
            return True
        else:
            return False


    #######################################
    #       Folgen                        #
    #######################################

    def followTruck(self,vehicle, truck):
        truckPos = truck.currentPosition

        if vehicle.currentPosition != truckPos:
            vehicle.currentSpeed += self.SPEEDUPHELI
            if vehicle.currentSpeed >= self.MAXSPEEDFORWARDHELI:
             vehicle.currentSpeed = self.MAXSPEEDFORWARDHELI
             vehicle.fuelConsumption()
        else:
            vehicle.currentSpeed = 0

        # Winkel berechnen
        delta_x = truckPos[0] - vehicle.currentPosition[0]
        delta_y = truckPos[1] - vehicle.currentPosition[1]
        if Settings.debug:
            pygame.draw.aaline(Settings.screen, (255, 0, 255), vehicle.currentPosition, truckPos)

        vehicle.angle = - math.degrees(math.atan2(delta_y, delta_x))

        if vehicle.currentPosition == truck.currentPosition:
            print("JEtz")
        else:
         self.update_vehicle_position(vehicle)



    def update_vehicle_position(self,vehicle):
        # Bewegungsvektor des Fahrzeugs berechnen
        car_dx = vehicle.currentSpeed * math.cos(math.radians(vehicle.angle))
        car_dy = vehicle.currentSpeed * math.sin(math.radians(vehicle.angle))

        # Position des Fahrzeugs aktualisieren
        vehicle.currentPosition[0] += car_dx
        vehicle.currentPosition[1] -= car_dy

        vehicle.steerVehicle()
