import pygame.event
import Settings
import bevorGameStart
import mainMenue
from Templates import *

def gameOverView(status):
    # status true = gewonnen
    # status false = verloren
    
    button_x = (Settings.screen.get_width() / 2 - 250)
    button_y = (Settings.screen.get_height() / 2 - 50)
    logo = pygame.image.load('src/img/ICON.png')
    logo = pygame.transform.scale(logo, (350,350))
    
    if status:
        text = "Herzlichen Glückwunsch!\nSie haben den Auftrag erfolgreich ausgeführt!"
    else:    
        text = "Sie haben den Auftrag leider nicht erfolgreich ausgeführt."
    lines = text.splitlines()

    pygame.mouse.set_system_cursor(3)
    while True:
        Settings.screen.fill((0, 0, 0))
        mouse_clickt = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0]:
                    mouse_clickt = True

        # Hole Maus Position
        mousePos = pygame.mouse.get_pos()

        # Zeichen logo
        Settings.screen.blit(logo, ((Settings.screen.get_width()/2) - 175, 0))

        frame(((Settings.screen.get_width()/2) - 400), 370, 800, 400, (217, 210, 173), (140, 133, 97), lines)

        #Text Start
        b0 = button(button_x, 800, 500, 100,  "Hauptmenü", 80, mousePos) #TODO: Pos
        b1 = button(button_x, 950, 500, 100,  "Nochmal Spielen", 80, mousePos) #<- TODO: POS
        if mouse_clickt:
            if b0.collidepoint(mousePos):
                mainMenue.mainMenue()
            if b1.collidepoint(mousePos):
                bevorGameStart.bevorGameStart()

        mouse_clickt = False
        pygame.display.flip()