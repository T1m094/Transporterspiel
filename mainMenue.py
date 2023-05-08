import pygame.event
import Settings
import bevorGameStart
import guidView
import Credits

def button(bx, by, laenge, hoehe, text, text_size, mouse):
    farbe_normal = (140, 133, 97)
    farbe_aktiv = (217, 210, 173)
    font = pygame.font.SysFont('''Arial Baltic''', text_size)
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

def mainMenue():
    button_x = (Settings.screen.get_width() / 2 - 250)
    button_y = (Settings.screen.get_height() / 2 - 50)

    #Begin Screen
    screenNumber = 1 #<-----TEST DEFAULT 1
    logo = pygame.image.load('src/img/ICON.png')
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
        b1 = button(button_x, (button_y - 120), 500, 100,  "Start", 80, mousePos)

        #Text Instruction
        b2 = button(button_x, button_y, 500, 100, "Anleitung", 80, mousePos)

        #Text Settings
        b3 = button(button_x, (button_y + 120), 500, 100,  "Einstellungen", 80, mousePos)

        #Text INFO
        b4 = button(button_x, (button_y + 240), 250, 100, "Info", 70, mousePos)

        #Text Exit
        b0 = button((button_x + 260), (button_y + 240), 240, 100, "Exit", 80, mousePos)

        if mouse_clickt:
            if b0.collidepoint(mousePos):
                quit()
            elif b1.collidepoint(mousePos):
                bevorGameStart.bevorGameStart()
            elif b2.collidepoint(mousePos):
                guidView.guidView()
            elif b3.collidepoint(mousePos):
                pass
            elif b4.collidepoint(mousePos):
                Credits.credits()

        mouse_clickt = False
        pygame.display.flip()