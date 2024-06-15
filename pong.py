import pygame
import sys
import math

from settings import Settings
from paddles import Paddle
from ball import Ball

class Pong:
	"""Class that defines the game"""
	def __init__(self):
		pygame.init()
		# initialize game settings
		self.settings = Settings()
		
		self.screen = pygame.display.set_mode((self.settings.screen_width, 
			self.settings.screen_height), 0 , 32)
		self.screen_rect = self.screen.get_rect()
		pygame.display.set_caption("Pong")

		# draw decorator line
		self.aux_rect = pygame.Rect(0, 0, self.settings.aux_width, self.settings.aux_height)
		self.aux_rect.center = self.screen_rect.center

		# initialize paddles and ball
		self.paddles = Paddle(self)
		self.ball = Ball(self)

		self.p1 = self.paddles.paddle_rect_1
		self.p2 = self.paddles.paddle_rect_2

		self.paddle1_i = 0
		self.paddle2_i = 0

		# a trigger to start the game
		self.running = False
		self.ball_run = False

	def _check_events(self):
		"""Respond to mouse and key presses"""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_a:
					self.paddles.up1_flag = True
				elif event.key == pygame.K_z:
					self.paddles.down1_flag = True
				elif event.key == pygame.K_k:
					self.paddles.up2_flag = True
				elif event.key == pygame.K_m:
					self.paddles.down2_flag = True
				
				elif event.key == pygame.K_q:
					sys.exit()
				
				elif event.key == pygame.K_SPACE:
					self.running = True
					self.ball_run = True

			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_a:
					self.paddles.up1_flag = False
				elif event.key == pygame.K_z:
					self.paddles.down1_flag = False
				elif event.key == pygame.K_k:
					self.paddles.up2_flag = False
				elif event.key == pygame.K_m:
					self.paddles.down2_flag = False

		if self.paddle1_i == 11 or self.paddle2_i == 11:
			self.running = False
			self.ball_run = False

	def _update_score(self, paddle):
		"""increment the counter to access a higher index"""
		if paddle == 1:
			self.paddle1_i += 1
		elif paddle == 2:
			self.paddle2_i += 1

	def _blit_scores(self):
		"""display the current scores for each player"""
		self.pts1 = self.settings.pts_font.render(self.settings.pts_array[self.paddle1_i], True, self.settings.color)
		self.pts2 = self.settings.pts_font.render(self.settings.pts_array[self.paddle2_i], True, self.settings.color)

		self.screen.blit(self.pts1, ((self.settings.screen_width + self.pts1.get_width()) / 2, 25))
		self.screen.blit(self.pts2, (self.settings.screen_width/2 - (3/2*self.pts2.get_width()), 25))

	def _check_collisions(self):
		"""determines course of action following a collision""" 
		if pygame.Rect.colliderect(self.ball.ball_rect, self.p1):
			# determine the angle based on a ratio of where the ball hit the left paddle
			self.d1 = self.ball.ball_rect.top - self.p1.top
			self.angle = (2*math.pi/3) * (self.d1 / self.settings.height) - (math.pi/3)

			# update the ball's movement
			self.settings.ball_vec.x = math.cos(self.angle)
			self.settings.ball_vec.y = math.sin(self.angle)

			# increase speed and play sound
			self.settings.speed += 0.01
			self.settings.paddle_hit.play()

		elif pygame.Rect.colliderect(self.ball.ball_rect, self.p2):
			# determine the angle based on a ratio of where the ball hit the right paddle
			self.d2 = self.ball.ball_rect.top - self.p2.top
			self.angle = (2 * math.pi/3) * (self.d2 / self.settings.height) - (math.pi/3)

			# update the ball's movement
			self.settings.ball_vec.x = -1 * math.cos(self.angle)
			self.settings.ball_vec.y = math.sin(self.angle)

			# increase speed
			self.settings.speed += 0.02
			self.settings.paddle_hit.play()

		elif self.ball.ball_rect.top <= 0:
			self.settings.ball_vec.y *= -1
			self.settings.wall_hit.play()

		elif self.ball.ball_rect.bottom >= self.screen.get_height():
			self.settings.ball_vec.y *= -1
			self.settings.wall_hit.play()

		elif self.ball.ball_rect.right < 0:
			self.ball_run = False
			# self.ball.reset_ball(1)
			self._update_score(1)
			self.ball.reset_ball(1)

		elif self.ball.ball_rect.left > self.screen.get_width():
			self.ball_run = False
			# self.ball.reset_ball(2)
			self._update_score(2)
			self.ball.reset_ball(2)

	def _update_screen(self):
		"""Update screen"""	
		# redraw the screen
		self.screen.fill(self.settings.bg_color)
		# draw auxiliary line
		pygame.draw.rect(self.screen, self.settings.color, self.aux_rect)
		# draw the scores
		self._blit_scores()
		# draw the paddles
		self.paddles.draw_paddles()
		# draw the ball
		self.ball.draw_ball()

	def run_game(self):
		"""Main game loop"""
		while True:
			# checks for input
			self._check_events()
				
			if self.running:
				# # checks for collision of paddle and ball or wall
				self._check_collisions()
				# moves the paddles
				self.paddles.update()
				# updates screen
				self._update_screen()

			else:
				if self.paddle1_i != 11 and self.paddle2_i != 11:
					# dispaly intro message
					# self._update_screen()
					self.screen.fill(self.settings.bg_color)
					self.screen.blit(self.settings.intro_msg, self.settings.coords)
					pygame.display.update()
				else:					
					if self.paddle1_i == 11:
						self.timer = pygame.time.get_ticks()
						while pygame.time.get_ticks() < self.timer+3000:
							self.screen.fill(self.settings.color)
							pygame.draw.rect(self.screen, self.settings.bg_color, self.p2)
							self.outro_rect = self.settings.outro2.get_rect()
							self.outro_rect.center = self.screen_rect.center
							self.screen.blit(self.settings.outro2, self.outro_rect)
							pygame.display.update()

							# reset scores, go back to intro screen
							self.paddle1_i, self.paddle2_i = 0, 0
					
					else:
						self.timer = pygame.time.get_ticks()
						while pygame.time.get_ticks() < self.timer+3000:
							self.screen.fill(self.settings.color)
							pygame.draw.rect(self.screen, self.settings.bg_color, self.p1)
							self.outro_rect = self.settings.outro1.get_rect()
							self.outro_rect.center = self.screen_rect.center
							self.screen.blit(self.settings.outro1, self.outro_rect)
							pygame.display.update()

						# reset scores, go back to intro screen
						self.paddle1_i, self.paddle2_i = 0, 0

			if self.ball_run:
				# updates the ball
				self.ball.update_ball()

			# puts changes to the screen
			pygame.display.flip()

if __name__ == '__main__':
	p = Pong()
	p.run_game()