import pygame
import random
pygame.init()

LAIUS, KÕRGUS = 800, 600
TAUSTAVÄRV = (255, 255, 255)
ALGNE_RAADIUS = 10
MAX_RINGID = 10
VÄRVI_MUUTUS = True

ekraan = pygame.display.set_mode((LAIUS, KÕRGUS))
pygame.display.set_caption("Ringide joonistamise mäng")

class Ring:
    def __init__(self, x, y, raadius, värv):
        self.x = x
        self.y = y
        self.raadius = raadius
        self.värv = värv

ringid = []
käimas = True
while käimas:
    for sündmus in pygame.event.get():
        if sündmus.type == pygame.QUIT:
            käimas = False 
        elif sündmus.type == pygame.MOUSEBUTTONDOWN:
            x, y = sündmus.pos
            if ringid and VÄRVI_MUUTUS:
                for ring in ringid:
                    ring.värv = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            uus_ring = Ring(x, y, ALGNE_RAADIUS, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            ringid.append(uus_ring)
            if len(ringid) > MAX_RINGID:
                ringid.pop(0)
            for ring in ringid:
                ring.raadius += 2
    ekraan.fill(TAUSTAVÄRV)
    for ring in ringid:
        pygame.draw.circle(ekraan, ring.värv, (ring.x, ring.y), ring.raadius)
    pygame.display.flip()
pygame.quit()
