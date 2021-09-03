import sys
import math
import pygame
from mcpi import minecraft
from mcpi import block

size = (256, 256)
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

    mc.postToChat('map addon loaded')
    while True:
        x, y, z = mc.player.getTilePos()
        xx = 128 + int(x)
        yy = 128 + int(z)
        surf.set_at((xx, yy), green)
        print(x, y, z)
        pygame.display.flip()
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if event.key == ord('a'):
                    mc.setBlock(x, y, z, block.STONE)
                elif event.key == ord('b'):
                    mc.setBlocks(x-1, y, z-1, x+1, y+1, z+1, block.STONE)
                elif event.key == ord('s'):
                    for i in range(0, 5):
                        mc.setBlocks(x-1, y, z+i, x+1, y+i, z+i, block.STONE)
                    mc.postToChat('stone stairs added')
                elif event.key == ord('t'):
                    mc.setBlocks(x-1, y, z-1, x+1, y+10, z+1, block.STONE)
                    mc.postToChat('stone tower added')
                else:
                    print('keypress', event.key)
            elif event.type == pygame.QUIT:
                mc.postToChat('unloading map')
                pygame.quit()
                sys.exit()


if __name__ == '__main__':
    main()
