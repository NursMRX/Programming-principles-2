import pygame
import math
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Main Window Settings
WIDTH, HEIGHT = 1080, 800
TOOLBAR_HEIGHT = 100  # Increased height for more tools
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")
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

# Colors - Expanded color palette
RED = (230, 0, 0)
GREEN = (0, 230, 0)
BLUE = (0, 0, 230)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
CYAN = (0, 255, 255)
ORANGE = (255, 165, 0)
PINK = (255, 192, 203)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)
colors = [RED, GREEN, BLUE, YELLOW, PURPLE, CYAN, ORANGE, PINK, BLACK]
color = BLACK  # Default color
selected_tool = "brush"  # Default tool
brush_thickness = 5
eraser_thickness = 20  # Separate thickness for eraser

# Load Eraser Image
eraser_img = pygame.image.load("/home/nursultan/Projects python/PP2/Lab9/paint/eraser.png") 
eraser_img = pygame.transform.scale(eraser_img, (60, 60))

# Font for thickness display
font = pygame.font.SysFont(None, 24)

def draw_toolbar():
    """Draws the toolbar with colors, shapes, and tools."""
    pygame.draw.rect(screen, (200, 200, 200), (0, 0, WIDTH, TOOLBAR_HEIGHT))  # Toolbar background

    # Color Buttons
    for i, col in enumerate(colors):
        pygame.draw.rect(screen, col, (i * 40 + 10, 10, 30, 30))
        pygame.draw.rect(screen, BLACK, (i * 40 + 10, 10, 30, 30), 1)

    # Shapes and Tools - organized in two rows
    # First row of tools
    pygame.draw.rect(screen, WHITE, (370, 10, 40, 30), 2)  # Rectangle
    pygame.draw.rect(screen, WHITE, (420, 10, 40, 30), 2)  # Square
    pygame.draw.circle(screen, WHITE, (480, 25), 15, 2)    # Circle
    
    # Second row of tools
    pygame.draw.polygon(screen, WHITE, [(540, 10), (560, 40), (520, 40)], 2)  # Right triangle
    pygame.draw.polygon(screen, WHITE, [(590, 25), (610, 40), (570, 40)], 2)  # Equilateral triangle
    pygame.draw.polygon(screen, WHITE, [(640, 25), (660, 10), (680, 25), (660, 40)], 2)  # Rhombus
    
    # Labels for tools
    small_font = pygame.font.SysFont(None, 12)
    labels = ["Rect", "Square", "Circle", "R-Tri", "E-Tri", "Rhombus"]
    for i, label in enumerate(labels):
        text = small_font.render(label, True, BLACK)
        screen.blit(text, (370 + i*50, 45))

    # Eraser
    screen.blit(eraser_img, (WIDTH - 80, 10))  # Eraser icon

    # Display current thickness and tool
    if selected_tool == "eraser":
        thickness_text = font.render(f"Eraser: {eraser_thickness}", True, BLACK)
    else:
        thickness_text = font.render(f"{selected_tool.capitalize()}: {brush_thickness}", True, BLACK)
    screen.blit(thickness_text, (WIDTH - 200, 50))

    pygame.display.update()

def pick_tool():
    """Handles tool and color selection."""
    global color, selected_tool
    x, y = pygame.mouse.get_pos()

    if y > TOOLBAR_HEIGHT:
        return  # Ignore clicks outside the toolbar

    # Check color buttons
    for i, col in enumerate(colors):
        if i * 40 + 10 < x < i * 40 + 40 and 10 < y < 40:
            color = col
            selected_tool = "brush"
            return

    # Check tool buttons
    if 370 < x < 410 and 10 < y < 40:
        selected_tool = "rectangle"
    elif 420 < x < 460 and 10 < y < 40:
        selected_tool = "square"
    elif 460 < x < 500 and 10 < y < 40:
        selected_tool = "circle"
    elif 520 < x < 560 and 10 < y < 40:
        selected_tool = "right_triangle"
    elif 570 < x < 610 and 10 < y < 40:
        selected_tool = "equilateral_triangle"
    elif 620 < x < 680 and 10 < y < 40:
        selected_tool = "rhombus"
    elif WIDTH - 80 < x < WIDTH and 10 < y < 70:
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
    if start_pos and selected_tool in ["rectangle", "square", "circle", "right_triangle", "equilateral_triangle", "rhombus"]:
        x1, y1 = start_pos
        x2, y2 = currX, currY
        
        # Create a temporary surface for the preview
        preview_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        
        if selected_tool == "rectangle":
            pygame.draw.rect(preview_surface, (*color, 128), 
                           pygame.Rect(min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1)), 
                           brush_thickness)
        elif selected_tool == "square":
            size = min(abs(x2 - x1), abs(y2 - y1))
            pygame.draw.rect(preview_surface, (*color, 128), 
                           pygame.Rect(x1 if x2 > x1 else x1 - size, 
                                     y1 if y2 > y1 else y1 - size, 
                                     size, size), 
                           brush_thickness)
        elif selected_tool == "circle":
            pygame.draw.ellipse(preview_surface, (*color, 128), 
                              pygame.Rect(min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1)), 
                              brush_thickness)
        elif selected_tool == "right_triangle":
            points = [(x1, y1), (x1, y2), (x2, y2)]
            pygame.draw.polygon(preview_surface, (*color, 128), points, brush_thickness)
        elif selected_tool == "equilateral_triangle":
            height = y2 - y1
            side_length = abs(x2 - x1)
            points = [
                (x1, y1),
                (x1 + side_length, y1),
                (x1 + side_length/2, y1 + height)
            ]
            pygame.draw.polygon(preview_surface, (*color, 128), points, brush_thickness)
        elif selected_tool == "rhombus":
            center_x = (x1 + x2) / 2
            center_y = (y1 + y2) / 2
            width = abs(x2 - x1)
            height = abs(y2 - y1)
            points = [
                (center_x, y1),
                (x2, center_y),
                (center_x, y2),
                (x1, center_y)
            ]
            pygame.draw.polygon(preview_surface, (*color, 128), points, brush_thickness)
        
        # Draw the preview
        screen.blit(preview_surface, (0, 0))

def finalize_shape():
    """Finalizes the shape when mouse is released."""
    if start_pos and selected_tool in ["rectangle", "square", "circle", "right_triangle", "equilateral_triangle", "rhombus"]:
        x1, y1 = start_pos
        x2, y2 = currX, currY
        
        if selected_tool == "rectangle":
            pygame.draw.rect(drawing_surface, color, 
                           pygame.Rect(min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1)), 
                           brush_thickness)
        elif selected_tool == "square":
            size = min(abs(x2 - x1), abs(y2 - y1))
            pygame.draw.rect(drawing_surface, color, 
                           pygame.Rect(x1 if x2 > x1 else x1 - size, 
                                     y1 if y2 > y1 else y1 - size, 
                                     size, size), 
                           brush_thickness)
        elif selected_tool == "circle":
            pygame.draw.ellipse(drawing_surface, color, 
                              pygame.Rect(min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1)), 
                              brush_thickness)
        elif selected_tool == "right_triangle":
            points = [(x1, y1), (x1, y2), (x2, y2)]
            pygame.draw.polygon(drawing_surface, color, points, brush_thickness)
        elif selected_tool == "equilateral_triangle":
            height = y2 - y1
            side_length = abs(x2 - x1)
            points = [
                (x1, y1),
                (x1 + side_length, y1),
                (x1 + side_length/2, y1 + height)
            ]
            pygame.draw.polygon(drawing_surface, color, points, brush_thickness)
        elif selected_tool == "rhombus":
            center_x = (x1 + x2) / 2
            center_y = (y1 + y2) / 2
            width = abs(x2 - x1)
            height = abs(y2 - y1)
            points = [
                (center_x, y1),
                (x2, center_y),
                (center_x, y2),
                (x1, center_y)
            ]
            pygame.draw.polygon(drawing_surface, color, points, brush_thickness)

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
            if drawing and selected_tool in ["rectangle", "square", "circle", "right_triangle", "equilateral_triangle", "rhombus"]:
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
            if event.key == K_EQUALS or event.key == K_PLUS:
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
    if drawing and selected_tool in ["rectangle", "square", "circle", "right_triangle", "equilateral_triangle", "rhombus"]:
        draw_shape_preview()
    
    draw_toolbar()  # Redraw toolbar to keep it on top
    
    pygame.display.update()
    clock.tick(60)

pygame.quit()