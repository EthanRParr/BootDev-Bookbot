# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = pygame.Vector2(0, 0)  # This is the missing line!
        print(f"Shot created at position: {x}, {y}")

    def draw(self, screen):
        print(f"Drawing shot at: {self.position}")
        pygame.draw.circle(screen, "white", self.position, SHOT_RADIUS)

    def update(self, dt):
        print(f"Shot position before update: {self.position}, velocity: {self.velocity}")
        self.position = self.position + (self.velocity * dt)
        print(f"Shot position after update: {self.position}")

def main():
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable,)
    Shot.containers = (shots, updateable, drawable)
    print("Starting Asteroids!")
    print("Screen width: 1280")
    print("Screen height: 720")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    my_player = Player(x, y, shots, updateable, drawable)
    asteroid_field = AsteroidField()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000

        updateable.update(dt)
        
        for asteroid in list(asteroids):
            for shot in list(shots):
                if shot.collides_with(asteroid):
                    shot.kill()
                    asteroid.split()

        # Check for collisions between player and asteroids
        for asteroid in asteroids:
            if my_player.collides_with(asteroid):
                print("Game over!")
                sys.exit()
        # Exit the program

        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        

if __name__ == "__main__":
    main()
