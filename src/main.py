#!/usr/bin/env python3
import sys
import importlib

import pygame

def main():
    # Branch on which game module we're testing
    # Game modules have a simple interface, one fuction which takes
    # A list of event to process and the time since the last game tick.
    controller = None
    if len(sys.argv) == 1:
        print("Pass a game module dummy")
        sys.exit(1)
    else:
        controller = importlib.import_module(sys.argv[1])
        
    if controller == None:
        print("No, pass a REAL module")
        sys.exit(2)
    pygame.init()
    
    screen = pygame.display.set_mode(size=(320, 200), flags=pygame.SCALED)
    running = True
    clock = pygame.time.Clock()
    
    while running:
        dt = clock.tick(60)
        screen.fill((0, 255, 255))
        running = controller.step(pygame.event.get(), dt)
        pygame.display.flip()
    
    pygame.display.quit()
    
if __name__ == '__main__':
    main()

