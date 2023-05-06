import pygame

import Settings


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

def buttonChange(bx, by, laenge, hoehe, text, text_size, mouse):
    farbe_normal = (140, 133, 97)
    farbe_aktiv = (217, 210, 173)

    font = pygame.font.SysFont('''Arial Baltic''', text_size)
    b_l = False
    b_r = False

    # leftside choice
    if ((mouse[0] > bx) and (mouse[0] < bx + 60) and (mouse[1] > by) and (mouse[1] < by + hoehe)):
        pygame.draw.rect(Settings.screen, farbe_aktiv, (bx, by, 60, hoehe))
        pygame.draw.rect(Settings.screen, farbe_normal, (bx, by, 60, hoehe), 5)
        b_l = True

    else:
        pygame.draw.rect(Settings.screen, farbe_normal, (bx, by, 60, hoehe))
        pygame.draw.rect(Settings.screen, farbe_aktiv, (bx, by, 60, hoehe), 5)

    # Rightside  choice
    if ((mouse[0] > (bx + laenge - 60)) and (mouse[0] < bx + laenge) and (mouse[1] > by) and (mouse[1] < by + hoehe)):
        pygame.draw.rect(Settings.screen, farbe_aktiv, (bx + laenge - 60, by, 60, hoehe))
        pygame.draw.rect(Settings.screen, farbe_normal, (bx + laenge - 60, by, 60, hoehe), 5)
        b_r = True

    else:
        pygame.draw.rect(Settings.screen, farbe_normal, (bx + laenge - 60, by, 60, hoehe))
        pygame.draw.rect(Settings.screen, farbe_aktiv, (bx + laenge - 60, by, 60, hoehe), 5)

    if (b_l or b_r):
        pygame.draw.rect(Settings.screen, farbe_aktiv, (bx + 65, by, laenge - 65 - 65, hoehe))
    else:
        pygame.draw.rect(Settings.screen, farbe_normal, (bx + 65, by, laenge - 65 - 65, hoehe))

    text_surface = font.render(text, True, (0, 0, 0))
    Settings.screen.blit(text_surface, ((bx + 65), (by + 10)))

    if b_l:
        return 0
    if b_r:
        return 1

def textfield(bx, by, laenge, hoehe, text, text_size):
    farbe_aktiv = (140, 133, 97)
    farbe_normal = (217, 210, 173)
    font = pygame.font.SysFont('''Arial Baltic''', text_size)

    pygame.draw.rect(Settings.screen, farbe_aktiv, (bx, by, laenge, hoehe))
    field = pygame.draw.rect(Settings.screen, farbe_normal, (bx, by, laenge, hoehe), 5)
    text_surface = font.render(text, True, (0, 0, 0))
    text_rec = text_surface.get_rect(center=(field.center))
    Settings.screen.blit(text_surface, text_rec)

def frame(bx, by, laenge, hoehe, farbe_bg, farbe_fr, lines):

    pygame.draw.rect(Settings.screen, farbe_fr, (bx, by, laenge, hoehe), 5)
    y = by + 30
    for line in lines:
        text_surface = Settings.fontGuidText.render(line, True, (255, 255, 255))  # Text rendern
        Settings.screen.blit(text_surface,  ((bx + 50), y)) # Text ins Spiel einfügen
        y += 30  # Position für die nächste Zeile erhöhen
