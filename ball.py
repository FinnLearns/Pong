import pygame
import math
import random

class Ball:
	def __init__(self, pong_game):
		self.settings = pong_game.settings

		self.screen = pong_game.screen
		self.screen_rect = pong_game.screen.get_rect()

		# define ball rect object and its position variables
		self.ball_rect = pygame.Rect(0, 0, self.settings.ball_width, self.settings.ball_height)
		self.ball_rect.center = self.screen_rect.center


	def update_ball(self):
		# update ball rect position
		self.ball_rect.x += self.settings.ball_vec.x * self.settings.speed * self.settings.dt
		self.ball_rect.y += self.settings.ball_vec.y * self.settings.speed * self.settings.dt

	def draw_ball(self):
		"""Draw the ball to its current location"""
		pygame.draw.rect(self.screen, self.settings.ball_color, self.ball_rect)

	def reset_ball(self, edge):
		"""When ball hits edge, reset to middle of screen and shoot towards player who lost"""
		self.ball_rect.x = (self.screen.get_width() - self.settings.ball_width) / 2
		self.ball_rect.y = random.randint(10, self.screen.get_height() - 10)
		self.settings.speed = 0.15
		self.settings.ball_vec.x = 0
		self.settings.ball_vec.y = 0
		
		if edge == 1:
			self.rando = random.uniform(3*math.pi/4, 5*math.pi/4)
			self.x = math.cos(self.rando)
			self.x = round(self.x, 1)
			self.y = math.sin(self.rando)
			self.y = round(self.y, 1)
			self.settings.ball_vec.x = self.x
			self.settings.ball_vec.y = self.y

		elif edge == 2:
			self.rando = random.uniform(math.pi/4, -1*math.pi/4)
			self.x = math.cos(self.rando)
			self.x = round(self.x, 1)
			self.y = math.sin(self.rando)
			self.y = round(self.y, 1)
			self.settings.ball_vec.x = self.x
			self.settings.ball_vec.y = self.y

