import pygame

class Paddle:
	"""A class to define the paddle rackets"""
	def __init__(self, pong_game):
		self.settings = pong_game.settings
		
		self.screen = pong_game.screen
		
		# define paddle rect objects
		self.paddle_rect_1 = pygame.Rect(20, self.settings.middle_y,
			self.settings.thickness, self.settings.height)
		
		self.paddle_rect_2 = pygame.Rect(self.settings.right_edge, self.settings.middle_y,
			self.settings.thickness, self.settings.height)

		self.VER_ACC = 0.1
		self.FRICTION = 0.08

		# flags for movement
		self.up1_flag = False
		self.down1_flag = False
		self.up2_flag = False
		self.down2_flag = False


	def update(self):
		"""Moves paddle if flag is true"""
		
		# stops acceleration in key is not pressed
		self.settings.acc1 = 0
		self.settings.acc2 = 0
		
		if self.up1_flag:
			self.settings.acc1 = -1 * self.VER_ACC
		if self.down1_flag:
			self.settings.acc1 = self.VER_ACC
		if self.up2_flag:
			self.settings.acc2 = -1 * self.VER_ACC
		if self.down2_flag:
			self.settings.acc2 = self.VER_ACC

		# use kinematic equations
		self.settings.acc1 -= self.settings.vel1 * self.FRICTION
		self.settings.acc2 -= self.settings.vel2 * self.FRICTION
		self.settings.vel1 += self.settings.acc1
		self.settings.vel2 += self.settings.acc2
		self.paddle_rect_1.y += (self.settings.vel1 + 0.5 * self.settings.acc1) * self.settings.dt
		self.paddle_rect_2.y += (self.settings.vel2 + 0.5 * self.settings.acc2) * self.settings.dt

		# stop paddles if hitting screen boundaries
		if self.paddle_rect_1.top <= 0:
			self.paddle_rect_1.top = 0
		if self.paddle_rect_1.bottom >= self.screen.get_height():
			self.paddle_rect_1.bottom = self.screen.get_height()
		if self.paddle_rect_2.top <= 0:
			self.paddle_rect_2.top = 0
		if self.paddle_rect_2.bottom >= self.screen.get_height():
			self.paddle_rect_2.bottom = self.screen.get_height()

	def draw_paddles(self):
		"""Draw the paddles at their current locations"""
		pygame.draw.rect(self.screen, self.settings.color, self.paddle_rect_1)
		pygame.draw.rect(self.screen, self.settings.color, self.paddle_rect_2)

