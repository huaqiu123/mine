import pygame

class Ship:
	"""管理飞船的类"""

	def _init_(self,ai_game):
		"""初始化飞船并设置其初始位置"""
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()
		self.settings = ai_game.settings
		# 加载飞船图像并且获取其外接矩形
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()



		moving_right = False
		moving_left = False

		# 对于每搜新飞船都将其放在屏幕底部的中央

		self.rect.midbottom = self.screen_rect.midbottom

		self.x=float(self.rect.x)

	def update(self):
		"""根据标志移动调整飞船的位置"""
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += self.settings.ship_speed
		if self.moving_left and self.rect.left > 0:
			self.x -= self.settings.ship_speed
		self.rect.x = self.x
	def bitme(self):
		"""在指定位置绘制飞船"""
		self.screen.blit(self.image,self.rect)
