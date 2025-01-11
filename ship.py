import pygame
import os

class Ship:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Путь к изображению корабля
        self.image_path = os.path.join('resources', 'ship.bmp')

        # Загрузка и изменение размера изображения корабля
        self.image = pygame.image.load(self.image_path)
        self.image = pygame.transform.scale(self.image, (120, 100))  # Укажите желаемые размеры (ширина, высота)

        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

        # Флаги движения
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Обновляет позицию корабля в зависимости от флагов движения."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Размещает корабль в центре нижней части экрана."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
