import pygame
import math
import random

class Settings():
	"""Stores settings for Pong"""
	
	# initialize game settings
	def __init__(self):
		self.screen_width = 1280
		self.screen_height = 720
		self.bg_color = (255, 255, 255)
		
		# a clock function to keep the framerate manageable
		self.clock = pygame.time.Clock()
		self.dt = self.clock.tick(60)

		# sounds
		self.wall_hit = pygame.mixer.Sound("wall_hit.mp3")
		self.paddle_hit = pygame.mixer.Sound("paddle_hit.mp3")

		# decorator rectangle settings
		self.aux_width = 2
		self.aux_height = self.screen_height - 20

		# Paddle settings
		self.thickness = 17
		self.height = 100
		self.color = (0, 0, 0)
		self.middle_y = ((self.screen_height / 2) - (self.height / 2))
		self.right_edge = ((self.screen_width - self.thickness - 20))
		self.acc1 = 0
		self.vel1 = 0
		self.acc2 = 0
		self.vel2 = 0

		# Ball settings
		self.ball_width = 10
		self.ball_height = 10
		self.ball_color = (0, 0, 0)
		self.speed = 0.15
		self.rando = random.uniform(2 * math.pi / 3, 4 * math.pi / 3)
		self.ball_vec = pygame.math.Vector2(0, 0)
		self.x = math.cos(self.rando)
		self.x = round(self.x, 1)
		self.y = math.sin(self.rando)
		self.y = round(self.y, 1)
		self.ball_vec.x = self.x
		self.ball_vec.y = self.y
		

		# Text settings
		self.font = pygame.font.Font("pixeloid.ttf", 30)
		self.intro_msg = self.font.render("The first to 11 points wins! Press the space bar to start...",
			True, self.color)
		self.coords = ((self.screen_width - self.intro_msg.get_width()) / 2, (self.screen_height - self.intro_msg.get_height()) / 2 - 50)

		self.outro1 = self.font.render("Congratulations, Player 1!", True, self.bg_color)
		self.outro2 = self.font.render("Congratulations, Player 2!", True, self.bg_color)
		
		# Score settings
		self.pts_array = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11']
		self.pts_font = pygame.font.Font("pixeloid.ttf", 60)
		self.pts1_coords = (self.screen_width / 2)
