# Schleife Hauptprogramm
import pygame

import Places
import Settings
import Truck
import Helicopter
import View
from Control import Control
from Settings import screen

# Bildschirm Aktualisierungen einstellen
clock = pygame.time.Clock()



def spielStart():

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

        # LKW
        tankFull = lkw.steering()


        View.drawLevelDisplay(lkw, currentAngle)
        currentAngle -= 1


        # Heli

        # Prüft ob Heli klauen kann und klaut
        heli.checkAndStealOre(lkw)
        helicopterBase.checkIfInBase(heli)
        # Wenn Heli leer oder Voll
        if ((heli.currentFuelLevel < 0) or (heli.currentLoadedQuantity == heli.maxLoadedQuantity)):
            heli.flyToBase()
        else:
            heli.followTruck(lkw)


        # Stautus und Spielstand
        if not tankFull:
            gameOver = True
        if helicopterBase.percentOre >= 20:
            gameOver = True


        # DEBUGGER
        status = []
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
