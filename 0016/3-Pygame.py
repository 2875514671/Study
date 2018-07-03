# -*- coding: utf-8 -*-
# !/usr/bin/env python

import pygame
import sys
import math

pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([255, 255, 255])
for x in range(0, 640):
	y = int(math.sin(x/640.0 * 4 * math.pi) * 200 + 240)
	# screen.set_at([x, y], [0, 0, 0])
	pygame.draw.rect(screen, [0, 0, 0], [x, y, 1, 1], 1)
pygame.display.flip()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()