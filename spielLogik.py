import pygame
import Places
import Settings
import Truck
import Helicopter
import View
import gameOverView
from Control import Control
from Settings import screen

# Bildschirm Aktualisierungen einstellen
clock = pygame.time.Clock()
pygame.font.init()
font = pygame.font.SysFont('Gabriola', 80)

def spielStart():
    # Hintergrund
    bgImage = pygame.image.load("src/img/BG.png")

    # Orte
    tankstelle = Places.GasStation()
    erzMine = Places.oreMine()
    lkwZiel = Places.truckDestination()
    helicopterBase = Places.helicopterBase()

    #Fahrzeuge
    lkw = Truck.Truck()
    heli = Helicopter.Helicopter(helicopterBase)

    # Spielstand
    win = False
    gameOver = False
    tankFull = True

    # solange die Variable True ist, soll das Spiel laufen
    gameActiv = True
    currentAngle = 0
    while gameActiv:
        # Exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameActiv = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_CARET:
                    if Settings.debugPrints:
                        Settings.debugPrints = False
                        Settings.debug = False
                    else:
                        Settings.debugPrints = True
                        Settings.debug = True

        # Zeichne Hintergrundbild
        Settings.screen.blit(bgImage, (0,0))
        # Orte
        # Tankstelle
        tankstelle.draw()
        tankstelle.checkRefuels(lkw)

        # Erz Miene
        erzMine.draw()
        erzMine.checkLoad(lkw)

        # LKW Ziel
        lkwZiel.draw()
        win = lkwZiel.checkUnload(lkw)

        # Helicopter Base
        helicopterBase.draw()

        # Fahrzeuge
        lkw.steering()
        View.drawLevelDisplay(lkw, currentAngle)
        currentAngle -= 1

        # Heli
        # Prüft ob Heli klauen kann und klaut
        heli.checkAndStealOre(lkw)
        helicopterBase.checkIfInBase(heli)
        # Wenn Heli leer oder Voll
        if ((heli.currentFuelLevel < 0) or (heli.currentLoadedQuantity == heli.maxLoadedQuantity) or (lkw.currentLoadedQuantity == 0)):
            heli.flyToBase()
        else:
            heli.followTruck(lkw)
        Places.notAllowArea(lkw)

        # Stautus und Spielstand
        if lkw.currentFuelLevel < (-10):
            gameOver = True
            gameOverView.gameOverView(False)
        if helicopterBase.percentOre >= 20:
            gameOver = True
            gameOverView.gameOverView(False)
        if lkwZiel.percentOre >= Settings.thresholdToWin:
            gameOverView.gameOverView(True)

        View.drawQuantityReached(str(lkw.currentLoadedQuantity),str(lkwZiel.percentOre), str(helicopterBase.percentOre))

        # DEBUGGER
        status = []
        text = 'difficult: ' + str(Settings.difficulty)
        text_surface = Settings.font.render(str(text), False, Settings.debugInfoColor)
        status.append(text_surface)

        text = "__Status__"
        text_surface = Settings.font.render(str(text), False, Settings.debugInfoColor)
        status.append(text_surface)

        text = 'Gewonnen: ' + str(win)
        text_surface = Settings.font.render(str(text), False, Settings.debugInfoColor)
        status.append(text_surface)

        text = 'Verloren: ' + str(gameOver)
        text_surface = Settings.font.render(str(text), False, Settings.debugInfoColor)
        status.append(text_surface)

        text = 'Tanken: ' + str(tankFull)
        text_surface = Settings.font.render(str(text), False, Settings.debugInfoColor)
        status.append(text_surface)


        if Settings.debugPrints:
            Settings.printDebugInfo(lkw.debugPrinterArry(), heli.debugPrinterArry(), erzMine.debugPrinterArry(), lkwZiel.debugPrinterArry(), helicopterBase.debugPrinterArry(), status)

        # Fenster aktualisieren
        pygame.display.flip()
        screen.fill((255, 255, 255))

        # Refresh-Zeiten festlegen
        clock.tick(60)
    pygame.quit()
