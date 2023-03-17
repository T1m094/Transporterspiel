import pygame

class Vehicle:
    def __init__(self):
        self.basePosition = 0
        self.currentPosition = [0,0]
        self.degree = 0 # Min 0 Max 360  Oben=0 Links=90 unten=180 rechts=270
        self.speed = 0
        self.fuelLevel = 0
        self.loadedQuantity = 0

    # Erz laden
    def loadOre(self):
        pass
    # Erz entladen
    def uploadOre(self):
        pass

    # Erz laden
    def loadOre(self):
        pass

    # Tanken
    def refuel(self):
        pass
    def rotateImg(self, degree):

        self.scaled_image = pygame.transform.rotate(self.scaled_image, degree)

    def rotateImgRight(self):
        self.degree = self.degree + 0.5

        if self.degree > 360:
            self.degree = 0

        self.scaled_image = pygame.transform.rotate(self.scaled_image, self.degree)

    def rotateImgLeft(self):
        self.degree = self.degree - 0.5

        if self.degree > 0:
            self.degree = 360

        self.scaled_image = pygame.transform.rotate(self.scaled_image, self.degree)

    def blitRotate(self, surf, pos, originPos, angle):

        # offset from pivot to center
        image_rect = self.scaled_image.get_rect(topleft=(pos[0] - originPos[0], pos[1] - originPos[1]))
        offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center

        # roatated offset from pivot to center
        rotated_offset = offset_center_to_pivot.rotate(-angle)

        # roatetd image center
        rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)

        # get a rotated image
        rotated_image = pygame.transform.rotate(self.scaled_image, angle)
        rotated_image_rect = rotated_image.get_rect(center=rotated_image_center)

        # rotate and blit the image
        surf.blit(rotated_image, rotated_image_rect)

        # draw rectangle around the image
        pygame.draw.rect(surf, (255, 0, 0), (*rotated_image_rect.topleft, *rotated_image.get_size()), 2)

    # Fahren/ Sprit verbrauchen
    def drive(self):
        pass

    # Zeichen
    def show(self, screen):
        screen.blit(self.scaled_image, (0, 0))
        pass

class Lkw(Vehicle):
    # Bild laden
    image_path = "./scr/img/LKW.png"
    image = pygame.image.load(image_path)
    # Bild auf die Größe 200x200 skalieren
    scaled_image = pygame.transform.scale(image, (200, 200))
    #scaled_image = pygame.transform.rotate(scaled_image, degree)

    def __init__(self):
        super().__init__()

    def showSpeed(self):
        print(self.speed)

    def steerCarRight(self):
        self.rotateImgRight()

    def steerCarLeft(self):
        self.rotateImgLeft()

