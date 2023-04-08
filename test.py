import pygame

import Settings


class MapView:
    def __init__(self, map_path, window_width, window_height):
        self.map_data = pygame.image.load(map_path)  # Karten-Daten laden
        self.map_width = self.map_data.get_width()
        self.map_height = self.map_data.get_height()
        self.window_width = window_width
        self.window_height = window_height
        self.zoom = 1.0
        self.offset_x = 0
        self.offset_y = 0
        self.objekte = []  # Liste für GasStation-Objekte


        self.screen = Settings.screen


    def addObjekt(self, objekt):
        self.objekte.append(objekt)

    def draw_map(self):
        # Karte mit aktuellem Zoom-Level und Offset auf das Fenster zeichnen
        scaled_width = int(self.map_width * self.zoom)
        scaled_height = int(self.map_height * self.zoom)
        scaled_map = pygame.transform.scale(self.map_data, (scaled_width, scaled_height))
        self.screen.blit(scaled_map, (self.offset_x, self.offset_y))

    def drawObjects(self):
        # GasStation-Objekte auf der Karte zeichnen
        for objekt in self.objekte:
            gas_station_pos = [objekt.pos[0] * self.zoom + self.offset_x,
                                objekt.pos[1] * self.zoom + self.offset_y]
            gas_station_size = [objekt.size[0] * self.zoom, objekt.size[1] * self.zoom]
            gas_station_rec = pygame.Rect(gas_station_pos, gas_station_size)
            pygame.draw.rect(self.screen, (0, 0, 255), gas_station_rec, 2)

    def update(self):
        # Fenster aktualisieren
        pygame.display.flip()

    def run(self):
        # Haupt-Loop
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            # Tasten- oder Mausereignisse abfangen
            keys = pygame.key.get_pressed()
            mouse_buttons = pygame.mouse.get_pressed()
            mouse_x, mouse_y = pygame.mouse.get_pos()
            mouse_x -= self.offset_x
            mouse_y -= self.offset_y

            # Zoom-Level anpassen
            if keys[K_PLUS] or keys[K_KP_PLUS] or mouse_buttons[4]:  # Zoom in
                self.zoom += 0.1
            elif keys[K_MINUS] or keys[K_KP_MINUS] or mouse_buttons[5]:  # Zoom out
                self.zoom -= 0.1
                if self.zoom < 0.1:
                    self.zoom = 0.1

            # Kartenverschiebung (Offset) anpassen
            if keys[K_LEFT] or mouse_x < 10:  # Nach links bewegen
                self.offset_x += 10
            elif keys[K_RIGHT] or mouse_x > self.window_width - 10:  # Nach rechts bewegen
                self.offset_x -= 10
            if keys[K_UP] or mouse_y < 10:  #


