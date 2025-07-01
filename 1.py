import pygame
import pygine as pg

# Создаем игру и спрайт
game = pg.Game(800, 600, "Тест движения")
sprite = pg.AnimatedSprite("./platformer_sprites.png", (64, 64), (400, 300))
sprite.set_scale(2.0)

# Скорость движения
speed = 5  # пикселей в секунду

# Создаем список стен
walls = []

# Добавляем несколько стен
walls.append(pg.AnimatedSprite("./platformer_sprites.png", (64, 64), (500, 300)))
walls.append(pg.AnimatedSprite("./platformer_sprites.png", (64, 64), (600, 300)))
walls.append(pg.AnimatedSprite("./platformer_sprites.png", (64, 64), (500, 400)))
walls.append(pg.AnimatedSprite("./platformer_sprites.png", (64, 64), (400, 400)))

# Добавляем стены в игру
for wall in walls:
    game.add_sprite(wall)

def collides_with_any(sprite, sprites_list):
    for s in sprites_list:
        if sprite.collides_with(s):
            return True
    return False

def update():
    dx = dy = 0
    if pg.key_pressed(pygame.K_LEFT):
        dx = -speed
        sprite.mirror(True)
    elif pg.key_pressed(pygame.K_RIGHT):
        dx = speed
        sprite.mirror(False)
    if pg.key_pressed(pygame.K_UP):
        dy = -speed
    elif pg.key_pressed(pygame.K_DOWN):
        dy = speed

    # Движение по X
    sprite.x += dx
    if collides_with_any(sprite, walls):
        sprite.x -= dx

    # Движение по Y
    sprite.y += dy
    if collides_with_any(sprite, walls):
        sprite.y -= dy

def draw():
    # Показываем хитбокс для наглядности
    sprite.debug_draw(game.screen)
    for wall in walls:
        wall.debug_draw(game.screen)

    # Координаты спрайта
    pg.Text(0, 0, f"X: {sprite.x:.1f}", size=18, color=(255, 255, 0)).draw(game.screen)
    pg.Text(0, 15, f"Y: {sprite.y:.1f}", size=18, color=(255, 255, 0)).draw(game.screen)

game.add_sprite(sprite)
game.run(update, draw)
