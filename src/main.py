#!/usr/bin/env python3
import sys
import importlib

import pygame

from util.scene import SceneStack

def main():
    initial_scene = None
    # Branch on which game module we're testing
    # Game modules have a simple interface, one fuction which takes
    # A list of event to process and the time since the last game tick.
    if len(sys.argv) == 1:
        print("Pass a game module dummy")
        sys.exit(1)
    else:
        initial_scene = importlib.import_module(sys.argv[1])
        
    if initial_scene == None:
        print("No, pass a REAL module")
        sys.exit(2)
    pygame.init()
    
    screen = pygame.display.set_mode(size=(320, 200), flags=pygame.SCALED)
    running = True
    clock = pygame.time.Clock()
    game = SceneStack()
    game.push(initial_scene.Scene(screen, game))
    
    while game.running():
        dt = clock.tick(60)
        screen.fill((0, 255, 255))
        events = pygame.event.get()
        maybe_quit = [event for event in events if event.type == pygame.QUIT]
        if len(maybe_quit) != 0:
            break
        running = game.current().update(events, dt)
        pygame.display.flip()
    
    pygame.display.quit()
    pygame.quit()
if __name__ == '__main__':
    main()

