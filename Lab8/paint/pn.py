import pygame
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Main Window Settings
WIDTH, HEIGHT = 1080, 800
TOOLBAR_HEIGHT = 80
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Advanced Paint")
clock = pygame.time.Clock()

# Create a separate surface for drawing that we can modify
drawing_surface = pygame.Surface((WIDTH, HEIGHT))
drawing_surface.fill((255, 255, 255))

# Drawing Variables
drawing = False
start_pos = None
currX, currY = 0, 0  # Current mouse position
prevX, prevY = 0, 0  # Previous mouse position
show_preview = False  # For shape preview

# Colors
RED = (230, 0, 0)
GREEN = (0, 230, 0)
BLUE = (0, 0, 230)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)
colors = [RED, GREEN, BLUE]
color = BLACK  # Default color
selected_tool = "brush"  # Default tool
brush_thickness = 5
eraser_thickness = 20  # Separate thickness for eraser

# Load Eraser Image
try:
    eraser_img = pygame.image.load("eraser.png")
    eraser_img = pygame.transform.scale(eraser_img, (60, 60))
except:
    # Create a simple eraser icon if image not found
    eraser_img = pygame.Surface((60, 60))
    eraser_img.fill((200, 200, 200))
    pygame.draw.rect(eraser_img, BLACK, (0, 0, 60, 60), 2)
    font = pygame.font.SysFont(None, 30)
    text = font.render("E", True, BLACK)
    eraser_img.blit(text, (25, 15))

# Font for thickness display
font = pygame.font.SysFont(None, 24)

def draw_toolbar():
    """Draws the toolbar with colors, shapes, and tools."""
    pygame.draw.rect(screen, (200, 200, 200), (0, 0, WIDTH, TOOLBAR_HEIGHT))  # Toolbar background

    # Color Buttons
    for i, col in enumerate(colors):
        pygame.draw.rect(screen, col, (i * 50 + 10, 10, 40, 40))
        pygame.draw.rect(screen, BLACK, (i * 50 + 10, 10, 40, 40), 2)

    # Shapes and Tools
    pygame.draw.rect(screen, WHITE, (170, 10, 40, 40), 2)  # Rectangle
    pygame.draw.circle(screen, WHITE, (240, 30), 20, 2)  # Circle

    # Eraser
    screen.blit(eraser_img, (WIDTH - 80, 10))  # Eraser icon

    # Display current thickness
    if selected_tool == "eraser":
        thickness_text = font.render(f"Eraser: {eraser_thickness}", True, BLACK)
    else:
        thickness_text = font.render(f"Brush: {brush_thickness}", True, BLACK)
    screen.blit(thickness_text, (WIDTH - 200, 50))

    pygame.display.update()

def pick_tool():
    """Handles tool and color selection."""
    global color, selected_tool
    x, y = pygame.mouse.get_pos()

    if y > TOOLBAR_HEIGHT:
        return  # Ignore clicks outside the toolbar

    if 10 < x < 50:
        color = RED
        selected_tool = "brush"
    elif 60 < x < 100:
        color = GREEN
        selected_tool = "brush"
    elif 110 < x < 150:
        color = BLUE
        selected_tool = "brush"
    elif 170 < x < 210:
        selected_tool = "rectangle"
    elif 220 < x < 260:
        selected_tool = "circle"
    elif WIDTH - 80 < x < WIDTH:
        selected_tool = "eraser"

def paint():
    """Draws shapes or erases based on the selected tool."""
    global start_pos, drawing, prevX, prevY, currX, currY, show_preview

    if selected_tool == "brush":
        pygame.draw.line(drawing_surface, color, (prevX, prevY), (currX, currY), brush_thickness)
    elif selected_tool == "eraser":
        pygame.draw.circle(drawing_surface, WHITE, (currX, currY), eraser_thickness)

def draw_shape_preview():
    """Draws a preview of the shape being created."""
    if start_pos and selected_tool in ["rectangle", "circle"]:
        x1, y1 = start_pos
        x2, y2 = currX, currY
        
        # Create a temporary surface for the preview
        preview_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        
        if selected_tool == "rectangle":
            pygame.draw.rect(preview_surface, (*color, 128), 
                           pygame.Rect(min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1)), 
                           brush_thickness)
        elif selected_tool == "circle":
            pygame.draw.ellipse(preview_surface, (*color, 128), 
                              pygame.Rect(min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1)), 
                              brush_thickness)
        
        # Draw the preview
        screen.blit(preview_surface, (0, 0))

def finalize_shape():
    """Finalizes the shape when mouse is released."""
    if start_pos and selected_tool in ["rectangle", "circle"]:
        x1, y1 = start_pos
        x2, y2 = currX, currY
        
        if selected_tool == "rectangle":
            pygame.draw.rect(drawing_surface, color, 
                           pygame.Rect(min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1)), 
                           brush_thickness)
        elif selected_tool == "circle":
            pygame.draw.ellipse(drawing_surface, color, 
                              pygame.Rect(min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1)), 
                              brush_thickness)

# Initial Drawing of Toolbar
drawing_surface.fill(WHITE)
draw_toolbar()

# Main Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN and event.button == 1:
            pick_tool()  # Pick tool or color
            if event.pos[1] > TOOLBAR_HEIGHT:
                drawing = True
                start_pos = event.pos
                prevX, prevY = event.pos
        elif event.type == MOUSEBUTTONUP and event.button == 1:
            if drawing and selected_tool in ["rectangle", "circle"]:
                finalize_shape()
            drawing = False
            start_pos = None
        elif event.type == MOUSEMOTION:
            currX, currY = event.pos
            if drawing and selected_tool in ["brush", "eraser"]:
                paint()
            prevX, prevY = currX, currY

        # Handle thickness adjustments
        if event.type == KEYDOWN:
            if event.key == K_EQUALS:
                if selected_tool == "eraser":
                    eraser_thickness += 1
                else:
                    brush_thickness += 1
            elif event.key == K_MINUS:
                if selected_tool == "eraser":
                    eraser_thickness = max(1, eraser_thickness - 1)
                else:
                    brush_thickness = max(1, brush_thickness - 1)
            elif event.key == K_c:
                drawing_surface.fill(WHITE)
                draw_toolbar()

    # Draw everything
    screen.blit(drawing_surface, (0, 0))
    
    # Show shape preview while drawing
    if drawing and selected_tool in ["rectangle", "circle"]:
        draw_shape_preview()
    
    draw_toolbar()  # Redraw toolbar to keep it on top
    
    pygame.display.update()
    clock.tick(60)

pygame.quit()