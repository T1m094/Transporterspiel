# Schleife Hauptprogramm
import pygame
import Vehicle

# Bildschirm Aktualisierungen einstellen
clock = pygame.time.Clock()

def spielStart():
    # Screen
    screen = pygame.display.set_mode((1028, 500))

    lkw = Vehicle.Lkw()
    lkw.rotateImg(20)
    # solange die Variable True ist, soll das Spiel laufen
    gameActiv = True

    while gameActiv:

        ###############################
        #       Steuerung LKW         #
        ###############################

        # Überprüfe den Status aller Tasten
        keys = pygame.key.get_pressed()

        # Rechts
        if keys[pygame.K_RIGHT]:
            lkw.steerCarRight()
            print("LKW fährt nah rechts")
        # Links
        if keys[pygame.K_LEFT]:
            lkw.steerCarLeft()
            print("LWK fährt nach links")
        # Oben
        if keys[pygame.K_UP]:
            print("LKW fährt hoch")
        # Unten
        if keys[pygame.K_DOWN]:
            print("LKW fährt runter")

        # Exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameActiv = False
                print("Spieler hat Quit-Button angeklickt")


        # Spielfeld löschen
        screen.fill((0,0,0))
        lkw.show(screen)
        # Spielfeld/figuren zeichnen

        # Fenster aktualisieren
        pygame.display.flip()

        # Refresh-Zeiten festlegen
        clock.tick(60)
    pygame.quit()

