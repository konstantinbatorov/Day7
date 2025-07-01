import pygine as pg
import pygame
from pygine.scene import Scene, SceneManager

pygame.init()
<<<<<<< HEAD

WIDTH, HEIGHT = 512, 512
FPS = 60


game = pg.Game(WIDTH, HEIGHT, 'Sokoban', FPS)
scene_manager = SceneManager()

# speed = 5

# def update():
#     # Обрабатываем движение
#     if pg.key_pressed(pygame.K_LEFT):
#         player.x -= speed
#         player.mirror(True)  # Зеркалим влево

#     if pg.key_pressed(pygame.K_RIGHT):
#         player.x += speed
#         player.mirror(False)  # Обычное направление

#     if pg.key_pressed(pygame.K_UP):
#         player.y -= speed

#     if pg.key_pressed(pygame.K_DOWN):
#         player.y += speed



class MenuScene(Scene):
    def __init__(self):
        super().__init__("menu")
        self.title_text = "ГЛАВНОЕ МЕНЮ"
        self.instruction_text = "Нажмите ПРОБЕЛ для перехода в игру"
    
    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            scene_manager.switch_to("game")
    
    def draw(self, screen):
        # Очищаем экран
        screen.fill((100, 50, 100))
        
        # Рисуем текст
        font = pygame.font.Font(None, 24)
        title = font.render(self.title_text, True, (255, 255, 0))
        instruction = font.render(self.instruction_text, True, (255, 255, 255))
        
        # Центрируем текст
        title_rect = title.get_rect(center=(WIDTH/2, HEIGHT/2))
        instruction_rect = instruction.get_rect(center=(WIDTH/2, HEIGHT/2 + HEIGHT/4))
        
        screen.blit(title, title_rect)
        screen.blit(instruction, instruction_rect)

# Сцена 2: Игровая сцена
class GameScene(Scene):
    def __init__(self):
        super().__init__("game")
        self.player = pg.AnimatedSprite('platformer_sprites.png', (64, 64), (0, 0))
        self.player.add_animation('walk', [0, 1, 2, 3, 4, 5, 6, 7, 8], 5, loop=True)
        self.player.add_animation('push', [4, 5, 6], 5, loop=True)
        self.player.play_animation('walk')
        self.instruction_text = "Нажмите ESC для возврата в меню"
    
    def update(self, dt):
        # Движение игрока за мышью
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.player.x = mouse_x
        self.player.y = mouse_y
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            scene_manager.switch_to("menu")
    
    def draw(self, screen):
        # Очищаем экран
        # screen.fill((50, 100, 50))
        
        # Рисуем игрока
        # screen.blit(self.player.image, self.player.rect)
        
        
        # Рисуем инструкцию
        font = pygame.font.Font(None, 24)
        instruction = font.render(self.instruction_text, True, (255, 255, 255))
        screen.blit(instruction, (0, 0))

# Создаем сцены
menu_scene = MenuScene()
game_scene = GameScene()

# Добавляем сцены в менеджер
scene_manager.add_scene(menu_scene)
scene_manager.add_scene(game_scene)

# Начинаем с главного меню
scene_manager.switch_to("menu")

def update():
    """Обновление игры"""
    dt = game.get_delta_time()
    scene_manager.update(dt)
    game.add_sprite(game_scene.player)


def draw():
    """Отрисовка игры"""
    scene_manager.draw(game.screen)
    

game.run(update, draw)
=======
>>>>>>> 9b8da78970a8d779a2df6a84e8751b525dbbcd9e
