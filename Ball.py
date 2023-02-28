import pygame
class Ball:

   def __init__ (self, ball_radius, ball_speed):
       self.__rect = int(ball_radius * 2 ** 0.5)
       self.__speed = ball_speed
       self.__radius = ball_radius

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
   def radius(self):
       return self.__radius

   @radius.setter
   def radius(self, valor):
       self.__radius = valor
