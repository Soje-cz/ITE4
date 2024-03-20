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


#Richie
#Skóre
score = 0

#Proměnná pro kontrolu stavu hry
game_over = False

#Tlačítko restart
restart_button = pyglet.text.Label('RESTART', x=WIDTH // 2, y=HEIGHT // 2, anchor_x='center', anchor_y='center'
font_size=24, color=(255, 255, 255, 255))
=======
#vykresleni hada a jidla

@window.event
def on_draw():
    window.clear()
    # Vykreslení hada
    for x, y in snake:
        pyglet.shapes.Rectangle(x, y, BLOCK_SIZE, BLOCK_SIZE, color=(0, 255, 0)).draw()
    # Vykreslení jídla
    food_sprite.draw()
    # Vykreslení skóre
    label = pyglet.text.Label(f"Skóre: {score}", font_size=12, x=10, y=HEIGHT - 20)
    label.draw()

    # Pokud je hra ukončena, zobraz tlačítko restart
    if game_over:
        restart_button.draw()

