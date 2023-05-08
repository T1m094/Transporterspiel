import pygame.event
import Settings
from Templates import *
    
def credits():
    button_x = (Settings.screen.get_width() / 2 - 250)
    button_y = (Settings.screen.get_height() / 2 - 50)
    logo = pygame.image.load('src/img/ICON.png')
    logo = pygame.transform.scale(logo, (350,350))

    guidText = "CREDITS\n_______\nDieses Transporterspiel wurde im Rahmen eines \nLeistungsnachweises für das Lernfeld 08 programmiert.\n\nBilder: https://www.freepik.com/\nLogo: dall e\n\nPorjektleitung: Dr.Schäfer\nProgrammierer: T.Heinz, A. Laurenti, J. Jajszczok"
    lines = guidText.splitlines()

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
        frame(((Settings.screen.get_width()/2) - 400), 370, 800, 400, (217, 210, 173), (140, 133, 97), lines)

        #Text Start
        b1 = button(button_x, 800, 500, 100,  "Zurück", 80, mousePos)
        if mouse_clickt:
            if b1.collidepoint(mousePos):
                return

        mouse_clickt = False
        pygame.display.flip()