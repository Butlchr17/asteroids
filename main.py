import pygame
from constants import *
from circleshape import *
from player import *

def main():

    pygame.init()

    game_clock = pygame.time.Clock() 
    dt = 0

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        player.draw(screen)

        pygame.display.flip()
    
        dt = game_clock.tick(60) / 1000

if __name__ == "__main__":
    main()