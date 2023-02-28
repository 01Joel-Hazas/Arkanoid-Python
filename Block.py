import pygame
import random

blocks = ["images/bricks/Breakout-001-B_01_01.png","images/bricks/Breakout-001-B_01_02.png","images/bricks/Breakout-001-B_01_03.png","images/bricks/Breakout-001-B_01_04.png","images/bricks/Breakout-001-B_01_05.png","images/bricks/Breakout-001-B_02_01.png","images/bricks/Breakout-001-B_02_02.png","images/bricks/Breakout-001-B_02_03.png","images/bricks/Breakout-001-B_02_04.png","images/bricks/Breakout-001-B_02_05.png"]
class Block:

   def __init__ (self, img=None, posx=0, posy=0):
       self.__posx = posx
       self.__posy = posy
       if img != None:
           self.__img = pygame.image.load(img)
           self.__rect = self.__img.get_rect()
       else:
           self.image = pygame.image.load(random.choice(blocks))
           self.__img = self.image
           self.__rect = self.__img.get_rect()
           self.__rect.move_ip(posx,posy)

   @property
   def rect(self):
       return self.__rect

   @rect.setter
   def rect(self, valor):
       self.__rect = valor

   @property
   def img(self):
       return self.__img

   @img.setter
   def img(self, valor):
       self.__img = valor

   @property
   def posx(self):
       return self.__posx

   @img.setter
   def posx(self, valor):
       self.__posx = valor

   @property
   def posy(self):
       return self.__posy

   @posy.setter
   def posy(self, valor):
    self.__posy = valor

