import pygame
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():

    pygame.init()

    game_clock = pygame.time.Clock() 
    dt = 0

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        updatable.update(dt)

        for asteroid in asteroids:

            if(player.collision_check(asteroid)):
                print("Game over!")
                pygame.time.delay(1000)
                pygame.quit()
                return
            
            for shot in shots:
                if (shot.collision_check(asteroid)):
                    shot.kill()
                    asteroid.split(dt)

        for item in drawable: 
            item.draw(screen)

        pygame.display.flip()
    
        dt = game_clock.tick(60) / 1000

if __name__ == "__main__":
    main()