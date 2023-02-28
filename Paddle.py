import pygame
class Bate:

   def __init__ (self, speed, img):
       self.__img = pygame.image.load(img)
       self.__rect = self.__img.get_rect()
       self.__speed = speed

   @property
   def rect(self):
       return self.__rect

   @rect.setter
   def rect(self, valor):
       self.__rect = valor

   @property
   def speed(self):
       return self.__speed

   @speed.setter
   def speed(self, valor):
       self.__speed = valor

   @property
   def img(self):
       return self.__img

   @img.setter
   def img(self, valor):
       self.__img = valor
