from ship import Ship
import sys
import pygame
from settings import Settings
class AlienInvasion:s
	"""管理游戏资源或行为的类"""
	def _init_(self):
		"""初始化游戏并创建游戏资源"""
		pygame.init()
		self.settings = Settings()
		self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
		pygame.display.set_caption("Alien Invasion")
		self.ship =Ship(self)
	def _check_keydown_events(self,event):
		if event.key == pygame.K_RIGHT:
			# 向右移动飞船
			self.ship.moving_right = True
		elif event.type == pygame.K_LEFT:
			self.ship.moving_left = True
		elif event.key == pygame.K_q:
			sys.exit()


    def _check_keyup_events(self,event):
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = False
		elif event.key == pygame.KEFT:
			self.ship.moving_left = False



	def _check_events(self):
		"""响应按键和鼠标事件"""
		for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				elif event.type == pygame.KEYDOWN:
					self._check_keydown_events(event)
				elif event.key == pygame.KEYUP:
					self._check_keyup_events(event)

	def _update_screen(self):
		"""更新屏幕上的图案，并且切换到新屏幕"""
			self.screen,fill(self.settings.bg_color)
			self.ship.blitme()

			# 让最近绘制的屏幕可见
			pygame.display.flip()

	def run_game(self):
		"""开始游戏的主循环"""
		while True:
			# 监视键盘和鼠标事件
			self._check_events()
			self.ship.update()
			self._update_screen()
		

if _name_ == '_main_':
	# 创建游戏实例并运行游戏
	ai = AlienInvasion()
	ai.run_game()
