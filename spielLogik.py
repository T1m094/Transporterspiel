# Schleife Hauptprogramm
import pygame

import Places
import Settings
import Vehicle
from Settings import screen

# Bildschirm Aktualisierungen einstellen
clock = pygame.time.Clock()


def spielStart():
    lkw = Vehicle.Truck()
    tankstelle = Places.GasStation()
    # solange die Variable True ist, soll das Spiel laufen
    gameActiv = True

    while gameActiv:
        # Exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameActiv = False
                print("Spieler hat Quit-Button angeklickt")
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_CARET:
                    if Settings.debugPrints:
                        Settings.debugPrints = False
                    else:
                        Settings.debugPrints = True

        tankstelle.draw()
        tankstelle.checkRefuels(lkw)
        lkw.driveWithMouse()
        #lkw.drive()
        Settings.printDebugInfo(lkw.debugPrinterArry())

        # Spielfeld löschen

        # Spielfeld/figuren zeichnen

        # Fenster aktualisieren
        pygame.display.flip()
        screen.fill((0, 0, 0))
        # Refresh-Zeiten festlegen
        clock.tick(60)
    pygame.quit()
