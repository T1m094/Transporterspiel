import math
import pygame
import Settings
import main

class Control:
    MAXSPEEDFORWARD = Settings.maxSpeedForwardTruck[Settings.difficulty]
    MAXSPEEDBACKWARD = Settings.maxSpeedBackwardTruck[Settings.difficulty]
    SPEEDUP = Settings.speedUpTruck[Settings.difficulty]
    MAXANGLESPEED = Settings.maxAngleSpeedTruck[Settings.difficulty]

    MAXSPEEDFORWARDHELI = Settings.maxSpeedForwardHeli[Settings.difficulty]
    MAXSPEEDBACKWARDHELI = Settings.maxSpeedBackwardHeli[Settings.difficulty]
    SPEEDUPHELI = Settings.speedUpHeli[Settings.difficulty]
    MAXANGLESPEEDHELI = Settings.maxAngleSpeedHeli[Settings.difficulty]

    # Steuerung für
    # 0 - Tastatur
    # 1 - Maus
    # 2 - Joystick
    # 3 - Folgen

    def __init__(self,cotrollType):
        self.cotrollType = cotrollType

    def drive(self, vehicle, truck=None):
        if self.cotrollType == 0:

            self.driveKeyboard(vehicle)
        elif self.cotrollType == 1:
            self.driveToPoint(vehicle)
        elif self.cotrollType == 2:
            self.dirveJoysick(vehicle)
        elif self.cotrollType == 3:
            print("Test")
            self.followTruck(vehicle,truck)

    #######################################
    #       Steuerung      Tastatur       #
    #######################################
    def driveKeyboard(self, vehicle):
        # Überprüfe den Status aller Tasten
        keys = pygame.key.get_pressed()
        if vehicle.currentSpeed != 0:
            # Lenken
            if keys[pygame.K_LEFT]:
                vehicle.angleSpeed = self.MAXANGLESPEED
            elif keys[pygame.K_RIGHT]:
                vehicle.angleSpeed = -self.MAXANGLESPEED
            else:
                vehicle.angleSpeed = 0

            # Winkel des Autos aktualisieren
            vehicle.angle += vehicle.angleSpeed
            if vehicle.angle > 360:
                vehicle.angle = 0
            elif vehicle.angle < 0:
                vehicle.angle = 360

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
        if vehicle.currentSpeed != 0:
            #Winkel berechnen
            delta_x = mousePos[0] - vehicle.currentPosition[0]
            delta_y = mousePos[1] - vehicle.currentPosition[1]
            vehicle.angle =  - math.degrees(math.atan2(delta_y, delta_x))

        if Settings.debug:
            pygame.draw.aaline(Settings.screen, (0, 255, 0), vehicle.currentPosition, mousePos)

        self.update_vehicle_position(vehicle)

        if vehicle.currentFuelLevel > 0:
            return True
        else:
            return False
    #######################################
    #       Steuerung Joysick             #
    #######################################
    def dirveJoysick(self, vehicle):
        pygame.joystick.Joystick(0).rumble(0.5, 0.5, 11)

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

            pygame.joystick.Joystick(0).rumble(0.2, 0.2, 15)
            # Maximalwert für die Geschwindigkeit beachten
            if vehicle.currentSpeed > self.MAXSPEEDFORWARD:
                vehicle.currentSpeed = self.MAXSPEEDFORWARD

        elif (accelerate == 0) and (driveBackward > 0):
            vehicle.fuelConsumption()
            pygame.joystick.Joystick(0).rumble(0.2, 0.2, 12)
            vehicle.currentSpeed  = -self.MAXSPEEDBACKWARD
        else:
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

    def followTruck(self,heli, truck):
        truckPos = truck.currentPosition
        if truck.rotated_image_rect.colliderect(heli.rotated_image_rect):
            heli.currentPosition[0] = truck.currentPosition[0]
            heli.currentPosition[1] = truck.currentPosition[1]
            heli.angle = truck.angle
            heli.steerVehicle()
        else:
            if heli.currentPosition == truckPos:
                heli.currentSpeed = 0
                heli.angle = truck.angle
                heli.currentPosition

            elif heli.currentPosition != truckPos:
                heli.currentSpeed += self.SPEEDUPHELI
                if heli.currentSpeed >= self.MAXSPEEDFORWARDHELI:
                 heli.currentSpeed = self.MAXSPEEDFORWARDHELI
                 heli.fuelConsumption()

            # Winkel berechnen
            delta_x = truckPos[0] - heli.currentPosition[0]
            delta_y = truckPos[1] - heli.currentPosition[1]
            if Settings.debug:
                pygame.draw.aaline(Settings.screen, (255, 0, 255), heli.currentPosition, truckPos)
            heli.angle = - math.degrees(math.atan2(delta_y, delta_x))
            self.update_vehicle_position(heli)
            
        # Bewegungsvektor des Fahrzeugs berechnen
    def update_vehicle_position(self,vehicle):
        car_dx = vehicle.currentSpeed * math.cos(math.radians(vehicle.angle))
        car_dy = vehicle.currentSpeed * math.sin(math.radians(vehicle.angle))

        # Position des Fahrzeugs aktualisieren
        vehicle.currentPosition[0] += car_dx
        vehicle.currentPosition[1] -= car_dy
        vehicle.steerVehicle()
