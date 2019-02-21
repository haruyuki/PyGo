import math
import sys

import pygame


class PyGo:
	def __init__(self):
		pygame.init()
		width, height = 800, 600
		self.board_x_offset = 50
		self.board_y_offset = 30
		self.screen = pygame.display.set_mode((width, height))
		pygame.display.set_caption("PyGo")
		self.clock = pygame.time.Clock()
		self.board_rows = 19
		self.board_columns = 19
		self.board_height = [[None for _ in range(self.board_rows)] for _ in range(self.board_columns)]
		self.board_width = [[None for _ in range(self.board_rows)] for _ in range(self.board_columns)]

		# Initialise graphics
		self.black_stone = pygame.image.load('assets/black_stone.png')
		self.black_hover = pygame.image.load('assets/black_stone_hover.png')
		self.white_stone = pygame.image.load('assets/white_stone.png')
		self.white_hover = pygame.image.load('assets/white_stone_hover.png')

	def update(self):
		self.clock.tick(60)
		self.screen.fill((248, 210, 161))
		self.draw_board()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		mouse = pygame.mouse.get_pos()
		board_x_position = math.ceil((mouse[0] - self.board_x_offset - 15) / 30.0)
		board_y_position = math.ceil((mouse[1] - self.board_y_offset - 15) / 30.0)
		pygame.display.flip()

	def draw_board(self):
		for x in range(self.board_rows):
			if x == 0 or x == self.board_rows - 1:
				x *= 30
				x += self.board_x_offset
				pygame.draw.line(self.screen, (0, 0, 0), (x, self.board_y_offset), (x, 571), 3)
			else:
				x *= 30
				x += self.board_x_offset
				pygame.draw.line(self.screen, (0, 0, 0), (x, self.board_y_offset), (x, 571), 1)

		for y in range(self.board_columns):
			if y == 0 or y == self.board_columns - 1:
				y *= 30
				y += self.board_y_offset
				pygame.draw.line(self.screen, (0, 0, 0), (self.board_x_offset, y), (591, y), 3)
			else:
				y *= 30
				y += self.board_y_offset
				pygame.draw.line(self.screen, (0, 0, 0), (self.board_x_offset, y), (591, y), 1)


bg = PyGo()
while True:
	bg.update()
