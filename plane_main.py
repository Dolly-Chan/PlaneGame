import pygame
from plane_sprites import *


class PlaneGame(object)

def __init__(self):
  print("game is loading...")
  
  self.screen = pygame.display.set_mode(SCREEN_RECT.size)
  self.clock = pygame.time.Clock()
  self.__create_sprites()
  
def start_game(self):
  print("game starts")

  
if __name__ = '__main__':
  game = PlaneGame()
  
  game.start_game()
