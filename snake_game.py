import pygame
import random

pygame.init()
WIDTH, HEIGHT = 600, 600
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

snake = [(WIDTH//2, HEIGHT//2)]
direction = (CELL_SIZE, 0)
food = (random.randint(0, WIDTH//CELL_SIZE-1) * CELL_SIZE, 
        random.randint(0, HEIGHT//CELL_SIZE-1) * CELL_SIZE)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, CELL_SIZE):
                direction = (0, -CELL_SIZE)
            elif event.key == pygame.K_DOWN and direction != (0, -CELL_SIZE):
                direction = (0, CELL_SIZE)
            elif event.key == pygame.K_LEFT and direction != (CELL_SIZE, 0):
                direction = (-CELL_SIZE, 0)
            elif event.key == pygame.K_RIGHT and direction != (-CELL_SIZE, 0):
                direction = (CELL_SIZE, 0)
    
    head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    
    if (head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT or head in snake):
        running = False
    
    snake.insert(0, head)
    
    if head == food:
        food = (random.randint(0, WIDTH//CELL_SIZE-1) * CELL_SIZE, 
                random.randint(0, HEIGHT//CELL_SIZE-1) * CELL_SIZE)
    else:
        snake.pop()
    
    screen.fill((0, 0, 0))
    for segment in snake:
        pygame.draw.rect(screen, (0, 255, 0), (*segment, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen, (255, 0, 0), (*food, CELL_SIZE, CELL_SIZE))
    
    pygame.display.flip()
    clock.tick(10)

pygame.quit()