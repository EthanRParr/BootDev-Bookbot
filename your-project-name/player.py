import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED

PLAYER_SHOOT_COOLDOWN = 0.3

class Player(CircleShape):

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)      # Forward
        if keys[pygame.K_s]:
            self.move(-dt)     # Backward
        self.timer -= dt
        if keys[pygame.K_SPACE] and self.timer <= 0:
            self.shoot()

    def __init__(self, x, y, shots_group, updateable_group, drawable_group):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shots_group = shots_group
        self.updateable_group = updateable_group
        self.drawable_group = drawable_group
        self.timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        from main import Shot
        new_shot = Shot(self.position.x, self.position.y)
        initial_direction = pygame.Vector2(0, 1)
        shot_direction = initial_direction.rotate(self.rotation)
        new_shot.velocity = shot_direction * PLAYER_SHOOT_SPEED
        self.shots_group.add(new_shot)
        self.updateable_group.add(new_shot)
        self.drawable_group.add(new_shot)
        print("Shot created!")
        self.timer = PLAYER_SHOOT_COOLDOWN
