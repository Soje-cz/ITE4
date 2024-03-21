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

<<<<<<< HEAD

#Richie
#Skóre
score = 0

#Proměnná pro kontrolu stavu hry
game_over = False

#Tlačítko restart
restart_button = pyglet.text.Label('RESTART', x=WIDTH // 2, y=HEIGHT // 2, anchor_x='center', anchor_y='center'
font_size=24, color=(255, 255, 255, 255))
=======
=======
>>>>>>> 2919beb2591228744580429c32b8eab1dcdb5515
#vykresleni hada a jidla

#Marek Buchta
def restart_game():
    global snake, snake_direction, score, game_over
    snake = [(WIDTH // 2, HEIGHT // 2)]
    snake_direction = key.RIGHT
    food_sprite.x = random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
    food_sprite.y = random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
    score = 0
    game_over = False

#Michal Kubala
def check_collision():
    # Kolize s okrajem
    x, y = snake[0]
    if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
        return True

    # Kolize s tělem hada
    if snake[0] in snake[1:]:
        return True

    return False

#Zbyňa
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

#Miťko Daniel
def update(dt):
    global snake_direction, score, game_over

    if not game_over:
        # Pohyb hada
        x, y = snake[0]
        if snake_direction == key.LEFT:
            x -= BLOCK_SIZE
        elif snake_direction == key.RIGHT:
            x += BLOCK_SIZE
        elif snake_direction == key.UP:
            y += BLOCK_SIZE
        elif snake_direction == key.DOWN:
            y -= BLOCK_SIZE

#Aktualizace pozice hada - Buchta
    snake.insert(0, (x, y))

    # Kolize s jídlem
    if (x, y) == (food_sprite.x, food_sprite.y):
        # Vygenerování nového jídla
        food_sprite.x = random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        food_sprite.y = random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        score += 1
    else:
        # Odebrání posledního bloku hada
        snake.pop()

    # Kontrola kolize
    if check_collision():
        game_over = True
