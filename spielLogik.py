# Schleife Hauptprogramm
import pygame
import Vehicle
from Settings import screen

# Bildschirm Aktualisierungen einstellen
clock = pygame.time.Clock()

def spielStart():
    lkw = Vehicle.Lkw()
    # solange die Variable True ist, soll das Spiel laufen
    gameActiv = True

    while gameActiv:

        #######################################
        #       Steuerung LKW  Tastatur       #
        ######################################

        # Überprüfe den Status aller Tasten
        keys = pygame.key.get_pressed()


        # Exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameActiv = False
                print("Spieler hat Quit-Button angeklickt")

        lkw.drive(keys)
        # Spielfeld löschen

        # Spielfeld/figuren zeichnen

        # Fenster aktualisieren
        pygame.display.flip()
        screen.fill((0,0,0))
        # Refresh-Zeiten festlegen
        clock.tick(60)
    pygame.quit()

