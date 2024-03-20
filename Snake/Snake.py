import pyglet
from pyglet.window import key
import random
from pyglet.window import Window

# Velikost okna
WIDTH = 1920
HEIGHT = 1080

# Velikost hada
BLOCK_SIZE = 20

# Rychlost hada
SNAKE_SPEED = 0.5

# Inicializace okna
window = pyglet.window.Window(WIDTH, HEIGHT)

# Inicializace hada
snake = [(WIDTH // 2, HEIGHT // 2)]
snake_direction = key.RIGHT



#toto napsal Patrik - konfigurace food
#Inicializace jídla
food = pyglet.resource.image('food.png')
food_sprite = pyglet.sprite.Sprite(food)
food_sprite.scale = BLOCK_SIZE / max(food.width, food.height)
food_sprite.x = random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
food_sprite.y = random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
