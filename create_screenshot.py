"""
Create a screenshot-style demonstration of the Oil Painting Application UI
"""

import pygame
import numpy as np
from main import OilPaintingCanvas, BrushStroke
import random
import math


def create_application_screenshot():
    """Create a screenshot-style image showing the application interface."""
    pygame.init()
    
    # Create application window surface
    width, height = 1024, 768
    screen = pygame.Surface((width, height))
    screen.fill((240, 240, 240))  # Light gray background
    
    # Create the painting canvas
    canvas = OilPaintingCanvas(width, height - 100)  # Leave space for UI elements
    
    # Add some realistic brush strokes to demonstrate the painting
    print("Creating demonstration painting...")
    color_palette = [
        (120, 80, 40),    # Brown
        (180, 140, 100),  # Light brown
        (60, 120, 60),    # Green
        (100, 150, 200),  # Blue
        (200, 100, 100),  # Red
        (150, 100, 200),  # Purple
        (200, 200, 100),  # Yellow
        (100, 100, 100),  # Gray
    ]
    
    # Create a small, artistic demonstration
    num_strokes = 35
    for i in range(num_strokes):
        # Create varied stroke positions and angles
        start_x = random.randint(100, width - 200)
        start_y = random.randint(100, height - 200)
        
        angle = random.uniform(0, 2 * math.pi)
        length = random.randint(50, 150)
        
        end_x = start_x + int(length * math.cos(angle))
        end_y = start_y + int(length * math.sin(angle))
        
        # Keep within bounds
        end_x = max(50, min(width - 50, end_x))
        end_y = max(50, min(height - 150, end_y))
        
        color = random.choice(color_palette)
        brush_size = random.randint(25, 45)
        
        stroke = BrushStroke((start_x, start_y), (end_x, end_y), color, brush_size)
        canvas.add_brush_stroke(stroke)
        
        if (i + 1) % 10 == 0:
            print(f"Added {i + 1}/{num_strokes} demonstration strokes")
    
    # Draw the canvas onto the screen
    screen.blit(canvas.surface, (0, 100))  # Leave space at top for title
    
    # Add UI elements to show it's an application
    # Title bar
    title_font = pygame.font.Font(None, 48)
    title_text = title_font.render("Oil Painting Simulator", True, (50, 50, 50))
    screen.blit(title_text, (20, 20))
    
    # Status bar
    font = pygame.font.Font(None, 32)
    status_text = font.render(f"Strokes: {num_strokes} | Press any key to paint | ESC to exit", True, (100, 100, 100))
    screen.blit(status_text, (20, 60))
    
    # Save the demonstration screenshot
    pygame.image.save(screen, "oil_painting_demo_ui.png")
    print("Application UI demonstration saved as: oil_painting_demo_ui.png")
    
    return screen


if __name__ == "__main__":
    create_application_screenshot()
    pygame.quit()
    print("Screenshot demonstration complete!")