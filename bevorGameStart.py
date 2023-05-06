import pygame.event
import Settings
from Templates import *
import mainMenue
import spielLogik


'''
Schwirigkeitsgrad
 leicht mittel schwer
Steuerung
 Tastatur|Maus|Joystick <= Wenn vorhanden
 
 Gegner 
 PC | Tastaur| Maus | Joysic
 
 zurück 
 
'''

def bevorGameStart():
    button_x = (Settings.screen.get_width() / 2 - 250)
    button_y = (Settings.screen.get_height() / 2 - 50)

    difficulty = ["Einfach", "Mittel", "Schwer"]
    difficultyCurrently = 0
    controlTruck = ["Tastatur", "Maus", "Joystick"]
    controlTruckCurrently = 0
    controlHeli= ["Tastatur", "Maus", "Joystick", "Computer"]
    controlHeliCurrently = 0


    logo = pygame.image.load('scr/img/ICON.png')
    logo = pygame.transform.scale(logo, (350,350))

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

        # Schwiergkeitsstufe
        textfield(button_x - 100, (button_y - 100), 700, 60,  "Schwiergkeitsstufe", 70)
        difficultyButton =  buttonChange(((Settings.screen.get_width()/2) - 175), button_y - 30, 350, 50, difficulty[difficultyCurrently], 60, mousePos)

        # Steuerung LKW
        textfield(button_x - 100, (button_y + 30), 700, 60, "Steuerung LKW", 70)
        controlTruckButton =  buttonChange(((Settings.screen.get_width()/2) - 175), button_y + 100, 350, 50, controlTruck[controlTruckCurrently], 60, mousePos)

        # Steuerung Heli
        textfield(button_x - 100, (button_y + 160), 700, 60, "Steuerung Heli", 70)
        controlHeliButton =  buttonChange(((Settings.screen.get_width()/2) - 175), button_y + 230, 350, 50, controlHeli[controlHeliCurrently], 60, mousePos)

        back = mainMenue.button(button_x - 100, button_y + 400, 200, 80, "Zurück", 70, mousePos)
        go = mainMenue.button(button_x + 200, button_y + 400, 400, 80, "Spiel Starten", 60, mousePos)
        if mouse_clickt:
            # Schwierigkeitsgrad
            if (difficultyButton == 0):
                difficultyCurrently -= 1
                if difficultyCurrently < 0 :
                   difficultyCurrently = 2
            if (difficultyButton == 1):
                difficultyCurrently += 1
                if difficultyCurrently > 2:
                   difficultyCurrently = 0

             # Steuerung LKW
            if (controlTruckButton == 0):
                controlTruckCurrently -= 1
                if controlTruckCurrently < 0 :
                   controlTruckCurrently = 2
            if (controlTruckButton == 1):
                controlTruckCurrently += 1
                if controlTruckCurrently > 2:
                   controlTruckCurrently = 0

            # Steuerung Heli
            if (controlHeliButton == 0):
                controlHeliCurrently -= 1
                if controlHeliCurrently < 0 :
                   controlHeliCurrently = 3
            if (controlHeliButton == 1):
                controlHeliCurrently += 1
                if controlHeliCurrently > 3:
                   controlHeliCurrently = 0
            # Start Spiel
            if go.collidepoint(mousePos):
                Settings.difficulty = difficultyCurrently
                Settings.controllerTruck = controlTruckCurrently
                Settings.controllerHeli = controlHeliCurrently


                spielLogik.spielStart()
            if back.collidepoint(mousePos):
                return

        mouse_clickt = False
        pygame.display.flip()