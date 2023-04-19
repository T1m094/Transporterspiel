import pygame

import Settings

colorGreen = (0, 255, 0)

#Schwellenwert für den Gewinn
thresholdToWin = 80

class Places():
    def __init__(self, link:str, startposition:tuple, eventRec:tuple) -> None:
        self.image = pygame.image.load(link)
        self.rec = self.image.get_rect()
        self.rec = self.rec.move(startposition)

        self.eventRec = pygame.Rect(eventRec)

class GasStation(Places):
    def __init__(self) -> None:
        position = (80, 750)
        eventRec = (((position[0] + 50), (position[1] + 105)),(500,100))
        image = "scr/img/places/Tankstelle.png"
        super().__init__(image, position, eventRec)

    def draw(self):
        # Zeichne Tankstelle
        Settings.screen.blit(self.image, self.rec)

        if Settings.debug:
            # Zeichne Aktionsfelder
            pygame.draw.rect(Settings.screen, (255,0,0), self.eventRec, 1)



    #Prüfe ob getakt wird
    def checkRefuels(self, vehicle):
        if self.eventRec.contains(vehicle.rotated_image_rect):
            vehicle.refuel()

    def debugPrinterArry(self):
        infoGasStation = []

        text = "__GasStation__"
        text_surface = Settings.font.render(str(text), False, colorGreen)
        infoGasStation.append(text_surface)

        text = 'pos: ' + str(self.pos)
        text_surface = Settings.font.render(str(text), False, colorGreen)
        infoGasStation.append(text_surface)

        return infoGasStation

class oreMine:
    def __init__(self):
        self.pos = ((Settings.screen.get_height()/2) + 400, 50)
        self.size = (400,400)
        self.rec = pygame.Rect(self.pos, self.size)
        self.percentOre = 100

    def draw(self):
        text = "Quelle"
        text_surface = Settings.font.render(str(text), False, Settings.debugInfoColor)
        Settings.screen.blit(text_surface, (self.rec.center))
        pygame.draw.rect(Settings.screen, (255,0,0), self.rec, 2)

    # Prüfen ob LKW an der Miene ist
    # Wenn ja, dann aufladen
    def checkLoad(self, vehicle):
        if self.rec.contains(vehicle.rotated_image_rect):
            if self.percentOre > 0:
                if vehicle.currentLoadedQuantity < vehicle.maxLoadedQuantity:
                 self.percentOre -= 1
                 vehicle.loadOre()



    def debugPrinterArry(self):
        infoOreMine = []

        text = "__oreMine__"
        text_surface = Settings.font.render(str(text) , False, Settings.debugInfoColor)
        infoOreMine.append(text_surface)

        text = 'pos: ' + str(self.pos)
        text_surface = Settings.font.render(str(text), False, Settings.debugInfoColor)
        infoOreMine.append(text_surface)

        text = 'percentOre: ' + str(self.percentOre)
        text_surface = Settings.font.render(str(text) , False, Settings.debugInfoColor)
        infoOreMine.append(text_surface)

        return infoOreMine

class truckDestination:
    def __init__(self):
        self.pos = ((Settings.screen.get_height()/2 )+ 400, 550)
        self.size = (400,400)
        self.rec = pygame.Rect(self.pos, self.size)
        self.percentOre = 0

        self.win = False
    def draw(self):
        text = "Ziel"
        text_surface = Settings.font.render(str(text), False, Settings.debugInfoColor)
        Settings.screen.blit(text_surface, (self.rec.center))
        pygame.draw.rect(Settings.screen, (0,255,0), self.rec, 2)

    # Prüfen ob LKW im Ziel ist
    # Wenn ja, dann abladen
    def checkUnload(self, vehicle):
        if self.rec.contains(vehicle.rotated_image_rect):
            if vehicle.currentLoadedQuantity > 0:
                vehicle.unloadOre()
                self.percentOre += 1

            if self.percentOre >= thresholdToWin:
                return True

        return False



    # Debug info truckDestination
    def debugPrinterArry(self):
        infoTruckDestination = []

        text = "__truckDestination__"
        text_surface = Settings.font.render(str(text) , False, Settings.debugInfoColor)
        infoTruckDestination.append(text_surface)

        text = 'pos: ' + str(self.pos)
        text_surface = Settings.font.render(str(text), False, Settings.debugInfoColor)
        infoTruckDestination.append(text_surface)

        text = 'percentOre: ' + str(self.percentOre)
        text_surface = Settings.font.render(str(text) , False, Settings.debugInfoColor)
        infoTruckDestination.append(text_surface)

        text = 'Win: ' + str(self.win)
        text_surface = Settings.font.render(str(text) , False, Settings.debugInfoColor)
        infoTruckDestination.append(text_surface)

        return infoTruckDestination

class helicopterBase:
    def __init__(self):
        self.pos = ((Settings.screen.get_height()/2) + 950, 350)
        self.size = (500,500)
        self.rec = pygame.Rect(self.pos, self.size)

        self.inBase = False

        self.percentOre = 0
    def draw(self):
        text = "Hubschrauber Base"
        text_surface = Settings.font.render(str(text), False, Settings.debugInfoColor)
        Settings.screen.blit(text_surface, (self.rec.center))
        pygame.draw.rect(Settings.screen, (255,0,255), self.rec, 2)

    def checkUnload(self, vehicle):
        if self.rec.contains(vehicle.rotated_image_rect):
            if vehicle.currentLoadedQuantity > 0:
                vehicle.unloadOre()
                self.percentOre += 1

    def checkIfInBase(self, vehicle):
        if self.rec.contains(vehicle.rotated_image_rect):
            self.inBase = True
            vehicle.currentFuelLevel = vehicle.maxFuelLevel
            self.percentOre += vehicle.currentLoadedQuantity
            vehicle.currentLoadedQuantity = 0
        else:
            self.inBase = False


    # Debug info truckDestination
    def debugPrinterArry(self):
        infoHelicopterBase = []

        text = "__helicopterBase__"
        text_surface = Settings.font.render(str(text) , False, Settings.debugInfoColor)
        infoHelicopterBase.append(text_surface)

        text = f"pos: {self.pos}"
        text_surface = Settings.font.render(str(text), False, Settings.debugInfoColor)
        infoHelicopterBase.append(text_surface)

        text = 'percentOre: ' + str(self.percentOre)
        text_surface = Settings.font.render(str(text) , False, Settings.debugInfoColor)
        infoHelicopterBase.append(text_surface)

        text = f"In Base: {self.inBase}"
        text_surface = Settings.font.render(str(text) , False, Settings.debugInfoColor)
        infoHelicopterBase.append(text_surface)

        return infoHelicopterBase

