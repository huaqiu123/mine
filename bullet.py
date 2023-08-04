import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""管理飞船所发射子弹的类"""

	def _init_(self,ai_game):
		"""在飞船当前位置创建一个子弹对象"""
		super()._init_()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.color = self.settings.bullet_color

		#在（0，0）处创建一个表示子弹的矩形在设置正确位置
		self.rect = pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height)
		self.rect.midtop = ai_game.ship.rect.midtop

		#self.y=float(self.rect.y)