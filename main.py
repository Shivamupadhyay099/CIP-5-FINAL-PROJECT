import pygame
import random

pygame.init()

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
green = (0, 200, 0)

# Screen size
screen_width = 900
screen_height = 400
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# Title
pygame.display.set_caption("Shivam's Snake Simulator")
font = pygame.font.SysFont(None, 35)

# Clock
clock = pygame.time.Clock()
fps = 30

# Function to show score
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])

# Function to plot snake
def plot_snake(gameWindow, color, snake_list, snake_size):
    for x, y in snake_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

# Game loop
def game_loop():
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    snake_size = 15
    velocity_x = 0
    velocity_y = 0
    init_velocity = 5
    score = 0

    snake_list = []
    snake_length = 1

    food_x = random.randint(20, screen_width - 20)
    food_y = random.randint(20, screen_height - 20)

    while not exit_game:
        if game_over:
            gameWindow.fill(white)
            text_screen("Game Over! Press R to Restart or Q to Quit", red, 200, 180)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        game_loop()
                    elif event.key == pygame.K_q:
                        exit_game = True
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0
                    elif event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0
                    elif event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0
                    elif event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0

            snake_x += velocity_x
            snake_y += velocity_y

            # Wall Collision
            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                game_over = True

            # Eat food
            if abs(snake_x - food_x) < 10 and abs(snake_y - food_y) < 10:
                score += 10
                food_x = random.randint(20, screen_width - 20)
                food_y = random.randint(20, screen_height - 20)
                snake_length += 5

            gameWindow.fill(white)
            text_screen("Score: " + str(score), green, 5, 5)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])

            head = [snake_x, snake_y]
            snake_list.append(head)

            if len(snake_list) > snake_length:
                del snake_list[0]

            # Self Collision
            if head in snake_list[:-1]:
                game_over = True

            plot_snake(gameWindow, black, snake_list, snake_size)
            pygame.display.update()
            clock.tick(fps)

    pygame.quit()
    quit()

# Start the game
game_loop()
