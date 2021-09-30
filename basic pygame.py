# Simple pygame program

# Import and initialize the pygame library
import pygame
import time
pygame.init()

WIDTH = 800
HEIGHT = 600

# Set up the drawing window
screen = pygame.display.set_mode( (WIDTH, HEIGHT) )

#ball variables
ball_x = WIDTH//2
ball_y = HEIGHT//2

ball_delta_x = .2
ball_delta_y = .5
ball_radius = 15

clock = pygame.time.Clock()

# Run until the user asks to quit
running = True
dt = 1
font = pygame.font.SysFont("Arial", 18)
print("Window set up!")
time.sleep(3)


while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0, 0, 255), (ball_x,ball_y), ball_radius)
    ball_x = ball_x + ball_delta_x * dt
    ball_y = ball_y + ball_delta_y * dt
    
    if ball_x < ball_radius:
        ball_x = ball_radius
        ball_delta_x = -(ball_delta_x)
    if ball_x > WIDTH - ball_radius:
        ball_x = WIDTH-ball_radius
        ball_delta_x = -(ball_delta_x)
    
    if ball_y < ball_radius:
        ball_y = ball_radius
        ball_delta_y = -(ball_delta_y)
    if ball_y > HEIGHT - ball_radius:
        ball_y = HEIGHT-ball_radius
        ball_delta_y = -(ball_delta_y)  


    fps = str(int(clock.get_fps()))
    fps_text = font.render(fps, 1, pygame.Color("coral"))
    screen.blit(fps_text, (10,0))
    
    # Flip the display
    dt=clock.tick(60)
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
