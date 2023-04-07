import pygame

import Settings


class MapView:
    def __init__(self, karte, scroll_schritt=10):
        self.karte = karte
        self.kartenansicht = Settings.screen
        self.zoomfaktor = 0.2
        self.scroll_schritt = scroll_schritt
        self.kartenansicht_x = 1500
        self.kartenansicht_y = 850
        self.objects = []

    def addObjekt(self, objekt):
        self.objects.append(objekt)

    def draw_object(self, objekt):
        # Objekt (LKW oder Tankstelle) auf Kartenansicht zeichnen
        # Hier können Sie die Position des Objekts basierend auf der Position der Kartenansicht und dem Zoomfaktor festlegen
        image = objekt.image
        obj_pos = [objekt.currentPosition[0] * self.zoomfaktor + self.kartenansicht_x,
                   objekt.currentPosition[1] * self.zoomfaktor + self.kartenansicht_y]
        self.kartenansicht.blit(pygame.transform.scale(image,
                            (int(image.get_width() * self.zoomfaktor), int(image.get_height() * self.zoomfaktor))),
                            obj_pos)

    def draw_object_v(self, objekt):


        # Lenkung
        # offset from pivot to center
        image_rect = objekt.image.get_rect(topleft=(objekt.currentPosition[0] - objekt.imageCenterPoint[0], objekt.currentPosition[1] - objekt.imageCenterPoint[1]))
        offset_center_to_pivot = pygame.math.Vector2(objekt.currentPosition) - image_rect.center

        # Drehpunkt Mitte
        rotated_offset = offset_center_to_pivot.rotate(-objekt.angle)

        # roatetd image center
        rotated_image_center = (objekt.currentPosition[0] - rotated_offset.x, objekt.currentPosition[1] - rotated_offset.y)

        # gedrehtes Bild erhalten
        rotated_image = pygame.transform.rotate(objekt.image, objekt.angle)

        # Pos
        rotated_image_rect = rotated_image.get_rect(center=rotated_image_center)
        rotated_image_rect = [rotated_image_rect[0] * self.zoomfaktor + self.kartenansicht_x, rotated_image_rect[1] * self.zoomfaktor + self.kartenansicht_y]

        # Zeichen und updaten
        #Bild
        image = pygame.transform.scale(rotated_image,
                            (int(rotated_image.get_width() * self.zoomfaktor), int(rotated_image.get_height() * self.zoomfaktor)))

        self.kartenansicht.blit(image, rotated_image_rect)


    def draw_objects(self):
        # Objekte auf der Kartenansicht zeichnen
        for objekt in self.objects:
            self.draw_object(objekt)

    def update(self, screen):
        scaled_karte = pygame.transform.scale(self.karte,
                            (int(self.karte.get_width() * self.zoomfaktor), int(self.karte.get_height() * self.zoomfaktor)))
        screen.blit(scaled_karte, (self.kartenansicht_x, self.kartenansicht_y))


    def handle_input_events(self):
        pygame.event.pump()
        # Beispielhafte Verarbeitung von Tastenereignissen
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.kartenansicht_y -= self.scroll_schritt  # Nach oben scrollen
                elif event.key == pygame.K_s:
                    self.kartenansicht_y += self.scroll_schritt  # Nach unten scrollen
                elif event.key == pygame.K_a:
                    self.kartenansicht_x -= self.scroll_schritt  # Nach links scrollen
                elif event.key == pygame.K_d:
                    self.kartenansicht_x += self.scroll_schritt  # Nach rechts scrollen
                elif event.key == pygame.K_PLUS or event.key == pygame.K_KP_PLUS:
                    self.update_zoom(self.zoomfaktor + 0.1)
                elif event.key == pygame.K_MINUS or event.key == pygame.K_KP_MINUS:
                    self.update_zoom(self.zoomfaktor - 0.1)



    def update_zoom(self, zoomfaktor):
        if zoomfaktor >= 0.1 and zoomfaktor <= 2.0:
            self.zoomfaktor = zoomfaktor

