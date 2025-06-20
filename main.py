#pgzero
import random

cell = Actor('border', size=(50, 50))
cell1 = Actor('floor', size=(50, 50))
cell2 = Actor("crack", size=(50, 50))
cell3 = Actor("f_carck", size=(50, 50))
size_w = 8
size_h = 10
WIDTH = cell.width * size_w
HEIGHT = cell.height * size_h
mode = "menu" 
win = 0
level = 1  #nivel
score = 0
HEALTH_PRICE = 20
ATTACK_PRICE = 30


TITLE = "Wolf"
FPS = 30

menu_bg = Actor("menu", topleft=(0, 0), size = (WIDTH, HEIGHT))
start_button = Actor("star", center=(WIDTH / 2, HEIGHT / 2 + 50), size = (100, 100))
back_menu = Actor("back_menu", center =(WIDTH / 2, HEIGHT / 2 + 200), size = (75, 75))
shop = Actor("shop", center=(WIDTH / 2, HEIGHT / 2 + 100), size = (100, 100))

more_health = Actor("more_health",center =(WIDTH / 2, HEIGHT / 2), size = (75, 75))
more_attacks = Actor("more_attacks",center =(WIDTH / 2, HEIGHT / 2 + 100), size = (75, 75))


# niveles
levels = [
     [[0, 0, 0, 0, 0, 0, 0, 0, 0], 
     [0, 1, 1, 1, 1, 1, 1, 1, 0], 
     [0, 1, 1, 2, 1, 3, 1, 1, 0], 
     [0, 1, 1, 1, 2, 1, 1, 1, 0], 
     [0, 1, 3, 2, 1, 1, 3, 1, 0], 
     [0, 1, 1, 1, 1, 3, 1, 1, 0], 
     [0, 1, 1, 3, 1, 1, 2, 1, 0], 
     [0, 1, 1, 1, 1, 1, 1, 1, 0], 
     [0, 0, 0, 0, 0, 0, 0, 0, 0]],
    
    # Nivel 2
    [[0, 0, 0, 0, 0, 0, 0, 0, 0], 
     [0, 1, 2, 1, 1, 2, 1, 1, 0], 
     [0, 1, 1, 1, 1, 1, 3, 1, 0], 
     [0, 1, 3, 1, 2, 1, 1, 1, 0], 
     [0, 1, 1, 1, 1, 3, 1, 1, 0], 
     [0, 1, 2, 3, 1, 1, 1, 1, 0], 
     [0, 1, 1, 1, 2, 1, 1, 1, 0], 
     [0, 1, 1, 1, 1, 1, 1, 1, 0], 
     [0, 0, 0, 0, 0, 0, 0, 0, 0]],

    # Nivel 3
    [[0, 0, 0, 0, 0, 0, 0, 0, 0], 
     [0, 1, 1, 2, 1, 3, 1, 1, 0], 
     [0, 1, 1, 1, 1, 1, 1, 2, 0], 
     [0, 3, 1, 1, 3, 2, 1, 1, 0], 
     [0, 1, 1, 1, 1, 1, 1, 1, 0], 
     [0, 2, 1, 3, 1, 2, 3, 1, 0], 
     [0, 1, 1, 1, 1, 1, 1, 1, 0], 
     [0, 1, 1, 2, 1, 1, 1, 1, 0], 
     [0, 0, 0, 0, 0, 0, 0, 0, 0]],
    
    # Nivel 4
    [[0, 0, 0, 0, 0, 0, 0, 0, 0], 
     [0, 1, 1, 1, 1, 1, 3, 1, 0], 
     [0, 1, 1, 3, 1, 1, 1, 1, 0], 
     [0, 1, 2, 1, 1, 1, 1, 1, 0], 
     [0, 3, 1, 1, 3, 1, 1, 2, 0], 
     [0, 1, 1, 1, 1, 1, 1, 1, 0], 
     [0, 1, 3, 1, 2, 1, 3, 1, 0], 
     [0, 1, 1, 1, 1, 1, 1, 1, 0], 
     [0, 0, 0, 0, 0, 0, 0, 0, 0]],

    # Nivel 5
    [[0, 0, 0, 0, 0, 0, 0, 0, 0], 
     [0, 1, 1, 3, 1, 1, 1, 1, 0], 
     [0, 1, 1, 1, 1, 1, 1, 1, 0], 
     [0, 3, 1, 1, 1, 3, 2, 1, 0], 
     [0, 1, 1, 3, 1, 1, 1, 1, 0], 
     [0, 1, 1, 1, 1, 1, 2, 1, 0], 
     [0, 1, 2, 1, 1, 1, 1, 3, 0], 
     [0, 1, 1, 1, 1, 1, 1, 1, 0], 
     [0, 0, 0, 0, 0, 0, 0, 0, 0]]
]
my_map = levels[level - 1]

char = Actor('stand', size=(50, 50))
char.top = cell.height
char.left = cell.width
char.health = 100
char.attack = 5

def create_enemies(level):
    enemies = []
    for i in range(level + 3):
        x = random.randint(1, 7) * cell.width
        y = random.randint(1, 7) * cell.height
        enemy = Actor("enemy", topleft=(x, y), size=(50, 50))
        enemy.health = random.randint(10 + level * 2, 20 + level * 2)
        enemy.attack = random.randint(5 + level, 10 + level)
        enemy.bonus = random.randint(0, 2)
        enemies.append(enemy)
    return enemies

hearts = []
swords = []
enemies = create_enemies(level)

def map_draw():
    for i in range(len(my_map)):
        for j in range(len(my_map[0])):
            if my_map[i][j] == 0:
                cell.left = cell.width * j
                cell.top = cell.height * i
                cell.draw()
            elif my_map[i][j] == 1:
                cell1.left = cell.width * j
                cell1.top = cell.height * i
                cell1.draw()
            elif my_map[i][j] == 2:
                cell2.left = cell.width * j
                cell2.top = cell.height * i
                cell2.draw()  
            elif my_map[i][j] == 3:
                cell3.left = cell.width * j
                cell3.top = cell.height * i
                cell3.draw()

def update(dt):
    global level, my_map, enemies, mode, char
    if mode == "game":
        if not enemies:
            level += 1
            if level > 5:
                mode = "game_over"
            else:
                my_map = levels[level - 1]
                enemies = create_enemies(level)
        for i in range(len(hearts)):
            if char.colliderect(hearts[i]):
                char.health += 5
                hearts.pop(i)
                break
        for i in range(len(swords)):
            if char.colliderect(swords[i]):
                char.attack += 5
                swords.pop(i)
                break
        victory()

def victory():
    global mode, win
    if enemies == [] and char.health > 0:
        mode = "end"
        win = 1
    elif char.health <= 0:
        mode = "end"
        win = 2



def draw():
    if mode == "menu":
        menu_bg.draw()
        start_button.draw()
        screen.draw.text("Wolf", center=(WIDTH / 2, HEIGHT / 2), color="white", fontsize=40)
        screen.draw.text((("score: ")+str(score)), center=(WIDTH / 2, 20), color="white")
        shop.draw()
    elif mode == "game":
        screen.fill("#2f3542")
        map_draw()
        char.draw()
        screen.draw.text("HP:", center=(25, 475), color = 'white', fontsize = 20, size = (50,50))
        screen.draw.text(char.health, center=(75, 475), color = 'white', fontsize = 20, size = (50,50))
        screen.draw.text("AP:", center=(325, 475), color = 'white', fontsize = 20, size = (50,50))
        screen.draw.text(char.attack, center=(355, 475), color = 'white', fontsize = 20, size = (50,50))
        screen.draw.text((("score: ")+str(score)), center=(WIDTH / 2, 20), color="white")
        for i in range(len(enemies)):
            enemies[i].draw()
        for i in range(len(hearts)):
            hearts[i].draw()
        for i in range(len(swords)):
            swords[i].draw()
    elif mode == "end":
        screen.fill("#2f3542")
        if win == 1:
            screen.draw.text("¡Ganaste!", center=(WIDTH // 2, HEIGHT // 2), color="white", fontsize=46)
        else:
            screen.draw.text("¡Perdiste!", center=(WIDTH // 2, HEIGHT // 2), color="white", fontsize=46)
            back_menu.draw()
    elif mode == "shop":
        menu_bg.draw()
        back_menu.draw()
        more_health.draw()
        more_attacks.draw()
        screen.draw.text((("score: ")+str(score)), center=(WIDTH / 2, 20), color="white")
        screen.draw.text("Tienda", center=(WIDTH / 2, HEIGHT / 2 - 100), color="white", fontsize=20)
        screen.draw.text("1. Comprar Salud (+20 HP) - 20 puntos", center=(WIDTH / 2, HEIGHT / 2 - 50), color="white", fontsize=20)
        screen.draw.text("2. Comprar Ataque (+5 AP) - 30 puntos", center=(WIDTH / 2, HEIGHT / 2 + 50), color="white", fontsize=20)
        screen.draw.text("Recuerda, cada vez que mueras tu vida y ataque se reincia!", center=(WIDTH / 2, HEIGHT / 2 + 150), color="white", fontsize=12)


HEALTH_PRICE = 20
ATTACK_PRICE = 30

def on_mouse_down(button,pos):
    global mode, level, char, enemies, hearts, swords, my_map, score
    if mode == "menu" and button == mouse.LEFT:
        if start_button.collidepoint(pos):
            mode = "game"
        elif shop.collidepoint(pos):
            mode = "shop"
    elif mode == "end" and back_menu.collidepoint(pos) and button == mouse.LEFT: 
                mode = "menu"
                win = 0
                level = 1
                char.health = 100
                char.attack = 5
                enemies = create_enemies(level)
                hearts = []
                swords = []
                my_map = levels[level - 1]
                char.top = cell.height
                char.left = cell.width
    elif mode == "shop" and back_menu.collidepoint(pos) and button == mouse.LEFT:
        mode = "menu"
        win = 0
        level = 1
        enemies = create_enemies(level)
        my_map = levels[level - 1]
        char.top = cell.height
        char.left = cell.width
    elif mode == "shop" and more_health.collidepoint(pos) and button == mouse.LEFT:
        if score >= HEALTH_PRICE:
            char.health += 20
            score -= HEALTH_PRICE
    elif mode == "shop" and more_attacks.collidepoint(pos):
        if score >= ATTACK_PRICE:
            char.attack += 5
            score -= ATTACK_PRICE
        
def on_key_down(key):
    global score
    if mode == "game":
        old_x = char.x
        old_y = char.y
        if keyboard.right and char.x + cell.width < WIDTH:
            char.x += cell.width
            char.image = 'stand'
        elif keyboard.left and char.x - cell.width >= 0:
            char.x -= cell.width
            char.image = 'left'
        elif keyboard.down and char.y + cell.height < HEIGHT:
            char.y += cell.height
        elif keyboard.up and char.y - cell.height >= 0:
            char.y -= cell.height
        enemy_index = char.collidelist(enemies) 
        if enemy_index != -1:
            enemy = enemies[enemy_index]
            char.health -= enemy.attack
            enemy.health -= char.attack
            char.x = old_x
            char.y = old_y
            if enemy.health <= 0:
                score += 10
                if enemy.bonus == 1:
                    heart = Actor("heart", size=(20,20))
                    heart.pos = enemy.pos
                    hearts.append(heart)
                elif enemy.bonus == 2:
                    sword = Actor("sword", size=(20,20))
                    sword.pos = enemy.pos
                    swords.append(sword)
                enemies.pop(enemy_index)