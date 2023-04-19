import pygame

import Settings

colorGreen = (0, 255, 0)

#Schwellenwert für den Gewinn
thresholdToWin = 80

class Places():
    def __init__(self, link:str, startposition:tuple, eventRec:tuple ) -> None:
        self.image = pygame.image.load(link)
        self.rec = self.image.get_rect()
        self.rec = self.rec.move(startposition)

        self.eventRec = pygame.Rect(eventRec)

    def draw(self):
        # Zeichne Bild
        Settings.screen.blit(self.image, self.rec)

        if Settings.debug:
            # Zeichne Aktionsfelder
            pygame.draw.rect(Settings.screen, (255,0,0), self.eventRec, 1)

class GasStation(Places):
    def __init__(self) -> None:
        position = (80, 750)
        eventRec = (((position[0] + 50), (position[1] + 105)),(500,100))
        image = "scr/img/places/Tankstelle.png"
        super().__init__(image, position, eventRec)

    #Prüfe ob getakt wird
    def checkRefuels(self, vehicle):
        if self.eventRec.contains(vehicle.rotated_image_rect):
            vehicle.refuel()

    def debugPrinterArry(self):
        infoGasStation = []

        text = "__GasStation__"
        text_surface = Settings.font.render(str(text), False, colorGreen)
        infoGasStation.append(text_surface)

        text = 'pos: ' + str(self.rec)
        text_surface = Settings.font.render(str(text), False, colorGreen)
        infoGasStation.append(text_surface)

        return infoGasStation

class oreMine(Places):
    def __init__(self) -> None:
        position = (0, 0)
        eventRec = (((position[0] + 170), (position[1] + 10)),(320,130))
        image = "scr/img/places/Quelle.png"
        self.percentOre = 100
        super().__init__(image, position, eventRec)

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

        text = 'pos: ' + str(self.rec)
        text_surface = Settings.font.render(str(text), False, Settings.debugInfoColor)
        infoOreMine.append(text_surface)

        text = 'percentOre: ' + str(self.percentOre)
        text_surface = Settings.font.render(str(text) , False, Settings.debugInfoColor)
        infoOreMine.append(text_surface)

        return infoOreMine

class truckDestination(Places):
    def __init__(self) -> None:
        imageLink = "scr/img/places/Ziel.png"
        image = pygame.image.load(imageLink)
        position = ((Settings.screen.get_width() - image.get_width()), (Settings.screen.get_height() - image.get_height()))
        eventRec = (((position[0] + 500), (position[1] + 200)),(320,300))


        self.percentOre = 100

        super().__init__(imageLink, position, eventRec)

        self.win = False

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

        text = 'pos: ' + str(self.rec)
        text_surface = Settings.font.render(str(text), False, Settings.debugInfoColor)
        infoTruckDestination.append(text_surface)

        text = 'percentOre: ' + str(self.percentOre)
        text_surface = Settings.font.render(str(text) , False, Settings.debugInfoColor)
        infoTruckDestination.append(text_surface)

        text = 'Win: ' + str(self.win)
        text_surface = Settings.font.render(str(text) , False, Settings.debugInfoColor)
        infoTruckDestination.append(text_surface)

        return infoTruckDestination

class helicopterBase(Places):

    def __init__(self) -> None:
        imageLink = "scr/img/places/hubschrauberlandeplatz.png"
        image = pygame.image.load(imageLink)
        position = (Settings.screen.get_width() - 400, 100)


        self.percentOre = 100

        super().__init__(imageLink, position, (0,0,0,0))
        self.eventRec = pygame.Rect(((position[0] - 150),(position[1]  - 100)), (500,500))


    def checkUnload(self, vehicle):
        if self.eventRec.contains(vehicle.rotated_image_rect):
            if vehicle.currentLoadedQuantity > 0:
                vehicle.unloadOre()
                self.percentOre += 1

    def checkIfInBase(self, vehicle):
        if self.eventRec.contains(vehicle.rotated_image_rect):
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

        text = f"pos: {self.rec}"
        text_surface = Settings.font.render(str(text), False, Settings.debugInfoColor)
        infoHelicopterBase.append(text_surface)

        text = 'percentOre: ' + str(self.percentOre)
        text_surface = Settings.font.render(str(text) , False, Settings.debugInfoColor)
        infoHelicopterBase.append(text_surface)

        text = f"In Base: {self.inBase}"
        text_surface = Settings.font.render(str(text) , False, Settings.debugInfoColor)
        infoHelicopterBase.append(text_surface)

        return infoHelicopterBase

