import pygame.event

import Settings
import guidView
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
def textfield(bx, by, laenge, hoehe, text, text_size):
    farbe_aktiv = (140, 133, 97)
    farbe_normal = (217, 210, 173)
    font = pygame.font.SysFont('''Arial Baltic''', text_size)

    pygame.draw.rect(Settings.screen, farbe_aktiv, (bx, by, laenge, hoehe))
    field = pygame.draw.rect(Settings.screen, farbe_normal, (bx, by, laenge, hoehe), 5)
    text_surface = font.render(text, True, (0, 0, 0))
    text_rec = text_surface.get_rect(center=(field.center))
    Settings.screen.blit(text_surface, text_rec)

def button(bx, by, laenge, hoehe, text, text_size, mouse, what):
    # what 1 ist normaler Button
    #      2 ist ausgegraut
    #      3 ist Text
    font = pygame.font.SysFont('''Arial Baltic''', text_size)

    if what == 1 or 2:
        if what == 1:
            farbe_normal = (140, 133, 97)
            farbe_aktiv = (217, 210, 173)
        else:
            farbe_normal = (190, 190, 190)
            farbe_aktiv = (105, 105, 105)


        if (mouse[0] > bx and mouse[0] < bx + laenge and mouse[1] > by and mouse[1] < by + hoehe):
            button = pygame.draw.rect(Settings.screen, farbe_aktiv, (bx, by, laenge, hoehe))
            border = pygame.draw.rect(Settings.screen, farbe_normal, (bx, by, laenge, hoehe), 5)
            text_surface = font.render(text, True, (0, 0, 0))
            text_rec = text_surface.get_rect(center=(button.center))

        else:
            button = pygame.draw.rect(Settings.screen, farbe_normal, (bx, by, laenge, hoehe))
            border = pygame.draw.rect(Settings.screen, farbe_aktiv, (bx, by, laenge, hoehe), 5)
            text_surface = font.render(text, True, (farbe_aktiv))
            text_rec = text_surface.get_rect(center=(button.center))

        Settings.screen.blit(text_surface, text_rec)
        return button
def bevorGameStart():
    button_x = (Settings.screen.get_width() / 2 - 250)
    button_y = (Settings.screen.get_height() / 2 - 50)


    #Begin Screen
    screenNumber = 1 #<-----TEST DEFAULT 1

    logo = pygame.image.load('scr/img/ICON.png')
    logo = pygame.transform.scale(logo, (350,350))



    '''
    #Text Start
    b1 = button(button_x, (button_y - 120), 500, 100, (0, 155, 155), (0, 255, 255), language.tr().M1(1), 80)
    #Text Instruction
    b2 = button(button_x, button_y, 500, 100, (0, 155, 155), (0, 255, 255), language.tr().M1(2), 80)
    #Text Settings
    b3 = button(button_x, (button_y + 120), 500, 100, (0, 155, 155), (0, 255, 255), language.tr().M1(3), 80)
    #Text INFO
    b4 = button(button_x, (button_y + 240), 250, 100, (0, 155, 155), (0, 255, 255), language.tr().M0(6), 70)
    #Text Exit
    b0 = button((button_x + 260), (button_y + 240), 240, 100, (0, 155, 155), (0, 255, 255), language.tr().M1(0), 80)

    '''
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

        #Text Start
        textfield(button_x - 100, (button_y - 100), 700, 60,  "Schwirgkeitsstufe", 70)
        #Text Instruction
        b2 = button(button_x - 100, button_y - 30, 200, 50, "Einfach", 60, mousePos,1)
        b2 = button(button_x + 150, button_y - 30, 200, 50, "Mittel", 60, mousePos,1)
        b2 = button(button_x + 400, button_y - 30, 200, 50, "Schwer", 60, mousePos,1)

        textfield(button_x - 100, (button_y + 30), 700, 60,  "Steuerung LKW", 70)
        b2 = button(button_x - 100, button_y + 100, 200, 50, "Tastatur", 60, mousePos,1)
        b2 = button(button_x + 150, button_y + 100, 200, 50, "Maus", 60, mousePos,1)
        b2 = button(button_x + 400, button_y + 100, 200, 50, "Joystick", 60, mousePos,2)

        textfield(button_x - 100, (button_y + 160), 700, 60, "Steuerung Heli", 70)


        b2 = button(button_x - 100, button_y + 230, 200, 50, "Tastatur", 60, mousePos,1)
        b2 = button(button_x + 150, button_y + 230, 200, 50, "Maus", 60, mousePos,1)
        b2 = button(button_x + 400, button_y + 230, 200, 50, "Joystick", 60, mousePos,1)

        b2 = button(button_x + 150, button_y + 290, 200, 50, "Computer", 50, mousePos,1)

        back = button(button_x - 100, button_y + 400, 200, 80, "Zurück", 70, mousePos,1)
        go = button(button_x + 200, button_y + 400, 400, 80, "Spiel Starten", 60, mousePos,1)
        if mouse_clickt:
            if back.collidepoint(mousePos):
                return
            elif go.collidepoint(mousePos):
                spielLogik.spielStart()
            elif b2.collidepoint(mousePos):
                return
            elif b3.collidepoint(mousePos):
                return
            elif b4.collidepoint(mousePos):
                return

        mouse_clickt = False
        pygame.display.flip()