import sys
import math
import pygame
from mcpi import minecraft

size = (1024, 768)
width, height = size
fps = 1

black  = (0, 0, 0)
red    = (255, 0, 0)
orange = (255, 128, 0)
yellow = (255, 255, 0)
green  = (0, 255, 0)
cyan   = (0, 255, 255)
blue   = (0, 0, 255)
purple = (255, 0, 255)
grey   = (64, 64, 64)


def main():
    mc = minecraft.Minecraft.create()
    pygame.init()
    surf = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(0)

    while True:
        x, y, z = mc.player.getPos()
        xx = 200 + int(x)
        yy = 200 + int(z)
        surf.set_at((xx, yy), green)
        print(x, y, z, xx, yy)
        pygame.display.flip()
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                pygame.quit()
                sys.exit()


if __name__ == '__main__':
    main()
