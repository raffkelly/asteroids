import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    score = 0
    font = pygame.font.SysFont("Consolas", 30)

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    

    background = pygame.image.load("space.jpg").convert()


    while True:
        score_surface = font.render(f"Score: {score}", False, "white")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.blit(background, (0, 0))
        screen.blit(score_surface, (0, 0))
        for thing in updatable:
            thing.update(dt)
        for asteroid in asteroids:
            if asteroid.collision_check(player):
                final_score_surface = font.render(f"Final Score: {score}", False, "white")                
                screen.fill("black")
                screen.blit(final_score_surface, (500, 200))
                pygame.display.flip()
                while True:
                    pygame.event.pump()
                    endgame = pygame.key.get_pressed()
                    if endgame[pygame.K_ESCAPE]:
                        pygame.quit()
                        sys.exit()
            for shot in shots:
                if asteroid.collision_check(shot):
                    asteroid.split()
                    shot.kill()
                    score += 1
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()