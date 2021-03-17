import pygame

SCREEN_RECT = pygame.Rect(0,0,480,700)

class GameSprites(pygame.sprites.Sprites):
  
  def __int__(self, image_name, speed=1):
    super().__init__()
    
    self.image = pygame.image.load(image_name)
    self.rect = self.image.get_rect()
    self.speed = speed
    
  def update(self):
